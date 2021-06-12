import sys
from Heart import Heart


def exit():
    sys.exit(0)


def start(app):
    while True:
        print()
        print("\n==============================\n"
              "============ MENU ============\n"
              "==============================\n"
              "select 1 - WAGI NEURONÓW\n"
              "select 2 - SKUTECZNŚĆ\n"
              "select 3 - PEŁNA SKUTECZNOŚĆ\n"
              "select 4 - TRENUJ\n"
              "select 5 - SPRAWDZ W JAKIM\n"
              "JEZYKU JEST TWOJE ZDANIE\n"
              "select 6 - WYJSCIE\n"
              "==============================\n\n")
        option = input("Wybierz opcje: ")
        if int(option) == 1:
            app.show_neurony()
        elif int(option) == 2:
            app.show_skutecznosc()
        elif int(option) == 3:
            app.show_skutecznosc(True)
        elif int(option) == 4:
            app.trening()
        elif int(option) == 5:
            app.jaki_to_jezyk()
        elif int(option) == 6:
            exit()
        else:
            print("Nie ma takiej opcji :(")


def test():
    if len(sys.argv) != 5:
        print("\nNiepoprawna liczba argumentów!\n"
              "Program zostanie uruchomiony z danymi z treści zadania :)\n")
        app = Heart()
        start(app)
    else:
        app = Heart(traindata=sys.argv[1], testdata=sys.argv[2], alfa=float(
            sys.argv[3]), k=int(sys.argv[4]))
        start(app)


def start_app():
    if len(sys.argv) != 5:
        raise TypeError("Niepoprawna liczba argumentow!!!")
    else:
        app = Heart(traindata=sys.argv[1], testdata=sys.argv[2], alfa=float(
            sys.argv[3]), k=int(sys.argv[4]))
        start(app)


test()

# start_app()
