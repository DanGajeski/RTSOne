import tk_simple_canvas as tsc
import tkinter as tk
import unit_data as ud

class GameSettingsUI:
    def __init__(self, display_environment):
        self.display_environment = display_environment

        self.game_settings_canvas_bg_color = "#0FF000"#red
        self.game_settings_canvas_x_placement: int = 0
        self.game_settings_canvas_y_placement: int = 0

        #self.pause_screen_display_frame_width: float = float(self.display_environment.main_window_width) / 2.0 - self.display_environment.display_frame_main_window_offset * 2
        #self.pause_screen_display_frame_height: float = float(self.display_environment.main_window_height) / 2.0 - self.display_environment.display_frame_main_window_offset * 2

        self.game_settings_display_frame = tk.Frame(self.display_environment.main_window, width=self.display_environment.main_window_width - self.display_environment.display_frame_main_window_offset*2, height=self.display_environment.main_window_height - self.display_environment.display_frame_main_window_offset*2)
        self.game_settings_display_frame.place(x=self.display_environment.display_frame_main_window_offset, y=self.display_environment.display_frame_main_window_offset)
        self.game_settings_display_frame_aabb: ud.AABB = ud.AABB(0, 0, self.game_settings_display_frame.winfo_reqwidth(), self.game_settings_display_frame.winfo_reqheight())

        self.game_settings_canvas = tk.Canvas(self.game_settings_display_frame, bg=self.game_settings_canvas_bg_color, width=self.display_environment.map_width, height=self.display_environment.map_height)
        self.game_settings_canvas.place(x=self.game_settings_canvas_x_placement,y=self.game_settings_canvas_y_placement)
        self.game_settings_canvas_aabb: ud.AABB = ud.AABB(0, 0, self.game_settings_canvas.winfo_reqwidth(), self.game_settings_canvas.winfo_reqheight())

    def remove_environment(self):
        self.game_settings_canvas.place_forget()
        self.game_settings_display_frame.place_forget()

    def transition_to_game_display_environment_ui(self):
        self.display_environment.swap_to_game_display_environment_ui()

    #deploy-difficulty-button
    #deploy-color-settings-button