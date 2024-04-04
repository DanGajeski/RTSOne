import tk_simple_canvas as tsc
import tkinter as tk
import unit_data as ud

class StartScreenUI:
    def __init__(self, display_environment: tsc.DisplayEnvironment):
        self.display_environment = display_environment
        self.start_screen_canvas_bg_color = "0000FF"
        self.start_screen_canvas_x_placement: int = 0
        self.start_screen_canvas_y_placement: int = 0

        self.start_screen_display_frame = tk.Frame(self.display_environment.main_window, width=self.display_environment.main_window_width - self.display_environment.display_frame_main_window_offset*2, height=self.display_environment.main_window_height - self.display_environment.display_frame_main_window_offset*2)
        self.start_screen_display_frame.place(x=self.display_environment.display_frame_main_window_offset, y=self.display_environment.display_frame_main_window_offset)
        self.start_screen_display_frame_aabb: ud.AABB = ud.AABB(0, 0, self.display_environment.display_frame.winfo_reqwidth(), self.display_environment.display_frame.winfo_reqheight())

        self.start_screen_canvas = tk.Canvas(self.start_screen_display_frame, bg=self.start_screen_canvas_bg_color, width=self.display_environment.map_width, height=self.display_environment.map_height)
        self.start_screen_canvas.place(x=self.start_screen_canvas_x_placement,y=self.start_screen_canvas_y_placement)
        self.start_screen_canvas_aabb: ud.AABB = ud.AABB(0, 0, self.start_screen_canvas.winfo_reqwidth(), self.start_screen_canvas.winfo_reqheight())

        #next-up->need to add switching functionality to display_environment + game_environment