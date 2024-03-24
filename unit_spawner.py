import canvas_entities as ce
import all_entities as ae

class SpawnPoint():
    def __init__(self, location: tuple, all_entities: ae.AllEntities):
        self.location = location
        self.spawn_cooldown_init: float = None
        self.spawn_cooldown_fin: float = None

    def tick(self):
        self.spawn_enemy_entities()

    def spawn_enemy_entitiy(self):
        pass

    def spawn_enemy_entities(self):
        self.spawn_enemy_entity()
        

