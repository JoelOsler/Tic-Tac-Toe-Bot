
import serial
import time
import sys


class Roboter():
    x = 0
    y = 0
    z = 0
    connected = 0
    error = 0
    line = 0

    def __init__(self, x=0, y=0, z=0, connected=0, error=0):
        self.x = x
        self.y = y
        self.z = z
        self.error = error
        self.connected = connected
        self.message = ''
        self.ok = True
        self.ser = None
        self.line = 0

    def fastto(self, x, y, z):
        if self.ok == True:
            self.x = x
            self.y = y
            self.z = z
            # self.printAttributes()
            if self.connected == 1 and self.error == 0:
                self.ser.write(bytes('G0 X' + str(x) + ' Y' +
                                     str(y) + ' Z' + str(z) + '\n', 'utf-8'))
            else:
                self.error = 1
        self.wait_ok()

    def gcode(self, gcode):
        if self.ok == True:
            # self.printAttributes()
            if self.connected == 1 and self.error == 0:
                self.ser.write(bytes(str(gcode) + '\n', 'utf-8'))
            else:
                self.error = 1
        self.wait_ok()

    def wait_ok(self):
        # self.ser.write(bytes('M114\n', 'utf-8'))
        loop = True
        while loop == True:
            all = self.ser.readline()
            if (all.decode('utf-8') == 'ok\n'):
                loop = False
                return
            else:
                time.sleep(0.5)

            # if len(coo) > 4:
            #    x1 = int(coo[0].split(':')[1].split('.')[0])
            #    y1 = int(coo[1].split(':')[1].split('.')[0])
            #    z1 = int(coo[2].split(':')[1].split('.')[0])

            #    if self.x == x1 and self.y == y1 and self.z == z1:
            #        loop = False
            #    else:
            #        time.sleep(1)

    def reset(self):
        if self.ok == True:
            self.x = 0
            self.y = 0
            self.z = 0
            # self.printAttributes()
            if self.connected == 1 and self.error == 0:
                self.ser.write(bytes('M1111\n', 'utf-8'))
                self.wait_ok()
            else:
                self.error = 1

    def printAttributes(self):
        print('X', self.x, '| Y', self.y, '| Z',
              self.z, ' ( c = ', self.connected, ') ')
        if self.error == 1:
            print('error: ', self.error)
        # print('ser: ', self.ser)
        print(self.message)

    def connect(self):
        try:
            self.ser = serial.Serial(
                sys.argv[1], 115200, bytesize=8, parity='N', stopbits=1)
            self.connected = 1
        except:
            self.error = 1

    def disconnect(self):
        self.ser.close()
        self.connected = 0


print('Welcome to Tic Tac Toe Unit Tests!')
time.sleep(0.8)
print('Initializing Robot...')
robot = Roboter()
# Connects to robot
robot.connect()
# Wait a few for fun
time.sleep(0.5)
# I discarded this because it was unnecessary
# robot.reset()
# I instead used M1112 to move to HOME
robot.gcode("M1112")
# Tell robot that we are using the pen holder, for the correct middle offset
robot.gcode("M888 P0")
# Tell robot to set work origin to HOME, for my ease and to keep me sane while developing this program
robot.gcode("G92 X0 Y0 Z60")
# Tell robot to move to the "idle" position behind the board
robot.fastto(0, -105, 60)

