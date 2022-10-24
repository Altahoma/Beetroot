import json
import os
import pytest
from context_manager import Phonebook, ManagedPhonebook


@pytest.fixture
def phonebook():
    file_path = "test_phonebook.json"
    with open(file_path, "w") as file:
        data = {
            "0931234567": {"first_name": "Tim", "last_name": "Cook", "city": "Mobile"}
        }
        json.dump(data, file)
    yield file_path
    os.remove(file_path)


def test_enter_context_manager_file_exist(phonebook):
    with ManagedPhonebook(phonebook) as file:
        assert isinstance(file, Phonebook)


def test_enter_context_manager_file_not_exist():
    with pytest.raises(FileNotFoundError):
        with ManagedPhonebook("not_exist.json"):
            pass


def test_phonebook_read(phonebook):
    data = {"0931234567": {"first_name": "Tim", "last_name": "Cook", "city": "Mobile"}}
    with ManagedPhonebook(phonebook) as file:
        file_data = file.read()
    assert data == file_data


def test_phonebook_write(phonebook):
    data = {
        "0931234567": {"first_name": "Tim", "last_name": "Cook", "city": "Mobile"},
        "0631234567": {"first_name": "Tom", "last_name": "Jobs", "city": "Seattle"},
    }
    with ManagedPhonebook(phonebook) as file:
        file.write("0631234567", "Tom", "Jobs", "Seattle")
    with ManagedPhonebook(phonebook) as file:
        file_data = file.read()
    assert data == file_data
