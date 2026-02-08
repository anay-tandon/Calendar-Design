from tkinter import *

screen = Tk()

Calendar = Label(screen, text = "Calendar", font = ("Arial", 30))
Calendar.pack(pady = 15)

Enter = Label(screen, text = "Enter Year ", font = ("Arial", 10), bg = "green")
Enter.pack(pady = 5)

Entry1 = Entry(screen, width = 20, font = ("Arial", 10))
Entry1.pack(pady = 5)

show = Button(screen, text = "Show Calendar", font = ("Arial", 10), bg = "red")
show.pack(pady = 5)

exit = Button(screen, text = "Exit", font = ("Arial", 10), bg = "red", command = screen.quit)
exit.pack(pady = 5)

screen.mainloop()