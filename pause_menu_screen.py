import tk_simple_canvas as tsc
import tkinter as tk
import unit_data as ud

class PauseScreenUI:
    def __init__(self, display_environment):
        self.display_environment = display_environment
        self.pause_screen_canvas_bg_color = "#FF0000"#red
        self.pause_screen_canvas_x_placement: int = 0
        self.pause_screen_canvas_y_placement: int = 0

        self.pause_screen_display_frame_width: float = float(self.display_environment.main_window_width) / 2.0 - self.display_environment.display_frame_main_window_offset * 2
        self.pause_screen_display_frame_height: float = float(self.display_environment.main_window_height) / 2.0 - self.display_environment.display_frame_main_window_offset * 2

        self.pause_screen_display_frame = tk.Frame(self.display_environment.main_window, width=self.pause_screen_display_frame_width, height=self.pause_screen_display_frame_height)
        self.pause_screen_display_frame.place(x=self.display_environment.display_frame_main_window_offset, y=self.display_environment.display_frame_main_window_offset)#NEED-TO-UPDATE-PLACEMENT-TO-FORMAT-IN-MIDDLE-OF-MAIN-WINDOW-FRAME
        self.pause_screen_display_frame_aabb: ud.AABB = ud.AABB(0, 0, self.display_environment.display_frame.winfo_reqwidth(), self.display_environment.display_frame.winfo_reqheight())#UPDATE-FOR-HALVED-CORRECT-VALUES

        self.pause_screen_canvas = tk.Canvas(self.pause_screen_display_frame, bg=self.pause_screen_canvas_bg_color, width=self.display_environment.map_width, height=self.display_environment.map_height)
        self.pause_screen_canvas.place(x=self.pause_screen_canvas_x_placement,y=self.pause_screen_canvas_y_placement)
        self.pause_screen_canvas_aabb: ud.AABB = ud.AABB(0, 0, self.pause_screen_canvas.winfo_reqwidth(), self.pause_screen_canvas.winfo_reqheight())

    def remove_environment(self):
        self.pause_screen_canvas.place_forget()
        self.pause_screen_display_frame.place_forget()