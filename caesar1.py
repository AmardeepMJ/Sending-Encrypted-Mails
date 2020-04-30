def encrypt(string, shift):
    cipher=''
    for char in string:
        if char =='':
            cipher = cipher+char
        elif char.isupper():
            cipher = cipher + chr((ord(char)+ shift - 65)%26+65)
        else:
            cipher = cipher + chr((ord(char)+shift-97)%26+97)
    return cipher

text = input("Enter string")
s = int(input("Enter shift number"))*-1
print("original string:",text)
print("after decrypting", encrypt(text,s))