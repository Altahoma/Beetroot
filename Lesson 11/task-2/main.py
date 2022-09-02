import json

from pathlib import Path


def phonebook(name):
    if not Path(name).is_file():
        choice = input('Phonebook does not exist. Do you want to create it? (yes/no): ')

        if choice == 'yes':
            with open('phonebook.json', 'w') as file:
                json.dump({}, file)
                print('Phonebook created!')
        return

    while True:
        choice = input('Do you want change or find some data? (change/find/exit): ')

        if choice == 'change':
            choice = input('Do you want add, update or delete an entry? (add/update/delete): ')

            if choice == 'add':
                with open(name, 'r+') as file:
                    file_data = json.load(file)
                    phone = input('Enter a numer: ')
                    new_entry = {
                        'first_name': input('Enter a first name: '),
                        'last_name': input('Enter a last name: '),
                        'city': input('Enter a city name: '),
                    }
                    file_data[phone] = new_entry
                    file.seek(0)
                    json.dump(file_data, file, indent=4)
                    print('Added successfully!')
            elif choice == 'update':
                phone = input('Enter a phone for update: ')

                with open(name, 'r+') as file:
                    file_data = json.load(file)
                    if phone in file_data:
                        new_entry = {
                            'first_name': input('Enter a new first name: '),
                            'last_name': input('Enter a a new last name: '),
                            'city': input('Enter a new city name: '),
                        }
                        file_data[phone] = new_entry
                        file.seek(0)
                        json.dump(file_data, file, indent=4)
                        print('Updated successfully!')
                    else:
                        print('Not find!')
            elif choice == 'delete':
                phone = input('Enter a phone for delete: ')

                with open(name, 'r+') as file:
                    file_data = json.load(file)
                    try:
                        del file_data[phone]
                        file.seek(0)
                        json.dump(file_data, file, indent=4)
                        file.truncate()
                        print('Deleted successfully!')
                    except KeyError:
                        print(f'Not find the entry by number {phone}!')
        elif choice == 'find':
            with open(name, 'r+') as file:
                file_data = json.load(file)
                choice = input('Should find by (first_name/last_name/city)?: ')
                needed = input('Enter the find keyword: ')
                for entry in file_data.values():
                    if entry[choice] == needed:
                        print(entry)
                        break
                else:
                    print('Not find!')
            pass
        else:
            break


phonebook('phonebook.json')
