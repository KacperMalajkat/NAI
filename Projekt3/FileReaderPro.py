import csv


def readfile(filepath, delimiter=';', pierwszalinia=True):
    with open(filepath, newline='') as plik:
        data = list(csv.reader(plik, delimiter=delimiter))
        if len(data[-1]) != len(data[-2]):
            data.pop()
        if not pierwszalinia:
            data.pop(0)
        return data
