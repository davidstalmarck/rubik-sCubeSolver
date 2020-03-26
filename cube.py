import random
from tkinter import *

# sidornas numrering är white = W = 0 aka grey, blue = B = 1, red = R = 2, green = G = 3, orange = O = 4, yellow = Y = 5

window = Tk()

coloursMiddleLabel = {'W': Label(window, width="3", height="3", bg="grey"),
                      'B': Label(window, width="3", height="3", bg="blue"),
                      'R': Label(window, width="3", height="3", bg="red"),
                      'G': Label(window, width="3", height="3", bg="green"),
                      'O': Label(window, width="3", height="3", bg="Orange"),
                      'Y': Label(window, width="3", height="3", bg="Yellow")}

colourMiddle = ['W', 'B', 'R', 'G', 'O', 'Y']

# c = {'W0', Label(window, width="5", height="5", bg="white"), 'W1', Label(window, width="5", height="5", bg="white"), 'W2', Label(window, width="5", height="5", bg="white"), 'W3', Label(window, width="5", height="5", bg="white"), 'W4', Label(window, width="5", height="5", bg="white"), 'W5', Label(window, width="5", height="5", bg="white"), 'W6', Label(window, width="5", height="5",bg = "blue"), 'W7', Label(window, width="5", height="5",bg = "blue"), 'B0', Label(window, width="5", height="5",bg = "blue"), 'B1', Label(window, width="5", height="5",bg = "blue"), 'B2', Label(window, width="5", height="5",bg = "blue"), 'B3', Label(window, width="5", height="5",bg = "blue"), 'B4', Label(window, width="5", height="5",bg = "red"), 'B5', Label(window, width="5", height="5",bg = "red"), 'B6', Label(window, width="5", height="5",bg = "red"), 'B7', Label(window, width="5", height="5",bg = "red"), 'R0', Label(window, width="5", height="5",bg = "red"), 'R1', Label(window, width="5", height="5",bg = "red"), 'R2', Label(window, width="5", height="5",bg = "green"), 'R3', Label(window, width="5", height="5",bg = "green"), 'R4', Label(window, width="5", height="5",bg = "green"), 'R5', Label(window, width="5", height="5",bg = "green"), 'R6', Label(window, width="5", height="5",bg = "green"), 'R7', Label(window, width="5", height="5",bg = "green"), 'G0', Label(window, width="5", height="5",bg = "Orange"), 'G1', Label(window, width="5", height="5",bg = "Orange"), 'G2', Label(window, width="5", height="5",bg = "Orange"), ('G3', 'Label(window, width="5", height="5",bg = "Orange")'), ('G4', 'Label(window, width="5", height="5",bg = "Orange")'), ('G5', 'Label(window, width="5", height="5",bg = "Orange")'), ('G6', 'Label(window, width="5", height="5",bg = "Yellow")'), ('G7', 'Label(window, width="5", height="5",bg = "Yellow")'), ('O0', 'Label(window, width="5", height="5",bg = "Yellow")'), ('O1', 'Label(window, width="5", height="5",bg = "Yellow")'), ('O2', 'Label(window, width="5", height="5",bg = "Yellow")'), ('O3', 'Label(window, width="5", height="5",bg = "Yellow")'), ('O4', 'Label(window, width="5", height="5",bg = "Yellow")'), ('O5', 'Label(window, width="5", height="5",bg = "Yellow")')])}