while True:
    print("Draw X's or Draw Win Lines? (0 or 1)")
    option = int(input())
    if (option == 0):
        print("Which grid position? (1-9)")
        move = int(input())
        if (move == 9):
            # Coords:     X    Y   Z
            robot.fastto(-25, -25, 5)
            time.sleep(0.2)
            robot.fastto(-25, -25, 0)
            time.sleep(0.2)
            robot.fastto(-30, -30, 0)
            time.sleep(0.2)
            robot.fastto(-20, -20, 0)
            time.sleep(0.2)
            robot.fastto(-20, -20, 5)
            time.sleep(0.2)
            robot.fastto(-30, -20, 5)
            time.sleep(0.2)
            robot.fastto(-30, -20, 0)
            time.sleep(0.2)
            robot.fastto(-20, -30, 0)
            time.sleep(0.2)
            robot.fastto(-20, -30, 5)
            time.sleep(0.2)
            robot.fastto(-25, -25, 5)
            time.sleep(0.5)
            robot.fastto(0, -105, 60)
        if (move == 8):
            # Coords:    X   Y   Z
            robot.fastto(0, -25, 5)
            time.sleep(0.2)
            robot.fastto(0, -25, 0)
            time.sleep(0.2)
            robot.fastto(-5, -30, 0)
            time.sleep(0.2)
            robot.fastto(5, -20, 0)
            time.sleep(0.2)
            robot.fastto(5, -20, 5)
            time.sleep(0.2)
            robot.fastto(-5, -20, 5)
            time.sleep(0.2)
            robot.fastto(-5, -20, 0)
            time.sleep(0.2)
            robot.fastto(5, -30, 0)
            time.sleep(0.2)
            robot.fastto(5, -30, 5)
            time.sleep(0.2)
            robot.fastto(0, -25, 5)
            time.sleep(0.5)
            robot.fastto(0, -105, 60)
        if (move == 7):
            # Coords:    X    Y   Z
            robot.fastto(25, -25, 5)
            time.sleep(0.2)
            robot.fastto(25, -25, 0)
            time.sleep(0.2)
            robot.fastto(20, -30, 0)
            time.sleep(0.2)
            robot.fastto(30, -20, 0)
            time.sleep(0.2)
            robot.fastto(30, -20, 5)
            time.sleep(0.2)
            robot.fastto(20, -20, 5)
            time.sleep(0.2)
            robot.fastto(20, -20, 0)
            time.sleep(0.2)
            robot.fastto(30, -30, 0)
            time.sleep(0.2)
            robot.fastto(30, -30, 5)
            time.sleep(0.2)
            robot.fastto(25, -25, 5)
            time.sleep(0.5)
            robot.fastto(0, -105, 60)
        if (move == 6):
            # Coords:     X   Y  Z
            robot.fastto(-25, 0, 5)
            time.sleep(0.2)
            robot.fastto(-25, 0, 0)
            time.sleep(0.2)
            robot.fastto(-30, -5, 0)
            time.sleep(0.2)
            robot.fastto(-20, 5, 0)
            time.sleep(0.2)
            robot.fastto(-20, 5, 5)
            time.sleep(0.2)
            robot.fastto(-30, 5, 5)
            time.sleep(0.2)
            robot.fastto(-30, 5, 0)
            time.sleep(0.2)
            robot.fastto(-20, -5, 0)
            time.sleep(0.2)
            robot.fastto(-20, -5, 5)
            time.sleep(0.2)
            robot.fastto(-25, 0, 5)
            time.sleep(0.5)
            robot.fastto(0, -105, 60)
        if (move == 5):
            # Coords:    X  Y  Z
            robot.fastto(0, 0, 5)
            time.sleep(0.2)
            robot.fastto(0, 0, 0)
            time.sleep(0.2)
            robot.fastto(-5, -5, 0)
            time.sleep(0.2)
            robot.fastto(5, 5, 0)
            time.sleep(0.2)
            robot.fastto(5, 5, 5)
            time.sleep(0.2)
            robot.fastto(-5, 5, 5)
            time.sleep(0.2)
            robot.fastto(-5, 5, 0)
            time.sleep(0.2)
            robot.fastto(5, -5, 0)
            time.sleep(0.2)
            robot.fastto(5, -5, 5)
            time.sleep(0.2)
            robot.fastto(0, 0, 5)
            time.sleep(0.5)
            robot.fastto(0, -105, 60)
        if (move == 4):
            # Coords:    X   Y  Z
            robot.fastto(25, 0, 5)
            time.sleep(0.2)
            robot.fastto(25, 0, 0)
            time.sleep(0.2)
            robot.fastto(20, -5, 0)
            time.sleep(0.2)
            robot.fastto(30, 5, 0)
            time.sleep(0.2)
            robot.fastto(30, 5, 5)
            time.sleep(0.2)
            robot.fastto(20, 5, 5)
            time.sleep(0.2)
            robot.fastto(20, 5, 0)
            time.sleep(0.2)
            robot.fastto(30, -5, 0)
            time.sleep(0.2)
            robot.fastto(30, -5, 5)
            time.sleep(0.2)
            robot.fastto(25, 0, 5)
            time.sleep(0.5)
            robot.fastto(0, -105, 60)
        if (move == 3):
            # Coords:     X   Y   Z
            robot.fastto(-25, 25, 5)
            time.sleep(0.2)
            robot.fastto(-25, 25, 0)
            time.sleep(0.2)
            robot.fastto(-30, 20, 0)
            time.sleep(0.2)
            robot.fastto(-20, 30, 0)
            time.sleep(0.2)
            robot.fastto(-20, 30, 5)
            time.sleep(0.2)
            robot.fastto(-30, 30, 5)
            time.sleep(0.2)
            robot.fastto(-30, 30, 0)
            time.sleep(0.2)
            robot.fastto(-20, 20, 0)
            time.sleep(0.2)
            robot.fastto(-20, 20, 5)
            time.sleep(0.2)
            robot.fastto(-25, 25, 5)
            time.sleep(0.5)
            robot.fastto(0, -105, 60)
        if (move == 2):
            # Coords:    X  Y   Z
            robot.fastto(0, 25, 5)
            time.sleep(0.2)
            robot.fastto(0, 25, 0)
            time.sleep(0.2)
            robot.fastto(-5, 20, 0)
            time.sleep(0.2)
            robot.fastto(5, 30, 0)
            time.sleep(0.2)
            robot.fastto(5, 30, 5)
            time.sleep(0.2)
            robot.fastto(-5, 30, 5)
            time.sleep(0.2)
            robot.fastto(-5, 30, 0)
            time.sleep(0.2)
            robot.fastto(5, 20, 0)
            time.sleep(0.2)
            robot.fastto(5, 20, 5)
            time.sleep(0.2)
            robot.fastto(0, 25, 5)
            time.sleep(0.5)
            robot.fastto(0, -105, 60)
        if (move == 1):
            # Coords:    X   Y   Z
            robot.fastto(25, 25, 5)
            time.sleep(0.2)
            robot.fastto(25, 25, 0)
            time.sleep(0.2)
            robot.fastto(20, 20, 0)
            time.sleep(0.2)
            robot.fastto(30, 30, 0)
            time.sleep(0.2)
            robot.fastto(30, 30, 5)
            time.sleep(0.2)
            robot.fastto(20, 30, 5)
            time.sleep(0.2)
            robot.fastto(20, 30, 0)
            time.sleep(0.2)
            robot.fastto(30, 20, 0)
            time.sleep(0.2)
            robot.fastto(30, 20, 5)
            time.sleep(0.2)
            robot.fastto(25, 25, 5)
            time.sleep(0.5)
            robot.fastto(0, -105, 60)
    elif (option == 1):
        print("Which direction? (rows, columns, diagonals)")
        direction = input()
        if (direction.lower().startswith('r')):
            print("What row? (grid boxes 7-9 = 0, 4-6 = 1, 1-3 = 2)")
            row = int(input())
            if (row == 0):
                robot.fastto(-30, -25, 5)
                time.sleep(0.2)
                robot.fastto(-30, -25, 0)
                time.sleep(0.2)
                robot.fastto(0, -25, 0)
                time.sleep(0.2)
                robot.fastto(30, -25, 0)
                time.sleep(0.2)
                robot.fastto(30, -25, 5)
            if (row == 1):
                robot.fastto(-30, 0, 5)
                time.sleep(0.2)
                robot.fastto(-30, 0, 0)
                time.sleep(0.2)
                robot.fastto(30, 0, 0)
                time.sleep(0.2)
                robot.fastto(30, 0, 5)
            if (row == 2):
                robot.fastto(-30, 25, 5)
                time.sleep(0.2)
                robot.fastto(-30, 25, 0)
                time.sleep(0.2)
                robot.fastto(30, 25, 0)
                time.sleep(0.2)
                robot.fastto(30, 25, 5)
        if (direction.lower().startswith('c')):
            print("What column? (grid boxes 7-1 = 0, 8-2 = 1, 9-3 = 2)")
            row = int(input())
            if (row == 0):
                robot.fastto(25, -30, 5)
                time.sleep(0.2)
                robot.fastto(25, -30, 0)
                time.sleep(0.2)
                robot.fastto(25, 30, 0)
                time.sleep(0.2)
                robot.fastto(25, 30, 5)
            if (row == 1):
                robot.fastto(0, -30, 5)
                time.sleep(0.2)
                robot.fastto(0, -30, 0)
                time.sleep(0.2)
                robot.fastto(0, 30, 0)
                time.sleep(0.2)
                robot.fastto(0, 30, 5)
            if (row == 2):
                robot.fastto(-25, -30, 5)
                time.sleep(0.2)
                robot.fastto(-25, -30, 0)
                time.sleep(0.2)
                robot.fastto(-25, 30, 0)
                time.sleep(0.2)
                robot.fastto(-25, 30, 5)
        if (direction.lower().startswith('d')):
            print("Which diagonal? (grid boxes 7-3 = 0, 9-1 = 1)")
            row = int(input())
            if (row == 0):
                robot.fastto(-30, 30, 5)
                time.sleep(0.2)
                robot.fastto(-30, 30, 0)
                time.sleep(0.2)
                robot.fastto(30, -30, 0)
                time.sleep(0.2)
                robot.fastto(30, -30, 5)
            if (row == 1):
                robot.fastto(-30, -30, 5)
                time.sleep(0.2)
                robot.fastto(-30, -30, 0)
                time.sleep(0.2)
                robot.fastto(30, 30, 0)
                time.sleep(0.2)
                robot.fastto(30, 30, 5)
    robot.fastto(0, -105, 60)
