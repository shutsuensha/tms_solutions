class SuperStr(str):
    def is_repeatance(self, s):
        if not s or len(self) % len(s) != 0:
            return False
        return self == s * (len(self) // len(s))

    def is_palindrom(self):
        return self.lower() == self.lower()[::-1]


s = SuperStr("abcabcabc")
print(s.is_repeatance("abc"))      # True
print(s.is_repeatance("ab"))       # False
print(s.is_palindrom())            # False

p1 = SuperStr("racecar")
p2 = SuperStr("")
print(p1.is_palindrom())  
print(p2.is_palindrom()) 