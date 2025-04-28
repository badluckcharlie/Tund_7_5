from class1 import *
#saada_kiri()

print("Welcome to phones numbers and emails archive")
print("_"*20)

archieve= load_archieve("archieve.txt")
#archieve=[[],[],[]]

while True:
    print("_"*20)
    print("Options:")
    print("1. Add new contact")
    print("2. Change contact")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Show archieve")
    print("6. Show archieve by name")
    print("7. Send Email")
    print("8. SAVE CHANGES")
    print("9. EXIT")

    try:
        choice= print("Select option: ")
    except ValueError:
        print("input Error")
        continue
    if choice == 1:
        name = input("Enter new contact name: ")
        number = input("Enter new contact number: ")
        email = input("Enter new contact email: ")
        print(add_contact(archieve, name, number, email))
    elif choice == 2:
        name = input("Enter contact name to change: ")
        new_name = input("Enter new contact name: ")
        new_number = input("Enter new contact number: ")
        new_email = input("Enter new contact email: ")
        print(change_contact(archieve, name, new_name, new_number, new_email))
    elif choice == 3:
        contact = input("Enter contact name, number or email to search: ")
        print(search_contact(archieve, contact))
    elif choice == 4:
        name = input("Enter contact name to delete: ")
        print(delete_contact(archieve, name))
    elif choice == 5:
        show_archieve(archieve)
    elif choice == 6:
        sort_archieve(archieve)
        print("Archieve sorted by name")
    elif choice == 7:
        send_email()
    elif choice == 8:
        save_archieve(archieve, "archieve.txt")
        print("Changes saved")
    elif choice == 9:
        print("Exiting program...")
        break
