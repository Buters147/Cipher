
#Dictionary: Letters to numbers
d = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4,
     "f": 5, "g": 6, "h": 7, "i": 8, "j": 9,
     "k": 10, "l": 11, "m": 12, "n": 13, "o": 14,
     "p": 15, "q": 16, "r": 17, "s": 18, "t": 19,
     "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25,
     "A": 26, "B": 27, "C": 28, "D": 29, "E": 30,
     "F": 31, "G": 32, "H": 33, "I": 34, "J": 35,
     "K": 36, "L": 37, "M": 38, "N": 39, "O": 40,
     "P": 41, "Q": 42, "R": 43, "S": 44, "T": 45,
     "U": 46, "V": 47, "W": 48, "X": 49, "Y": 50, "Z": 51
     }

#Dictionary: Numbers to letters
e = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e",
     5: "f", 6: "g", 7: "h", 8: "i", 9: "j",
     10: "k", 11: "l", 12: "m", 13: "n", 14: "o",
     15: "p", 16: "q", 17: "r", 18: "s", 19: "t",
     20: "u", 21: "v", 22: "w", 23: "x", 24: "y", 25: "z",
     26: "A", 27: "B", 28: "C", 29: "D", 30: "E",
     31: "F", 32: "G", 33: "H", 34: "I", 35: "J",
     36: "K", 37: "L", 38: "M", 39: "N", 40: "O",
     41: "P", 42: "Q", 43: "R", 44: "S", 45: "T",
     46: "U", 47: "V", 48: "W", 49: "X", 50: "Y", 51: "Z"
     }

#Number of key-value-pairs
length = len(e)

t = input("Enter your text here: ")
l = list(t) #Conversion to a list
#print(l)
h = int(len(l) / (length+1))

#Punctuation marks we want to eliminate for the simple cipher
space = []
question = []
full_stop = []
comma = []
exclamation = []
semicolon = []
colon = []
open = []
close = []
hypen = []
apostrohe = []
quotation = []
zero = []
one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []

for i in range(len(l)):
    if l[i] == " ":
        space.append(i)
    if l[i] == "?":
        question.append(i)
    if l[i] == ".":
        full_stop.append(i)
    if l[i] == ",":
        comma.append(i)
    if l[i] == "!":
        exclamation.append(i)
    if l[i] == ";":
        semicolon.append(i)
    if l[i] == ":":
        colon.append(i)
    if l[i] == "(":
        open.append(i)
    if l[i] == ")":
        close.append(i)
    if l[i] == "-":
        hypen.append(i)
    if l[i] == "'":
        apostrohe.append(i)
    if l[i] == '"':
        quotation.append(i)
    if l[i] == "0":
        zero.append(i)
    if l[i] == "1":
        one.append(i)
    if l[i] == "2":
        two.append(i)
    if l[i] == "3":
        three.append(i)
    if l[i] == "4":
        four.append(i)
    if l[i] == "5":
        five.append(i)
    if l[i] == "6":
        six.append(i)
    if l[i] == "7":
        seven.append(i)
    if l[i] == "8":
        eight.append(i)
    if l[i] == "9":
        nine.append(i)


#List of positions for the punctuation marks
general = []
#List of punctuation marks
unit = []

for i in range(len(l)):
    if l[i] == " " or l[i] == "?" or l[i] == "." or l[i] == "," or l[i] == "!" or l[i] == ";" \
            or l[i] == ":" or l[i] == "(" or l[i] == ")" or l[i] == "-" or l[i] == "'" or l[i] == '"' \
            or l[i] == "0" or l[i] == "1" or l[i] == "2" or l[i] == "3" or l[i] == "4" or l[i] == "5" \
            or l[i] == "6" or l[i] == "7" or l[i] == "8" or l[i] == "9":
        general.append(i)
        unit.append(l[i])

print(general)
print(unit)

for i in range(len(space)):
    l.remove(" ")
for i in range(len(question)):
    l.remove("?")
for i in range(len(full_stop)):
    l.remove(".")
for i in range(len(comma)):
    l.remove(",")
for i in range(len(exclamation)):
    l.remove("!")
for i in range(len(semicolon)):
    l.remove(";")
for i in range(len(colon)):
    l.remove(":")
for i in range(len(open)):
    l.remove("(")
for i in range(len(close)):
    l.remove(")")
for i in range(len(hypen)):
    l.remove("-")
for i in range(len(apostrohe)):
    l.remove("'")
for i in range(len(quotation)):
    l.remove('"')
for i in range(len(zero)):
    l.remove("0")
for i in range(len(one)):
    l.remove("1")
for i in range(len(two)):
    l.remove("2")
for i in range(len(three)):
    l.remove("3")
for i in range(len(four)):
    l.remove("4")
for i in range(len(five)):
    l.remove("5")
for i in range(len(six)):
    l.remove("6")
for i in range(len(seven)):
    l.remove("7")
for i in range(len(eight)):
    l.remove("8")
for i in range(len(nine)):
    l.remove("9")

#print(l)

#Get a list of decryption numbers
y = []
y = list(range(1, (length+1)))*(h+1)

#for i in range(len(l)):
#    y.append(random.randint(1, 27))

#print(y)

#Decryption
#Define an empty list
m = []

i = 0
while i < len(l):
    m.append(e[(d[l[i]] + y[i]) % length])
    i = i + 1

for i in range(len(general)):
    m.insert(general[i], unit[i])

#Define a help string
s = ""

j = 0
while j < len(m):
    s = s + m[j]
    j = j + 1

print("Decrypted Text: " + s)

