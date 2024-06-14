class Shark():
    def swim(self):
        print("The shark is swimming.")

    def swim_backwards(self):
        print("The shark can't swim backwards.")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")

class Clownfish():
    def swim(self):
        print("The Clownfish is swimming.")
    
    def swim_backwards(self):
        print("The Clownfish can swim backwards.")

    def skeleton(self):
        print("The Clownfish's skeleton is made of bone.")

def polimorfism_fish(fish):
    fish.swim()
    fish.swim_backwards()
    fish.skeleton()

shark = Shark()
clownfish = Clownfish()

polimorfism_fish(shark)
polimorfism_fish(clownfish)

for fish in (shark, clownfish):
    fish.swim()
    fish.swim_backwards()
    fish.skeleton()