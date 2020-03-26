from tkinter import *

window = Tk()

lst = {'hej': Label(bg="red"), 'h': Label(bg="red")}

lst['hej'].grid(row=0, column=0)
lst['h'].grid(row=0, column=1)

#colours = {0: Button(window, text = '',width="5", height="5", bg='blue'), 1: Label(window, width="5", height="5",bg = "blue"), 2: Label(window, width="5", height="5",bg = "red"), 3: Label(window, width="5", height="5",bg = "green"), 4: Label(window, width="5", height="5",bg = "Orange"), 5: Label(window, width="5", height="5",bg = "Yellow"), 6: Label( text='hello', width="5", height="5", bg="white")}

#for i in range(7):
    #colours[i%6].grid(row=0, column = i)


window.mainloop()