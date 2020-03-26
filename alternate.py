import random

row1 = ["x", "x", "x", 45, 46, 47, "x", "x", "x", "x", "x", "x"]
row2 = ["x", "x", "x", 52, 53, 48, "x", "x", "x", "x", "x", "x"]
row3 = ["x", "x", "x", 51, 50, 49, "x", "x", "x", "x", "x", "x"]
row4 = [9, 10, 11, 18, 19, 20, 27, 28, 29, 36, 37, 38]
row5 = [16, 17, 12, 25, 26, 21, 34, 35, 30, 43, 44, 39]
row6 = [15, 14, 13, 24, 23, 22, 33, 32, 31, 42, 41, 40]
row7 = ["x", "x", "x", 0, 1, 2, "x", "x", "x", "x", "x", "x"]
row8 = ["x", "x", "x", 7, 8, 3, "x", "x", "x", "x", "x", "x"]
row9 = ["x", "x", "x", 6, 5, 4, "x", "x", "x", "x", "x", "x"]

#kuben har positioner ungefär enligt bild som david skickade på discord

class Cube():
    def __init__(self):
        self.pos = []
        colours = ["W", "B", "R", "G", "O", "Y"]
        for k in range(6):
            for n in range(k, k+9):
                self.pos.append(colours[k])
    
    def shuffle(self):
        random.shuffle(self.pos)
    
    def R(self):
        order = [x for x in range(54)]
        order[20], order[21], order[22] = 2, 3, 4
        order[47], order[48], order[49] = 20, 21, 22
        order[36], order[43], order[42] = 49, 48, 47
        order[2], order[3], order[4] = 36, 43, 42
        order[27], order[28], order[29], order[30], order[31], order[32], order[33], order[34] = 33, 34, 27, 28, 29, 30, 31, 32
        self.pos = [self.pos[k] for k in order]

    def Ri(self):
        pass

    def L(self):
        pass

    def Li(self):
        pass

    def U(self):
        pass
    
    def Ui(self):
        pass

    def D(self):
        pass
    
    def Di(self):
        pass

    def F(self):
        pass
    
    def Fi(self):
        pass

    def B(self):
        pass

    def Bi(self):
        pass

    def X(self):
        pass

    def Xi(self):
        pass

    def Y(self):
        pass

    def Yi(self):
        pass
    
    def Z(self):
        pass

    def Zi(self):
        pass

    def tempshow(self):
        string = ""
        for el in row1:
            string += ("x" if el == "x" else str(self.pos[el]))
        print(string)
        string = ""
        for el in row2:
            string += ("x" if el == "x" else str(self.pos[el]))
        print(string)
        string = ""
        for el in row3:
            string += ("x" if el == "x" else str(self.pos[el]))
        print(string)
        string = ""
        for el in row4:
            string += ("x" if el == "x" else str(self.pos[el]))
        print(string)
        string = ""
        for el in row5:
            string += ("x" if el == "x" else str(self.pos[el]))
        print(string)
        string = ""
        for el in row6:
            string += ("x" if el == "x" else str(self.pos[el]))
        print(string)
        string = ""
        for el in row7:
            string += ("x" if el == "x" else str(self.pos[el]))
        print(string)
        string = ""
        for el in row8:
            string += ("x" if el == "x" else str(self.pos[el]))
        print(string)
        string = ""
        for el in row9:
            string += ("x" if el == "x" else str(self.pos[el]))
        print(string)
        # print("x x x" + str((self.pos[45:47+1])) + "x x x x x x")
        # print("x x x" + str((self.pos[52:53+1])) + str(self.pos[48]) + "x)"*6)
        # print("x x x" + str(self.pos[51]) + str(self.pos[50]) + str(self.pos[49]) + "x x x x x x")
        # print(str((self.pos[9:11+1]))+ str((self.pos[18:20+1])) +str(( self.pos[27:29+1])) + str((self.pos[36: 38+1])))
        # print(str((self.pos[16:17+1])) + str(self.pos[12]) + str((self.pos[25:26+1])) +str(self.pos[21]) + str((self.pos[34:35+1])) + str(self.pos[30]) + str((self.pos[43:44+1])) + str(self.pos[39]))
        # print(str(self.pos[15]) + str(self.pos[14]) + str(self.pos[13]) + str(self.pos[24]) + str(self.pos[23]) + str(self.pos[22]) + str(self.pos[33]) + str(self.pos[32]) + str(self.pos[31]) + str(self.pos[42]) + str(self.pos[41]) + str(self.pos[40]))
        # print("x x x" + str((self.pos[0:2+1])) + "x x x x x x")
        # print("x x x" + str((self.pos[7:8 + 1])) + str(self.pos[9] )+ "x x x x x x")
        # print("x x x" + str(self.pos[6]) + str(self.pos[5]) + str(self.pos[4]) + "x x x x x x")
        # #print("x x x" + str(self.pos[6]) + str(self.pos[5]) + str(self.pos[4]) + "x x x x x x")
print("---------")
c = Cube()
c.tempshow()
print("---------")
c.R()
c.tempshow()
print("---------")
c.R()
c.tempshow()