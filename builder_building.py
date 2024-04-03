import unit_spawner as us
import unit_data as ud

class Builder_Building:
    def __init__(self, x, y, team_id: int, all_entities, projectiles):
        self.x = x
        self.y = y
        self.img_info = ud.ImgInfo()
        self.img = self.img_info.builder_building_img
        self.team_id = team_id
        self.all_entities = all_entities
        self.projectiles = projectiles
        self.spawn_point: us.SpawnPoint = None

        self.init_spawn_point()

    def tick(self):
        if self.spawn_point != None:
            self.spawn_point.tick()

    def init_spawn_point(self):
        location_tuple: tuple = (self.x, self.y)
        self.spawn_point = us.SpawnPoint(location_tuple, self.all_entities, self.projectiles, self.team_id)