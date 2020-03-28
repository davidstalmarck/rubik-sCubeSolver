import random
from tkinter import Label, Tk, mainloop

window = Tk()

colourmap = {
    "W" : "Grey",
    "B" : "Blue",
    "R" : "Red",
    "G" : "Green",
    "O" : "Orange",
    "Y" : "Yellow"
}

def getcolour(tilestring):
    colour = tilestring[0]
    return Label(window, width="2", height="1", bg=colourmap[colour])

initialcube = [ 'W0', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'R0','R1',
                'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'G0', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'O0', 'O1','O2', 'O3',
                'O4', 'O5', 'O6', 'O7', 'Y0', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'W8', 'B8', 'R8', 'G8', 'O8', 'Y8']


# Slices has 3 keys - X, Y and Z - indicating along which axes they lie. Here, we assume one is looking at the cube from the front(side 2)
# in that case, X-slices rotate around the axis through faces 1 and 3, Y-slices rotate around the axis through faces 0 and 5 and Z-slices,
# finally, rotate aroung the axis through faces 2 and 4. In each slice, only the order of the tiles matters, not the actual first item.
# The convention used is to begin with the numerically lowest face, and then continuing clockwise around the axis

# Next, each key contains a list of the tiles involved in the 3 possible slices around the axis associated with said key. These are indexed
# from left to right, from top to bottom and from front to back.

# For example the slice involved in a simple R or Ri move is stored in slices["X"][2].

slices = {
    "X" : [
         [6, 7, 0, 22, 23, 16, 46, 47, 40, 34, 35, 36],
         [5, 48, 1, 21, 50, 17, 45, 51, 41, 33, 52, 37],
         [4, 3, 2, 20, 19, 18, 44, 43, 42, 32, 39, 38]
         ],
    "Y" : [
         [10, 9, 8, 34, 33, 32, 26, 25, 24, 18, 17, 16],
         [11, 49, 15, 35, 52, 39, 27, 51, 31, 19, 50, 23],
         [12, 13, 14, 36, 37, 38, 28, 29, 30, 20, 21, 22]
         ],
    "Z" : [
         [2, 1, 0, 12, 11, 10, 46, 45, 44, 24, 31, 30],
         [3, 48, 7, 13, 49, 15, 47, 53, 43, 25, 51, 29],
         [4, 5, 6, 14, 15, 8, 40, 41, 42, 26, 27, 28]
         ]
}

# I want to be able to scale to any sizes
cubeSideSize = 3
sidesAffectedByEachMove = 4
totalPositions = 54 # 0 till och med 53
moveableTilesPerSide = 9
deltaInner = 2

def shift3(oldindexlist):
    newindexlist = oldindexlist[3:].copy()
    for k in range(3):
        newindexlist.append(oldindexlist[k])
    return newindexlist

def reverseshift3(oldindexlist):
    newindexlist = oldindexlist[:9].copy()
    for k in range(1, 4):
        newindexlist.insert(0, oldindexlist[-k])
    return newindexlist


