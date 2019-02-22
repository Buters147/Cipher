
#Dictionary: Letters to numbers
d = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4,
     "f": 5, "g": 6, "h": 7, "i": 8, "j": 9,
     "k": 10, "l": 11, "m": 12, "n": 13, "o": 14,
     "p": 15, "q": 16, "r": 17, "s": 18, "t": 19,
     "u": 20, "v": 21, "w": 22, "x": 23, "y": 24,
     "z": 25, " ": 26, ".": 27, "?": 28, "!": 29,
     ",": 30, "1": 31, "2": 32, "3": 33, "4": 34,
     "5": 35, "6": 36, "7": 37, "8": 38, "9": 39,
     "0": 40, ":": 41, ";": 42, "(": 43, ")": 44,
     "ä": 45, "ü": 46, "ö": 47, "'": 48
     }

#Dictionary: Numbers to letters
e = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e",
     5: "f", 6: "g", 7: "h", 8: "i", 9: "j",
     10: "k", 11: "l", 12: "m", 13: "n", 14: "o",
     15: "p", 16: "q", 17: "r", 18: "s", 19: "t",
     20: "u", 21: "v", 22: "w", 23: "x", 24: "y",
     25: "z", 26: " ", 27: ".", 28: "?", 29: "!",
     30: ",", 31: "1", 32: "2", 33: "3", 34: "4",
     35: "5", 36: "6", 37: "7", 38: "8", 39: "9",
     40: "0", 41: ":", 42: ";", 43: "(", 44: ")",
     45: "ä", 46: "ü", 47: "ö", 48: "'"
     }

#Definition of the encryption function:
def encryption(message1):
    i = 0
    while i < len(message1):
        m.append(e[(d[message1[i]] + y[i]) % len(d)])
        i = i + 1

def decryption(message2):
    i = 0
    while i < len(message2):
        n.append(e[(d[message2[i]] + (len(d) - y[i])) % len(d)])
        i = i + 1


t = input("Enter your text here: ")
t = t.lower() #Conversion to lower case letters
l = list(t)
h = int(len(l) / (len(d)+1))
#print(len(t))
#print(h)

#Get a list of increasing numbers
y = list(range(1, (len(d)+1)))*(h+1)
#print(y)


#Encryption
#Define an empty list
m = []

'''
i = 0
while i < len(l):
    m.append(e[(d[l[i]] + y[i]) % len(d)])
    i = i + 1
'''

encryption(l)

#Define a help string
s = ""

j = 0
while j < len(m):
    s = s + m[j]
    j = j + 1

print("Encrypted Text: " + s)


#Decryption
n = []

'''
i = 0
while i < len(s):
    m.append(e[(d[s[i]] + (len(d)-y[i])) % len(d)])
    i = i + 1
'''

decryption(s)

#Define a help string
s = ""

j = 0
while j < len(n):
    s = s + n[j]
    j = j + 1

#print("Decrypted Text: " + s)

input("Press Enter to continue the program!")
print()

#For the decryption
text = input("Enter your encrypted text here: ")

#Decryption
n = []

'''
i = 0
while i < len(s):
    m.append(e[(d[s[i]] + (len(d)-y[i])) % len(d)])
    i = i + 1
'''

decryption(text)

#Define a help string
s = ""

j = 0
while j < len(n):
    s = s + n[j]
    j = j + 1

print("Decrypted Text: " + s)

input("Press Enter to terminate the program!")
