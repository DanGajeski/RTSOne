import unit_data as ud
import time as time
import dan_math as dm
import laser_shot as laser_shot

class Entity:
    def __init__(self, Vec2d: ud.Vec2d, id: int, team_id: int, laser_shots):
        self.id = id
        self.team_id: int = team_id
        self.img_info = ud.ImgInfo()
        self.health: int = 10
        self.pos = Vec2d
        self.img_width = self.img_info.img_width
        self.img_height = self.img_info.img_height
        self.attack_tick_counter: int = 0
        self.target_vec: ud.Vec2d = ud.Vec2d(50.0, 50.0)
        self.distance_from_target_vec: float
        #low-level-tick-tied-entity-speed
        self.attack_range: int = 150
        self.speed: int = 6
        self.laser_shots: list = laser_shots
        self.aabb = ud.AABB(self.pos.x, self.pos.y, (self.pos.x + self.img_info.img_width), (self.pos.y + self.img_info.img_height))
        self.normalizer: dm.Normalizer

        self.laser_on_cooldown: bool = False
        self.cooldown_counter_one: float
        self.cooldown_counter_two: float
        self.laser_shot_cooldown: float = 1.0

        def init_img():
            #contains-new-att-self.img
            if self.team_id == 0:
                self.img = self.img_info.main_character_img
            elif self.team_id == 1:
                self.img = self.img_info.player_two_trooper_img

        init_img()

        self.can_attack: bool = True

        self.immobile_tick_counter: int = 0

    def tick(self):
        if self.laser_on_cooldown:
            self.track_cooldown()

    #def add_to_tick_attack_count(self):
    #    self.attack_tick_counter += 1

    #def reset_tick_attack_count(self):
    #    self.attack_tick_counter = 0

    def track_cooldown(self):
        self.cooldown_counter_two = time.perf_counter()

        if self.cooldown_counter_two - self.cooldown_counter_one >= self.laser_shot_cooldown:
            self.laser_on_cooldown = False

    def set_target_vec(self, target_vec: ud.Vec2d):
        self.target_vec = target_vec

    def update_normalizer(self):
        self.normalizer = dm.Normalizer(self.pos, self.target_vec)

    def move_entity(self):
        self.update_normalizer()

        self.pos.x += self.normalizer.normalized_movement_vec.x
        self.pos.y += self.normalizer.normalized_movement_vec.y
        self.aabb.x1 += self.normalizer.normalized_movement_vec.x
        self.aabb.y1 += self.normalizer.normalized_movement_vec.y
        self.aabb.x2 += self.normalizer.normalized_movement_vec.x
        self.aabb.y2 += self.normalizer.normalized_movement_vec.y

    def move_entity_only_x(self):
        self.update_normalizer()

        self.pos.x += self.normalizer.normalized_movement_vec.x
        self.aabb.x1 += self.normalizer.normalized_movement_vec.x
        self.aabb.x2 += self.normalizer.normalized_movement_vec.x

    def move_entity_only_y(self):
        self.update_normalizer()

        self.pos.y += self.normalizer.normalized_movement_vec.y
        self.aabb.y1 += self.normalizer.normalized_movement_vec.y
        self.aabb.y2 += self.normalizer.normalized_movement_vec.y

    def check_if_entity_at_target_vec(self):
        if self.pos.x < self.target_vec.x + 1 and self.pos.x > self.target_vec.x - 1 and self.pos.y < self.target_vec.y + 1 and self.pos.y > self.target_vec.y - 1:
            return True
        else:
            return False

    def check_range_to_other_entity(self, other_entity):
        if self.aabb.distance_to_other_aabb(other_entity.aabb) <= self.attack_range:
            #print(str(self.id) + " is in range of " + str(other_entity.id) + " at a range of " + str(self.aabb.distance_to_other_aabb(other_entity.aabb)))
            self.shoot_at_entity(other_entity)

    #if-check_range_to_other_entity-already-ran
    def shoot_at_entity(self, other_entity):
        # if self.can_attack:
        #     #if self.team_id == 0:
        #     #print(str(self.id) + " is shooting at " + str(other_entity.id))
        #     self.aabb.find_center_point()
        #     other_entity.aabb.find_center_point()
        #
        #     self.laser_shots.append(laser_shot.LaserShot(self.aabb.center_point, other_entity.aabb.center_point, self.team_id))
        #     self.can_attack = False
            #else:
            #    pass

        if not self.laser_on_cooldown:
            self.cooldown_counter_one = time.perf_counter()
            self.aabb.find_center_point()
            other_entity.aabb.find_center_point()

            self.laser_shots.append(laser_shot.LaserShot(self.aabb.center_point, other_entity.aabb.center_point, self.team_id))
            self.laser_on_cooldown = True