class Cube():
    def __init__(self):
        self.cube = initialcube

    def shuffle(self):
        random.shuffle(self.cube)

    def tkinterdraw(self):
        # lager 1
        r = 0
        face = 5
        for col in range(0, 3):
            Label(window, width="2", height="1", fg="White", bg="White").grid(row=r * 3, column=col)
        getcolour(self.cube[face * (moveableTilesPerSide-1) + 0]).grid(row=r * 3, column=3)
        getcolour(self.cube[face * (moveableTilesPerSide-1) + 1]).grid(row=r * 3, column=4)
        getcolour(self.cube[face * (moveableTilesPerSide-1) + 2]).grid(row=r * 3, column=5)
        for col in range(6, 12):
            Label(window, width="2", height="1", fg="White", bg="White").grid(row=r * 3, column=col)
        # _____________________
        for col in range(0, 3):
            Label(window, width="2", height="1", fg="White", bg="White").grid(row=r * 3 + 1, column=col)
        getcolour(self.cube[face * (moveableTilesPerSide-1) + 7]).grid(row=r * 3 + 1, column=3)
        getcolour(self.cube[48+face]).grid(row=r * 3 + 1, column=4)
        getcolour(self.cube[face * (moveableTilesPerSide-1) + 3]).grid(row=r * 3 + 1, column=5)
        for col in range(6, 12):
            Label(window, width="2", height="1", fg="White", bg="White").grid(row=r * 3 + 1, column=col)
        # _________________________
        for col in range(0, 3):
            Label(window, width="2", height="1", fg="White", bg="White").grid(row=r * 3 + 2, column=col)
        getcolour(self.cube[face * (moveableTilesPerSide-1) + 6]).grid(row=r * 3 + 2, column=3)
        getcolour(self.cube[face * (moveableTilesPerSide-1) + 5]).grid(row=r * 3 + 2, column=4)
        getcolour(self.cube[face * (moveableTilesPerSide-1) + 4]).grid(row=r * 3 + 2, column=5)
        for col in range(6, 12):
            Label(window, width="2", height="1", fg="White", bg="White").grid(row=r * 3 + 2, column=col)

        # lager 2
        r = 1
        for face in range(1, 5):
            getcolour(self.cube[face * (moveableTilesPerSide-1) + 0]).grid(row=r * 3, column=(face-1) * 3 + 0)
            getcolour(self.cube[face * (moveableTilesPerSide-1) + 1]).grid(row=r * 3, column=(face-1) * 3 + 1)
            getcolour(self.cube[face * (moveableTilesPerSide-1) + 2]).grid(row=r * 3, column=(face-1) * 3 + 2)
            getcolour(self.cube[face * (moveableTilesPerSide-1) + 7]).grid(row=r * 3 + 1, column=(face-1) * 3 + 0)
            getcolour(self.cube[48+face]).grid(row=r * 3 + 1, column=(face-1) * 3 + 1)
            getcolour(self.cube[face * (moveableTilesPerSide-1) + 3]).grid(row=r * 3 + 1, column=(face-1) * 3 + 2)
            getcolour(self.cube[face * (moveableTilesPerSide-1) + 6]).grid(row=r * 3 + 2, column=(face-1) * 3 + 0)
            getcolour(self.cube[face * (moveableTilesPerSide-1) + 5]).grid(row=r * 3 + 2, column=(face-1) * 3 + 1)
            getcolour(self.cube[face * (moveableTilesPerSide-1) + 4]).grid(row=r * 3 + 2, column=(face-1) * 3 + 2)

        # lager 3
        r = 2
        face = 0
        for col in range(0, 3):
            Label(window, width="2", height="1", fg="White", bg="White").grid(row=r * 3, column=col)
        getcolour(self.cube[face * (moveableTilesPerSide-1) + 0]).grid(row=r * 3, column=3)
        getcolour(self.cube[face * (moveableTilesPerSide-1) + 1]).grid(row=r * 3, column=4)
        getcolour(self.cube[face * (moveableTilesPerSide-1) + 2]).grid(row=r * 3, column=5)
        for col in range(6, 12):
            Label(window, width="2", height="1", fg="White", bg="White").grid(row=r * 3, column=col)
        # _____________________
        for col in range(0, 3):
            Label(window, width="2", height="1", fg="White", bg="White").grid(row=r * 3 + 1, column=col)
        getcolour(self.cube[face * (moveableTilesPerSide-1) + 7]).grid(row=r * 3 + 1, column=3)
        getcolour(self.cube[48+face]).grid(row=r * 3 + 1, column=4)
        getcolour(self.cube[face * (moveableTilesPerSide-1) + 3]).grid(row=r * 3 + 1, column=5)
        for col in range(6, 12):
            Label(window, width="2", height="1", fg="White", bg="White").grid(row=r * 3 + 1, column=col)
        # _________________________
        for col in range(0, 3):
            Label(window, width="2", height="1", fg="White", bg="White").grid(row=r * 3 + 2, column=col)
        getcolour(self.cube[face * (moveableTilesPerSide-1) + 6]).grid(row=r * 3 + 2, column=3)
        getcolour(self.cube[face * (moveableTilesPerSide-1) + 5]).grid(row=r * 3 + 2, column=4)
        getcolour(self.cube[face * (moveableTilesPerSide-1) + 4]).grid(row=r * 3 + 2, column=5)
        for col in range(6, 12):
            Label(window, width="2", height="1", fg="White", bg="White").grid(row=r * 3 + 2, column=col)

    def asciidraw(self):
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

    def rotatesideclockwise(self, side):
        oldtileindices = [side*8 + n for n in range(8)]
        oldtiles = [self.cube[ind] for ind in oldtileindices]
        newtileindices = oldtileindices[2:].copy()
        for k in range(2):
            newtileindices.append(oldtileindices[k])
        for newtileindex, oldtile in zip(newtileindices, oldtiles):
            self.cube[newtileindex] = oldtile
    
    def rotatesidecounterclockwise(self, side):
        oldtileindices = [side*8 + n for n in range(8)]
        oldtiles = [self.cube[ind] for ind in oldtileindices]
        newtileindices = oldtileindices[:6].copy()
        for k in range(1, 3):
            newtileindices.insert(0, oldtileindices[-k])
        for newtileindex, oldtile in zip(newtileindices, oldtiles):
            self.cube[newtileindex] = oldtile
    
    def standardpermute(self, oldtileindices):
        oldtiles = [self.cube[ind] for ind in oldtileindices]
        newtileindices = shift3(oldtileindices)
        for newtileindex, oldtile in zip(newtileindices, oldtiles):
            self.cube[newtileindex] = oldtile
    
    def reversepermute(self, oldtileindices):
        oldtiles = [self.cube[ind] for ind in oldtileindices]
        newtileindices = reverseshift3(oldtileindices)
        for newtileindex, oldtile in zip(newtileindices, oldtiles):
            self.cube[newtileindex] = oldtile

    def R(self):
        self.rotatesideclockwise(3)
        self.standardpermute(slices["X"][2])
    
    def Ri(self):
        self.rotatesidecounterclockwise(3)
        self.reversepermute(slices["X"][2])
    
    def U(self):
        self.rotatesideclockwise(5)
        self.standardpermute(slices["Y"][0])

    def Ui(self):
        self.rotatesidecounterclockwise(5)
        self.reversepermute(slices["Y"][0])

cube = Cube()

for _ in range(6):
    cube.R()
    cube.U()
    cube.Ri()
    cube.Ui()
    
cube.tkinterdraw()

window.mainloop()
