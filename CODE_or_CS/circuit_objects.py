

class ThreeToEightDecoder:

    def __init__(self, binput):

        self.binput = str(binput)
        self.s2 = int(self.binput[0])
        self.s1 = int(self.binput[1])
        self.s0 = int(self.binput[2])

        self.zero = (1 - self.s2) and (1 - self.s1) and (1 - self.s0)
        self.one = (1 - self.s2) and (1 - self.s1) and self.s0
        self.two = (1 - self.s2) and self.s1 and (1 - self.s0)
        self.three = (1 - self.s2) and self.s1 and self.s0
        self.four = self.s2 and (1 - self.s1) and (1 - self.s0)
        self.five = self.s2 and (1 - self.s1) and self.s0
        self.six = self.s2 and self.s1 and (1 - self.s0)
        self.seven = self.s2 and self.s1 and self.s0

        self.result = [self.zero, self.one, self.two, self.three, self.four, self.five, self.six, self.seven]

        self.result_str = '  '.join(map(lambda x: str(self.result.index(x)) if x == 1 else ' ', self.result))

        self.arabic_number = self.result.index(1)

    def __repr__(self):
        return str(self.result) + '\n ' + '|  ' * 8 + '\n 0  1  2  3  4  5  6  7' + '\n ' + self.result_str


class FourToSixteenDecoder:

    def __init__(self, binput):

        self.binput = str(binput)
        self.s3 = int(self.binput[0])
        self.s2 = int(self.binput[1])
        self.s1 = int(self.binput[2])
        self.s0 = int(self.binput[3])


        self.zero = (1 - self.s3) and (1 - self.s2) and (1 - self.s1) and (1 - self.s0)
        self.one = (1 - self.s3) and (1 - self.s2) and (1 - self.s1) and self.s0
        self.two = (1 - self.s3) and (1 - self.s2) and self.s1 and (1 - self.s0)
        self.three = (1 - self.s3) and (1 - self.s2) and self.s1 and self.s0
        self.four = (1 - self.s3) and self.s2 and (1 - self.s1) and (1 - self.s0)
        self.five = (1 - self.s3) and self.s2 and (1 - self.s1) and self.s0
        self.six = (1 - self.s3) and self.s2 and self.s1 and (1 - self.s0)
        self.seven = (1 - self.s3) and self.s2 and self.s1 and self.s0

        self.eight = self.s3 and (1 - self.s2) and (1 - self.s1) and (1 - self.s0)
        self.nine = self.s3 and (1 - self.s2) and (1 - self.s1) and self.s0
        self.ten = self.s3 and (1 - self.s2) and self.s1 and (1 - self.s0)
        self.eleven = self.s3 and (1 - self.s2) and self.s1 and self.s0
        self.twelve = self.s3 and self.s2 and (1 - self.s1) and (1 - self.s0)
        self.thirteen = self.s3 and self.s2 and (1 - self.s1) and self.s0
        self.fourteen = self.s3 and self.s2 and self.s1 and (1 - self.s0)
        self.fifteen = self.s3 and self.s2 and self.s1 and self.s0


        self.result = [self.zero, self.one, self.two, self.three, self.four, self.five, self.six, self.seven,
                       self.eight, self.nine, self.ten, self.eleven, self.twelve, self.thirteen, self.fourteen,
                       self.fifteen]
        self.arabic_number = self.result.index(1)

        self.result_str = '  '.join(map(lambda x: str(self.result.index(x)) if x == 1 else ' ', self.result))

        if self.arabic_number >= 10:
            self.result_str = self.result_str[1:]


    def __repr__(self):
        return str(self.result) + '\n ' + '|  ' * 16 + '\n 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15' + '\n ' + self.result_str


print(FourToSixteenDecoder('1001'))