import tkinter as tk

import game_environment
import unit_data as ud
import canvas_entities as ce
import selected_entities as se
import win32api as win32api
import player as player
import laser_shot as ls
import dan_math as dm
import math as math
import builder_building as bb
#import start_screen as ss
import pause_menu_screen as pms
import start_screen as ss
import main_menu_screen as mms
import exit_game_screen as egs
import game_settings_screen as gss
import game_environment_ui as geu
import all_uis as au


class DisplayEnvironment():

    def __init__(self):
        self.all_uis: au.AllUIs = au.AllUIs()#TRANSFERRED
        #contianer_frame_main_window_offset
        self.map_width: float = 1000.0#TRANSFERRED
        self.map_height: float = 1000.0#TRANSFERRED

        self.display_frame_main_window_offset: float = 10.0#TRANSFERRED

        self.main_window_width: float = 520.0#TRANSFERRED
        self.main_window_height: float = 520.0#TRANSFERRED

        self.canvas_x_placement: int = 0#TRANSFERRED
        self.canvas_y_placement: int = 0#TRANSFERRED

        #main_window_dimensions_geometry_object_formatted
        self.main_window_dimensions_geometry_formatted: str = str(int(self.main_window_width)) + "x" + str(int(self.main_window_height))#TRANSFERRED
        #main_window_title
        self.main_window_title_text: str = "Dan's Fuckin' RTS"#TRANSFERRED

        #canvas_color
        self.canvas_bg_color: str = "#00FF00"#TRANSFERRED
        self.canvas_vertical_stripe_color: str = "#FFFFFF"#TRANSFERRED
        self.canvas_horitontal_stripe_color: str = "#000000"#TRANSFERRED

        #MAIN-UI-ELEMENT
        #init_window
        self.main_window = tk.Tk()#TRANSFERRED
        self.main_window.geometry(self.main_window_dimensions_geometry_formatted)#TRANSFERRED
        self.main_window.title(self.main_window_title_text)#TRANSFERRED

        #GAME-UI-ELEMENTS
        #init_frame
        self.display_frame = tk.Frame(self.main_window, width=self.main_window_width - self.display_frame_main_window_offset*2, height=self.main_window_height - self.display_frame_main_window_offset*2)#TRANSFERRED
        self.display_frame.place(x=self.display_frame_main_window_offset, y=self.display_frame_main_window_offset)#TRANSFERRED
        self.display_frame_aabb: ud.AABB = ud.AABB(0, 0, self.display_frame.winfo_reqwidth(), self.display_frame.winfo_reqheight())#TRANSFERRED

        #GAME-UI-ELEMENTS
        #init_canvas
        #self.canvas = tk.Canvas(self.display_frame, bg=self.canvas_bg_color, width=self.map_width, height=self.map_height)
        #self.canvas.place(x=self.canvas_x_placement,y=self.canvas_y_placement)
        #self.canvas_aabb: ud.AABB = ud.AABB(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight())


        self.game_environment_enabled: bool = False#TRANSFERRED
        self.game_environment_keybindings_set: bool = False#TRANSFERRED
        self.game_environment: None#TRANSFERRED

        self.start_screen_environment_enabled: bool = False#TRANSFERRED
        self.start_screen_environment_keybindings_set: bool = False#TRANSFERRED
        self.start_screen_environment: None#TRANSFERRED

        self.main_menu_screen_environment_enabled: bool = False#TRANSFERRED
        self.main_menu_screen_environment_keybindings_set: bool = False#TRANSFERRED
        self.main_menu_screen_environment: None#TRANSFERRED

        self.exit_game_screen_environment_enabled: bool = False#TRANSFERRED
        self.exit_game_screen_environment_keybindings_set: bool = False#TRANSFERRED
        self.exit_game_screen_environment: None#TRANSFERRED

        #MOVING
        #MOVE-GAMEENVIRONMENT
        #self.laser_shots: list = []

        #MOVING
        #MOVE-GAMEENVIRONMENT
        #self.player_entity: ce.Entity = ce.Entity(ud.Vec2d(50.0, 50.0), 1, 0, self.laser_shots)
        #self.game_entity_one: ce.Entity = ce.Entity(ud.Vec2d(100.0, 100.0), 2, 0, self.laser_shots)
        #self.game_entity_two: ce.Entity = ce.Entity(ud.Vec2d(200.0, 200.0), 3, 0, self.laser_shots)
        #self.game_entity_three: ce.Entity = ce.Entity(ud.Vec2d(300.0, 300.0), 4, 0, self.laser_shots)
        #self.game_entity_four: ce.Entity = ce.Entity(ud.Vec2d(400.0, 400.0), 5, 0, self.laser_shots)
        #self.game_entity_five: ce.Entity = ce.Entity(ud.Vec2d(200.0, 100.0), 6, 0, self.laser_shots)

        #MOVING
        #MOVE-GAMEENVIRONMENT
        #self.enemy_entity_one: ce.Entity = ce.Entity(ud.Vec2d(100.0, 400.0), 7, 1, self.laser_shots)
        #self.enemy_entity_two: ce.Entity = ce.Entity(ud.Vec2d(400.0, 100.0), 8, 1, self.laser_shots)
        #self.enemy_entity_three: ce.Entity = ce.Entity(ud.Vec2d(400.0, 150), 9, 1, self.laser_shots)
        #self.enemy_entity_four: ce.Entity = ce.Entity(ud.Vec2d(100.0, 450), 10, 1, self.laser_shots)
        #self.enemy_entity_five: ce.Entity = ce.Entity(ud.Vec2d(150.0, 370), 11, 1, self.laser_shots)

        #MOVING
        #MOVE-GAMEENVIRONMENT
        #inits w/ player_entity and game_entity_one, game_entity_two
        #self.all_entities: list = [self.player_entity, self.game_entity_one, self.game_entity_two, self.game_entity_three, self.game_entity_four, self.game_entity_five, self.enemy_entity_one, self.enemy_entity_two, self.enemy_entity_three, self.enemy_entity_four, self.enemy_entity_five]


        #MOVE-GAMEENVIRONMENT
        #default-target_vec_value
        #self.target_vec: ud.Vec2d = ud.Vec2d(100.0, 100.0)


        #FOR-PRINT-TESTING-ONLY
        #self.example_entity: ce.Entity = self.game_entity_one
        #self.x_differential: int = 0
        #self.y_differential: int = 0

        #MOVE-GAMEENVIRONMENT
        #game_spaceNON_UI_ELEMENTS

        #MOVING
        #self.selected_entities = se.SelectedEntities()

        #MOVE-SECTION-TO-GAME-ENVIRONMENT-UI****************************************************<<<<<<<<<<<<<<<<<<<<<<<<
        self.origin_x: float = 0.0
        self.origin_y: float = 0.0
        self.destination_x: float = 0.0
        self.destination_y: float = 0.0
        self.unit_selector_enabled: bool = False
        self.motion_selection_aabb: ud.AABB = ud.AABB(0,0,0,0)

        self.mouse_border_monitoring: bool = False

        self.display_screen_canvas_scroll_speed: int = 5

        self.track_entity_attack_ranges_enabled: bool = False
        #MOVE-SECTION-TO-GAME-ENVIRONMENT-UI****************************************************<<<<<<<<<<<<<<<<<<<<<<<<

        self.display_environment_tick_enabled: bool = False#TRANSFERRED
        #self.pause_menu_ui: pms.PauseScreenUI = None
        #self.start_screen_ui: ss.StartScreenUI = None
        #self.main_menu_screen_ui: mms.MainMenuUI = None
        #self.exit_game_screen_ui: egs.ExitGameUI = None
        #self.game_settings_screen_ui: gss.GameSettingsUI = None
        #self.game_environment_ui: geu.GameEnvironmentUI = None

        self.pause_menu_ui_name: str = "pause_menu_screen"#TRANSFERRED
        self.start_screen_ui_name: str = "start_screen"#TRANSFERRED
        self.main_menu_screen_ui_name: str = "main_menu_screen"#TRANSFERRED
        self.exit_game_screen_ui_name: str = "exit_game_screen"#TRANSFERRED
        self.game_settings_screen_ui_name: str = "game_settings_screen"#TRANSFERRED
        self.canvas_ui_name: str = "canvas_screen"#TRANSFERRED/UPDATED

        self.game_environment_reset: bool = True#TRANSFERRED
        #Switch-to-All_Entities class

        #self.set_window_bindings()
        #change-to-call-tick-from-rts-main?
        #self.tick()

        #self.enable_start_screen_environment()

        #initial-UI-loader
        self.enable_game_display_environment()


    def enable_game_display_environment(self):#UNNEEDED
        self.game_display_environment_enabled = True
        self.display_environment_tick_enabled = True
        #GAME-UI-ELEMENTS
        #init_frame
        #self.display_frame = tk.Frame(self.main_window, width=self.main_window_width - self.display_frame_main_window_offset*2, height=self.main_window_height - self.display_frame_main_window_offset*2)
        #self.display_frame.place(x=self.display_frame_main_window_offset, y=self.display_frame_main_window_offset)
        #self.display_frame_aabb: ud.AABB = ud.AABB(0, 0, self.display_frame.winfo_reqwidth(), self.display_frame.winfo_reqheight())

        #GAME-UI-ELEMENTS
        #init_canvas
        self.canvas = tk.Canvas(self.display_frame, bg=self.canvas_bg_color, width=self.map_width, height=self.map_height)
        self.canvas.place(x=self.canvas_x_placement,y=self.canvas_y_placement)
        self.canvas_aabb: ud.AABB = ud.AABB(0, 0, self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight())
        self.all_uis.all[self.canvas_ui_name] = 1
        if self.game_environment:
            self.game_environment.toggle_game_environment_tick()

    def enable_start_screen_environment(self):#UNNEEDED
        self.start_screen_environment = ss.StartScreenUI(self)

    def disable_start_screen_environment(self):#UNNEDED??
        self.start_screen_environment.remove_environment()
        self.start_screen_environment = None

    #attach-to-game-environment
    def import_game_environment(self, game_environment):
        self.game_environment = game_environment

        #INITIAL-DISPLAY-CALL
        #for entity in self.game_environment.all_entities.all:
        #    self.display_entity(entity)

    #for-key_bindings
    def get_main_window(self):
        return self.main_window

    def draw_map_stripes_background(self):#FOR-GAME_ENVIRONMENT_UI
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

    #MOVING
    def set_target_movement_location(self):#FOR-GAME_ENVIRONMENT_UI
        #self.target_vec = ud.Vec2d(self.canvas_mouse_location_x, self.canvas_mouse_location_y)
        self.game_environment.all_entities.set_target_vec_selected(ud.Vec2d(self.canvas_mouse_location_x, self.canvas_mouse_location_y))

    def set_display_key_bindings(self):#SPLIT-KEY-BINDINGS-INTO-UI-KEYBINDINGS
        self.game_display_environment_keybindings_set = True

        self.main_window.bind('<Motion>', lambda event: self.track_mouse_location())
        self.main_window.bind('<Button-3>', lambda event: self.set_target_movement_location())
        self.main_window.bind('<Button-1>', lambda event: self.set_unit_selector_origin())
        self.main_window.bind('<ButtonRelease-1>', lambda event: self.button_release_checks())
        self.main_window.bind('l', lambda event: self.lock_cursor_to_frame())

        self.main_window.bind('<Escape>', lambda event: self.toggle_pause_menu_ui())

        self.main_window.bind('<Key-1>', lambda event: self.swap_to_start_screen_ui())
        self.main_window.bind('<Key-2>', lambda event: self.swap_to_main_menu_screen_ui())
        self.main_window.bind('<Key-3>', lambda event: self.swap_to_game_display_environment_ui())
        self.main_window.bind('<Key-4>', lambda event: self.swap_to_exit_game_screen_ui())

        #self.main_window.bind('t', lambda event: self.enable_track_entity_attack_ranges())
        #self.main_window.bind('<Up>', lambda event: self.move_display_frame_up())
        #self.main_window.bind('<Left>', lambda event: self.move_display_frame_left())
        #self.main_window.bind('<Right>', lambda event: self.move_display_frame_right())
        #self.main_window.bind('<Down>', lambda event: self.move_display_frame_down())

    # def swap_to_start_screen_ui(self):
    #     if self.main_menu_screen_ui:
    #         self.unload_main_menu_screen_ui()
    #     elif self.exit_game_screen_ui:
    #         self.unload_exit_game_screen_ui()
    #     elif self.canvas:
    #         self.unload_game_display_environment_ui()
    #
    #     if self.start_screen_ui:
    #         pass
    #     elif not self.start_screen_ui:
    #         self.start_screen_ui = ss.StartScreenUI(self)

    def swap_to_start_screen_ui(self):#TRANSFERRED
        if self.all_uis.all[self.main_menu_screen_ui_name]:
            self.all_uis.all[self.main_menu_screen_ui_name].unload_main_menu_screen_ui()
        elif self.all_uis.all[self.exit_game_screen_ui_name]:
            self.all_uis.all[self.exit_game_screen_ui_name].unload_exit_game_screen_ui()
        elif self.all_uis.all[self.canvas_ui_name]:
            self.all_uis.all[self.canvas_ui_name].unload_game_display_environment_ui()

        if self.all_uis.all[self.start_screen_ui_name]:
            self.unload_start_screen_ui()
        elif not self.all_uis.all[self.start_screen_ui_name]:
            self.all_uis.add_ui(self.start_screen_ui_name, ss.StartScreenUI(self))

    def unload_start_screen_ui(self):#TRANSFERRED
        self.all_uis.all[self.start_screen_ui_name].remove_environment()
        self.all_uis.reset_ui_to_none(self.start_screen_ui_name)

    #def unload_start_screen_ui(self):
    #    self.start_screen_ui.remove_environment()
    #    self.start_screen_ui = None


    # def swap_to_main_menu_screen_ui(self):
    #     if self.start_screen_ui:
    #         self.unload_start_screen_ui()
    #     elif self.exit_game_screen_ui:
    #         self.unload_exit_game_screen_ui()
    #     elif self.canvas:
    #         self.unload_game_display_environment_ui()
    #
    #     if self.main_menu_screen_ui:
    #         pass
    #     elif not self.main_menu_screen_ui:
    #         self.main_menu_screen_ui = mms.MainMenuUI(self)
    # def unload_main_menu_screen_ui(self):
    #     self.main_menu_screen_ui.remove_environment()
    #     self.main_menu_screen_ui = None

    def swap_to_main_menu_screen_ui(self):#TRANSFERRED
        if self.all_uis.all[self.start_screen_ui_name]:
            self.all_uis.all[self.start_screen_ui_name].unload_start_screen_ui()
        elif self.all_uis.all[self.exit_game_screen_ui_name]:
            self.all_uis.all[self.exit_game_screen_ui_name].unload_exit_game_screen_ui()
        elif self.all_uis.all[self.canvas_ui_name]:
            self.all_uis.all[self.canvas_ui_name].unload_game_display_environment_ui()

        if self.all_uis.all[self.main_menu_screen_ui_name]:
            pass
        elif not self.all_uis.all[self.main_menu_screen_ui_name]:
            self.all_uis.add_ui(self.main_menu_screen_ui_name, mms.MainMenuUI(self))

    def unload_main_menu_screen_ui(self):#TRANSFERRED
        self.all_uis.all[self.main_menu_screen_ui_name].remove_environment()
        self.all_uis.reset_ui_to_none(self.main_menu_screen_ui_name)

    # def swap_to_game_display_environment_ui(self):
    #     if self.start_screen_ui:
    #         self.unload_start_screen_ui()
    #     elif self.exit_game_screen_ui:
    #         self.unload_exit_game_screen_ui()
    #     elif self.main_menu_screen_ui:
    #         self.unload_main_menu_screen_ui()
    #
    #     if self.canvas:
    #         pass
    #     elif not self.canvas:
    #         self.enable_game_display_environment()
    # def unload_game_display_environment_ui(self):
    #     self.game_environment.toggle_game_environment_tick()
    #     self.canvas.place_forget()
    #     self.canvas: tk.Canvas = None
    #     self.game_environment.reset_game_environment()
    #     self.display_environment_tick_enabled = False

    def swap_to_display_environment_ui_ui_streamlined(self):#TRANSFERRED
        if self.all_uis.all[self.start_screen_ui_name]:
            self.all_uis.all[self.start_screen_ui_name].unload_start_screen_ui()
        elif self.all_uis.all[self.exit_game_screen_ui_name]:
            self.all_uis.all[self.exit_game_screen_ui_name].unload_exit_game_screen_ui()
        elif self.all_uis.all[self.main_menu_screen_ui_name]:
            self.all_uis.all[self.main_menu_screen_ui_name].unload_main_menu_screen_ui()

        if self.all_uis.all[self.canvas_ui_name]:
            pass
        elif not self.all_uis.all[self.canvas_ui_name]:
            self.all_uis.add_ui(self.canvas_ui_name, geu.GameEnvironmentUI(self))

    def unload_display_environment_ui_streamlined(self):#TRANSFERRED
        self.all_uis.all[self.main_menu_screen_ui_name].remove_environment()
        self.all_uis.reset_ui_to_none(self.main_menu_screen_ui_name)

    #COME-BACK-HERE_ADD-self.canvas_ui_name canvas to self.all_uis.all
    def swap_to_game_display_environment_ui(self):#TRANSFERRED
        if self.all_uis.all[self.main_menu_screen_ui_name]:
            self.all_uis.all[self.main_menu_screen_ui_name].unload_main_menu_screen_ui()
        elif self.all_uis.all[self.exit_game_screen_ui_name]:
            self.all_uis.all[self.exit_game_screen_ui_name].unload_exit_game_screen_ui()
        elif self.all_uis.all[self.start_screen_ui_name]:
            self.all_uis.all[self.start_screen_ui_name].unload_start_screen_ui()

        if self.all_uis.all[self.canvas_ui_name]:
            self.unload_game_display_environment_ui()
        elif not self.all_uis.all[self.canvas_ui_name]:
            self.enable_game_display_environment()
            #Perhaps-update-game-environment-ui-to-own-file-for-streamlined-tick-with-other-uis
            #self.enable_game_display_environment()...?#perhaps-not-needed-after-tick-change
            #self.all_uis.add_ui(self.canvas_ui_name, self.canvas)

    def unload_game_display_environment_ui(self):#TRANSFERRED
        #self.all_uis.all[self.canvas_ui_name].remove_environment()
        self.game_environment.toggle_game_environment_tick()
        self.canvas.place_forget()
        self.canvas: tk.Canvas = None
        self.all_uis.all[self.canvas_ui_name] = 0
        self.game_environment.reset_game_environment()
        self.diplay_environment_tick_enabled = False

    # def swap_to_exit_game_screen_ui(self):
    #     if self.main_menu_screen_ui:
    #         self.unload_main_menu_screen_ui()
    #     elif self.start_screen_ui:
    #         self.unload_start_screen_ui()
    #     elif self.canvas:
    #         self.unload_game_display_environment_ui()
    #
    #     if self.exit_game_screen_ui:
    #         pass
    #     elif not self.exit_game_screen_ui:
    #         self.exit_game_screen_ui = egs.ExitGameUI(self)
    # def unload_exit_game_screen_ui(self):
    #     self.exit_game_screen_ui.remove_environment()
    #     self.exit_game_screen_ui = None

    def swap_to_exit_game_screen_ui(self):#TRANSFERRED
        if self.all_uis.all[self.main_menu_screen_ui_name]:
            self.all_uis.all[self.main_menu_screen_ui_name].unload_main_menu_screen_ui()
        elif self.all_uis.all[self.start_screen_ui_name]:
            self.all_uis.all[self.start_screen_ui_name].unload_start_screen_ui()
        elif self.all_uis.all[self.canvas_ui_name]:
            self.all_uis.all[self.canvas_ui_name].unload_game_display_environment_ui()

        if self.all_uis.all[self.exit_game_screen_ui]:
            self.unload_exit_game_screen_ui()
        elif not self.all_uis.all[self.exit_game_screen_ui_name]:
            self.all_uis.add_ui(self.exit_game_screen_ui_name, egs.ExitGameUI(self))

    def unload_exit_game_screen_ui(self):#TRANSFERRED
        self.all_uis.all[self.exit_game_screen_ui].remove_environment()
        self.all_uis.reset_ui_to_none(self.exit_game_screen_ui_name)

    def toggle_pause_menu_ui(self):#TRANSFERRED
        if self.pause_menu_ui:
            self.display_environment_tick_enabled = True
            self.pause_menu_ui.pause_screen_display_frame.place_forget()
            self.pause_menu_ui = None
            self.game_environment.toggle_game_environment_tick()
        elif not self.pause_menu_ui:
            self.pause_menu_ui = pms.PauseScreenUI(self)
            self.display_environment_tick_enabled = False
            self.game_environment.toggle_game_environment_tick()

    #PRIORITY-UPDATE
    def toggle_game_settings_screen(self):#TRANSFERRED
        pass
        #if self.game_settings_screen_ui:
        #UPDATE-to-display-and-toggle-on-top-of-main_menu_screen

    #UPDATE-FRAMEWORK
    def transition_to_exit_game_screen_ui(self):#TRANSFERRED
        self.swap_to_exit_game_screen_ui()

    def check_for_key_binding_set_parameters(self):#UPDATE-FOR-ALL-KEYBINDINGS/UIS
        if self.game_display_environment_enabled:
            if not self.game_display_environment_keybindings_set:
                self.set_display_key_bindings()


    def track_mouse_location(self):#FOR-GAME_ENVIRONMENT_UI
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


    def move_display_frame_up(self):#FOR-GAME_ENVIRONMENT_UI
        self.canvas_y_placement-=5
    def move_display_frame_up_right(self):#FOR-GAME_ENVIRONMENT_UI
        self.canvas_y_placement-=5
        self.canvas_x_placement+=5
    def move_display_frame_up_left(self):#FOR-GAME_ENVIRONMENT_UI
        self.canvas_y_placement-=5
        self.canvas_x_placement-=5
    def move_display_frame_left(self):#FOR-GAME_ENVIRONMENT_UI
        self.canvas_x_placement-=5
    def move_display_frame_right(self):#FOR-GAME_ENVIRONMENT_UI
        self.canvas_x_placement+=5
    def move_display_frame_down(self):#FOR-GAME_ENVIRONMENT_UI
        self.canvas_y_placement+=5
    def move_display_frame_down_right(self):#FOR-GAME_ENVIRONMENT_UI
        self.canvas_y_placement+=5
        self.canvas_x_placement+=5
    def move_display_frame_down_left(self):#FOR-GAME_ENVIRONMENT_UI
        self.canvas_y_placement+=5
        self.canvas_x_placement-=5

    def set_unit_selector_origin(self):#FOR-GAME_ENVIRONMENT_UI
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

    def select_entity(self, entity):#FOR-GAME_ENVIRONMENT_UI
        self.game_environment.all_entities.add_to_selected_entities(entity)

    def enable_unit_selector(self):#FOR-GAME_ENVIRONMENT_UI
        self.unit_selector_enabled = True
        self.motion_selection_aabb.x1 = self.origin_x
        self.motion_selection_aabb.y1 = self.origin_y

    def make_selection(self):#FOR-GAME_ENVIRONMENT_UI
        #clear-selected-entities-first
        self.game_environment.all_entities.remove_all_selected_entities()
        for entity in self.game_environment.all_entities.all:
            if self.motion_selection_aabb.check_aabb_in_aabb(entity.aabb):
                if self.game_environment.player.team_id == entity.team_id:
                    self.game_environment.all_entities.add_to_selected_entities(entity)

    #MOVING
    def enable_track_entity_attack_ranges(self):#FOR-GAME_ENVIRONMENT_UI
        self.track_entity_attack_ranges_enabled: bool = True

    def update_canvas_frame_placement(self):#FOR-GAME_ENVIRONMENT_UI
        self.canvas.place(x=self.canvas_x_placement,y=self.canvas_y_placement)

    #CLEANTHISUPUPONREFACTOR
    def lock_cursor_to_frame(self):#FOR-GAME_ENVIRONMENT_UI
        if self.mouse_border_monitoring == True:
            self.mouse_border_monitoring = False
        else:
            if self.display_frame_aabb.check_xy_in_aabb(self.display_frame_mouse_location_point[0], self.display_frame_mouse_location_point[1]):
                print("Mouse in display frame")
                self.mouse_border_monitoring = True
            else:
                print("Mouse not in display frame")

    def display_frame_point_get_screen_xy(self, x: float, y: float):#FOR-GAME_ENVIRONMENT_UI
        new_windows_x = x + self.display_frame_main_window_offset + self.main_window_x_location_SCREEN
        new_windows_y = y + self.display_frame_main_window_offset + self.main_window_y_location_SCREEN
        return (new_windows_x, new_windows_y)

    #intotal-restricts-mouse-to-display-frame-and-scrolls-display-frame-dependent-on-scroll-speed
    #plan->for-update-to-only-allow-movement-within-game-environment-frame
    def restrict_mouse_within_display_area(self):#FOR-GAME_ENVIRONMENT_UI
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

    def button_release_checks(self):#FOR-GAME_ENVIRONMENT_UI
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

    def draw_unit_selector(self):#FOR-GAME_ENVIRONMENT_UI
        #current_destination_x = self.get_mouse_x_location()
        current_destination_x = self.canvas_mouse_location_x
        #current_destination_y = self.get_mouse_y_location()
        current_destination_y = self.canvas_mouse_location_y
        self.canvas.create_rectangle(self.origin_x, self.origin_y, current_destination_x, current_destination_y, outline='white')

    def run_main_window(self):#TRANSFERRED
        self.main_window.mainloop()

    def highlight_selected_entities(self):#FOR-GAME_ENVIRONMENT_UI
        for entity in self.game_environment.all_entities.selected:
            self.canvas.create_rectangle(entity.aabb.x1, entity.aabb.y1, entity.aabb.x2, entity.aabb.y2, outline='red', width=2)

    def display_entity(self, entity: ce.Entity):#FOR-GAME_ENVIRONMENT_UI
        self.canvas.create_image(entity.pos.x, entity.pos.y, image=entity.img, anchor=tk.NW)

    def display_laser_shot(self, laser_shot: ls.LaserShot):#FOR-GAME_ENVIRONMENT_UI
        #print('displaying-laser-shot')
        self.canvas.create_line(laser_shot.laser_pulse_beginning_point_vec.x, laser_shot.laser_pulse_beginning_point_vec.y, laser_shot.laser_pulse_end_point_vec.x, laser_shot.laser_pulse_end_point_vec.y, fill=laser_shot.laser_pulse_color, width=laser_shot.laser_pulse_width)

    def display_building(self, building):#FOR-GAME_ENVIRONMENT_UI
        self.canvas.create_image(building.x, building.y, image=building.img, anchor=tk.NW)

    #UPDATE-AFTER-REFACTOR
    def display_all_elements(self):#FOR-GAME_ENVIRONMENT_UI
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
                #collision_check_UPDATE

            #print('displaying LASER SHOT')

    def tick(self):#FOR-GAME_ENVIRONMENT_UI
        #self.main_window.after(60, self.tick)
        if self.display_environment_tick_enabled:
            self.canvas.delete('all')
            self.check_for_key_binding_set_parameters()
            self.update_canvas_frame_placement()
            self.draw_map_stripes_background()

            self.track_mouse_location()
            self.restrict_mouse_within_display_area()

            self.display_all_elements()

            #UPDATE-HERE-UPDATE-FUNCTIONS-TO-TAKE-IN-CANVAS
            #self.reset_canvas(canvas)#self.canvas.delete('all')
            #self.update_canvas_frame_placement()?
            #self.draw_map_stripes_background(canvas)
            #self.display_all_elements(canvas)


        #UPDATE-HERE->streamlined_uis_tick
        #for ui in self.all_uis.all:
        #    ui.tick()

        #moving-to-game_environment
        #MOVING
        # if self.track_entity_attack_ranges_enabled:
        #     for entity in self.all_entities:
        #         for other_entity in self.all_entities:
        #             if other_entity.id != entity.id:
        #                 if other_entity.team_id != entity.team_id:
        #                     entity.check_range_to_other_entity(other_entity)
        #MOVING-(tick)
        #for entity in self.all_entities:
        #    entity.tick()

        # removing_index_nums: list = []
        # for index, laser_shot in enumerate(self.laser_shots):
        #     #print(laser_shot)
        #     if laser_shot.disabled():
        #         removing_index_nums.append(index)
        # for num in removing_index_nums:
        #     self.laser_shots.pop(num)
        #     for num in removing_index_nums:
        #         num-=1

        #MOVING-(tick)
        #for laser_shot in self.laser_shots:
        #    if laser_shot.disabled():
        #        self.laser_shots.remove(laser_shot)
        #for laser_shot in self.laser_shots:
        #    laser_shot.tick()

        #MOVING-(tick)

        #if not self.selected_entities.is_empty():
        #    self.selected_entities.move_entities(self.target_vec, self.all_entities)