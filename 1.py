Count = 1
Total = 0
Weight = 10
while Count != 9:
    Digit = int(input("Digit: "))
    DigitValue = Digit * Weight
    Total += DigitValue
    Weight -= 1
Remainder = Total % 11
CheckDigit = 11-Remainder
