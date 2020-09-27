#!/usr/bin/env python
import datetime as dt


# Date Formats: %a(Sun,Mon..)  %A(Sunday,Monday..) %d(01,02..31) %b(Jan,Feb..) %B (January,February..) %m(01,02..12) %y(2 digit year)  %Y(4 digit year)
# Time Formats: %H(24 hour clock 00,01..23)  %I(12 hour clock 00,01..12) %M(00,01..59) %S(01,02..59)   %f(microsecond 6 digits)    %Z(UTC,EST,PDT..)
# Misc Formats: %j(DayOfTheYear 001,002..366)   %U(WeekNumOfTheYear 00,01..53)
# Shortcut Formats: %c(%a %b %d %H:%M:%S %Y - Tue Aug 08 21:23:00 2018)   %x(%m/%d/%Y 08/23/2018)     %X(%H:%M:%S 22:34:00)

class DateMath:
    @staticmethod
    def __get_other_date__(nums_days_offset, from_date=None):
        if from_date is None:
            other_date = dt.datetime.today() + dt.timedelta(nums_days_offset)
        else:
            other_date = from_date + dt.timedelta(nums_days_offset)
        return other_date

    @staticmethod
    def get_previous_date(num_days_in_past, from_date=None):
        return DateMath.__get_other_date__(0 - num_days_in_past, from_date)

    @staticmethod
    def get_future_date(num_days_in_future, from_date=None):
        return DateMath.__get_other_date__(num_days_in_future, from_date)

    @staticmethod
    # Returns None if date_str could not be converted to datetime format
    def str_to_date(date_str, in_format="%m-%d-%Y"):
        try:
            converted_date = dt.datetime.strptime(date_str, in_format)
        except ValueError as err:
            converted_date = None
        return converted_date

    @staticmethod
    def date_to_str(in_date, format="%m-%d-%Y"):
        return in_date.strftime(format)

    @staticmethod
    def today():
        return dt.datetime.today()

    @staticmethod
    def tomorrow():
        return DateMath.get_future_date(1)


if __name__ == '__main__':
    print(DateMath.str_to_date("10-20-2018"))
    print(DateMath.str_to_date("10202018", in_format="%m%d%Y"))

    print(DateMath.get_previous_date(1))
    print(DateMath.get_future_date(1))

    print(DateMath.today())

    print(DateMath.date_to_str(DateMath.today()))
    start_date = DateMath.str_to_date("01-01-2018")
    print(DateMath.date_to_str(DateMath.get_previous_date(2, from_date=start_date)))
    print(DateMath.date_to_str(DateMath.get_future_date(2, from_date=start_date), format="%a %d %b,%Y"))

    print(DateMath.str_to_date('10-20-2018') < DateMath.str_to_date('11-20-2018'))
