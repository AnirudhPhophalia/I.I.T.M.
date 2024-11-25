'''Create a class Time with the following specification:

Attributes

time: int, represents time in seconds

Methods

(1) __init__: accept time in seconds as an argument and assign it to the corresponding attribute

(2) seconds_to_minutes: convert the value of time into minutes and return a string in the format: "<minutes> min <seconds> sec". For example: if the value of the attribute time is 
170
170, this method should return the string "2 min 50 sec"

(3) seconds_to_hours: convert the value of time into hours and return a string in the format: "<hours> hrs <minutes> min <seconds> sec". For example: if the value of the attribute time is 
10890
10890, this method should return the string "3 hrs 1 min 30 sec"

(4) seconds_to_days: convert the value of time into days and return a string in the format: "<days> days <hours> hrs <minutes> min <seconds> sec". For example: if the value of the attribute time is 
86460
86460, this method should return the string "1 days 0 hrs 1 min 0 sec"

(1) Each test case corresponds to one or more method calls. We will use T to denote the name of the object.

(2) You do not have to accept input from the user or print output to the console. You just have to define the class based on the specifications given in the question.'''
class Time:
    def __init__(self, time: int):
        self.time = time  # Assign time in seconds to the attribute

    def seconds_to_minutes(self) -> str:
        minutes = self.time // 60
        seconds = self.time % 60
        return f"{minutes} min {seconds} sec"

    def seconds_to_hours(self) -> str:
        hours = self.time // 3600
        remaining_seconds = self.time % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        return f"{hours} hrs {minutes} min {seconds} sec"

    def seconds_to_days(self) -> str:
        days = self.time // 86400
        remaining_seconds = self.time % 86400
        hours = remaining_seconds // 3600
        remaining_seconds %= 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        return f"{days} days {hours} hrs {minutes} min {seconds} sec"
