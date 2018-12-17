class Item(object):
    def __init__(self, w, v):
        self.value = int(v) # Item's value
        self.weight = int(w) # Item's weight
    def __str__(self):
        return ("weight : " + str(self.weight) + ", value : " + str(self.value)) 
