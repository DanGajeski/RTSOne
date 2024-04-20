import tk_simple_canvas as tsc
import tkinter as tk
import unit_data as ud

class GameEnvironmentUI:
    def __init__(self, display_environment):
        self.display_environment = display_environment

        self.display_frame = tk.Frame(self.display_environment.main_window, width=self.display_environment.main_window_width - self.display_environment.display_frame_main_window_offset*2, height=self.display_environment.main_window_height - self.display_environment.display_frame_main_window_offset*2)
        self.display_frame.place(x=self.display_environment.display_frame_main_window_offset, y=self.display_environment.display_frame_main_window_offset)
        self.display_frame_aabb: ud.AABB = ud.AABB(0, 0, self.display_frame.winfo_reqwidth(), self.display_frame.winfo_reqheight())

        #canvas-settings
        self.canvas_bg_color: str = "#00FF00"
        self.canvas_vertical_stripe_color: str = "#FFFFFF"
        self.canvas_horitontal_stripe_color: str = "#000000"
        self.canvas_x_placement: int = 0
        self.canvas_y_placement: int = 0

        self.canvas = tk.Canvas(self.display_environment.display_frame, bg=self.display_environment.canvas_bg_color, width=self.display_environment.map_width, height=self.display_environment.map_height)
        self.canvas.place(x=self.display_environment.canvas_x_placement,y=self.display_environment.canvas_y_placement)
        self.canvas_aabb: ud.AABB = ud.AABB(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight())

        #transeferred
        #unyet_utilized
        self.origin_x: float = 0.0
        self.origin_y: float = 0.0
        self.destination_x: float = 0.0
        self.destination_y: float = 0.0
        self.unit_selector_enabled: bool = False
        self.motion_selection_aabb: ud.AABB = ud.AABB(0,0,0,0)
        self.mouse_border_monitoring: bool = False
        self.display_screen_canvas_scroll_speed: int = 5
        self.track_entity_attack_ranges_enabled: bool = False

    def remove_environment(self):
        self.canvas.place_forget()
        #self.diplay_environment.display_frame.place_forget()

    #def transition_to_game_environment_ui(self):
    #    self.display_environment.swap_to_game_environment_ui()

    def draw_map_stripes_background(self):#JUST-TRANSFERRED
        #new_vars
        self.working_canvas_width: float = float(self.canvas.winfo_width())
        self.working_canvas_width_twenty_spaces_count: int = int(self.working_canvas_width / 20)
        self.working_canvas_height: float = float(self.canvas.winfo_height())
        self.working_canvas_height_twenty_spaces_count: int = int(self.working_canvas_height / 20)

        #add-20-y-every-turn
        def draw_map_stripes_horizontal(x, y):
            draw_point_x1: int = x
            draw_point_y1: int = y
            draw_point_x2: int = self.canvas.winfo_width()
            draw_point_y2: int = y + 10

            draw_point_two_x1: int = x
            draw_point_two_y1: int = draw_point_y2
            draw_point_two_x2: int = draw_point_x2
            draw_point_two_y2: int = draw_point_two_y1 + 10
            self.canvas.create_rectangle(draw_point_two_x1, draw_point_two_y1, draw_point_two_x2, draw_point_two_y2, fill=self.canvas_horitontal_stripe_color, outline="")
        #add-20-x-every-runCAN_EDIT_IN_STRIPE_WIDTH_LATER
        def draw_map_stripes_vertical(x, y):
            draw_point_x1: int = x
            draw_point_y1: int = y
            draw_point_x2: int = x + 10
            draw_point_y2: int = self.canvas.winfo_height()
            #self.canvas.create_rectangle(draw_point_x1, draw_point_y1, draw_point_x2, draw_point_y2, fill=self.canvas_vertical_stripe_color)
            draw_point_two_x1: int = draw_point_x2
            draw_point_two_y1: int = y
            draw_point_two_x2: int = draw_point_two_x1 + 10
            draw_point_two_y2: int = draw_point_y2
            self.canvas.create_rectangle(draw_point_two_x1, draw_point_two_y1, draw_point_two_x2, draw_point_two_y2, fill=self.canvas_vertical_stripe_color, outline="")
        def draw_map_stripes_black():
            init_x = 0
            init_y = 0
            for count in range(self.working_canvas_height_twenty_spaces_count):
                draw_map_stripes_horizontal(init_x,init_y)
                init_y += 20
        #CAN_EDIT_IN_STRIPE_WIDTH_LATER
        def draw_map_stripes_black_dominance():
            init_x = 0
            init_y = 0
            for count in range(self.working_canvas_width_twenty_spaces_count):
                draw_map_stripes_vertical(init_x,init_y)
                init_x += 20
            init_x = 0
            for count in range(self.working_canvas_height_twenty_spaces_count):
                draw_map_stripes_horizontal(init_x,init_y)
                init_y += 20
        def draw_map_stripes_white_dominance():
            init_x = 0
            init_y = 0
            for count in range(self.working_canvas_height_twenty_spaces_count):
                draw_map_stripes_horizontal(init_x,init_y)
                init_y += 20
            init_y = 0
            for count in range(self.working_canvas_width_twenty_spaces_count):
                draw_map_stripes_vertical(init_x,init_y)
                init_x += 20

        draw_map_stripes_black()
        #draw_map_stripes_white_dominance()
        #draw_map_stripes_black_dominance()

    def set_target_movement_location(self):#JUST-TRANSFERRED
        #self.target_vec = ud.Vec2d(self.canvas_mouse_location_x, self.canvas_mouse_location_y)
        self.game_environment.all_entities.set_target_vec_selected(ud.Vec2d(self.canvas_mouse_location_x, self.canvas_mouse_location_y))

    def set_key_bindings(self):#JUST-TRANSFERRED
        #self.game_display_environment_keybindings_set = True

        #self.main_window.bind('<Motion>', lambda event: self.track_mouse_location())
        #self.main_window.bind('<Button-3>', lambda event: self.set_target_movement_location())
        #self.main_window.bind('<Button-1>', lambda event: self.set_unit_selector_origin())
        #self.main_window.bind('<ButtonRelease-1>', lambda event: self.button_release_checks())
        #self.main_window.bind('l', lambda event: self.lock_cursor_to_frame())

        #self.main_window.bind('<Escape>', lambda event: self.toggle_pause_menu_ui())

    def track_mouse_location(self):#JUST-TRANSFERRED
        #new_VALS
        #verified
        self.main_window_x_location_SCREEN: int = self.main_window.winfo_rootx()
        self.main_window_y_location_SCREEN: int = self.main_window.winfo_rooty()

        #verified
        self.display_frame_x_location_SCREEN: int = self.main_window_x_location_SCREEN + self.display_frame_main_window_offset
        self.display_frame_y_location_SCREEN: int = self.main_window_y_location_SCREEN + self.display_frame_main_window_offset

        #verified
        self.main_window_mouse_location_x: int = self.main_window.winfo_pointerx() - self.main_window_x_location_SCREEN
        self.main_window_mouse_location_y: int = self.main_window.winfo_pointery() - self.main_window_y_location_SCREEN

        #verified
        self.display_frame_mouse_location_x: int = self.main_window_mouse_location_x - self.display_frame_main_window_offset
        self.display_frame_mouse_location_y: int = self.main_window_mouse_location_y - self.display_frame_main_window_offset
        self.display_frame_mouse_location_point: tuple = (self.display_frame_mouse_location_x, self.display_frame_mouse_location_y)

        #verified
        self.canvas_mouse_location_x: int = self.display_frame_mouse_location_x - self.canvas_x_placement
        self.canvas_mouse_location_y: int = self.display_frame_mouse_location_y - self.canvas_y_placement

    def move_display_frame_up(self):#JUST-TRANSFERRED
        self.canvas_y_placement-=5
    def move_display_frame_up_right(self):#JUST-TRANSFERRED
        self.canvas_y_placement-=5
        self.canvas_x_placement+=5
    def move_display_frame_up_left(self):#JUST-TRANSFERRED
        self.canvas_y_placement-=5
        self.canvas_x_placement-=5
    def move_display_frame_left(self):#JUST-TRANSFERRED
        self.canvas_x_placement-=5
    def move_display_frame_right(self):#JUST-TRANSFERRED
        self.canvas_x_placement+=5
    def move_display_frame_down(self):#JUST-TRANSFERRED
        self.canvas_y_placement+=5
    def move_display_frame_down_right(self):#JUST-TRANSFERRED
        self.canvas_y_placement+=5
        self.canvas_x_placement+=5
    def move_display_frame_down_left(self):#JUST-TRANSFERRED
        self.canvas_y_placement+=5
        self.canvas_x_placement-=5

    def set_unit_selector_origin(self):#JUST-TRANSFERRED
        origin_on_unit: bool = False
        selecting_entity: ce.Entity

        self.origin_x = self.canvas_mouse_location_x
        self.origin_y = self.canvas_mouse_location_y
        #FORTESTING_EP_1
        print(self.origin_x)
        print(self.origin_y)

        for entity in self.game_environment.all_entities.all:
            if entity.aabb.check_xy_in_aabb(self.origin_x, self.origin_y):
                origin_on_unit = True
                selecting_entity = entity
                continue

        if origin_on_unit:
            self.select_entity(selecting_entity)
        else:
            self.enable_unit_selector()

    def select_entity(self, entity):#JUST-TRANSFERRED
        self.game_environment.all_entities.add_to_selected_entities(entity)

    def enable_unit_selector(self):#JUST-TRANSFERRED
        self.unit_selector_enabled = True
        self.motion_selection_aabb.x1 = self.origin_x
        self.motion_selection_aabb.y1 = self.origin_y

    def make_selection(self):#JUST-TRANSFERRED
        #clear-selected-entities-first
        self.game_environment.all_entities.remove_all_selected_entities()
        for entity in self.game_environment.all_entities.all:
            if self.motion_selection_aabb.check_aabb_in_aabb(entity.aabb):
                if self.game_environment.player.team_id == entity.team_id:
                    self.game_environment.all_entities.add_to_selected_entities(entity)

    def enable_track_entity_attack_ranges(self):#JUST-TRANSFERRED
        self.track_entity_attack_ranges_enabled: bool = True

    def update_canvas_frame_placement(self):#JUST-TRANSFERRED
        self.canvas.place(x=self.canvas_x_placement,y=self.canvas_y_placement)

    #CLEANTHISUPUPONREFACTOR
    def lock_cursor_to_frame(self):#JUST-TRANSFERRED
        if self.mouse_border_monitoring == True:
            self.mouse_border_monitoring = False
        else:
            if self.display_frame_aabb.check_xy_in_aabb(self.display_frame_mouse_location_point[0], self.display_frame_mouse_location_point[1]):
                print("Mouse in display frame")
                self.mouse_border_monitoring = True
            else:
                print("Mouse not in display frame")

    def display_frame_point_get_screen_xy(self, x: float, y: float):#JUST-TRANSFERRED
        new_windows_x = x + self.display_frame_main_window_offset + self.main_window_x_location_SCREEN
        new_windows_y = y + self.display_frame_main_window_offset + self.main_window_y_location_SCREEN
        return (new_windows_x, new_windows_y)

    #intotal-restricts-mouse-to-display-frame-and-scrolls-display-frame-dependent-on-scroll-speed
    #plan->for-update-to-only-allow-movement-within-game-environment-frame
    def restrict_mouse_within_display_area(self):#JUST-TRANSFERRED
        if self.mouse_border_monitoring:
            if self.display_frame_aabb.check_xy_in_aabb(self.display_frame_mouse_location_point[0], self.display_frame_mouse_location_point[1]):
                print("INSIDE_FRAME")
                if self.display_frame_aabb.check_xy_on_border(self.display_frame_mouse_location_point[0], self.display_frame_mouse_location_point[1]):
                    for speed in range(self.display_screen_canvas_scroll_speed):
                        if self.display_frame_aabb.check_xy_on_which_border(self.display_frame_mouse_location_point[0], self.display_frame_mouse_location_point[1]) == "up":
                            self.move_display_frame_up()
                        elif self.display_frame_aabb.check_xy_on_which_border(self.display_frame_mouse_location_point[0], self.display_frame_mouse_location_point[1]) == "upright":
                            self.move_display_frame_up_right()
                        elif self.display_frame_aabb.check_xy_on_which_border(self.display_frame_mouse_location_point[0], self.display_frame_mouse_location_point[1]) == "right":
                            self.move_display_frame_right()
                        elif self.display_frame_aabb.check_xy_on_which_border(self.display_frame_mouse_location_point[0], self.display_frame_mouse_location_point[1]) == "downright":
                            self.move_display_frame_down_right()
                        elif self.display_frame_aabb.check_xy_on_which_border(self.display_frame_mouse_location_point[0], self.display_frame_mouse_location_point[1]) == "down":
                            self.move_display_frame_down()
                        elif self.display_frame_aabb.check_xy_on_which_border(self.display_frame_mouse_location_point[0], self.display_frame_mouse_location_point[1]) == "downleft":
                            self.move_display_frame_down_left()
                        elif self.display_frame_aabb.check_xy_on_which_border(self.display_frame_mouse_location_point[0], self.display_frame_mouse_location_point[1]) == "left":
                            self.move_display_frame_left()
                        elif self.display_frame_aabb.check_xy_on_which_border(self.display_frame_mouse_location_point[0], self.display_frame_mouse_location_point[1]) == "upleft":
                            self.move_display_frame_up_left()
                else:
                    pass
            else:
                display_area_restriction_point = self.display_frame_aabb.restrict_point_within_aabb(self.display_frame_mouse_location_point[0], self.display_frame_mouse_location_point[1])
                print(display_area_restriction_point)

                restricted_windows_xy = self.display_frame_point_get_screen_xy(display_area_restriction_point[0], display_area_restriction_point[1])
                print(restricted_windows_xy[0], restricted_windows_xy[1])
                win32api.SetCursorPos((int(restricted_windows_xy[0]), int(restricted_windows_xy[1])))
                #pass speed into method
                for speed in range(self.display_screen_canvas_scroll_speed):
                    if display_area_restriction_point[2] == 0:
                        self.move_display_frame_up()
                    elif display_area_restriction_point[2] == 1:
                        self.move_display_frame_up_right()
                    elif display_area_restriction_point[2] == 2:
                        self.move_display_frame_right()
                    elif display_area_restriction_point[2] == 3:
                        self.move_display_frame_down_right()
                    elif display_area_restriction_point[2] == 4:
                        self.move_display_frame_down()
                    elif display_area_restriction_point[2] == 5:
                        self.move_display_frame_down_left()
                    elif display_area_restriction_point[2] == 6:
                        self.move_display_frame_left()
                    elif display_area_restriction_point[2] == 7:
                        self.move_display_frame_up_left()
        else:
            pass

    def button_release_checks(self):#JUST-TRANSFERRED
        if self.unit_selector_enabled:
            self.unit_selector_enabled = False
            self.destination_x = self.canvas_mouse_location_x
            #self.destination_x = self.get_mouse_x_location()
            self.destination_y = self.canvas_mouse_location_y
            #self.destination_y = self.get_mouse_y_location()

            #FORTESTING
            print(self.destination_x)
            print(self.destination_y)

            self.motion_selection_aabb.x2 = self.destination_x
            self.motion_selection_aabb.y2 = self.destination_y

            self.make_selection()

    def draw_unit_selector(self):#JUST-TRANSFERRED
        #current_destination_x = self.get_mouse_x_location()
        current_destination_x = self.canvas_mouse_location_x
        #current_destination_y = self.get_mouse_y_location()
        current_destination_y = self.canvas_mouse_location_y
        self.canvas.create_rectangle(self.origin_x, self.origin_y, current_destination_x, current_destination_y, outline='white')


    def highlight_selected_entities(self):#JUST-TRANSFERRED
        for entity in self.game_environment.all_entities.selected:
            self.canvas.create_rectangle(entity.aabb.x1, entity.aabb.y1, entity.aabb.x2, entity.aabb.y2, outline='red', width=2)

    def display_entity(self, entity: ce.Entity):#JUST-TRANSFERRED
        self.canvas.create_image(entity.pos.x, entity.pos.y, image=entity.img, anchor=tk.NW)

    def display_laser_shot(self, laser_shot: ls.LaserShot):#JUST-TRANSFERRED
        #print('displaying-laser-shot')
        self.canvas.create_line(laser_shot.laser_pulse_beginning_point_vec.x, laser_shot.laser_pulse_beginning_point_vec.y, laser_shot.laser_pulse_end_point_vec.x, laser_shot.laser_pulse_end_point_vec.y, fill=laser_shot.laser_pulse_color, width=laser_shot.laser_pulse_width)

    def display_building(self, building):#JUST-TRANSFERRED
        self.canvas.create_image(building.x, building.y, image=building.img, anchor=tk.NW)

        #UPDATE-AFTER-REFACTOR
    def display_all_elements(self):#JUST-TRANSFERRED
        if self.unit_selector_enabled:
            self.draw_unit_selector()
        for entity in self.game_environment.all_entities.all:
            self.display_entity(entity)
            if not self.game_environment.all_entities.selected_is_empty():
                self.highlight_selected_entities()
        for laser_shot in self.game_environment.projectiles.laser_shots:
            self.display_laser_shot(laser_shot)
        if self.game_environment.buildings.all != []:
            for building in self.game_environment.buildings.all:
                self.display_building(building)

    def tick(self):#JUST-TRANSFERRED
        #self.main_window.after(60, self.tick)
        if self.display_environment_tick_enabled:
            self.canvas.delete('all')
            self.check_for_key_binding_set_parameters()
            self.update_canvas_frame_placement()
            self.draw_map_stripes_background()

            self.track_mouse_location()
            self.restrict_mouse_within_display_area()

            self.display_all_elements()
