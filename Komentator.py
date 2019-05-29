class Komentator:
    @staticmethod
    def new_record(message):
        path = "../saves/logs.txt"
        message += "\n"
        with open(path, "a", encoding='utf-8') as file:
            file.write(message)

    @staticmethod
    def clear_file():
        path = "../saves/logs.txt"
        with open(path, "w", encoding='utf-8') as file:
            pass
