import smtplib, ssl
import getpass
import string

def encrypt(text, shift):
    orig_lc = string.ascii_lowercase
    tran_lc = orig_lc[(shift % 26):] + orig_lc[:shift % 26] 
    orig_uc = string.ascii_uppercase
    tran_uc = orig_uc[shift % 26:] + orig_uc[:shift % 26]
    table_lc = str.maketrans(orig_lc, tran_lc)
    table_uc = str.maketrans(orig_uc, tran_uc)
    return text.translate(table_uc).translate(table_lc) 



if __name__ == "__main__":
    
    smtp_server='smtp.gmail.com'
    port = 465

    sender='mjcsba98@gmail.com'
    password = getpass.getpass('Enter the password- ')

    receiver = 'amardeep.mj@gmail.com','mjcsba98@gmail.com'

    context= ssl.create_default_context()

    text = input("Enter string- ")
    s = int(input("Enter shift number- "))

    encrypted = f'{encrypt(text, s)}\n{str(s)}'

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, encrypted)
