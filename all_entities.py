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
        self.move_entities()
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
            #if entity.is_attacking:
            #    print(str(entity) + " is attacking!")


    #MOVE-AND-UPDATE-TO-SINGLE-ENTITY-RUN_ENTITY_ATTACKS()
    #def run_entity_attacks(self):
    #    for entity in self.all:
    #        for other_entity in self.all:
    #            if other_entity.id != entity.id:
    #                if other_entity.team_id != entity.team_id:
    #                    entity.check_range_to_other_entity(other_entity)


    #    for entity in self.all:
    #        for other_entity in self.all:
    #            if other_entity.id != entity.id:
    #                if other_entity.team_id != entity.team_id:
    #                    entity.check_range_to_other_entity(other_entity)

    #MOVE-AND-UPDATE-TO-SINGLE-ENTITY-MOVE_ENTITY()
    def move_entities(self):
        for entity in self.all:
            for count in range(entity.speed):
                if not entity.check_if_entity_at_target_vec():
                    #if-no-collision
                    if self.check_entity_collision(entity):
                        entity.move_entity()
                        #if-collision
                    else:
                        if self.check_entity_x_collision(entity):#true-if-no-x-collision
                            entity.move_entity_only_x()
                        elif self.check_entity_y_collision(entity):#true-if-no-y-collision
                            entity.move_entity_only_y()
                    entity.stop_counter += 0 #TEST-add-to-this-to-re-enable-stop-counter

    #MOVE-TO-ENTITY
    #aabb_blocker_tester_method
    def check_entity_collision(self, entity):
        entity.update_normalizer()

        test_entity_displacement: int = 10

        can_move: bool = True
        test_movement_aabb = ud.AABB(entity.aabb.x1, entity.aabb.y1, entity.aabb.x2, entity.aabb.y2)

        test_movement_aabb.x1 += entity.normalizer.normalized_movement_vec.x
        test_movement_aabb.y1 += entity.normalizer.normalized_movement_vec.y
        test_movement_aabb.x2 += entity.normalizer.normalized_movement_vec.x
        test_movement_aabb.y2 += entity.normalizer.normalized_movement_vec.y

        for other_entity in self.all:
            if other_entity.id != entity.id:
                #blocker_aabb_test = ud.AABB(other_entity.aabb.x1 - test_entity_displacement, other_entity.aabb.y1 - test_entity_displacement, other_entity.aabb.x2 + test_entity_displacement, other_entity.aabb.y2 + test_entity_displacement)
                #if blocker_aabb_test.check_aabb_in_aabb(test_movement_aabb):
                if other_entity.aabb.check_aabb_in_aabb(test_movement_aabb):
                    can_move = False

        return can_move

    #MOVE-TO-ENTITY
    def check_entity_x_collision(self, entity):
        entity.update_normalizer()

        can_move: bool = True
        test_movement_aabb = ud.AABB(entity.aabb.x1, entity.aabb.y1, entity.aabb.x2, entity.aabb.y2)

        test_movement_aabb.x1 += entity.normalizer.normalized_movement_vec.x
        test_movement_aabb.x2 += entity.normalizer.normalized_movement_vec.x

        for other_entity in self.all:
            if other_entity.id != entity.id:
                if other_entity.aabb.check_aabb_in_aabb(test_movement_aabb):
                    can_move = False

        return can_move

    #MOVE-TO-ENTITY
    def check_entity_y_collision(self, entity):
        entity.update_normalizer()

        can_move: bool = True
        test_movement_aabb = ud.AABB(entity.aabb.x1, entity.aabb.y1, entity.aabb.x2, entity.aabb.y2)

        test_movement_aabb.y1 += entity.normalizer.normalized_movement_vec.y
        test_movement_aabb.y2 += entity.normalizer.normalized_movement_vec.y

        for other_entity in self.all:
            if other_entity.id != entity.id:
                if other_entity.aabb.check_aabb_in_aabb(test_movement_aabb):
                    can_move = False

        return can_move