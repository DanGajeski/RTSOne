import tk_simple_canvas as tsc
import tkinter as tk
import unit_data as ud

class ExitGameUI:
    def __init__(self, display_environment):
        self.display_environment = display_environment

        self.exit_game_screen_canvas_bg_color = "#FF0000"#red
        self.exit_game_screen_canvas_x_placement: int = 0
        self.exit_game_screen_canvas_y_placement: int = 0

        self.exit_game_screen_display_frame = tk.Frame(self.display_environment.main_window, width=self.display_environment.main_window_width - self.display_environment.display_frame_main_window_offset*2, height=self.display_environment.main_window_height - self.display_environment.display_frame_main_window_offset*2)
        self.exit_game_screen_display_frame.place(x=self.display_environment.display_frame_main_window_offset, y=self.display_environment.display_frame_main_window_offset)
        self.exit_game_screen_display_frame_aabb: ud.AABB = ud.AABB(0, 0, self.exit_game_screen_display_frame.winfo_reqwidth(), self.exit_game_screen_display_frame.winfo_reqheight())

        self.exit_game_screen_canvas = tk.Canvas(self.exit_game_screen_display_frame, bg=self.exit_game_screen_canvas_bg_color, width=self.display_environment.map_width, height=self.display_environment.map_height)
        self.exit_game_screen_canvas.place(x=self.exit_game_screen_canvas_x_placement,y=self.exit_game_screen_canvas_y_placement)
        self.exit_game_screen_canvas_aabb: ud.AABB = ud.AABB(0, 0, self.exit_game_screen_canvas.winfo_reqwidth(), self.exit_game_screen_canvas.winfo_reqheight())

    def remove_environment(self):
        self.exit_game_screen_canvas.place_forget()
        self.exit_game_screen_display_frame.place_forget()

    def play_exit_animation(self):
        pass
        #use_perf_timer

    def transition_to_closing_program(self):
        pass

    def tick(self):
        pass