from random import randint


#file 1
newFile = open("twitter-banned1.txt", "w")

with open("twitter-banned.txt") as f:
    for data in f.readlines():
        newFile.write(data.capitalize())

newFile.close()



#file 2
newFile1 = open("twitter-banned2.txt", "w")

with open("twitter-banned.txt") as f:
    for data in f.readlines():
        letters = ['a', 'd', 'h', 'j', 'l', 'p', 'q', 'z']
        
        newData = ""
        for c in data.strip():
            if (c in letters):
                newData += c.upper()
            else:
                newData += c
        newData += '\n' 
        newFile1.write(newData)

newFile1.close()



#file 3 = guessable replacements
newFile2 = open("twitter-banned3.txt", "w")

with open("twitter-banned.txt") as f:
    for data in f.readlines():
        replacement = {
            'a' : '@',
            'e' : '3',
            'o' : '0',
        }

        newData = ""
        for c in data.strip():
            if (c in replacement.keys()):
                newData += replacement[c]
            else:
                newData += c
        newData += '\n' 
        newFile2.write(newData)

newFile2.close()



#file 4 guessable replacements (more of them)

newFile3 = open("twitter-banned4.txt", "w")

with open("twitter-banned.txt") as f:
    for data in f.readlines():
        replacement = {
            'a' : '@',
            'e' : '3',
            'o' : '0',
            's' : '5',
            'l' : '1',
            't' : '7',
            'h' : 'H',
            'p' : 'P',
            'w' : 'W',
            'd' : 'D',
            'r' : 'R',
            'n' : 'N'
        }

        newData = ""
        for c in data.strip():
            if (c in replacement.keys()):
                newData += replacement[c]
            else:
                newData += c
        newData += '\n' 
        newFile3.write(newData)

newFile3.close()


#file 5 RANDOM DIGITS AT END OF ORIGNA PASSWORD

newFile4 = open("twitter-banned5.txt", "w")

with open("twitter-banned.txt") as f:
    for data in f.readlines():
        digits = ''.join([str(randint(0, 9)) for _ in range(2)])
        newData = data.strip() + digits + '\n'

        newFile4.write(newData)

newFile4.close()



#file 6 RANDOM DIGITS AT END OF ORIGNA PASSWORD

newFile5 = open("twitter-banned6.txt", "w")

with open("twitter-banned.txt") as f:
    for data in f.readlines():
        digits = ''.join([str(randint(0, 9)) for _ in range(4)])
        newData = data.strip() + digits + '\n'

        newFile5.write(newData)

newFile5.close()



#file 7 weird one have to combine previous password if i 
#understand this correctly...

newFile6 = open("twitter-banned7.txt", "w")

with open("twitter-banned6.txt") as f:
    prevPassword = ""
    for data in f.readlines():
        newData = prevPassword + data
        newFile6.write(newData)
        prevPassword = data.strip()

newFile6.close()


#file 8 guessable replacements (more of them)

newFile3 = open("twitter-banned8.txt", "w")

with open("twitter-banned7.txt") as f:
    for data in f.readlines():
        replacement = {
            'a' : '@',
            'e' : '3',
            'o' : '0',
            's' : '5',
            'l' : '1',
            't' : '7',
            'h' : 'H',
            'p' : 'P',
            'w' : 'W',
            'd' : 'D',
            'r' : 'R',
            'n' : 'N'
        }

        newData = ""
        for c in data.strip():
            if (c in replacement.keys()):
                newData += replacement[c]
            else:
                newData += c
        newData += '\n' 
        newFile3.write(newData)

newFile3.close()
