"""A small in-memory contact book demonstrating dictionaries and loops."""


def main():
    contacts = {}

    while True:
        print("\nContact Book")
        print("1. Add or update contact")
        print("2. Find contact")
        print("3. List contacts")
        print("4. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            if name and phone:
                contacts[name] = phone
                print(f"Saved {name}.")
            else:
                print("Name and phone are required.")
        elif choice == "2":
            name = input("Name to find: ").strip()
            phone = contacts.get(name)
            print(f"{name}: {phone}" if phone else "Contact not found.")
        elif choice == "3":
            if not contacts:
                print("The contact book is empty.")
            else:
                for name, phone in sorted(contacts.items()):
                    print(f"{name}: {phone}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
