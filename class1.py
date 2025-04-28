from re import A
import smtplib,ssl
from email.message import EmailMessage

def load_archieve(file):
    archieve=[[],[],[]]
    try:
        with open(file, "r", encoding="utf-8-sig") as f:
            for line in f:
                name, number, email= line.strip().split("|")
                archieve[0].append(name)
                archieve[1].append(number)
                archieve[2].append(email)
    except FileNotFoundError:
        print("File not found")
    return archieve

def send_email():
    kellele=input("Kellele: ")
    kiri="Tere, see on test"
    smtp_server="smtp.gmail.com"
    smtp_port=587
    kellelt="alexxxey.ivanovvv@gmail.com"
    parool=input("Parool")#"vknn ongl tfdt vuct"
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content(kiri)
    msg['Subject']="Test"
    msg['From']=kellelt
    msg['To']=kellele
    try:
        server=smtplib.SMTP(smtp_server,smtp_port)
        server.starttls(context=context)
        server.login(kellelt,parool)
        server.send_message(msg)
        print("kiri saadetud")
        pass
    except Exception as e:
        print("Viga",e)
    finally:
        server.quit()

def add_contact(archieve, name, number, email):
    archieve[0].append(name)
    archieve[1].append(number)
    archieve[2].append(email)
    return f"The contact '{name}' has been added to the archieve"

def search_contact(archieve, contact):
    if contact in archieve[0] or archieve[1] or archieve[2]:
        if contact in archieve[0]:
            index= archieve[0].index(contact)
        elif contact in archieve[1]:
            index= archieve[1].index(contact)
        else:
            index= archieve[2].index(contact)
        return (f"'{contact}' is found.\n"
    else:
        return f"'{contact}' is not found. "

def delete_contact(archieve, name):
    if name in archieve[0]:
        index = archieve[0].index(name)
        for n in archieve:
            n.pop(index)
        return f"The contact '{name}' has been removed from the archieve."
    
def change_contact(archieve, name, new_name, new_number, new_email):
    if name in archieve[0]:
        index = archieve[0].index(name)
        archieve[0][index] = new_name
        archieve[1][index] = new_number
        archieve[2][index] = new_email
        return f"The {name} has been edited."
    else:
        return f"The {name} is not present within the archieve."

#def sort_archieve:

def show_archieve(archieve):
    return [f"{archieve[0][i]} - {archieve[1][i]} {archieve[2][i]}" for i in range(len(dictionary[0]))]

def save_archieve(archieve, file):
    with open(file, "w", encoding="utf-8-sig") as f:
        for i in range(len(archieve[0])):
            f.write(f"{archieve[0][i]}|{archieve[1][i]}|{archieve[2][i]}\n}")


#saada_kiri()