dictColours = {'W0': Label(window, width="1", height="1", bg="grey"),
               'W1': Label(window, width="1", height="1", bg="grey"),
               'W2': Label(window, width="1", height="1", bg="grey"),
               'W3': Label(window, width="1", height="1", bg="grey"),
               'W4': Label(window, width="1", height="1", bg="grey"),
               'W5': Label(window, width="1", height="1", bg="grey"),
               'W6': Label(window, width="1", height="1", bg="grey"),
               'W7': Label(window, width="1", height="1", bg="grey"),
               'B0': Label(window, width="1", height="1", bg="blue"),
               'B1': Label(window, width="1", height="1", bg="blue"),
               'B2': Label(window, width="1", height="1", bg="blue"),
               'B3': Label(window, width="1", height="1", bg="blue"),
               'B4': Label(window, width="1", height="1", bg="blue"),
               'B5': Label(window, width="1", height="1", bg="blue"),
               'B6': Label(window, width="1", height="1", bg="blue"),
               'B7': Label(window, width="1", height="1", bg="blue"),
               'R0': Label(window, width="1", height="1", bg="red"),
               'R1': Label(window, width="1", height="1", bg="red"),
               'R2': Label(window, width="1", height="1", bg="red"),
               'R3': Label(window, width="1", height="1", bg="red"),
               'R4': Label(window, width="1", height="1", bg="red"),
               'R5': Label(window, width="1", height="1", bg="red"),
               'R6': Label(window, width="1", height="1", bg="red"),
               'R7': Label(window, width="1", height="1", bg="red"),
               'G0': Label(window, width="1", height="1", bg="green"),
               'G1': Label(window, width="1", height="1", bg="green"),
               'G2': Label(window, width="1", height="1", bg="green"),
               'G3': Label(window, width="1", height="1", bg="green"),
               'G4': Label(window, width="1", height="1", bg="green"),
               'G5': Label(window, width="1", height="1", bg="green"),
               'G6': Label(window, width="1", height="1", bg="green"),
               'G7': Label(window, width="1", height="1", bg="green"),
               'O0': Label(window, width="1", height="1", bg="Orange"),
               'O1': Label(window, width="1", height="1", bg="Orange"),
               'O2': Label(window, width="1", height="1", bg="Orange"),
               'O3': Label(window, width="1", height="1", bg="Orange"),
               'O4': Label(window, width="1", height="1", bg="Orange"),
               'O5': Label(window, width="1", height="1", bg="Orange"),
               'O6': Label(window, width="1", height="1", bg="Orange"),
               'O7': Label(window, width="1", height="1", bg="Orange"),
               'Y0': Label(window, width="1", height="1", bg="Yellow"),
               'Y1': Label(window, width="1", height="1", bg="Yellow"),
               'Y2': Label(window, width="1", height="1", bg="Yellow"),
               'Y3': Label(window, width="1", height="1", bg="Yellow"),
               'Y4': Label(window, width="1", height="1", bg="Yellow"),
               'Y5': Label(window, width="1", height="1", bg="Yellow"),
               'Y6': Label(window, width="1", height="1", bg="Yellow"),
               'Y7': Label(window, width="1", height="1", bg="Yellow")}


