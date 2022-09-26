from datetime import datetime


class CustomException(Exception):
    def __init__(self, msg):
        with open('exceptions.txt', 'a+') as file:
            file.write(f'{datetime.now()} - {msg}\n')


raise CustomException('unexpected error')
