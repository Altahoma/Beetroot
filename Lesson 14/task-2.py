def stop_words(words: list):
    def replace_words(func):
        def wrapper(*args):
            new_slogan = func(*args)
            for word in words:
                new_slogan = new_slogan.replace(word, '*')
            return new_slogan
        return wrapper
    return replace_words


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

print(create_slogan('Eugene'))
