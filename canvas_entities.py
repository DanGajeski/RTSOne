import unit_data as ud
import time as time
import dan_math as dm
import laser_shot as laser_shot
import selected_entities as se
import all_entities as ae
import projectiles as proj


class Entity:
    def __init__(self, Vec2d: ud.Vec2d, id: int, team_id: int, projectiles: proj.AllProjectiles, all_entities: ae.AllEntities):
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

        #self.laser_shots: list = laser_shots
        self.projectiles: proj = projectiles

        self.aabb = ud.AABB(self.pos.x, self.pos.y, (self.pos.x + self.img_info.img_width), (self.pos.y + self.img_info.img_height))
        self.normalizer: dm.Normalizer

        self.all_entities: ae.AllEntities = all_entities

        self.attacking: bool = False
        self.laser_on_cooldown: bool = False
        self.cooldown_counter_one: float
        self.cooldown_counter_two: float
        self.laser_shot_cooldown: float = 1.0

        self.stop_counter: int = 0 #gets-reset-to-0-in-selected_entities.set_target_vec()

        def init_img():
            #contains-new-att-self.img
            if self.team_id == 0:
                self.img = self.img_info.main_character_img
            elif self.team_id == 1:
                self.img = self.img_info.player_two_trooper_img

        init_img()

        self.can_attack: bool = True

        self.immobile_tick_counter: int = 0

    #REFACTOR=>Pass-In-environments-so-that-entity-tick-handles-shooting-moving//all-entity-actions
    #REFACTOR==>entity-must-know-of-all-other-entities-and-the-game-environment
    def tick(self):
        if self.laser_on_cooldown:
            self.track_cooldown()
        if self.attacking:
            self.run_entity_attacks()
        if not self.check_if_entity_at_target_vec():
            self.move_entity_check()

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

    def check_if_entity_at_target_vec(self,):
        if self.stop_counter > 5: #condition-for-blocked, reset-at-selected_entities.set_target_vec()
            return True
        if self.pos.x < self.target_vec.x + 1 and self.pos.x > self.target_vec.x - 1 and self.pos.y < self.target_vec.y + 1 and self.pos.y > self.target_vec.y - 1:
            return True
        else:
            return False

    def check_range_to_other_entity(self, other_entity):#checks-range-AND-attacks-other-entity-IF-in-range
        if self.aabb.distance_to_other_aabb(other_entity.aabb) <= self.attack_range:
            #print(str(self.id) + " is in range of " + str(other_entity.id) + " at a range of " + str(self.aabb.distance_to_other_aabb(other_entity.aabb)))
            self.shoot_at_entity(other_entity)

    def is_attacking(self):
        return self.attacking

    def start_attacking(self):
        self.attacking = True

    def stop_attacking(self):
        self.attacking = False

    #if-check_range_to_other_entity-already-ran
    def shoot_at_entity(self, other_entity):
        if not self.laser_on_cooldown:
            self.cooldown_counter_one = time.perf_counter()
            self.aabb.find_center_point()
            other_entity.aabb.find_center_point()

            self.projectiles.laser_shots.append(laser_shot.LaserShot(self.aabb.center_point, other_entity.aabb.center_point, self.team_id))
            self.laser_on_cooldown = True

    def run_entity_attacks(self):

        #for entity in self.all_entities:
        for other_entity in self.all_entities.all:
            if other_entity.id != self.id:
                if other_entity.team_id != self.team_id:
                    self.check_range_to_other_entity(other_entity)






    def move_entity_check(self):
        for count in range(self.speed):
            if self.check_entity_collision():
                self.move_entity()
            else:
                if self.check_entity_x_collision():#true-if-no-x-collision
                    self.move_entity_only_x()
                elif self.check_entity_y_collision():#true-if-no-y-collision
                    self.move_entity_only_y()
                #0->NOT-CURRENTLY-IN-USE
                self.stop_counter += 0 #TEST-add-to-this-to-re-enable-stop-counter

    #aabb_blocker_tester_method
    def check_entity_collision(self):
        self.update_normalizer()

        #test_entity_displacement: int = 10

        can_move: bool = True
        test_movement_aabb = ud.AABB(self.aabb.x1, self.aabb.y1, self.aabb.x2, self.aabb.y2)

        test_movement_aabb.x1 += self.normalizer.normalized_movement_vec.x
        test_movement_aabb.y1 += self.normalizer.normalized_movement_vec.y
        test_movement_aabb.x2 += self.normalizer.normalized_movement_vec.x
        test_movement_aabb.y2 += self.normalizer.normalized_movement_vec.y

        for other_entity in self.all_entities.all:
            if other_entity.id != self.id:
                #blocker_aabb_test = ud.AABB(other_entity.aabb.x1 - test_entity_displacement, other_entity.aabb.y1 - test_entity_displacement, other_entity.aabb.x2 + test_entity_displacement, other_entity.aabb.y2 + test_entity_displacement)
                #if blocker_aabb_test.check_aabb_in_aabb(test_movement_aabb):
                if other_entity.aabb.check_aabb_in_aabb(test_movement_aabb):
                    can_move = False

        return can_move

    def check_entity_x_collision(self):
        self.update_normalizer()

        can_move: bool = True
        test_movement_aabb = ud.AABB(self.aabb.x1, self.aabb.y1, self.aabb.x2, self.aabb.y2)

        test_movement_aabb.x1 += self.normalizer.normalized_movement_vec.x
        test_movement_aabb.x2 += self.normalizer.normalized_movement_vec.x

        for other_entity in self.all_entities.all:
            if other_entity.id != self.id:
                if other_entity.aabb.check_aabb_in_aabb(test_movement_aabb):
                    can_move = False

        return can_move

    def check_entity_y_collision(self):
        self.update_normalizer()

        can_move: bool = True
        test_movement_aabb = ud.AABB(self.aabb.x1, self.aabb.y1, self.aabb.x2, self.aabb.y2)

        test_movement_aabb.y1 += self.normalizer.normalized_movement_vec.y
        test_movement_aabb.y2 += self.normalizer.normalized_movement_vec.y

        for other_entity in self.all_entities.all:
            if other_entity.id != self.id:
                if other_entity.aabb.check_aabb_in_aabb(test_movement_aabb):
                    can_move = False

        return can_move