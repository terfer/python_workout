class Bowl:
    def __init__(self):
        self.scoops = []
    
    def add_scoops(self, *scoops):
        self.scoops += scoops

    def __repr__(self):
        return '| '.join([scoop.flavor for scoop in self.scoops])