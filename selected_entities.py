import unit_data as ud
import all_entities as ae

class SelectedEntities(ae.AllEntities):
    def __init__(self):
        super().__init__()
        self.selected = []

    def add_to_selected_entities(self, new_entity):
        self.selected.append(new_entity)

    #possibly update later to utilize an entity ID?
    def remove_from_selected_entities(self, current_entity):
        self.selected.remove(current_entity)

    def remove_all_selected_entities(self):
        for count in self.selected:
            self.selected.pop()

    def is_empty(self):
        return self.selected == []

    def set_target_vec(self, target_vec: ud.Vec2d):
        self.target_vec = target_vec
        for entity in self.selected:
            entity.set_target_vec(self.target_vec)
            entity.stop_counter = 0
            print(entity)
            print(entity.stop_counter)