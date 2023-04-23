def caps_str(str):
    return str.upper()


def caps_str_task_2(str):
    """Функция, переводящая первые буквы каждого слова в строке в верхний регистр"""
    splitted = str.split(' ')
    capitalized_words = [word.capitalize() for word in splitted]
    return " ".join(capitalized_words)

print(caps_str_task_2("asd sad"))