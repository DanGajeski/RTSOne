import unit_data as ud

class AllEntities():
    def __init__(self):
        self.all = []
        #selected-entities
        self.selected = []

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
            self.monitor_entity_health(entity)
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

    def monitor_entity_health(self, entity):
        if not entity.alive:
            self.remove_entity(entity)

    def add_to_selected_entities(self, new_entity):
        self.selected.append(new_entity)

    def remove_from_selected_entities(self, current_entity):
        self.selected.remove(current_entity)

    def remove_all_selected_entities(self):
        self.selected = []

    def selected_is_empty(self):
        return self.selected == []

    def set_target_vec_selected(self, target_vec: ud.Vec2d):
        self.target_vec = target_vec
        for entity in self.selected:
            entity.set_target_vec(self.target_vec)
            entity.stop_counter = 0