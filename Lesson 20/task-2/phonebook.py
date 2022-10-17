import json
from art import text2art


def generate_response(contact=None):
    if contact:
        print("-" * 24)
        print("| {:<20} |".format(contact["first name"] + " " + contact["last name"]))
        print("| {:<20} |".format(contact["phone number"]))
        print("| {:<20} |".format(contact["city"]))
        print("-" * 24)
    else:
        print("No info in PhoneBook")


def add_new(data):
    first_name = input("First name: ")
    second_name = input("Last name: ")
    phone_number = input("Phone number: ")
    city = input("City: ")
    new_contact: dict = {
        "first name": first_name,
        "last name": second_name,
        "phone number": phone_number,
        "city": city,
    }
    print("New entry added successfully!")
    generate_response(new_contact)
    data["contacts"].append(new_contact)
    return new_contact


def delete(request, data):
    matched = 0
    for contact in data["contacts"]:
        if contact["phone number"] == request:
            matched += 1
            generate_response(contact)
            confirm = input(
                "Do you really want to delete all this info? [Y/n]: "
            ).lower()
            if confirm == "y":
                data["contacts"].remove(contact)
                print(
                    f"{contact['first name']} {contact['last name']} has been removed from PhoneBook."
                )
            else:
                print("Deletion stopped.")
    if matched == 0:
        generate_response()


def update(request, data):
    matched = 0
    for contact in data["contacts"]:
        if contact["phone number"] == request:
            matched += 1
            generate_response(contact)
            print('Enter "e" to set the changes and return to main menu')
            print(
                "Items to update:   f - first name   |   l - last name   |   c - city   |   e - exit"
            )
            while True:
                item = input("Which item do you want to update? ")
                if item == "f":
                    new = input("Updated name: ")
                    contact["first name"] = new
                elif item == "l":
                    new = input("Updated surname: ")
                    contact["last name"] = new
                elif item == "c":
                    new = input("Updated city: ")
                    contact["city"] = new
                elif item == "e":
                    print("This contact has been updated.")
                    generate_response(contact)
                    break
                else:
                    print("Unknown parameter")
    if matched == 0:
        generate_response()


def search_by_first_name(request, data):
    matches = 0
    for contact in data["contacts"]:
        if contact["first name"] == request:
            matches += 1
            generate_response(contact)
            return contact
    if matches == 0:
        generate_response()
        return False


def search_by_last_name(request, data):
    matches = 0
    for contact in data["contacts"]:
        if contact["last name"] == request:
            matches += 1
            generate_response(contact)
            return contact
    if matches == 0:
        generate_response()
        return False


def search_by_full_name(request, data):
    matches = 0
    first_name, last_name = request.split()
    for contact in data["contacts"]:
        if contact["first name"] == first_name and contact["last name"] == last_name:
            matches += 1
            generate_response(contact)
            return contact
    if matches == 0:
        generate_response()
        return False


def search_by_number(request, data):
    matches = 0
    for contact in data["contacts"]:
        if request in contact["phone number"]:
            matches += 1
            generate_response(contact)
            return contact
    if matches == 0:
        generate_response()
        return False


def search_by_city(request, data):
    matches = 0
    for contact in data["contacts"]:
        if contact["city"] == request:
            matches += 1
            generate_response(contact)
    if matches == 0:
        generate_response()
    return matches


def print_menu():
    print(
        """                                   MAIN MENU

- a: add new entry          - d: delete by number       - u: update by number
- s: search by first name   - l: search by last name    - f: search by full name
- n: search by number       - c: search by city         - e: exit"""
    )


def app_run(phonebook):
    try:
        with open(phonebook, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"contacts": []}

    print(text2art("< < PhoneBook > >"), end="")
    while True:
        print_menu()
        option = input("\nChoose an option: ")
        if option == "s":
            request = input("Enter the first name: ")
            search_by_first_name(request, data)
        elif option == "l":
            request = input("Enter the last name: ")
            search_by_last_name(request, data)
        elif option == "f":
            request = input("Enter the full name: ")
            search_by_full_name(request, data)
        elif option == "n":
            request = input("Enter the phone number: ")
            search_by_number(request, data)
        elif option == "c":
            request = input("Enter the city: ")
            search_by_city(request, data)
        elif option == "a":
            add_new(data)
        elif option == "d":
            request = input("Enter phone number: ")
            delete(request, data)
        elif option == "u":
            request = input("Enter phone number: ")
            update(request, data)
        elif option == "e":
            print("Saving data...")
            print("Good bye")
            with open(phonebook, "w") as file:
                json.dump(data, file, indent=4)
            break
        else:
            print("Unknown command")


if __name__ == "__main__":
    app_run("contacts.json")
