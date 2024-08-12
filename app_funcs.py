import openpyxl
import enum
import json
from copy import deepcopy


class WeekDays(enum.Enum):
    Monday = 'monday'
    Tuesday = 'tuesday'
    Wednesday = 'wednesday'
    Thursday = 'thursday'
    Friday = 'friday'
    Saturday = 'saturday'

    @classmethod
    def get_day(cls, row: int):
        if 2 <= row <= 15:
            return cls.Monday
        if 16 <= row <= 29:
            return cls.Tuesday
        if 30 <= row <= 43:
            return cls.Wednesday
        if 44 <= row <= 57:
            return cls.Thursday
        if 58 <= row <= 71:
            return cls.Friday
        if 72 <= row <= 85:
            return cls.Saturday


class LessonsTimes(enum.Enum):
    Lesson_1_08 = '08.00-09.30'
    Lesson_2_09 = '09.40-11.10'
    Lesson_3_11 = '11.30-13.00'
    Lesson_4_13 = '13.10-14.40'
    Lesson_5_15 = '15.00-16.30'
    Lesson_6_16 = '16.40-18.10'
    Lesson_7_18 = '18.20-19.50'

    @classmethod
    def get_time(cls, row: int):
        if row in [2, 3, 16, 17, 30, 31, 44, 45, 58, 59, 72, 73]:
            return cls.Lesson_1_08
        if row in [4, 5, 18, 19, 32, 33, 46, 47, 60, 61, 74, 75]:
            return cls.Lesson_2_09
        if row in [6, 7, 20, 21, 34, 35, 48, 49, 62, 63, 76, 77]:
            return cls.Lesson_3_11
        if row in [8, 9, 22, 23, 36, 37, 50, 51, 64, 65, 78, 79]:
            return cls.Lesson_4_13
        if row in [10, 11, 24, 25, 38, 39, 52, 53, 66, 67, 80, 81]:
            return cls.Lesson_5_15
        if row in [12, 13, 26, 27, 40, 41, 54, 55, 68, 69, 82, 83]:
            return cls.Lesson_6_16
        if row in [14, 15, 28, 29, 42, 43, 56, 57, 70, 71, 84, 85]:
            return cls.Lesson_7_18


workbook = openpyxl.load_workbook('rasp2024.xlsx')
sheet = workbook[' 1 курс ']

group_name = None
group_lessons_info = {
    WeekDays.Monday: {
        LessonsTimes.Lesson_1_08: [],
        LessonsTimes.Lesson_2_09: [],
        LessonsTimes.Lesson_3_11: [],
        LessonsTimes.Lesson_4_13: [],
        LessonsTimes.Lesson_5_15: [],
        LessonsTimes.Lesson_6_16: [],
        LessonsTimes.Lesson_7_18: []
    },
    WeekDays.Tuesday: {
        LessonsTimes.Lesson_1_08: [],
        LessonsTimes.Lesson_2_09: [],
        LessonsTimes.Lesson_3_11: [],
        LessonsTimes.Lesson_4_13: [],
        LessonsTimes.Lesson_5_15: [],
        LessonsTimes.Lesson_6_16: [],
        LessonsTimes.Lesson_7_18: []
    },
    WeekDays.Wednesday: {
        LessonsTimes.Lesson_1_08: [],
        LessonsTimes.Lesson_2_09: [],
        LessonsTimes.Lesson_3_11: [],
        LessonsTimes.Lesson_4_13: [],
        LessonsTimes.Lesson_5_15: [],
        LessonsTimes.Lesson_6_16: [],
        LessonsTimes.Lesson_7_18: []
    },
    WeekDays.Thursday: {
        LessonsTimes.Lesson_1_08: [],
        LessonsTimes.Lesson_2_09: [],
        LessonsTimes.Lesson_3_11: [],
        LessonsTimes.Lesson_4_13: [],
        LessonsTimes.Lesson_5_15: [],
        LessonsTimes.Lesson_6_16: [],
        LessonsTimes.Lesson_7_18: []
    },
    WeekDays.Friday: {
        LessonsTimes.Lesson_1_08: [],
        LessonsTimes.Lesson_2_09: [],
        LessonsTimes.Lesson_3_11: [],
        LessonsTimes.Lesson_4_13: [],
        LessonsTimes.Lesson_5_15: [],
        LessonsTimes.Lesson_6_16: [],
        LessonsTimes.Lesson_7_18: []
    },
    WeekDays.Saturday: {
        LessonsTimes.Lesson_1_08: [],
        LessonsTimes.Lesson_2_09: [],
        LessonsTimes.Lesson_3_11: [],
        LessonsTimes.Lesson_4_13: [],
        LessonsTimes.Lesson_5_15: [],
        LessonsTimes.Lesson_6_16: [],
        LessonsTimes.Lesson_7_18: []
    }
}
final_data = {}

for col in sheet.iter_cols(3):
    group_name = col[0].value
    temp_info = deepcopy(group_lessons_info)
    for lesson in col[1:]:
        if lesson.value is None:
            continue
        sheet_row = lesson.row
        temp_info[WeekDays.get_day(sheet_row)][LessonsTimes.get_time(sheet_row)].append(lesson.value.strip())
    final_data[group_name] = temp_info

print(group_name)
print(final_data['ИБА-12'])