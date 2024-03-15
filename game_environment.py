import all_entities as all_entities
import selected_entities as selected_entities
import canvas_entities as ce
import projectiles as pro
import unit_data as ud
import player as player

class GameEnvironment():
    def __init__(self):
        self.projectiles = pro.AllProjectiles()
        self.all_entities = all_entities.AllEntities()
        self.selected_entities = selected_entities.SelectedEntities()
        self.target_vec = ud.Vec2d(0.0, 0.0)
        self.player = player.Player(0, 0)#pid:0,teamid:0

        #ABSTRACT-into-entity-class
        self.track_entity_attack_ranges_enabled: bool = False

        self.init_all_test_entities()

    #attach-to-single-display-environment
    def import_display_environment(self, display_environment):
        self.display_environment = display_environment

    def set_display_key_bindings(self, main_window):
        main_window.bind('t', lambda event: self.toggle_track_entity_attack_ranges())

    def toggle_track_entity_attack_ranges(self):
        #UPDATE-FOR-LATER-WHEN-MORE-SPECIFIC-ATTACK-MOVES-ARE-INTEGRATED
        self.all_entities.toggle_entity_attack_attitude()

        print('toggling-ATTACK-RANGES!!')
        # if self.track_entity_attack_ranges_enabled:
        #     self.track_entity_attack_ranges_enabled = False
        # elif not self.track_entity_attack_ranges_enabled:
        #     self.track_entity_attack_ranges_enabled = True

    def init_all_test_entities(self):
        def init_team_one_entities():
            entity_one = ce.Entity(ud.Vec2d(50.0, 50.0), 1, 0, self.projectiles, self.selected_entities, self.all_entities)
            entity_two = ce.Entity(ud.Vec2d(100.0, 100.0), 2, 0, self.projectiles, self.selected_entities, self.all_entities)
            entity_three = ce.Entity(ud.Vec2d(200.0, 200.0), 3, 0, self.projectiles, self.selected_entities, self.all_entities)
            entity_four = ce.Entity(ud.Vec2d(300.0, 300.0), 4, 0, self.projectiles, self.selected_entities, self.all_entities)
            entity_five = ce.Entity(ud.Vec2d(400.0, 400.0), 5, 0, self.projectiles, self.selected_entities, self.all_entities)
            entity_six = ce.Entity(ud.Vec2d(200.0, 100.0), 6, 0, self.projectiles, self.selected_entities, self.all_entities)

            return [entity_one, entity_two, entity_three, entity_four, entity_five, entity_six]
        def init_team_two_entities():
            enemy_entity_one = ce.Entity(ud.Vec2d(100.0, 400.0), 7, 1, self.projectiles, self.selected_entities, self.all_entities)
            enemy_entity_two = ce.Entity(ud.Vec2d(400.0, 100.0), 8, 1, self.projectiles, self.selected_entities, self.all_entities)
            enemy_entity_three = ce.Entity(ud.Vec2d(400.0, 150), 9, 1, self.projectiles, self.selected_entities, self.all_entities)
            enemy_entity_four = ce.Entity(ud.Vec2d(100.0, 450), 10, 1, self.projectiles, self.selected_entities, self.all_entities)
            enemy_entity_five = ce.Entity(ud.Vec2d(150.0, 370), 11, 1, self.projectiles, self.selected_entities, self.all_entities)

            return [enemy_entity_one, enemy_entity_two, enemy_entity_three, enemy_entity_four, enemy_entity_five]

        self.all_entities.add_entities(init_team_one_entities())
        self.all_entities.add_entities(init_team_two_entities())

    def tick(self):
        self.all_entities.tick()
        self.projectiles.tick()

        #ABSTRACT-into-entities_class
        #if self.track_entity_attack_ranges_enabled:
        #    for entity in self.all_entities.all:
        #        for other_entity in self.all_entities.all:
        #            if other_entity.id != entity.id:
        #                if other_entity.team_id != entity.team_id:
        #                    entity.check_range_to_other_entity(other_entity)

        #REWORK-TO-MOVE-ANY-ENTITY-THAT-TARGET_VEC-IS-DIFFERENT-TO-CURRENT_VEC
        #if not self.selected_entities.is_empty():
        #    self.selected_entities.move_entities(self.target_vec, self.all_entities.all)