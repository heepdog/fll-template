# LEGO slot:1 autostart

from hub import button, light_matrix, motion_sensor, port
import motor 
import motor_pair
import color_sensor

class robot:

    def __init__(self):
        self.left_motor = port.A
        self.right_motor = port.E
        try:
            motor_pair.pair(motor_pair.PAIR_1, self.left_motor, self.right_motor)
        except OSError as e:
            print(f'Error pairing motors: {e}')
        self.drive = motor_pair.PAIR_1
        self.motion = motion_sensor
        self.light = light_matrix
        self.button = button
        self.left_attachment = port.B
        self.right_attachment = port.D
        self.left_color_sensor = port.C
        self.right_color_sensor = port.F
        self.wheel_distance = 200
        self.wheel_diameter = 56 # mm

    def drive_forward(self, direction=0, distance_in=0, speed_pct=50):
        if distance_in == 0:
            move = motor_pair.move
        else:
            move = motor_pair.move_for_degrees
            distance_mm = distance_in * 25.4
            rotations = distance_mm / (self.wheel_diameter * 3.14159)
            degrees = rotations * 360

        speed = 1050 * speed_pct / 100
        print(f'driving forward: direction={direction}, distance_in={distance_in}, speed_pct={speed_pct}, degrees={degrees if distance_in != 0 else "N/A"}, speed={speed}')
        try:
            move(pair=self.drive, degrees= degrees,steering=direction, velocity=speed, acceleration=500,)
        except OSError as e:
            print(f'Error driving forward: {e}')

    def stop_robot(self):
        self.drive.stop()

    def get_left_wheel_degrees(self):
        return motor.relative_position(self.left_motor)

    def get_right_wheel_degrees(self):
        return motor.relative_position(self.right_motor)
    
    def reset_wheel_degrees(self):
        motor.reset_relative_position(self.left_motor)
        motor.reset_relative_position(self.right_motor)

robot = robot()

def report_devices():
    pass
if __name__ == '__main__':
    print('robot module')
    robot.drive_forward(direction= 10, distance_in=5, speed_pct=50)
