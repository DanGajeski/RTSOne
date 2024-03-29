import canvas_entities as ce
import projectiles as pro
import unit_data as ud
import all_entities as ae
import time as time

class SpawnPoint():
    unit_id: int = 0
    def __init__(self, location: tuple, all_entities: ae.AllEntities, projectiles: pro.AllProjectiles):
        self.location = location

        self.all_entities = all_entities
        self.projectiles = projectiles

        self.spawn_cooldown_one: float = None
        self.spawn_cooldown_two: float = None
        self.spawn_cooldown: float = 5.0
        self.spawn_on_cooldown: bool = False

        self.team_id = 1#enemy-team

        self.unit_spawn_location: tuple = None
        self.img_info = ud.ImgInfo()
        self.enemy_entity_img_height = self.img_info.img_height
        self.enemy_entity_img_width = self.img_info.img_width

        self.room_to_spawn: bool = True

    def tick(self):
        self.spawn_enemy_entities()
        self.track_spawn_cooldown()

    def determine_unit_spawn_location(self):
        self.room_to_spawn = True
        #top-left-point
        x1 = self.location[0]
        y1 = self.location[1]
        #top-right-point
        x2 = x1 + self.enemy_entity_img_width
        y2 = y1
        #bottom-left-point
        x3 = x1
        y3 = y1 + self.enemy_entity_img_height
        #bottom-right-point
        x4 = x1 + self.enemy_entity_img_width
        y4 = y1 + self.enemy_entity_img_height

        for entity in self.all_entities.all:
            if self.room_to_spawn == False:
                pass
            elif self.room_to_spawn == True:
                if entity.aabb.check_xy_in_aabb(x1, y1):
                    self.room_to_spawn = False
                if entity.aabb.check_xy_in_aabb(x2, y2):
                    self.room_to_spawn = False
                if entity.aabb.check_xy_in_aabb(x3, y3):
                    self.room_to_spawn = False
                if entity.aabb.check_xy_in_aabb(x4, y4):
                    self.room_to_spawn = False

        if self.room_to_spawn == True:
            self.spawn_enemy_entity(x1, y1)
        elif self.room_to_spawn == False:
            pass

    def spawn_enemy_entity(self, x1, y1):
        self.all_entities.add_entity(ce.Entity(ud.Vec2d(x1, y1), self.unit_id, self.team_id, self.projectiles, self.all_entities))
        self.unit_id += 1

    def spawn_enemy_entities(self):
        if not self.spawn_on_cooldown:
            self.spawn_cooldown_one = time.perf_counter()
            self.determine_unit_spawn_location()
            self.spawn_on_cooldown = True
        elif self.spawn_on_cooldown:
            pass

    def track_spawn_cooldown(self):
        self.spawn_cooldown_two = time.perf_counter()

        if self.spawn_cooldown_two - self.spawn_cooldown_one >= self.spawn_cooldown:
            self.spawn_on_cooldown = False