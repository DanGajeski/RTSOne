import tk_simple_canvas as tsc
import tkinter as tk
import unit_data as ud

class MainMenuUI:
    def __init__(self, display_environment):
        self.display_environment = display_environment

        self.main_menu_canvas_bg_color = "#00FF00"#red
        self.main_menu_canvas_x_placement: int = 0
        self.main_menu_canvas_y_placement: int = 0

        #self.pause_screen_display_frame_width: float = float(self.display_environment.main_window_width) / 2.0 - self.display_environment.display_frame_main_window_offset * 2
        #self.pause_screen_display_frame_height: float = float(self.display_environment.main_window_height) / 2.0 - self.display_environment.display_frame_main_window_offset * 2

        self.main_menu_display_frame = tk.Frame(self.display_environment.main_window, width=self.display_environment.main_window_width - self.display_environment.display_frame_main_window_offset*2, height=self.display_environment.main_window_height - self.display_environment.display_frame_main_window_offset*2)
        self.main_menu_display_frame.place(x=self.display_environment.display_frame_main_window_offset, y=self.display_environment.display_frame_main_window_offset)
        self.main_menu_display_frame_aabb: ud.AABB = ud.AABB(0, 0, self.main_menu_display_frame.winfo_reqwidth(), self.main_menu_display_frame.winfo_reqheight())

        self.main_menu_canvas = tk.Canvas(self.main_menu_display_frame, bg=self.main_menu_canvas_bg_color, width=self.display_environment.map_width, height=self.display_environment.map_height)
        self.main_menu_canvas.place(x=self.main_menu_canvas_x_placement,y=self.main_menu_canvas_y_placement)
        self.main_menu_canvas_aabb: ud.AABB = ud.AABB(0, 0, self.main_menu_canvas.winfo_reqwidth(), self.main_menu_canvas.winfo_reqheight())

    def remove_environment(self):
        self.main_menu_canvas.place_forget()
        self.main_menu_display_frame.place_forget()