coloursOfCube = ['W0', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'R0',
                 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'O0', 'O1',
                 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7']

coloursOfCube = ['W0', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'R0',
                 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'O0', 'O1',
                 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8']
#>>>>>>> adebec253b1744cf48b68eaab359bac40bc0a3a0

# I want to be able to scale to any sizes
cubeSideSize = 3
sidesAffectedByEachMove = 4
totalPositions = 54
moveableTilesPerSide = 9
deltaInner = 2


class makeACube():
    def __init__(self):
        self.cube = coloursOfCube
        self.colourMiddle = colourMiddle
        self.colours = dictColours

    def shuffle(self):
        pass

    def specialCaseswapOuterPositions(self, sides, start):
        waiting_to_be_moved = [self.cube[sides[-1] * moveableTilesPerSide + start[0]],
                               self.cube[sides[-1] * moveableTilesPerSide + start[1]],
                               self.cube[sides[-1] * moveableTilesPerSide + start[2]]]

        # now I start moving the bricks
        tile = 1
        for i in range(sidesAffectedByEachMove):
            tile -= 1
            for j in range(cubeSideSize):
                newTile, oldTile = waiting_to_be_moved.pop(0), self.cube[sides[i] * moveableTilesPerSide + tile]
                waiting_to_be_moved.append(oldTile)

                self.cube[sides[i] * moveableTilesPerSide + tile] = newTile

                tile = (tile + 1) % moveableTilesPerSide

    def swapOuterPositions(self, sides, move):
        # sides is a list, and says which sides is affected. Move is a constant depending on which move
        # first I take the last elements and make them ready to be moved

        waiting_to_be_moved = []

        for tile in range(cubeSideSize):
            waiting_to_be_moved.append(self.cube[sides[-1] * moveableTilesPerSide + (move + tile) % moveableTilesPerSide])

        # now I start moving the bricks

        for i in range(sidesAffectedByEachMove):
            for tile in range(cubeSideSize):
                newTile, oldTile = waiting_to_be_moved.pop(0), self.cube[
                    sides[i] * moveableTilesPerSide + (move + tile) % moveableTilesPerSide]
                waiting_to_be_moved.append(oldTile)

                self.cube[sides[i] * moveableTilesPerSide + (move + tile) % moveableTilesPerSide] = newTile

    def swapInnerPositions(self, side, clockwise):
        delta = deltaInner if clockwise else moveableTilesPerSide
        # the last one
        # inner sidan som snurrar, funkar, ifråga sätt inte för mycket, ja koden e  ful
        if clockwise:
            twoStepsBehind, oneStepBehind = self.cube[(side + 1) * moveableTilesPerSide - delta], self.cube[
                (side + 1) * moveableTilesPerSide - (delta - 1)]

            for brick in range(moveableTilesPerSide):
                _ = self.cube[side * moveableTilesPerSide + brick]

                self.cube[side * moveableTilesPerSide + brick] = twoStepsBehind

                twoStepsBehind = oneStepBehind
                oneStepBehind = _
        else:
            twoStepsBehind, oneStepBehind = self.cube[(side + 1) * moveableTilesPerSide - (delta - 1)], self.cube[
                (side + 1) * moveableTilesPerSide - delta]

            for brick in range(moveableTilesPerSide - 1, -1, -1):
                _ = self.cube[side * moveableTilesPerSide + brick]

                self.cube[side * moveableTilesPerSide + brick] = twoStepsBehind

                twoStepsBehind = oneStepBehind
                oneStepBehind = _

    def visualise(self):
        # lager 1
        i = 5
        print('-----------------------------------------')
        print("-- -- -- |", self.cube[i * moveableTilesPerSide + 0], self.cube[i * moveableTilesPerSide + 1],
                self.cube[i * moveableTilesPerSide + 2], "| -- -- -- | -- -- --")
        print("-- -- -- |", self.cube[i * moveableTilesPerSide + 7], self.cube[i * moveableTilesPerSide + 8],
                self.cube[i * moveableTilesPerSide + 3], "| -- -- -- | -- -- --")
        print("-- -- -- |", self.cube[i * moveableTilesPerSide + 6], self.cube[i * moveableTilesPerSide + 5],
                self.cube[i * moveableTilesPerSide + 4], "| -- -- -- | -- -- --")
        print('-----------------------------------------')
        # lager 2
        string = ""
        for i in range(1, 5):
            for j in range(3):
                string += str(self.cube[i * moveableTilesPerSide + j]) + " "
            if i != 4:
                string += "| "
        print(string)
        string = ""
        for i in range(1, 5):
            for j in [7, "middle", 3]:
                if j == "middle":
                    string += str(self.cube[48 + i]) + " "
                    continue
                string += str(self.cube[i * moveableTilesPerSide + j]) + " "
            if i != 4:
                string += "| "
        print(string)
        string = ""
        for i in range(1, 5):
            for j in reversed(range(4, 7)):
                string += str(self.cube[i * moveableTilesPerSide + j]) + " "
            if i != 4:
                string += "| "
        print(string)
        # lager 3
        i = 0
        print('-----------------------------------------')
        print("-- -- -- |", self.cube[i * moveableTilesPerSide + 0], self.cube[i * moveableTilesPerSide + 1],
                self.cube[i * moveableTilesPerSide + 2], "| -- -- -- | -- -- --")
        print("-- -- -- |", self.cube[i * moveableTilesPerSide + 7], self.cube[i * moveableTilesPerSide + 8],
                self.cube[i * moveableTilesPerSide + 3], "| -- -- -- | -- -- --")
        print("-- -- -- |", self.cube[i * moveableTilesPerSide + 6], self.cube[i * moveableTilesPerSide + 5],
                self.cube[i * moveableTilesPerSide + 4], "| -- -- -- | -- -- --")
        print('-----------------------------------------')

    def drawWithTkinter(self):
        for i in range(6):
            self.colours[self.cube[i * moveableTilesPerSide + 0]].grid(row=i * 3, column=0)
            self.colours[self.cube[i * moveableTilesPerSide + 1]].grid(row=i * 3, column=1)
            self.colours[self.cube[i * moveableTilesPerSide + 2]].grid(row=i * 3, column=2)
            # _____________________
            self.colours[self.cube[i * moveableTilesPerSide + 7]].grid(row=i * 3 + 1, column=0)
            coloursMiddleLabel[self.colourMiddle[i]].grid(row=i * 3 + 1, column=1)
            self.colours[self.cube[i * moveableTilesPerSide + 3]].grid(row=i * 3 + 1, column=2)
            # _________________________
            self.colours[self.cube[i * moveableTilesPerSide + 6]].grid(row=i * 3 + 2, column=0)
            self.colours[self.cube[i * moveableTilesPerSide + 5]].grid(row=i * 3 + 2, column=1)
            self.colours[self.cube[i * moveableTilesPerSide + 4]].grid(row=i * 3 + 2, column=2)


class Cube(makeACube):

    def clockwiseHorizontal(self):
        waiting = []
        for _ in range(moveableTilesPerSide):
            waiting.append(self.cube.pop(moveableTilesPerSide))

        self.colourMiddle.insert(4, self.colourMiddle.pop(1))
        for el in reversed(waiting):
            self.cube.insert(4 * moveableTilesPerSide, el)

    def counterclockwiseHorizontal(self):
        for i in range(3):
            self.clockwiseHorizontal()

    def R(self):
        # skriv in sides counter clockwise.
        # sides = vilka sidorm skriv in det i tvärtom ordning
        # move = vilket index bland rutorna på sidan
        # provad
        sides, move = [0, 2, 5, 4], 2
        side, clockwise = 3, True
        self.swapOuterPositions(sides, move)
        self.swapInnerPositions(side, clockwise)

    def Ri(self):
        # provad
        sides, move = [4, 5, 2, 0], 2
        side, clockwise = 3, False
        self.swapOuterPositions(sides, move)
        self.swapInnerPositions(side, clockwise)

    def L(self):
        # provad
        sides, move = [4, 5, 2, 0], 6
        side, clockwise = 1, True
        self.swapOuterPositions(sides, move)
        self.swapInnerPositions(side, clockwise)

    def Li(self):
        # provad
        sides, move = [0, 2, 5, 4], 6
        side, clockwise = 1, False
        self.swapOuterPositions(sides, move)
        self.swapInnerPositions(side, clockwise)

    def U(self):
        # provad
        sides, move = [2, 1, 4, 3], 0
        side, clockwise = 5, True
        self.swapOuterPositions(sides, move)
        self.swapInnerPositions(side, clockwise)

    def Ui(self):
        # provad
        sides, move = [3, 4, 1, 2], 0
        side, clockwise = 5, False
        self.swapOuterPositions(sides, move)
        self.swapInnerPositions(side, clockwise)

    def D(self):
        # provad
        sides, move = [3, 4, 1, 2], 4
        side, clockwise = 0, True
        self.swapOuterPositions(sides, move)
        self.swapInnerPositions(side, clockwise)

    def Di(self):
        # provad
        sides, move = [2, 1, 4, 3], 4
        side, clockwise = 0, False
        self.swapOuterPositions(sides, move)
        self.swapInnerPositions(side, clockwise)

    def F(self):
        # provad
        sides, start = [0, 1, 5, 3], [6, 7, 0]
        side, clockwise = 2, True
        self.specialCaseswapOuterPositions(sides, start)
        self.swapInnerPositions(side, clockwise)

    def Fi(self):
        # provad, inte fin, lite bruteforcig, men funkar. GÖr basically F 3 gånger
        sides, start = [0, 1, 5, 3], [6, 7, 0]
        side, clockwise = 2, False
        for _ in range(3):
            self.specialCaseswapOuterPositions(sides, start)
        self.swapInnerPositions(side, clockwise)

    def B(self):
        # provad
        sides, start = [5, 3, 0, 1], [6, 7, 0]
        side, clockwise = 4, True
        for _ in range(3):
            self.specialCaseswapOuterPositions(sides, start)
        self.swapInnerPositions(side, clockwise)

    def Bi(self):
        # provad
        sides, start = [5, 3, 0, 1], [6, 7, 0]
        side, clockwise = 4, False
        self.specialCaseswapOuterPositions(sides, start)
        self.swapInnerPositions(side, clockwise)


cube = Cube()

cube.R()

cube.L()

cube.U()

cube.drawWithTkinter()

window.mainloop()














'''
positionsOfCube = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]

representationOfCube = [['W0', 0], ['W1', 1], ['W2', 2], ['W3', 3], ['W4', 4], ['W5', 5], ['W6', 6], ['W7', 7],
                        ['B0', 8], ['B1', 9], ['B2', 10], ['B3', 11], ['B4', 12], ['B5', 13], ['B6', 14], ['B7', 15],
                        ['R0', 16], ['R1', 17], ['R2', 18], ['R3', 19], ['R4', 20], ['R5', 21], ['R6', 22], ['R7', 23],
                        ['G0', 24], ['G1', 25], ['G2', 26], ['G3', 27], ['G4', 28], ['G5', 29], ['G6', 30], ['G7', 31],
                        ['O0', 32], ['O1', 33], ['O2', 34], ['O3', 35], ['O4', 36], ['O5', 37], ['O6', 38], ['O7', 39],
                        ['Y0', 40], ['Y1', 41], ['Y2', 42], ['Y3', 43], ['Y4', 44], ['Y5', 45], ['Y6', 46], ['Y7', 47]]
'''

#cube = Moves()
cube = Cube()
cube.R()


cube.visualise()

'''

    def visualise(self):
        for i in range(6):
            print('______________________________________________________________')
            for j in range(3):
                local = []
                for k in range(3):
                    if j==1 and k==1:
                        local.append('middle')
                    local.append(self.cube[i * moveableBricksPerSide + (j * 3 + k) % 8])
                    if len(local)==3:
                        print(local)

'''

#experiment med färger (misslyckat)
'''
print("colour test")
print("\u001b[47m white")
print("\u001b[44m blue")
print("\u001b[41m red")
print("\u001b[42m green")
print("\u001b[45m orange")
print("\u001b[43m yellow")
'''