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

    def remove_environment(self):
        self.canvas.place_forget()
        #self.diplay_environment.display_frame.place_forget()

    #def transition_to_game_environment_ui(self):
    #    self.display_environment.swap_to_game_environment_ui()

    def tick(self):
        pass