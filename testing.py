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

dictColours = {'W0': Label(window, width="5", height="5", bg="white"),
               'W1': Label(window, width="5", height="5", bg="white"),
               'W2': Label(window, width="5", height="5", bg="white"),
               'W3': Label(window, width="5", height="5", bg="white"),
               'W4': Label(window, width="5", height="5", bg="white"),
               'W5': Label(window, width="5", height="5", bg="white"),
               'W6': Label(window, width="5", height="5", bg="white"),
               'W7': Label(window, width="5", height="5", bg="white"),
               'B0': Label(window, width="5", height="5", bg="blue"),
               'B1': Label(window, width="5", height="5", bg="blue"),
               'B2': Label(window, width="5", height="5", bg="blue"),
               'B3': Label(window, width="5", height="5", bg="blue"),
               'B4': Label(window, width="5", height="5", bg="blue"),
               'B5': Label(window, width="5", height="5", bg="blue"),
               'B6': Label(window, width="5", height="5", bg="blue"),
               'B7': Label(window, width="5", height="5", bg="blue"),
               'R0': Label(window, width="5", height="5", bg="red"),
               'R1': Label(window, width="5", height="5", bg="red"),
               'R2': Label(window, width="5", height="5", bg="red"),
               'R3': Label(window, width="5", height="5", bg="red"),
               'R4': Label(window, width="5", height="5", bg="red"),
               'R5': Label(window, width="5", height="5", bg="red"),
               'R6': Label(window, width="5", height="5", bg="red"),
               'R7': Label(window, width="5", height="5", bg="red"),
               'G0': Label(window, width="5", height="5", bg="green"),
               'G1': Label(window, width="5", height="5", bg="green"),
               'G2': Label(window, width="5", height="5", bg="green"),
               'G3': Label(window, width="5", height="5", bg="green"),
               'G4': Label(window, width="5", height="5", bg="green"),
               'G5': Label(window, width="5", height="5", bg="green"),
               'G6': Label(window, width="5", height="5", bg="green"),
               'G7': Label(window, width="5", height="5", bg="green"),
               'O0': Label(window, width="5", height="5", bg="Orange"),
               'O1': Label(window, width="5", height="5", bg="Orange"),
               'O2': Label(window, width="5", height="5", bg="Orange"),
               'O3': Label(window, width="5", height="5", bg="Orange"),
               'O4': Label(window, width="5", height="5", bg="Orange"),
               'O5': Label(window, width="5", height="5", bg="Orange"),
               'O6': Label(window, width="5", height="5", bg="Orange"),
               'O7': Label(window, width="5", height="5", bg="Orange"),
               'Y0': Label(window, width="5", height="5", bg="Yellow"),
               'Y1': Label(window, width="5", height="5", bg="Yellow"),
               'Y2': Label(window, width="5", height="5", bg="Yellow"),
               'Y3': Label(window, width="5", height="5", bg="Yellow"),
               'Y4': Label(window, width="5", height="5", bg="Yellow"),
               'Y5': Label(window, width="5", height="5", bg="Yellow"),
               'Y6': Label(window, width="5", height="5", bg="Yellow"),
               'Y7': Label(window, width="5", height="5", bg="Yellow")}
