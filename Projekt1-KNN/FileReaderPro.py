import csv

# funkcja do odczytu pliku


def readFile(filepath, delimiter=";"):
    with open(filepath, newline='') as file:
        data = list(csv.reader(file, delimiter=delimiter))
        data.pop()
        return data
