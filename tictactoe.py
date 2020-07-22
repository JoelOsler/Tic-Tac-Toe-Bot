#!/usr/bin/env python

# Tic Tac Toe

import random
import serial
import time
import sys


if len(sys.argv) != 2:
    raise ValueError('tictactoe.py -p <port (/dev/tty.***********) >')


def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the tuple is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            # down the right side
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def drawWinLine(bo, le):
    if (bo[7] == le and bo[8] == le and bo[9] == le):
        robot.fastto(-30, -25, 5)
        time.sleep(0.2)
        robot.fastto(-30, -25, 0)
        time.sleep(0.2)
        robot.fastto(0, -25, 0)
        time.sleep(0.2)
        robot.fastto(30, -25, 0)
        time.sleep(0.2)
        robot.fastto(30, -25, 5)
    if (bo[4] == le and bo[5] == le and bo[6] == le):
        robot.fastto(-30, 0, 5)
        time.sleep(0.2)
        robot.fastto(-30, 0, 0)
        time.sleep(0.2)
        robot.fastto(30, 0, 0)
        time.sleep(0.2)
        robot.fastto(30, 0, 5)
    if (bo[1] == le and bo[2] == le and bo[3] == le):
        robot.fastto(-30, 25, 5)
        time.sleep(0.2)
        robot.fastto(-30, 25, 0)
        time.sleep(0.2)
        robot.fastto(30, 25, 0)
        time.sleep(0.2)
        robot.fastto(30, 25, 5)
    if (bo[7] == le and bo[4] == le and bo[1] == le):
        robot.fastto(25, -30, 5)
        time.sleep(0.2)
        robot.fastto(25, -30, 0)
        time.sleep(0.2)
        robot.fastto(25, 30, 0)
        time.sleep(0.2)
        robot.fastto(25, 30, 5)
    if (bo[8] == le and bo[5] == le and bo[2] == le):
        robot.fastto(0, -30, 5)
        time.sleep(0.2)
        robot.fastto(0, -30, 0)
        time.sleep(0.2)
        robot.fastto(0, 30, 0)
        time.sleep(0.2)
        robot.fastto(0, 30, 5)
    if (bo[9] == le and bo[6] == le and bo[3] == le):
        robot.fastto(-25, -30, 5)
        time.sleep(0.2)
        robot.fastto(-25, -30, 0)
        time.sleep(0.2)
        robot.fastto(-25, 30, 0)
        time.sleep(0.2)
        robot.fastto(-25, 30, 5)
    if (bo[7] == le and bo[5] == le and bo[3] == le):
        robot.fastto(-30, 30, 5)
        time.sleep(0.2)
        robot.fastto(-30, 30, 0)
        time.sleep(0.2)
        robot.fastto(30, -30, 0)
        time.sleep(0.2)
        robot.fastto(30, -30, 5)
    if (bo[9] == le and bo[5] == le and bo[1] == le):
        robot.fastto(-30, -30, 5)
        time.sleep(0.2)
        robot.fastto(-30, -30, 0)
        time.sleep(0.2)
        robot.fastto(30, 30, 0)
        time.sleep(0.2)
        robot.fastto(30, 30, 5)


def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '


def getPlayerMove(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


# Robot Junk


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


def drawPhysicalBoard():
    # Raw GCODE for a tic tac toe board in svg
    robot.gcode("G0 Z10 F3800")
    robot.gcode("M2000")
    robot.gcode("M888 P0")
    robot.gcode("G0 F3800")
    robot.gcode("G1 F2500")
    robot.gcode("G0 X-38.83 Y11.83")
    robot.gcode("G1 Z0.00")
    robot.gcode("G1 X39.17 Y11.83")
    robot.gcode("G0 Z10")
    robot.gcode("G0 X-38.50 Y-13.17")
    robot.gcode("G1 Z0.00")
    robot.gcode("G1 X38.83 Y-13.17")
    robot.gcode("G0 Z10")
    robot.gcode("G0 X12.83 Y38.50")
    robot.gcode("G1 Z0.00")
    robot.gcode("G1 X12.83 Y-40.17")
    robot.gcode("G0 Z10")
    robot.gcode("G0 X-12.17 Y38.50")
    robot.gcode("G1 Z0.00")
    robot.gcode("G1 X-12.17 Y-40.17")
    robot.gcode("G0 Z10")
    robot.gcode("G0 X10.00 Y-11.00")
    robot.gcode("G0 Z10")
    robot.fastto(0, -105, 60)


print('Welcome to Tic Tac Toe!')
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


# BEGIN Scraped Code

# I scraped this because it made no sense, so now there are "Calibration Instructions" on GitHub

# Ask for pen tip offset, in units

# print('What is the pen offset? (Distance in units from tip of pen to board, +2 if using soft tipped dry erase markers, +0 to +1 for pens/pencils/styluses.) {!!Integers only please!!}')
# offset = int(input())

# END Scraped Code


while True:
    print('Does it need to be calibrated? (yes or no)')
    if (input().lower().startswith('y')):
        print('Moving to calibration position...')
        robot.fastto(0, 0, 2)
        print('Place writing utencil into pen holder and tighten, then type "ready" when completed.')
        if (not input().lower().startswith('r')):
            print('Restart program to try again.')
        robot.fastto(0, -105, 60)

    # Ask player if they need a board drawn
    print('Would you like a board drawn? (yes or no)')
    if (input().lower().startswith('y')):
        drawPhysicalBoard()

    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    # Main game loop
    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                # Robot turns left and right as if it were mad
                robot.fastto(0, -105, 60)
                robot.fastto(-25, -105, 60)
                robot.fastto(25, -105, 60)
                robot.fastto(0, -105, 60)
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    # Robot moves forward and backward as if it is declaring "truce"
                    robot.fastto(0, -105, 60)
                    robot.fastto(0, -80, 60)
                    robot.fastto(0, -130, 60)
                    robot.fastto(0, -80, 60)
                    robot.fastto(0, -130, 60)
                    robot.fastto(0, -105, 60)
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            # Below is my brain pain at 11:00 P.M. calculating each spot for an X
            if (move == 9):
                if (computerLetter == "X"):
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
            if (move == 8):
                if (computerLetter == "X"):
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
            if (move == 7):
                if (computerLetter == "X"):
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
            if (move == 6):
                if (computerLetter == "X"):
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
            if (move == 5):
                if (computerLetter == "X"):
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
            if (move == 4):
                if (computerLetter == "X"):
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
            if (move == 3):
                if (computerLetter == "X"):
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
            if (move == 2):
                if (computerLetter == "X"):
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
            if (move == 1):
                if (computerLetter == "X"):
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
            if isWinner(theBoard, computerLetter):
                drawWinLine(theBoard, computerLetter)
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                # Robot moves up and down as if it were happy
                robot.fastto(0, -105, 60)
                robot.fastto(0, -105, 85)
                robot.fastto(0, -105, 35)
                robot.fastto(0, -105, 60)
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    # Robot moves forward and backward as if it is declaring "truce"
                    robot.fastto(0, -105, 60)
                    robot.fastto(0, -80, 60)
                    robot.fastto(0, -130, 60)
                    robot.fastto(0, -80, 60)
                    robot.fastto(0, -130, 60)
                    robot.fastto(0, -105, 60)
                    break
                else:
                    robot.fastto(0, -105, 60)
                    turn = 'player'
    if not playAgain():
        # Return robot to "idle" position for next game or when they exit
        robot.fastto(0, -105, 60)
        robot.disconnect()
        break
sys.exit()
