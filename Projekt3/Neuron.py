
class Neuron:
    def __init__(self, wymiary=3, alfa=0.01, active_fun=None, normalizacja=1):
        self.wagi = [0] * wymiary
        self.prog = 0
        self.alfa = alfa
        self.normalizacja = normalizacja
        self.active_fun = active_fun

    def __str__(self):
        return str(self.wagi)

    def iloczyn_skalarny(self, v1, v2):
        if len(v1) != len(v2):
            raise ValueError("Różne długości wektorów!")
        return sum([float(e1) * float(e2) for e1, e2 in zip(v1, v2)])

    def normalizuj(self, v1: list, normalizacja=1):
        x = sum([float(el) ** 2 for el in v1]) ** 0.5
        v1 = [(float(el) * normalizacja) / x for el in v1]
        return v1

    def licz_wartosci(self, vektor: list):
        return self.active_fun(self.iloczyn_skalarny(self.wagi, vektor))

    def napraw_wagi(self, vektor, wzmocnij: bool = True):  # algorytm delta
        if len(vektor) != len(self.wagi):
            raise ValueError("Różne długości wektorów!")

        x = 1 if wzmocnij else -1
        a = self.alfa
        self.wagi = [float(stare) + (x * a * float(nowy)) for stare, nowy in
                     zip(self.wagi, self.normalizuj(vektor, normalizacja=self.normalizacja))]
        self.wagi = self.normalizuj(self.wagi, normalizacja=self.normalizacja)
