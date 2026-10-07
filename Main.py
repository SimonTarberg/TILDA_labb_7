class DictHash():
    """klass som skapar en hash av en dictionary genom att använda pythons dictonary
    """
    def __init__(self, nyckel, data):
        self.nyckel = nyckel
        self.data = data
        
    def store(self, nyckel, data):
        """Lagrar data som value i dictionary, med nyckel som key

        Args:
            nyckel(key): nyckel till data
            data(value):
        """
        pass
    
    def search(self,nyckel):
        """slår upp nyckel i din dictionary och returnerar data.
            return: data
        """
        return 
        

x = DictHash(111, "bil")

print(x.nyckel)

def read_file(filename):
    name_dict = {}
    with open(filename, encoding= "utf-8") as file:
        for line in file:
            words = line.split(",")
            name_dict[words[0]] = words[1:]
    return name_dict

print(read_file("kdramaMini.txt"))