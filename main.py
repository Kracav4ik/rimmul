# encoding: utf-8


class RimMul:
    def __init__(self, string=""):
        self.map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        self.check_strange(string)
        self.string = string
        if string:
            self.string = self.to_rim(self.to_num(string))
        self.i = 0

    def __add__(self, other):
        num1 = self.to_num(self.string)
        num2 = self.to_num(other.string)
        if num1 and num2:
            return RimMul(self.to_rim((num1 + num2) % 4000))
        else:
            return RimMul()

    def __sub__(self, other):
        num1 = self.to_num(self.string)
        num2 = self.to_num(other.string)
        if num1 and num2:
            return RimMul(self.to_rim(num1 - num2))
        else:
            return RimMul()

    def __truediv__(self, other):
        num1 = self.to_num(self.string)
        num2 = self.to_num(other.string)
        if num1 and num2:
            return RimMul(self.to_rim(num1 // num2))
        else:
            return RimMul()

    def __mul__(self, other):
        num1 = self.to_num(self.string)
        num2 = self.to_num(other.string)
        if num1 and num2:
            return RimMul(self.to_rim((num1 * num2) % 4000))
        else:
            return RimMul()

    def __str__(self):
        assert self.string, "Your number incorrect"
        return self.string

    def test(self):
        for i in range(1, 4000):
            rim = self.to_rim(i)
            print(rim)
            print(self.to_num(rim))

    def to_num(self, string):
        """
        :type string: str
        """
        assert string, "Your number incorrect"
        result = 0
        size = len(string)
        index = 0
        incorrect = 0
        self.check_strange(string)

        while index < size:
            assert incorrect < 3, "Your number incorrect"
            first_num = self.map.get(string[index])
            assert first_num, "Your number incorrect"

            if index != size - 1:
                second_num = self.map.get(string[index + 1])
                if first_num < second_num:
                    if index > 0:
                        prev = self.map.get(string[index - 1])
                        assert first_num < prev, "Your number incorrect"

                    assert second_num == 2 * first_num, "Your number incorrect"
                    assert second_num // 10 <= first_num, "Your number incorrect"
                    assert not (first_num == 5 or first_num == 50 or first_num == 500), "Your number incorrect"
                    result += second_num - first_num
                    index += 2
                    continue
                if first_num == 5 or first_num == 50 or first_num == 500:
                    if (size - 1 - index) > 1:
                        after_num = self.map.get(string[index + 2])
                        assert after_num <= first_num // 5, "Your number incorrect"
                if first_num == second_num:
                    assert not (first_num == 5 or first_num == 50 or first_num == 500), "Your number incorrect"
                    incorrect += 1
                else:
                    incorrect = 0
            result += first_num
            index += 1
        if result > 3999:
            result %= 4000
        return result

    def to_rim(self, inti):
        """
        :type inti: int
        """
        assert inti is not None, "Your number incorrect"
        if inti > 3999:
            inti %= 4000
        result = ""
        inti1k = inti // 1000
        if inti1k:
            for _ in range(inti1k):
                result += "M"
            result += self.to_rim(inti % 1000)
        elif inti // 900:
            result += "CM"
            result += self.to_rim(inti % 900)
        elif inti // 500:
            result += "D"
            result += self.to_rim(inti % 500)
        elif inti // 400:
            result += "CD"
            result += self.to_rim(inti % 400)
        elif inti // 100:
            for _ in range(inti // 100):
                result += "C"
            result += self.to_rim(inti % 100)
        elif inti // 90:
            result += "XC"
            result += self.to_rim(inti % 90)
        elif inti // 50:
            result += "L"
            result += self.to_rim(inti % 50)
        elif inti // 40:
            result += "XL"
            result += self.to_rim(inti % 40)
        elif inti // 10:
            for _ in range(inti // 10):
                result += "X"
            result += self.to_rim(inti % 10)
        elif inti // 9:
            result += "IX"
            result += self.to_rim(inti % 9)
        elif inti // 5:
            result += "V"
            result += self.to_rim(inti % 5)
        elif inti // 4:
            result += "IV"
            result += self.to_rim(inti % 4)
        elif inti:
            for _ in range(inti):
                result += "I"
        return result

    @staticmethod
    def check_strange(string):
        lenn = len(string)
        for idx in range(3, lenn):
            rim_num = ""
            if idx == 3:
                rim_num = "I"
            elif idx == 4:
                rim_num = "V"
            elif idx == 7:
                rim_num = "X"
            elif idx == 8:
                rim_num = "L"
            elif idx == 11:
                rim_num = "C"
            elif idx == 12:
                rim_num = "D"
            elif idx == 15:
                rim_num = "M"
            for corrix in range(0, lenn - idx):
                assert string[corrix] != rim_num, "Your number incorrect"

s1 = input("Enter first number >>>")
rim1 = RimMul(s1)
s2 = input("Enter second number >>>")
rim2 = RimMul(s2)
print(str(rim1), " + ", str(rim2), " = ", str(rim1 + rim2))
print(str(rim1), " - ", str(rim2), " = ", str(rim1 - rim2))
print(str(rim1), " * ", str(rim2), " = ", str(rim1 * rim2))
print(str(rim1), " / ", str(rim2), " = ", str(rim1 / rim2))
