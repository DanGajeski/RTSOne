import unit_data as ud

class AllEntities():
    def __init__(self):
        self.all = []

    def add_entity(self, entity):
        self.all.append(entity)

    def add_entities(self, entities):
        for entity in entities:
            self.all.append(entity)

    def remove_entity(self, entity):
        self.all.remove(entity)

    def remove_entities(self, entities):
        for entity in entities:
            self.all.remove(entity)

    def tick(self):
        #self.move_entities()
        for entity in self.all:
            entity.tick()
        #DOUBLE-CHECK-ORDER
        #self.run_entity_attacks()

    #MOVE-TO-ENTITY
    def toggle_entity_attack_attitude(self):
        for entity in self.all:
            if entity.is_attacking():
                entity.stop_attacking()
            elif not entity.is_attacking():
                entity.start_attacking()