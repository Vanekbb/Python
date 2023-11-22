'''

Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.

Input: a a a b c a a d c d d

Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

'''

inputData = "a a a b c a a d c d d"
inputList = inputData.split()

countDict = {}
output = ""

for letter in inputList:
    output += letter
    if letter in countDict:
        countDict[letter] += 1
        output += f"_{countDict[letter]}"
    else:
        countDict[letter] = 0
    output += " "

print(output)

# 2

for letter in inputList:
    numberLetter = countDict.get(letter, 0) + 1
    countDict.setdefault(letter, countDict.get(letter) + 1)
    output += " "

print(output)