class Bowl:
    def __init__(self):
        self.scoops = []
        self.max_scoops = 3
    
    def add_scoops(self, *scoops):
        self.scoops =  (self.scoops + list(scoops))[:self.max_scoops]

    def __repr__(self):
        return '| '.join([scoop.flavor for scoop in self.scoops])