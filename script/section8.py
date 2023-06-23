#problem 12
inStr = input("문자열을 입력하세요 : ")
up = ''
low = ''
digit = ''
korean = ''
etc = ''
strLen = len(inStr)

for char in inStr:
    if char.isupper():
        up+=char
    elif char.islower():
        low += char
    elif char.isdigit():
        digit += char
    elif char.isalpha():
        korean +=char
    else:
        etc +=char

print("uuper : ", up)
print("lower : ", low)
print("digit : ", digit)
print("korean : ", korean)
print("etc : ", etc)
