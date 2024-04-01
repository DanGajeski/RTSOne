import unit_spawner as us
import unit_data as ud

class Builder_Building:
    def __init__(self, x, y, team_id: int):
        self.x = x
        self.y = y
        self.img_info = ud.ImgInfo()
        self.img = self.img_info.builder_building_img
        self.team_id = team_id
        self.spawn_point: us.SpawnPoint = None

    def tick(self):
        pass