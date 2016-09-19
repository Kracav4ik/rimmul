class RimMul:
    def __init__(self, string):
        self.string = string
        self.map = {
            "0": 0,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        self.i = 0

    def __add__(self, other):
        num1 = self.to_num(self.string)
        num2 = self.to_num(other.string)
        return RimMul(self.to_rim((num1 + num2) % 4000))

    def __sub__(self, other):
        num1 = self.to_num(self.string)
        num2 = self.to_num(other.string)
        return RimMul(self.to_rim(num1 - num2))

    def __divmod__(self, other):
        num1 = self.to_num(self.string)
        num2 = self.to_num(other.string)
        return RimMul(self.to_rim(num1 // num2))

    def __mul__(self, other):
        num1 = self.to_num(self.string)
        num2 = self.to_num(other.string)
        return RimMul(self.to_rim((num1 * num2) % 4000))

    def print(self):
        print(self.string)

    def to_num(self, string):
        """
        :type string: str
        """
        result = 0
        j = len(string)
        i = 0
        uncorrect = 0
        while i < j:
            if uncorrect >= 3:
                print("Fuck you no\n")
                return
            first_num = self.map.get(string[i])
            if i != j - 1:
                second_num = self.map.get(string[i + 1])
                if first_num < second_num:
                    if i > 0:
                        if first_num == self.map.get(string[i - 1]):
                            print("Fuck you no\n")
                            return
                    result += second_num - first_num
                    i += 2
                    continue
                if first_num == second_num:
                    uncorrect += 1
                else:
                    uncorrect = 0
            result += first_num
            i += 1
        if result > 3999:
            print("Fuck you no\n")
            return
        return result

    def to_rim(self, inti):
        """
        :type inti: int
        """
        if inti > 3999:
            print("Fuck you no\n")
            return
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

