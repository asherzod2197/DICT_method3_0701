# ITEMS
class MyDict:
    def __init__(self):
        self.data = {}

    def items(self):
        juftliklar = []
        for key in self.data:
            juftliklar.append((key, self.data[key]))
        return juftliklar

d = MyDict()
d.data = {"a": 1, "b": 2, "c": 3}

print(d.items())  
