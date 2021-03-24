import csv

# funkcja do odczytu pliku


def readFile(filepath, delimiter=";"):
    with open(filepath, newline='') as file:
        data = list(csv.reader(file, delimiter=delimiter))
        data.pop()
        return data

# dodatkowa funkcja do rozbicia 1 pliku na 2 pliki: iris.vsv -> Trein.csv i Test.csv


def splitData(filepath, trainpath="Trein.csv", testpath="Test.csv", iledanychtestowych=45):
    try:
        dane = readFile(filepath)
    except FileNotFoundError:
        print("Nie udal sie znalezc tego pliku: ", filepath)
        return

    atrybuty = {}
    for atrybut in dane:
        if atrybuty.get(atrybut[-1]) is None:
            atrybuty[atrybut[-1]] = list()

        atrybuty.get(atrybut[-1]).append(atrybut[:-1])

    with open(trainpath, 'w', newline='') as treinfile, open(testpath, 'w', newline='') as testfile:
        treinw = csv.writer(treinfile, delimiter=';', quotechar='|',
                            quoting=csv.QUOTE_MINIMAL)
        testw = csv.writer(testfile, delimiter=';', quotechar='|',
                           quoting=csv.QUOTE_MINIMAL)

        for key in atrybuty.keys():

            for treindata in atrybuty.get(key)[:iledanychtestowych]:
                treinw.writerow(treindata + [key])

            for testdata in atrybuty.get(key)[iledanychtestowych:]:
                testw.writerow(testdata + [key])

    print("Podzielono Dane na: \n", "Dane Treningowe - ",
          iledanychtestowych, "\n", "Dane Testowe - POZOSTALE ")
