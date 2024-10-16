# Contact Book Program

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email, address):
        new_contact = Contact(name, phone_number, email, address)
        self.contacts.append(new_contact)
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts saved.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone_number]
        if not found_contacts:
            print("No contacts found.")
        else:
            print("Search Results:")
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")

    def update_contact(self, name, new_phone_number=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name == name:
                if new_phone_number:
                    contact.phone_number = new_phone_number
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                print(f"Contact {name} updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully!")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone_number, email, address)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == "4":
            name = input("Enter name of contact to update: ")
            new_phone_number = input("Enter new phone number (optional): ")
            new_email = input("Enter new email (optional): ")
            new_address = input("Enter new address (optional): ")
            contact_book.update_contact(name, new_phone_number, new_email, new_address)
        elif choice == "5":
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == "6":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
