contact={}
#choice filling
while True:
    choice= int(input("1.Add a new contact/n 2.Search contact/n 3.Delete a contact/n 4.Edit contact/n 5. view all contacts/n 6. quit"))
#logic behind choices
    if choice==1:
        name=input("Pls enter the name of the contact:")
        phone=input("Pls enter the contact's phone: ")
        contact[name]=phone
    elif choice==2:
        search_contact=input("Pls enter the name: ")
        if search_contact in  contact:
            print (search_contact," 's contact number is: " , contact[search_contact])
        else:
            print("Contact not found!!")
    elif choice==3:
        del_contact=input("Enter the contact name: ")
        if del_contact in contact:
            confirm=input("Are you sure.(once the contact is deleted , it would not be restore. )y/n")
            if "y" in confirm or "Y" in confirm:
                contact.pop(del_contact)
                print("successfully deleted contact!!")
            if "n" in confirm or "N" in confirm:
                print("The contact was not deleted.")
        else:
            print("contact not found.!")
    elif choice==4:
        edit_contact=input("Pls enter the contact to be edited: ")
        if edit_contact in contact:
            phone=int(input("Pls enter the mobile number: "))
            contact[edit_contact ]=phone 
            print("Contact editied.")
        else:
            print("Contact not found")        
    elif choice==5:
        print(contact)       
    else:
        quit()

#Thanks for viewing this code. Stay tuned for more fun projects.
