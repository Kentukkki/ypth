import tkinter as tk
import webbrowser

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}
def link():
    webbrowser.open_new(r"https://www.avito.ru/chelyabinsk?q=гараж")

window = tk.Tk()
question = tk.Label(
	text='Продам гараж',
	fg = "white",
	bg = "black",
	width = 20,
	height = 5,
	font = ("Arial", 25),
	)
button = tk.Button(
    text="Купить!",
    width=20,
    height=2,
    bg="black",
    fg="white",
    font = ("Arial", 25),
    command=link,
)
question.pack()
button.pack()

window.mainloop()
