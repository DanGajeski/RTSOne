from PIL import Image
from PIL import ImageTk
from pathlib import Path
import math as math

class ImgInfo():
    def __init__(self):
        self.img_height: int = 20 #CHANGE-to-entity_img_height
        self.img_width: int = 20 #CHANGE-to-entity-img_width
        self.builder_building_img_height: int = 40
        self.builder_building_img_width: int = 40

        self.img_folder_path: str = "imgs"
        self.main_character_img_name: str = "happy_guy.png"
        self.player_two_trooper_img_name: str = "mad_guy.png"
        self.builder_building_img_name: str = "builder_building.png"
        self.img_file_location = Path(__file__).parent/self.img_folder_path

        self.main_character_img: ImageTk.PhotoImage = ImageTk.PhotoImage(Image.open(self.img_file_location/self.main_character_img_name))
        self.player_two_trooper_img: ImageTk.PhotoImage = ImageTk.PhotoImage(Image.open(self.img_file_location/self.player_two_trooper_img_name))
        self.builder_building_img: ImageTk.PhotoImage = ImageTk.PhotoImage(Image.open(self.img_file_location/self.builder_building_img_name))

class Vec2d():
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other_vec):
        return math.sqrt( ((other_vec.x - self.x)*(other_vec.x - self.x)) + ((other_vec.y - self.y)*(other_vec.y - self.y)) )

class AABB():
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def check_xy_in_aabb(self, x: float, y: float):
        return x >= self.x1-1 and x <= self.x2+1 and y >= self.y1-1 and y <= self.y2+1 #TEST->adding1-to-buffer-size-to-prevent-overlap-of-barriers-and-subsequent-overlap-of-unit-locations

    def check_aabb_in_aabb(self, aabb_check):
        if self.check_xy_in_aabb(aabb_check.x1, aabb_check.y1):
            return True
        elif self.check_xy_in_aabb(aabb_check.x2, aabb_check.y2):
            return True
        elif self.check_xy_in_aabb(aabb_check.x1, aabb_check.y2):
            return True
        elif self.check_xy_in_aabb(aabb_check.x2, aabb_check.y1):
            return True
        else:
            return False

    def check_xy_on_border(self, x: float, y: float):
        return x == self.x1 or x == self.x2 or y == self.y1 or y == self.y2

    #confirmed-already-ran-check_xy_on_border-first
    def check_xy_on_which_border(self, x: float, y: float):
        if x == self.x1 and y == self.y1:
            return "downright"
        elif x == self.x1 and y == self.y2:
            return "upright"
        elif x == self.x2 and y == self.y1:
            return "downleft"
        elif x == self.x2 and y == self.y2:
            return "upleft"
        if x == self.x1:
            return "right"
        elif x == self.x2:
            return "left"
        elif y == self.y1:
            return "down"
        elif y == self.y2:
            return "up"

    #point-args-confirmed-outside-of-aabb
    def restrict_point_within_aabb(self, x: float, y: float):
        #0-up
        #1-upright
        #2-right
        #3-downright
        #4-down
        #5-downleft
        #6-left
        #7-upleft
        if x < self.x1 and y >= self.y1 and y <= self.y2:
            return (self.x1, y, 2)
        if x < self.x1 and y < self.y1:
            return (self.x1, self.y1, 3)
        if x < self.x1 and y > self.y2:
            return (self.x1, self.y2, 1)

        if x >= self.x1 and x <= self.x2 and y < self.y1:
            return (x, self.y1, 4)
        if x >= self.x1 and x <= self.x2 and y > self.y2:
            return (x, self.y2, 0)

        if x > self.x2 and y >= self.y1 and y <= self.y2:
            return (self.x2, y, 6)
        if x > self.x2 and y < self.y1:
            return (self.x2, self.y1, 5)
        if x > self.x2 and y > self.y2:
            return (self.x2, self.y2, 7)

    def find_center_point(self):
        width = self.x2 - self.x1
        height = self.y2 - self.y1

        new_x = self.x1 + width/2
        new_y = self.y1 + height/2

        self.center_point = (new_x, new_y)

    def distance_to_other_aabb(self, other_aabb):
        self.find_center_point()
        other_aabb.find_center_point()

        return math.sqrt( ((other_aabb.center_point[0] - self.center_point[0])*(other_aabb.center_point[0] - self.center_point[0])) + ((other_aabb.center_point[1] - self.center_point[1])*(other_aabb.center_point[1] - self.center_point[1])) )