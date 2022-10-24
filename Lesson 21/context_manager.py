import json
import logging
from pprint import pprint

logging.basicConfig(
    filename="phonebook.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class Phonebook:
    def __init__(self, file):
        self.file = file

    def write(self, number, first_name, last_name, city):
        data = json.load(self.file)
        new_entry = {
            "first_name": first_name,
            "last_name": last_name,
            "city": city,
        }
        data[number] = new_entry
        self.file.seek(0)
        json.dump(data, self.file, indent=4)
        logging.info(f"write new entry {number} to {self.file.name}")

    def read(self):
        data = json.load(self.file)
        logging.info(f"read {self.file.name}")
        return data


class ManagedPhonebook:
    counter = 0

    def __init__(self, filepath, method="r+"):
        ManagedPhonebook.counter += 1
        self.filepath = filepath
        self.method = method
        self.file = None

    def __enter__(self):
        logging.info(f"open {self.filepath}")
        try:
            self.file = open(self.filepath, self.method)
            return Phonebook(self.file)
        except FileNotFoundError:
            logging.error(f"not found {self.filepath}")
            raise FileNotFoundError(f"file '{self.filepath}' not exist")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            logging.error(f"{exc_type}, {exc_value}")
        logging.info(f"close {self.filepath}")
        return True


if __name__ == "__main__":
    with ManagedPhonebook("phonebook.json") as file:
        file.write("0671234567", "Tom", "Hanks", "Concord")

    with ManagedPhonebook("phonebook.json") as file:
        pprint(file.read())

    with ManagedPhonebook("phonebook.json") as file:
        file.dosomething()
