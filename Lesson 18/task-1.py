import re


VALID_EMAILS = ['abc-d@mail.com', 'abc.def@mail.com', 'abc@mail.com', 'abc_def@mail.com',
                'abc.def@mail.cc', 'abc.def@mail-archive.com', 'abc.def@mail.org', 'abc.def@mail.com']

INVALID_EMAILS = ['abc-@mail.com',  'abc..def@mail.com', '.abc@mail.com', 'abc#def@mail.com',
                  'abc.def@mail.c', 'abc.def@mail#archive.com', 'abc.def@mail', 'abc.def@mail..com']


class CreateEmail:
    def __init__(self, email):
        self.email = email
        self.is_valid = self.validate(email)

    @staticmethod
    def validate(email):
        regex = r'([A-Za-z0-9]+[-._])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})'

        if re.fullmatch(regex, email):
            print(f'valid - {email}')
            return True
        else:
            print(f'invalid - {email}')
            return False


my_email = CreateEmail('blizzard@horde.com')

for current_email in VALID_EMAILS:
    assert CreateEmail.validate(current_email)

for current_email in INVALID_EMAILS:
    assert CreateEmail.validate(current_email) is False