#Encryption

l = list(s)
#print(l)
h = int(len(l) / (length+1))

#Punctuation marks we want to eliminate for the simple cipher
space = []
question = []
full_stop = []
comma = []
exclamation = []
semicolon = []
colon = []
open = []
close = []
hypen = []
apostrohe = []
quotation = []
zero = []
one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []

for i in range(len(l)):
    if l[i] == " ":
        space.append(i)
    if l[i] == "?":
        question.append(i)
    if l[i] == ".":
        full_stop.append(i)
    if l[i] == ",":
        comma.append(i)
    if l[i] == "!":
        exclamation.append(i)
    if l[i] == ";":
        semicolon.append(i)
    if l[i] == ":":
        colon.append(i)
    if l[i] == "(":
        open.append(i)
    if l[i] == ")":
        close.append(i)
    if l[i] == "-":
        hypen.append(i)
    if l[i] == "'":
        apostrohe.append(i)
    if l[i] == '"':
        quotation.append(i)
    if l[i] == "0":
        zero.append(i)
    if l[i] == "1":
        one.append(i)
    if l[i] == "2":
        two.append(i)
    if l[i] == "3":
        three.append(i)
    if l[i] == "4":
        four.append(i)
    if l[i] == "5":
        five.append(i)
    if l[i] == "6":
        six.append(i)
    if l[i] == "7":
        seven.append(i)
    if l[i] == "8":
        eight.append(i)
    if l[i] == "9":
        nine.append(i)


#List of positions for the punctuation marks
general = []
#List of punctuation marks
unit = []

for i in range(len(l)):
    if l[i] == " " or l[i] == "?" or l[i] == "." or l[i] == "," or l[i] == "!" or l[i] == ";" \
            or l[i] == ":" or l[i] == "(" or l[i] == ")" or l[i] == "-" or l[i] == "'" or l[i] == '"' \
            or l[i] == "0" or l[i] == "1" or l[i] == "2" or l[i] == "3" or l[i] == "4" or l[i] == "5" \
            or l[i] == "6" or l[i] == "7" or l[i] == "8" or l[i] == "9":
        general.append(i)
        unit.append(l[i])

print(general)
print(unit)

for i in range(len(space)):
    l.remove(" ")
for i in range(len(question)):
    l.remove("?")
for i in range(len(full_stop)):
    l.remove(".")
for i in range(len(comma)):
    l.remove(",")
for i in range(len(exclamation)):
    l.remove("!")
for i in range(len(semicolon)):
    l.remove(";")
for i in range(len(colon)):
    l.remove(":")
for i in range(len(open)):
    l.remove("(")
for i in range(len(close)):
    l.remove(")")
for i in range(len(hypen)):
    l.remove("-")
for i in range(len(apostrohe)):
    l.remove("'")
for i in range(len(quotation)):
    l.remove('"')
for i in range(len(zero)):
    l.remove("0")
for i in range(len(one)):
    l.remove("1")
for i in range(len(two)):
    l.remove("2")
for i in range(len(three)):
    l.remove("3")
for i in range(len(four)):
    l.remove("4")
for i in range(len(five)):
    l.remove("5")
for i in range(len(six)):
    l.remove("6")
for i in range(len(seven)):
    l.remove("7")
for i in range(len(eight)):
    l.remove("8")
for i in range(len(nine)):
    l.remove("9")

#Get a list of decryption numbers
y = []
y = list(range(1, (length+1)))*(h+1)

#for i in range(len(l)):
#    y.append(random.randint(1, 27))

#print(y)

#Encryption
#Define an empty list
m = []

i = 0
while i < len(l):
    m.append(e[(d[l[i]] + (length-y[i])) % length])
    i = i + 1

for i in range(len(general)):
    m.insert(general[i], unit[i])

#Define a help string
t = ""

j = 0
while j < len(m):
    t = t + m[j]
    j = j + 1

print("Decrypted Text: " + t)

input("Press Enter to terminate the program!")

'''
#Get a list of decryption numbers
y = []
for i in range(len(l)):
    y.append(random.randint(1, 31))

print(y)

#Dictionary: Letters to numbers
d = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4,
     "f": 5, "g": 6, "h": 7, "i": 8, "j": 9,
     "k": 10, "l": 11, "m": 12, "n": 13, "o": 14,
     "p": 15, "q": 16, "r": 17, "s": 18, "t": 19,
     "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25,
     " ": 26, ".": 27, ",": 28, "!": 29, "?": 30
     }

#Dictionary: Numbers to letters
e = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e",
     5: "f", 6: "g", 7: "h", 8: "i", 9: "j",
     10: "k", 11: "l", 12: "m", 13: "n", 14: "o",
     15: "p", 16: "q", 17: "r", 18: "s", 19: "t",
     20: "u", 21: "v", 22: "w", 23: "x", 24: "y", 25: "z",
     26: " ", 27: ".", 28: ",", 29: "!", 30: "?"
     }

#Decryption
#Define an empty list
m = []

i = 0
while i < len(l):
    m.append(e[(d[l[i]] + y[i]) % 31])
    i = i + 1

#Define a help string
s = ""

j = 0
while j < len(m):
    s = s + m[j]
    j = j + 1

print("Decrypted Text: " + s)


#Encryption
m = []

i = 0
while i < len(l):
    m.append(e[(d[s[i]] + (31-y[i])) % 31])
    i = i + 1

#Define a help string
s = ""

j = 0
while j < len(m):
    s = s + m[j]
    j = j + 1

print("Encrypted Text: " + s)

input("Press Enter to terminate the program!")
'''
