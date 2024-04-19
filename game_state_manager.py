import start_screen as ss
import main_menu_screen as mms
import game_environment_ui as geu
import game_settings_screen as gss
import exit_game_screen as egs
import all_uis as au
import tkinter as tk
import pause_menu_screen as pms


#file meant to be where UIS get INITIALIZED and SWAPPED out for one another.

#Possible new origin point after main.   Load all necessary UI elements into this file and then enable proper UI swapping to take place here.

#UI-MANAGER
class GameStateManager():
    def __init__(self):
        pass
        self.all_uis: au.AllUIs = au.AllUIs()

        self.map_width: float = 1000.0
        self.map_height: float = 1000.0

        self.display_frame_main_window_offset: float = 10.0#xANDy placement

        self.canvas_x_placement: int = 0
        self.canvas_y_placement: int = 0

        self.main_window_width: float = 520.0
        self.main_window_height: float = 520.0

        #main_window_dimensions_geometry_object_formatted
        self.main_window_dimensions_geometry_formatted: str = str(int(self.main_window_width)) + "x" + str(int(self.main_window_height))
        #main_window_title
        self.main_window_title_text: str = "Dan's Fuckin' RTS"

        #MAIN-UI-ELEMENT
        #init_window
        self.main_window = tk.Tk()
        self.main_window.geometry(self.main_window_dimensions_geometry_formatted)
        self.main_window.title(self.main_window_title_text)


        self.pause_menu_ui_name: str = "pause_menu_screen"
        self.start_screen_ui_name: str = "start_screen"
        self.main_menu_screen_ui_name: str = "main_menu_screen"
        self.exit_game_screen_ui_name: str = "exit_game_screen"
        self.game_settings_screen_ui_name: str = "game_settings_screen"
        self.game_environment_ui_name: str = "game_environment_screen"

        self.game_environment_tick_enabled: bool = False
        self.start_screen_tick_enabled: bool = False
        self.exit_game_screen_tick_enabled: bool = False
        self.pause_menu_screen_tick_enabled: bool = False
        self.main_menu_screen_tick_enabled: bool = False
        self.game_settings_screen_tick_enabled: bool = False

        self.game_environment_reset: bool = True

        self.game_environment_enabled: bool = False
        self.game_environment_keybindings_set: bool = False
        self.game_environment: None
        self.start_screen_environment_enabled: bool = False
        self.start_screen_environment_keybindings_set: bool = False
        self.start_screen_environment: None
        self.main_menu_screen_environment_enabled: bool = False
        self.main_menu_screen_environment_keybindings_set: bool = False
        self.main_menu_screen_environment: None
        self.exit_game_screen_environment_enabled: bool = False
        self.exit_game_screen_environment_keybindings_set: bool = False
        self.exit_game_screen_environment: None

    def run_main_window(self):
        self.main_window.mainloop()

    def swap_to_start_screen_ui(self):
        if self.all_uis.all[self.main_menu_screen_ui_name]:
            self.all_uis.all[self.main_menu_screen_ui_name].unload_main_menu_screen_ui()
        elif self.all_uis.all[self.exit_game_screen_ui_name]:
            self.all_uis.all[self.exit_game_screen_ui_name].unload_exit_game_screen_ui()
        elif self.all_uis.all[self.game_environment_ui_name]:
            self.all_uis.all[self.game_environment_ui_name].unload_game_environment_ui()

        if self.all_uis.all[self.start_screen_ui_name]:
            self.unload_start_screen_ui()
        elif not self.all_uis.all[self.start_screen_ui_name]:
            self.all_uis.add_ui(self.start_screen_ui_name, ss.StartScreenUI(self))

    def unload_start_screen_ui(self):
        self.all_uis.all[self.start_screen_ui_name].remove_environment()
        self.all_uis.reset_ui_to_none(self.start_screen_ui_name)

    def swap_to_main_menu_screen_ui(self):
        if self.all_uis.all[self.start_screen_ui_name]:
            self.all_uis.all[self.start_screen_ui_name].unload_start_screen_ui()
        elif self.all_uis.all[self.exit_game_screen_ui_name]:
            self.all_uis.all[self.exit_game_screen_ui_name].unload_exit_game_screen_ui()
        elif self.all_uis.all[self.game_environment_ui_name]:
            self.all_uis.all[self.game_environment_ui_name].unload_game_environment_ui()

        if self.all_uis.all[self.main_menu_screen_ui_name]:
            pass
        elif not self.all_uis.all[self.main_menu_screen_ui_name]:
            self.all_uis.add_ui(self.main_menu_screen_ui_name, mms.MainMenuUI(self))

    def unload_main_menu_screen_ui(self):
        self.all_uis.all[self.main_menu_screen_ui_name].remove_environment()
        self.all_uis.reset_ui_to_none(self.main_menu_screen_ui_name)

    def swap_to_exit_game_screen_ui(self):
        if self.all_uis.all[self.main_menu_screen_ui_name]:
            self.all_uis.all[self.main_menu_screen_ui_name].unload_main_menu_screen_ui()
        elif self.all_uis.all[self.start_screen_ui_name]:
            self.all_uis.all[self.start_screen_ui_name].unload_start_screen_ui()
        elif self.all_uis.all[self.exit_game_screen_ui_name]:
            self.all_uis.all[self.exit_game_screen_ui_name].unload_game_display_environment_ui()

        if self.all_uis.all[self.exit_game_screen_ui_name]:
            self.unload_exit_game_screen_ui()
        elif not self.all_uis.all[self.exit_game_screen_ui_name]:
            self.all_uis.add_ui(self.exit_game_screen_ui_name, egs.ExitGameUI(self))

    def unload_exit_game_screen_ui(self):
        self.all_uis.all[self.exit_game_screen_ui_name].remove_environment()
        self.all_uis.reset_ui_to_none(self.exit_game_screen_ui_name)

    def swap_to_game_environment_ui(self):
        if self.all_uis.all[self.start_screen_ui_name]:
            self.all_uis.all[self.start_screen_ui_name].unload_start_screen_ui()
        elif self.all_uis.all[self.exit_game_screen_ui_name]:
            self.all_uis.all[self.exit_game_screen_ui_name].unload_exit_game_screen_ui()
        elif self.all_uis.all[self.main_menu_screen_ui_name]:
            self.all_uis.all[self.main_menu_screen_ui_name].unload_main_menu_screen_ui()

        if self.all_uis.all[self.game_environment_ui_name]:
            pass
        elif not self.all_uis.all[self.game_environment_ui_name]:
            self.all_uis.add_ui(self.game_environment_ui_name, geu.GameEnvironmentUI(self))

    def unload_game_environment_ui(self):
        self.all_uis.all[self.game_environment_ui_name].remove_environment()
        self.all_uis.reset_ui_to_none(self.game_environment_ui_name)



    # #COME-BACK-HERE_ADD-self.canvas_ui_name canvas to self.all_uis.all
    # def swap_to_game_environment_ui(self):
    #     if self.all_uis.all[self.main_menu_screen_ui_name]:
    #         self.all_uis.all[self.main_menu_screen_ui_name].unload_main_menu_screen_ui()
    #     elif self.all_uis.all[self.exit_game_screen_ui_name]:
    #         self.all_uis.all[self.exit_game_screen_ui_name].unload_exit_game_screen_ui()
    #     elif self.all_uis.all[self.start_screen_ui_name]:
    #         self.all_uis.all[self.start_screen_ui_name].unload_start_screen_ui()
    #
    #     if self.all_uis.all[self.game_environment_ui_name]:
    #         self.unload_game_environment_ui()
    #     elif not self.all_uis.all[self.game_environment_ui_name]:
    #         self.all_uis.add_ui(self.game_environment_ui_name, geu.GameEnvironmentUI())
    #
    #         #<-OR->
    #     #elif not self.all_uis.all[self.canvas_ui_name]:
    #         self.all_uis.add_ui(self.canvas_ui_name, )
    #
    #         #Perhaps-update-game-environment-ui-to-own-file-for-streamlined-tick-with-other-uis
    #         #self.enable_game_display_environment()...?#perhaps-not-needed-after-tick-change
    #         #self.all_uis.add_ui(self.canvas_ui_name, self.canvas)
    #
    # def unload_game_environment_ui(self):
    #     #self.all_uis.all[self.canvas_ui_name].remove_environment()
    #     self.game_environment.toggle_game_environment_tick()
    #     self.canvas.place_forget()
    #     self.canvas: tk.Canvas = None
    #     self.all_uis.all[self.canvas_ui_name] = 0
    #     self.game_environment.reset_game_environment()
    #     self.diplay_environment_tick_enabled = False




    #UNUSED
    def toggle_pause_menu_ui(self):
        if self.pause_menu_ui:
            self.display_environment_tick_enabled = True
            self.pause_menu_ui.pause_screen_display_frame.place_forget()
            self.pause_menu_ui = None
            self.game_environment.toggle_game_environment_tick()
        elif not self.pause_menu_ui:
            self.pause_menu_ui = pms.PauseScreenUI(self)
            self.display_environment_tick_enabled = False
            self.game_environment.toggle_game_environment_tick()

    #UNUSED
    #PRIORITY-UPDATE
    def toggle_game_settings_screen_ui(self):
        pass
        #if self.game_settings_screen_ui:
        #UPDATE-to-display-and-toggle-on-top-of-main_menu_screen