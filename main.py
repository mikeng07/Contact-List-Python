# Mike Nguen
# Spring 2024
# Rolodex - contact list that user may search and manipulate. Result may stored in file

import contact
import check_input

def read_file():
    """read in content of file to a list of contact objects"""
    contacts = []
    file = open("addresses.txt")
    for line in file:
        con = line.strip().split(",")
        contacts.append(contact.Contact(con[0], con[1], con[2], con[3], con[4], con[5]))
        # This create a new Contact using data from file. Creating Contact class in module contact
        # Each con represent a different attribute of Contact object
        # New Contact object is appended to contacts list 

    file.close()
    contacts.sort()
    # this sort the contacts list with the implementation of less-than __lt__ method for comparison
    return contacts


def write_file(contacts):
    """write the list of contacts to the file"""
    file = open("addresses.txt", "w")
    # Open file in write mode "w" 
    for c in contacts: 
        file.write(repr(c) + "\n")
        # It write a string representation of each contact to file
        # Using the __repr__ method
        # Add a newline character to next line
    
    file.close()
    # Close file to free up system resources. 


def get_menu_choice():
    """Display the main menu to user and return their valid input"""
    print("Rolodex Menu: \n"
          "1. Display Contact\n"
          "2. Add Contact\n"
          "3. Search Contacts\n"
          "4. Modify Contact\n"
          "5. Save and Quit")
    
    return check_input.get_int_range("> ", 1, 5)


def modify_contact(con):
    """Display s the modification menu to user so they can choose what data to update on the contact"""
    option = 0
    while option != 7:
        print("Modifly Menu: \n"
              "1. First Name\n"
              "2. Last Name\n"
              "3. Phone\n"
              "4. Address\n"
              "5. City\n"
              "6. Zip\n"
              "7. Save\n")
        
        option = check_input.get_int_range("> ", 1, 7)
        options ={
            # a dictionary of possible option
            1: "first_name",
            2: "last_name",
            3: "phone",
            4: "address",
            5: "city",
            6: "zip"
        }
        
        if option in options:
            setattr(con, options[option], input(f"Enter {options[option].replace('_',' ')}: "))
            # set attribute of contact object
            # take 3 argument: the object to set, the attribute name as string, new value for attribute
            # replace will replace the _ with a white space

def main():

    contacts = read_file()
    choice = 0 
    while choice != 5:
        choice = get_menu_choice()
        if choice == 1:
            # Display contact
            print("Numer of contacts: " + str(len(contacts)))
            for i,c in enumerate(contacts):
                # enumerate is a built in function that return an iterator
                # generate a pair of index and coressponding value of object
                # ie. you iterate, it yeild tupples containing 2 element: index and item
                print (str(i + 1) + ". " + str(c) + "\n")

        elif choice == 2:
            #Add contact
            print("Enter new contact: ")
            fn = input("First name: ")
            ln = input("Last name: ")
            ph = input("Phone #: ")
            addr = input("Address: ")
            city = input("City: ")
            zip = input("Zip: ")
            c = contact.Contact(fn, ln, ph, addr, city, zip)
            contacts.append(c)
            contacts.sort()

        elif choice == 3:
            #Search contacts
            print("Search: \n"
                  "1. Search by last name\n"
                  "2. Search by zip\n")
            
            opt = check_input.get_int_range("> ",1,2)
            if opt == 1:
                name = input ("Enter last name: ")
                for c in contacts:
                    if c.last_name.lower() == name.lower():
                        print(c)
                        print()

            else:
                zip = input ("Enter zip: ")
                for c in contacts:
                    if c.zip == zip:
                        print(c)
                        print()

        elif choice == 4:
            # modify contact
            fn = input("Enter first name: ")
            ln = input("Enter last name: ")

            #look for the contact
            for c in contacts:
                if c.first_name.lower() == fn.lower() and c.last_name.lower() == ln.lower():
                    print(c)
                    modify_contact(c)
            contacts.sort()

        elif choice == 5:
            #save and quit
            write_file(contacts)
            print("Saving File ...\n"
                  "Ending Program")

main()