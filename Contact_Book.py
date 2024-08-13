import json

# Define the Contact class
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

# Add a contact
def add_contact(contacts, name, phone, email):
    contact = Contact(name, phone, email)
    contacts.append(contact)
    print(f"Contact {name} added.")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    for contact in contacts:
        print(contact)

# Search for a contact by name
def search_contact(contacts, name):
    for contact in contacts:
        if contact.name.lower() == name.lower():
            print(contact)
            return
    print(f"No contact found with name {name}.")

# Update a contact
def update_contact(contacts, name, new_phone=None, new_email=None):
    for contact in contacts:
        if contact.name.lower() == name.lower():
            if new_phone:
                contact.phone = new_phone
            if new_email:
                contact.email = new_email
            print(f"Contact {name} updated.")
            return
    print(f"No contact found with name {name}.")

# Delete a contact
def delete_contact(contacts, name):
    for contact in contacts:
        if contact.name.lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact {name} deleted.")
            return
    print(f"No contact found with name {name}.")

# Save contacts to a file
def save_contacts(contacts, filename):
    with open(filename, 'w') as file:
        json_contacts = [
            {'name': contact.name, 'phone': contact.phone, 'email': contact.email}
            for contact in contacts
        ]
        json.dump(json_contacts, file)
    print(f"Contacts saved to {filename}.")

# Load contacts from a file
def load_contacts(filename):
    contacts = []
    try:
        with open(filename, 'r') as file:
            json_contacts = json.load(file)
            for item in json_contacts:
                contacts.append(Contact(item['name'], item['phone'], item['email']))
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty contact book.")
    return contacts

# Main program loop
def main():
    contacts = load_contacts('contacts.json')
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save & Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(contacts, name, phone, email)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            name = input("Enter name to search: ")
            search_contact(contacts, name)
        elif choice == '4':
            name = input("Enter name to update: ")
            phone = input("Enter new phone (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            update_contact(contacts, name, phone if phone else None, email if email else None)
        elif choice == '5':
            name = input("Enter name to delete: ")
            delete_contact(contacts, name)
        elif choice == '6':
            save_contacts(contacts, 'contacts.json')
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
