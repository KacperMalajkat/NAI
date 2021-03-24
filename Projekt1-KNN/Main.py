import sys
import KNNAlgorithm
import FileReaderPro
import matplotlib.pyplot as plt


k = int(sys.argv[1])
dane_treningowe = FileReaderPro.readFile(sys.argv[2])
dane_testowe = FileReaderPro.readFile(sys.argv[3])

# Test
# k = 3
# FileReaderPro.readFile("C:\\iris.csv")
# FileReaderPro.splitData("C:\\iris.csv")
# dane_treningowe = FileReaderPro.readFile("Trein.csv")
# dane_testowe = FileReaderPro.readFile("Test.csv")


def exit():
    sys.exit(0)


def spr():
    if len(sys.argv) != 4:
        raise TypeError("Niepoprawna liczba argumentow!!!")
        exit()


def fullraport():
    print("\nRAPORT: ")
    KNNAlgorithm.raport(dane_treningowe, dane_testowe, k)
    print("Skutecznosc: ", KNNAlgorithm.take_result(
        dane_treningowe, dane_testowe, k, True))


def add_flower():
    print("Dane kwiatka podajemy w Formacie: x1;x2;x3;x4  :) ")
    kwiatek = input("Podaj dane kwiatka: ")
    dane_kwiatka = kwiatek.split(";")
    print("\nTwoj kwiatek to: ", KNNAlgorithm.predict(
        dane_treningowe, dane_kwiatka, k))


def wykres():

    dane = dict()
    for k in range(1, 100, 1):
        dane[k] = KNNAlgorithm.take_result(
            dane_treningowe, dane_testowe, k)

    show_graf(dane)


def show_graf(dane):
    if isinstance(dane, dict):
        plt.plot(dane.keys(), dane.values())

    plt.title("Wykres")
    plt.xlabel("os X", fontsize=14)
    plt.ylabel("os Y", fontsize=14)
    plt.show()


def switchk(x):
    k = int(x)


def menu():
    print()
    print("\n==============================\n"
          "============ MENU ============\n"
          "==============================\n"
          "select 1 - FULL RAPORT\n"
          "select 2 - WLASNY KWIATKEK\n"
          "select 3 - WYKRES SKUTECZNOSCI\n"
          "select 4 - ZMIEN K\n"
          "select 5 - WYJSCIE\n"
          "==============================\n\n")


while True:
    menu()
    option = input("Wybierz opcje: ")
    if int(option) == 1:
        fullraport()
    elif int(option) == 2:
        add_flower()
    elif int(option) == 3:
        wykres()
    elif int(option) == 4:
        x = input("Podaj k: ")
        switchk(x)
    elif int(option) == 5:
        exit()
    else:
        print("Nie ma takiej opcji :(")
