import json
import os

import pytest

from phonebook import (
    app_run,
    add_new,
    update,
    delete,
    search_by_number,
    search_by_first_name,
    search_by_last_name,
    search_by_full_name,
    search_by_city,
)


def patched_input(*args):
    for command in args:
        yield command


@pytest.fixture
def phonebook():
    with open("contacts.json", "w") as file:
        data = {
            "contacts": [
                {
                    "first name": "Ihor",
                    "last name": "Taran",
                    "phone number": "0501234567",
                    "city": "Lviv",
                }
            ]
        }
        json.dump(data, file)
    yield data
    os.remove("contacts.json")


def test_app_run(phonebook, monkeypatch):
    generator = patched_input(
        "a", "Mark", "Zuckerberg", "0971234567", "Chernivtsi", "e"
    )
    monkeypatch.setattr("builtins.input", lambda _: next(generator))
    app_run("contacts.json")


def test_add_new(phonebook, monkeypatch):
    contact = {
        "first name": "Bill",
        "last name": "Gates",
        "phone number": "0631234567",
        "city": "Kyiv",
    }
    generator = patched_input("Bill", "Gates", "0631234567", "Kyiv")
    monkeypatch.setattr("builtins.input", lambda _: next(generator))

    assert add_new(phonebook) == contact


def test_delete(phonebook, monkeypatch):
    generator = patched_input("y")
    monkeypatch.setattr("builtins.input", lambda _: next(generator))
    delete("0501234567", phonebook)
    assert phonebook == {"contacts": []}


def test_update(phonebook, monkeypatch):
    updated_phonebook = {
        "contacts": [
            {
                "first name": "Ihor",
                "last name": "Taran",
                "phone number": "0501234567",
                "city": "Sumy",
            }
        ]
    }
    generator = patched_input("0501234567", "c", "Sumy", "e")
    monkeypatch.setattr("builtins.input", lambda _: next(generator))
    update("0501234567", phonebook)
    assert phonebook == updated_phonebook


def test_search_by_first_name(phonebook):
    assert search_by_first_name("Ihor", phonebook)
    assert search_by_first_name("Billy", phonebook) is False


def test_search_by_last_name(phonebook):
    assert search_by_last_name("Taran", phonebook)
    assert search_by_last_name("Herrington", phonebook) is False


def test_search_by_full_name(phonebook):
    assert search_by_full_name("Ihor Taran", phonebook)
    assert search_by_full_name("Billy Herrington", phonebook) is False


def test_search_by_number(phonebook):
    assert search_by_number("0501234567", phonebook)
    assert search_by_number("0691234567", phonebook) is False


def test_search_by_city(phonebook):
    assert search_by_city("Lviv", phonebook) == 1
    assert search_by_city("New York", phonebook) == 0
