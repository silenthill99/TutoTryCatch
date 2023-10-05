import json


class FileNotJsonFormatError(Exception):
    def __init__(self):
        self.message = "Veuillez faire attention au format"


def read_json_file(file_name):
    try:
        if not file_name.endswith('.json'):
            raise FileNotJsonFormatError
        fichier = open(file_name)
        print(json.load(fichier))
        fichier.close()
    except FileNotFoundError:
        print("Ce fichier n'existe pas !")

read_json_file('bonjour.txt')