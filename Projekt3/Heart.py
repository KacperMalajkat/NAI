from Neuron import Neuron
import FileReaderPro as fileReader


class Heart:
    def __init__(self, traindata="Data\\test.csv", testdata="Data\\test.csv", alfa=0.05, k=40):
        self.training_data = fileReader.readfile(traindata, ";", False)
        self.test_data = fileReader.readfile(testdata, ";", False)
        self.alfa = float(alfa)
        self.k = int(k)
        self.neurony = dict()
        self.trening()

    def _sgn(self, x: float):
        if x > 1:
            return 1
        elif x < -1:
            return -1
        return x

    def _trenuj(self, k: int):

        for _ in range(0, k):
            for element in self.training_data:
                # dodawanie nowego neuronu po napotkaniu nowej klasy
                if self.neurony.get(element[-1]) is None:
                    self.neurony[element[-1]] = Neuron(wymiary=len(
                        element) - 1, active_fun=self._sgn, normalizacja=2)

                # korekta wag
                otrzymany = self.wybierz(element[:-1])
                if otrzymany != element[-1]:
                    self.neurony.get(otrzymany).napraw_wagi(
                        element[:-1], wzmocnij=False)
                    self.neurony.get(
                        element[-1]).napraw_wagi(element[:-1], wzmocnij=True)

    def trening(self):
        self._trenuj(self.k)
        print("\nZakończono trening\n")

    def wybierz(self, vektor):
        wyniki = dict()
        for neuron in self.neurony:
            wyniki[neuron] = self.neurony.get(neuron).licz_wartosci(vektor)

        wynik = sorted(wyniki.items(), key=lambda x: x[1])[-1][0]
        return wynik

    def skutecznosc(self, szczegolowe=False):
        trafione = 0
        pomylki = {name: {subname: 0 for subname in self.neurony}
                   for name in self.neurony}

        for element in self.test_data:
            w = self.wybierz(element[:-1])
            pomylki.get(element[-1])[w] += 1
            if szczegolowe:
                print(f"Oczekiwany: {element[-1]} Otrzymano: {w}")
            if w == element[-1]:
                trafione += 1

        return trafione / len(self.test_data)

    def show_skutecznosc(self, s=False):
        s = round(self.skutecznosc(s) * 100, 3)
        print(f"Skuteczność: {s}%")

    def show_neurony(self):
        for neuron in [*self.neurony]:
            print(neuron, self.neurony.get(neuron))
            print()

    def jaki_to_jezyk(self):
        text = input("Podaj zdanie: \n")

        if len(text) < 1:
            print("Podane zdanie ma za mało znaków!")
            return

        znaki = {chr(one): 0 for one in range(97, 123)}

        for l in text:
            try:
                znaki[l.lower()] += 1
            except KeyError:
                pass

        suma = sum([l[1] for l in znaki.items()])
        frequency = [float(l[1]) / suma for l in znaki.items()]

        print(f"Zdanie zostało napisane w języku: {self.wybierz(frequency)}")
