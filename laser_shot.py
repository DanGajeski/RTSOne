import math as math
import dan_math as dm
import unit_data as ud


class LaserShot():
    def __init__(self, origin_point, target_point, origin_team_id):
        self.origin_x = origin_point[0]
        self.origin_y = origin_point[1]
        self.origin_vec = ud.Vec2d(self.origin_x, self.origin_y)
        self.target_x = target_point[0]
        self.target_y = target_point[1]
        self.target_vec = ud.Vec2d(self.target_x, self.target_y)
        self.team_id: int = origin_team_id
        self.laser_pulse_range: int = 60
        #self.laser_pulse_color: str = "#FF0000"
        self.laser_pulse_width: int = 3
        self.laser_pulse_length: int = 30
        self.laser_pulse_speed: int = 20

        def init_laser_pulse_color():
            #contains-new-att-self.laser_pulse_color
            if self.team_id == 0:
                self.laser_pulse_color = "#FF0000"
            elif self.team_id == 1:
                self.laser_pulse_color = "#0000FF"
        init_laser_pulse_color()

        #untested
        self.origin_target_angle = math.atan2(self.target_y - self.origin_y, self.target_x - self.origin_x)
        self.laser_normalizer = dm.Normalizer(self.origin_vec, self.target_vec)
        self.normalized_movement_vec = self.laser_normalizer.get_movement_vector()

        self.laser_pulse_end_point_vec = ud.Vec2d(self.origin_vec.x, self.origin_vec.y)
        self.laser_pulse_beginning_point_vec = ud.Vec2d(self.origin_vec.x, self.origin_vec.y)

        self.hit_target: bool = False
        self.able_to_disable: bool = False

        self.distance: float = 0.0

        #print("first" + str(self.normalized_movement_vec.x))
        #print("second" + str(self.normalized_movement_vec.x))

        #self.calculate_pulse_beginning_point()

    #def calculate_pulse_beginning_point(self):
        #beginning_point_x = self.laser_pulse_range * math.cos(self.origin_target_angle)
        #beginning_point_y = self.laser_pulse_range * math.sin(self.origin_target_angle)
        #self.laser_pulse_beginning_point_vec = ud.Vec2d(beginning_point_x, beginning_point_y)

    def disabled(self):
        return self.able_to_disable and self.distance <= 4
    def get_beginning_end_vec_distance(self):
        self.distance = math.sqrt((self.laser_pulse_end_point_vec.x - self.laser_pulse_beginning_point_vec.x) * (self.laser_pulse_end_point_vec.x - self.laser_pulse_beginning_point_vec.x) + (self.laser_pulse_end_point_vec.y - self.laser_pulse_beginning_point_vec.y) * (self.laser_pulse_end_point_vec.y - self.laser_pulse_beginning_point_vec.y))
        if self.distance >= 15:
            self.able_to_disable = True
    def update_pulse_end_point(self):
        if self.laser_pulse_end_point_vec.x > self.target_vec.x - 1 and self.laser_pulse_end_point_vec.x < self.target_vec.x + 1 and self.laser_pulse_end_point_vec.y > self.target_vec.y - 1 and self.laser_pulse_end_point_vec.y < self.target_vec.y + 1:
            self.hit_target = True
            pass
        else:
        #pass
        #print(self.laser_normalizer.normalized_x)
        #print(self.laser_pulse_beginning_point_vec.x)
        #print(self.laser_pulse_end_point_vec.x)
        #print(self.laser_pulse_beginning_point_vec.y)
        #(self.normalizer.normalized_x)
        #print(self.normalizer.normalized_y)
        #print("This should be changing:    " + str(self.laser_pulse_end_point_vec.x))
        #print(str(self.team_id) + "Normalized X : " + str(self.normalized_movement_vec.x))
            self.laser_pulse_end_point_vec.x += self.normalized_movement_vec.x
            self.laser_pulse_end_point_vec.y += self.normalized_movement_vec.y

    def update_pulse_beginning_point(self):
        if self.hit_target:
            if self.distance < 4:
                pass
            else:
                self.laser_pulse_beginning_point_vec.x += self.normalized_movement_vec.x
                self.laser_pulse_beginning_point_vec.y += self.normalized_movement_vec.y
        if self.distance >= self.laser_pulse_length:
            self.laser_pulse_beginning_point_vec.x += self.normalized_movement_vec.x
            self.laser_pulse_beginning_point_vec.y += self.normalized_movement_vec.y

    def tick(self):
        #print(self.origin_target_angle)
        #UPDATE-FOR-COLLISION-CHECK-UNITY-AND-EFFICIENCY
        for speed in range(self.laser_pulse_speed):
            self.update_pulse_end_point()
            self.get_beginning_end_vec_distance()
            self.update_pulse_beginning_point()