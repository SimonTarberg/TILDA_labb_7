class Drama:
    def __init__(self, name, rating, year):
        self.name = name
        self.rating = rating
        self.year = year

    def __str__(self):
        return self.name + " (" + self.year + "), betyg " + self.rating


class DictHash:
    def __init__(self):
        self.dictionary = {}

    def store(self, nyckel, data):
        self.dictionary[nyckel] = data

    def search(self, nyckel):
        return self.dictionary[nyckel]


class HashNode:
    """Noder till klassen Hashtable """

    def __init__(self, key="", data=None):
        """key är nyckeln som anvands vid hashningen
           data är det objekt som ska hashas in"""
        self.key = key
        self.data = data


class Hashtable:

    def __init__(self, size):
        """size: hashtabellens storlek"""
        self.size = size
        # varje plats är en lista med noder (krocklista)
        self.table = []
        for i in range(size):
            self.table.append([])

    def store(self, key, data):
        """key är nyckeln
           data är objektet som ska lagras
           Stoppar in "data" med nyckeln "key" i tabellen."""
        index = self.hashfunction(key)
        for node in self.table[index]:
            if node.key == key:
                node.data = data
                return
        self.table[index].append(HashNode(key, data))

    def search(self, key):
        """key är nyckeln
           Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
           Om "key" inte finns ska det bli KeyError """
        index = self.hashfunction(key)
        for node in self.table[index]:
            if node.key == key:
                return node.data
        raise KeyError(key)

    def hashfunction(self, key):
        """key är nyckeln
           Beräknar hashfunktionen för key"""
        summa = 0
        for tecken in key:
            summa = summa * 31 + ord(tecken)
        return summa % self.size


def read_file(filename):
    dramas = []
    with open(filename, encoding="utf-8") as file:
        file.readline()  # hoppa över första raden
        for line in file:
            words = line.strip().split(",")
            dramas.append(Drama(words[0], words[1], words[7]))
    return dramas


dramas = read_file("kdramaMini.txt")

print("DictHash:")
d = DictHash()
for drama in dramas:
    d.store(drama.name, drama)
print(d.search("The Heirs"))
try:
    d.search("Kalle Anka")
except KeyError:
    print("Kalle Anka finns inte")

print("Hashtable:")
h = Hashtable(23)
for drama in dramas:
    h.store(drama.name, drama)
print(h.search("The Heirs"))
try:
    h.search("Kalle Anka")
except KeyError:
    print("Kalle Anka finns inte")
