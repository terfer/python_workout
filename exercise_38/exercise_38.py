from typing import List, Tuple
from Scoop import Scoop

def create_scoops():
    return Scoop("Chocolate"), Scoop("Vanilla"), Scoop("Persimmon")

scoops = [i for i in create_scoops()]

for i in scoops:
    print(i.flavor)