import all_entities as all_entities
import selected_entities as selected_entities
import canvas_entities as ce
import projectiles as pro
import unit_data as ud
import unit_spawner as us
import all_buildings as ab
import builder_building as bb
import player as player

class GameEnvironment():
    spawn_point_x: int = 150
    spawn_point_y: int = 150
    def __init__(self):
        self.projectiles = pro.AllProjectiles()
        self.all_entities = all_entities.AllEntities()
        self.buildings = ab.Buildings()
        self.target_vec = ud.Vec2d(0.0, 0.0)
        self.player = player.Player(0, 0)#pid:0,teamid:0
        self.unit_spawner_group = []

        #ABSTRACT-into-entity-class
        self.track_entity_attack_ranges_enabled: bool = False
        self.game_environment_tick_enabled: bool = True

        self.init_all_test_entities()

    #attach-to-single-display-environment
    def import_display_environment(self, display_environment):
        self.display_environment = display_environment

    def set_display_key_bindings(self, main_window):
        main_window.bind('t', lambda event: self.toggle_track_entity_attack_ranges())
        main_window.bind('p', lambda event: self.create_unit_spawner())
        main_window.bind('b', lambda event: self.spawn_building_at_mouse_location())

    def create_unit_spawner(self):
        self.unit_spawner_group.append(us.SpawnPoint((self.spawn_point_x, self.spawn_point_y), self.all_entities, self.projectiles))
        self.spawn_point_x += 50
        self.spawn_point_y += 50

    def toggle_game_environment_tick(self):
        if self.game_environment_tick_enabled:
            self.game_environment_tick_enabled = False
        elif not self.game_environment_tick_enabled:
            self.game_environment_tick_enabled = True

    def run_entity_ticks(self):
        self.all_entities.tick()

    def run_projectile_ticks(self):
        self.projectiles.tick()

    def run_building_ticks(self):
        self.buildings.tick()

    def spawn_building_at_mouse_location(self):
        x = self.display_environment.canvas_mouse_location_x
        y = self.display_environment.canvas_mouse_location_y
        self.buildings.add_building(bb.Builder_Building(x, y, 0, self.all_entities, self.projectiles))

    def run_unit_spawner_ticks(self):
        if len(self.unit_spawner_group) >= 1:
            for unit_spawner in self.unit_spawner_group:
                unit_spawner.tick()

    def toggle_track_entity_attack_ranges(self):
        #UPDATE-FOR-LATER-WHEN-MORE-SPECIFIC-ATTACK-MOVES-ARE-INTEGRATED
        self.all_entities.toggle_entity_attack_attitude()

        print('toggling-ATTACK-RANGES!!')

    def init_all_test_entities(self):
        def init_team_one_entities():
            entity_one = ce.Entity(ud.Vec2d(50.0, 50.0), 1, 0, self.projectiles, self.all_entities)
            entity_two = ce.Entity(ud.Vec2d(100.0, 100.0), 2, 0, self.projectiles, self.all_entities)
            entity_three = ce.Entity(ud.Vec2d(200.0, 200.0), 3, 0, self.projectiles, self.all_entities)
            entity_four = ce.Entity(ud.Vec2d(300.0, 300.0), 4, 0, self.projectiles, self.all_entities)
            entity_five = ce.Entity(ud.Vec2d(400.0, 400.0), 5, 0, self.projectiles, self.all_entities)
            entity_six = ce.Entity(ud.Vec2d(200.0, 100.0), 6, 0, self.projectiles, self.all_entities)

            return [entity_one, entity_two, entity_three, entity_four, entity_five, entity_six]
        def init_team_two_entities():
            enemy_entity_one = ce.Entity(ud.Vec2d(100.0, 400.0), 7, 1, self.projectiles, self.all_entities)
            enemy_entity_two = ce.Entity(ud.Vec2d(400.0, 100.0), 8, 1, self.projectiles, self.all_entities)
            enemy_entity_three = ce.Entity(ud.Vec2d(400.0, 150), 9, 1, self.projectiles, self.all_entities)
            enemy_entity_four = ce.Entity(ud.Vec2d(100.0, 450), 10, 1, self.projectiles, self.all_entities)
            enemy_entity_five = ce.Entity(ud.Vec2d(150.0, 370), 11, 1, self.projectiles, self.all_entities)

            return [enemy_entity_one, enemy_entity_two, enemy_entity_three, enemy_entity_four, enemy_entity_five]

        self.all_entities.add_entities(init_team_one_entities())
        self.all_entities.add_entities(init_team_two_entities())

    def tick(self):
        self.run_entity_ticks()
        self.run_projectile_ticks()
        self.run_unit_spawner_ticks()
        self.run_building_ticks()

        #REWORK-TO-MOVE-ANY-ENTITY-THAT-TARGET_VEC-IS-DIFFERENT-TO-CURRENT_VEC
        #if not self.selected_entities.is_empty():
        #    self.selected_entities.move_entities(self.target_vec, self.all_entities.all)