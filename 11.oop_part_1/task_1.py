class MyTime:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            h, m, s = map(int, args[0].split(":"))
            self.hours, self.minutes, self.seconds = h, m, s
        elif len(args) == 3 and all(isinstance(arg, int) for arg in args):
            self.hours, self.minutes, self.seconds = args
        elif len(args) == 1 and isinstance(args[0], MyTime):
            self.hours = args[0].hours
            self.minutes = args[0].minutes
            self.seconds = args[0].seconds
        else:
            self.hours, self.minutes, self.seconds = 0, 0, 0
        self._normalize_time()

    def _normalize_time(self):
        self.minutes += self.seconds // 60
        self.seconds %= 60
        self.hours += self.minutes // 60
        self.minutes %= 60
        self.hours %= 24

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def __eq__(self, other):
        return (self.hours, self.minutes, self.seconds) == (other.hours, other.minutes, other.seconds)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return (self.hours, self.minutes, self.seconds) < (other.hours, other.minutes, other.seconds)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __add__(self, other):
        if isinstance(other, MyTime):
            return MyTime(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)
        raise TypeError("Операнд должен быть типа MyTime")

    def __sub__(self, other):
        if isinstance(other, MyTime):
            total_seconds = self.to_seconds() - other.to_seconds()
            if total_seconds < 0:
                raise ValueError("Результат операции отрицательный, что невозможно для времени.")
            return MyTime.from_seconds(total_seconds)
        raise TypeError("Операнд должен быть типа MyTime")

    def __mul__(self, multiplier):
        if isinstance(multiplier, int):
            total_seconds = self.to_seconds() * multiplier
            return MyTime.from_seconds(total_seconds)
        raise TypeError("Множитель должен быть целым числом")

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, total_seconds):
        hours = (total_seconds // 3600) % 24
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)
    

time1 = MyTime('8:100:14125125')
time2 = MyTime('3:100:14125125')

time3  = time1 - time2

print(time1)
print(time2)
print(time3)