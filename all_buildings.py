import builder_building as bb

class Buildings:
    def __init__(self):
        self.all: list = []

    def add_building(self, building):
        self.all.append(building)

    def remove_building(self, building):
        self.all.remove(building)

    def tick(self):
        for building in self.all:
            building.tick()