
def __count_distance(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Podane wektory maja rozne wymiary!")
    else:
        v3 = [abs(float(x) - float(y)) for x, y in zip(v1, v2)]
        return sum([z ** 2 for z in v3])
# przypisanie kategorii do odleglosci


def __tag(v1, v2):
    return [v1[-1], __count_distance(v1[:-1], v2)]


def predict(data, vector, k):
    distanceList = [__tag(v, vector) for v in data]
    sorteddistancelist = sorted(distanceList, key=lambda l: l[-1])[:k]

    decisionsdict = {}
    for v in sorteddistancelist:
        if decisionsdict.get(v[0]) is None:
            decisionsdict[v[0]] = 0
        decisionsdict[v[0]] += 1

    decision = sorted(decisionsdict, key=lambda el: el[1], reverse=False)[0]

    return decision


def raport(dane_treningowe, dane_testowe, k=3):
    skuteczne = 0
    for przypadek in dane_testowe:
        rezultat = predict(dane_treningowe, przypadek[:-1], k)
        if rezultat == przypadek[-1]:
            skuteczne += 1
        print("Oczekiwano: ", przypadek[-1], " otrzymano: ",
              rezultat, " zgodność: ", rezultat == przypadek[-1])


def take_result(dane_treningowe, dane_testowe, k=3, percent=False):
    skuteczne = 0
    for przypadek in dane_testowe:
        rezultat = predict(dane_treningowe, przypadek[:-1], k)
        if rezultat == przypadek[-1]:
            skuteczne += 1
    if percent:
        return ""+str(round(skuteczne/len(dane_testowe)*100, 2))+"%"
    else:
        return skuteczne/len(dane_testowe)
