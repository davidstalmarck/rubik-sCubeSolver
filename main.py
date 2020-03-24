import random

coloursOfCube = ['W0', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'O0', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7']

positionsOfCube = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]

representationOfCube = [['W0', 0], ['W1', 1], ['W2', 2], ['W3', 3], ['W4', 4], ['W5', 5], ['W6', 6], ['W7', 7], ['B0', 8], ['B1', 9], ['B2', 10], ['B3', 11], ['B4', 12], ['B5', 13], ['B6', 14], ['B7', 15], ['R0', 16], ['R1', 17], ['R2', 18], ['R3', 19], ['R4', 20], ['R5', 21], ['R6', 22], ['R7', 23], ['G0', 24], ['G1', 25], ['G2', 26], ['G3', 27], ['G4', 28], ['G5', 29], ['G6', 30], ['G7', 31], ['O0', 32], ['O1', 33], ['O2', 34], ['O3', 35], ['O4', 36], ['O5', 37], ['O6', 38], ['O7', 39], ['Y0', 40], ['Y1', 41], ['Y2', 42], ['Y3', 43], ['Y4', 44], ['Y5', 45], ['Y6', 46], ['Y7', 47]]


'''
lst = []
for i in range(48):
    lst.append([coloursOfCube[i], positionsOfCube[i]])
print(lst)

#drawing the cube
lst = ['Y', 'R', 'V', 'B', 'G','O']

lst1 = []
for j, el in enumerate(lst):
    for i in range(10):
        lst1.append(el+str(i))

print(lst1)
'''

# I want to be able to scale to any sizes
cubeSideSize = 3
sidesAffectedByEachMove = 4
totalPositions = 48
moveableBricksPerSide = 8
deltaInner = 2


class Cube():
    def __init__(self):
        self.colours = coloursOfCube
        self.positions = positionsOfCube
        self.cube = coloursOfCube

    def shuffle(self):
        random.shuffle(self.cube)

    def swapOuterPositions(self, sides, move):
        # sides is a list, and says which sides is affeckted. Move is a constant depending on which move
        # first I take the last elements and make them ready to be moved

        waiting_to_be_moved = []

        for brick in range(cubeSideSize):
            waiting_to_be_moved.append(self.cube[sides[-1] * moveableBricksPerSide + move + brick])

        # now I start moving the bricks

        for i in range(sidesAffectedByEachMove):
            for brick in range(cubeSideSize):
                newBrick, oldBrick = waiting_to_be_moved.pop(0), self.cube[
                    sides[i] * moveableBricksPerSide + move + brick]

                waiting_to_be_moved.append(oldBrick)

                self.cube[sides[i] * moveableBricksPerSide + move + brick] = newBrick

    def swapInnerPositions(self, side, clockwise):
        #delta = deltaInner if clockwise else -deltaInner
        # the last one
        # inner sidan som snurrar, funkar, ifråga sätt inte för mycket, ja koden e  ful
        twoStepsBehind = self.cube[(side + 1) * moveableBricksPerSide - 2]
        oneStepBehind = self.cube[(side + 1) * moveableBricksPerSide - 1]

        for brick in range(moveableBricksPerSide):
            _ = self.cube[side * moveableBricksPerSide + brick]
            self.cube[side * moveableBricksPerSide + brick] = twoStepsBehind
            twoStepsBehind = oneStepBehind
            oneStepBehind = _


    def visualise(self):
        for i in range(6):
            print('--------------------------------------------')
            print(self.cube[i * moveableBricksPerSide + 0], self.cube[i * moveableBricksPerSide + 1],
                  self.cube[i * moveableBricksPerSide + 2])
            print(self.cube[i * moveableBricksPerSide + 7], str(self.cube[i * moveableBricksPerSide])[2:3] + '-middle',
                  self.cube[i * moveableBricksPerSide + 3])
            print(self.cube[i * moveableBricksPerSide + 6], self.cube[i * moveableBricksPerSide + 5],
                  self.cube[i * moveableBricksPerSide + 4])


    def R(self):
        # skriv in counter clockwise
        sides, move = [0, 2, 5, 4], 2
        side, clockwise = 3, True
        self.swapOuterPositions(sides, move)
        self.swapInnerPositions(side, clockwise)

    def Ri(self):
        sides, move = [4, 5, 2, 0], 2
        side, clockwise = 3, False
        self.swapOuterPositions(sides, move)
        self.swapInnerPositions(side, clockwise)


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
