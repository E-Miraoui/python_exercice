# 1. Create a dictionary with 5 contacts
contact_book = {
    "Alice": "123-456-7890",
    "Bob": "234-567-8901",
    "Charlie": "345-678-9012",
    "David": "456-789-0123",
    "Eva": "567-890-1234"
}

# 2. Display the entire contact book
print("Initial Contact Book:")
for name, number in contact_book.items():
    print(f"{name}: {number}")

# 3. Ask the user for a name and display the phone number
search_name = input("\nEnter a name to find their phone number: ")
if search_name in contact_book:
    print(f"{search_name}'s phone number is {contact_book[search_name]}")
else:
    print(f"{search_name} not found in the contact book.")

# 4. Add a new contact
new_name = input("\nEnter the name of the new contact: ")
new_number = input("Enter the phone number: ")
contact_book[new_name] = new_number
print(f"{new_name} added successfully!")

# 5. Update an existing contact's phone number
update_name = input("\nEnter the name of the contact to update: ")
if update_name in contact_book:
    new_number = input("Enter the new phone number: ")
    contact_book[update_name] = new_number
    print(f"{update_name}'s phone number updated successfully!")
else:
    print(f"{update_name} not found in the contact book.")

# 6. Remove a contact
remove_name = input("\nEnter the name of the contact to remove: ")
if remove_name in contact_book:
    contact_book.pop(remove_name)
    print(f"{remove_name} removed successfully!")
else:
    print(f"{remove_name} not found in the contact book.")

# 7. Display the final contact book
print("\nFinal Contact Book:")
for name, number in contact_book.items():
    print(f"{name}: {number}")
