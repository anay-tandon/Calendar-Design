from tkinter import *
import calendar

def show_calendar():
    new = Tk()
    new.title("Calendar")
    new.geometry("550x600")
    new.configure(bg = "lightblue")

    #get method returns current text as string
    fetch_year = int(Entry1.get())

    # calendar method returns the calendar of the given year in string format
    cal_content = calendar.calendar(fetch_year)

    # label is used to display the calendar content in the new window
    cal_year = Label(new, text = cal_content, font = "Consolas 10 bold")

    # grid method is used for placing the widgets at respective positions in the table like structure
    cal_year.grid(row = 5, column = 1, padx = 20, pady = 10)

    # start the GUI event loop
    new.mainloop()

screen = Tk()
calendar1 = Label(screen, text = "Calendar", font = ("Arial", 30))

Enter = Label(screen, text = "Enter Year ", font = ("Arial", 10), bg = "green")
Entry1 = Entry(screen, width = 20, font = ("Arial", 10))

show = Button(screen, text = "Show Calendar", font = ("Arial", 10), bg = "red", command = show_calendar)
exit = Button(screen, text = "Exit", font = ("Arial", 10), bg = "red", command = screen.quit)

calendar1.grid(row = 1, column = 1)
Enter.grid(row = 2, column = 1)
Entry1.grid(row = 3, column = 1)

show.grid(row = 4, column = 1)
exit.grid(row = 5, column = 1)

screen.mainloop()
