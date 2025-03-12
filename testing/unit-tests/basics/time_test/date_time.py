
class Time():
    def __init__(self, hours, minutes, seconds):
        if hours < 0 or hours > 23:
            raise ValueError(f"Invalid hours value: '{hours}'!'")
        if minutes < 0 or minutes > 59:
            raise ValueError(f"Invalid minutes value: {minutes}!")
        if seconds < 0 or seconds > 59:
            raise ValueError(f"Invalid seconds value: {seconds}!")

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    def __repr__(self):
        return f"Time({self.hours}, {self.minutes}, {self.seconds})"

    def __str__(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds
