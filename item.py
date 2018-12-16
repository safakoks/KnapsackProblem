class Item(object):
    def __init__(self, w, v):
        self.value = int(v) # Item's value. You want to maximize that!
        self.weight = int(w) # Item's weight. The sum of all items should be <= CAPACITY
    def __str__(self):
        return ("w: " + str(self.weight) + ", v: " + str(self.value)) 
