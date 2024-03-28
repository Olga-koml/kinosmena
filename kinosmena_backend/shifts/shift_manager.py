import math
from datetime import timedelta

from shifts.models import Shift

DAY_OFF_HOURS = 36


class UpdateData:
    def __init__(self, obj, **kwargs):
        for key, value in obj.__dict__.items():
            setattr(self, key, value)

        for key, value in kwargs.items():
            if hasattr(obj, key):
                setattr(self, key, value)


class ShiftManager:
    def __init__(self, obj: Shift):
        self.obj = obj

    def update(self, data: dict):
        update_data: UpdateData = UpdateData(self.obj, **data)
        print(self._get_overwork_hours(update_data))

        shift_sum = self._calculate_shift_sum()
        overwork_hours = self._get_overwork_hours(update_data)
        overwork_sum = self._calculate_overwork_sum(overwork_hours)
        current_lunch_sum = self._calculate_current_lunch_sum(update_data)
        late_lunch_sum = self._calculate_late_lunch_sum(update_data)
        per_diem_sum = self._calculate_per_diem_sum(update_data)
        non_sleep_hours = self._get_non_sleep_hours(update_data)
        non_sleep_sum = self._calculate_non_sleep_sum(non_sleep_hours)
        day_off_hours = self.get_day_off_hours(update_data)
        day_off_sum = self._calculate_day_off_sum(day_off_hours)
        services_sum = self._calculate_services_sum(update_data)
        total = self._calculate_total(
            shift_sum,
            overwork_sum,
            current_lunch_sum,
            late_lunch_sum,
            per_diem_sum,
            day_off_sum,
            non_sleep_sum,
            services_sum
        )

        # Обновление данных объекта Shift
        self.obj.shift_sum = shift_sum
        self.obj.overwork_hours = overwork_hours
        self.obj.overwork_sum = overwork_sum
        self.obj.current_lunch_sum = current_lunch_sum
        self.obj.late_lunch_sum = late_lunch_sum
        self.obj.per_diem_sum = per_diem_sum
        self.obj.non_sleep_hours = non_sleep_hours
        self.obj.non_sleep_sum = non_sleep_sum
        self.obj.day_off_hours = day_off_hours
        self.obj.day_off_sum = day_off_sum
        self.obj.total = total

        self.obj.save()


    def _calculate_shift_sum(self):
        return self.obj.project.shift_rate

    def _calculate_services_sum(self, data):
        return data.services_sum

    def _get_overwork_hours(self, data):
        shift_duration = timedelta(hours=self.obj.project.shift_duration)
        return math.ceil(
            ((data.end_date - data.start_date - shift_duration).total_seconds() / 3600)
        ) if data.start_date + shift_duration < data.end_date else 0

    def _calculate_overwork_sum(self, overtime_hours):
        return self.obj.project.overtime_rate * overtime_hours

    def _calculate_current_lunch_sum(self, data):
        return (
            self.obj.project.current_lunch_rate
            if data.is_current_lunch
            else 0
        )

    def _calculate_late_lunch_sum(self, data):
        return (
            self.obj.project.late_lunch_rate
            if data.is_late_lunch
            else 0
        )

    def _calculate_per_diem_sum(self, data):
        return self.obj.project.per_diem if data.is_per_diem else 0

    def _get_non_rest_hours(self, data, rest_hours):
        previous_shift = Shift.objects.filter(
            project=self.obj.project, end_date__lt=data.start_date
        ).order_by('-end_date').first()
        print(previous_shift, "PREVIOUS SHIFT")
        if previous_shift:
            prev_shift_end_date = previous_shift.end_date
            print(prev_shift_end_date, 'PREV_SHIFT_END_DATE')
            prev_shift_start_date = previous_shift.start_date
            prev_fact_shift_duration = math.ceil(
                (prev_shift_end_date - prev_shift_start_date
                 ).total_seconds() / 3600)
            shift_duration = timedelta(hours=self.obj.project.shift_duration)
            prev_date_start_non_sleep = (
                prev_shift_start_date + timedelta(hours=prev_fact_shift_duration)
                if prev_fact_shift_duration > self.obj.project.shift_duration
                else prev_shift_start_date + shift_duration
            )
            print(prev_date_start_non_sleep, "DATE_START_NON_SLEEP")
            rest_duration = timedelta(hours=rest_hours)
            print(self.obj.start_date, 'НАЧАЛО ТЕКУЩЕЙ ДАТЫ')
            non_sleep_hours = (
                math.ceil((
                    prev_date_start_non_sleep + rest_duration - data.start_date
                ).total_seconds() / 3600)
                if prev_date_start_non_sleep + rest_duration > data.start_date
                else 0)
            return non_sleep_hours
        return 0

    def _get_non_sleep_hours(self, data):
        if not data.is_day_off:
            non_sleep_hours = self._get_non_rest_hours(
                data, self.obj.project.rest_duration
            )
            return non_sleep_hours
        return 0

    def _calculate_non_sleep_sum(self, non_sleep_hours):
        return non_sleep_hours * self.obj.project.non_sleep_rate

    def get_day_off_hours(self, data):
        if data.is_day_off:
            day_off_hours = self._get_non_rest_hours(data, DAY_OFF_HOURS)
            return day_off_hours
        return 0

    def _calculate_day_off_sum(self, day_off_hours):
        return self.obj.project.day_off_rate * day_off_hours

    def _calculate_total(
            self, shift_sum, overwork_sum, current_lunch_sum,
            late_lunch_sum, per_diem_sum, day_off_sum, non_sleep_sum,
            services_sum
            ):
        return (
            shift_sum + overwork_sum + current_lunch_sum +
            late_lunch_sum + per_diem_sum + day_off_sum +
            non_sleep_sum + services_sum
        )
