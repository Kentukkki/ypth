import tkinter as tk
from tkinter import *
 
win = tk.Tk()
win.title('Тестовая прога')
win.geometry('640x480')
win.resizable(width=True, height=True)

mainmenu = Menu(win) 
win.config(menu=mainmenu, bg='black',)

num1 = tk.IntVar()
num2 = tk.IntVar()

def sum_menu():
    clear_frame()
    text = tk.Label(frame, bg='black', fg='white',text='Введите числа(сложить)', font=('ARIAL',10),)
    button = tk.Button(frame, command = sum, bg='grey20', fg='white',text='Сложить', font=('ARIAL',15),)
    ng1 = tk.Entry(frame, bg='grey30', fg='white', textvariable=num1)
    ng2 = tk.Entry(frame, bg='grey30', fg='white', textvariable=num2)
    
    ng1.grid(row=1, column=1)
    ng2.grid(row=1, column=3)
    text.grid(row=1, column=2)
    button.grid(row=2, column=2)
    button.bind("<Enter>", func=lambda e: button.config(
        background='grey40',))
    button.bind("<Leave>", func=lambda e: button.config(
        background='grey20'))
    answer = tk.Label(frame,bg='black', fg='white', font=('ARIAL',15),) 
    answer.grid(row=3, column=2)

def sum():
    try:
        sum_menu.answer.destroy()
        n1 = num1.get()
        n2 = num2.get()
        summary = n1 + n2 
        sum_menu.answer.config(text = summary)
    except(AttributeError):
        n1 = num1.get()
        n2 = num2.get()
        summary = n1 + n2 
        sum_menu.answer.config(text = summary) 
    
    
def dif_menu():
    clear_frame()
    text = tk.Label(frame,bg='black', fg='white', text='Введите числа(вычесть)', font=('ARIAL',10),)
    button = tk.Button(frame, command = dif, bg='grey20', fg='white', text='Вычесть', font=('ARIAL',15),)
    ng1 = tk.Entry(frame, bg='grey30', fg='white', textvariable=num1)
    ng2 = tk.Entry(frame, bg='grey30', fg='white', textvariable=num2)
    
    ng1.grid(row=1, column=1)
    ng2.grid(row=1, column=3)
    text.grid(row=1, column=2)
    button.grid(row=2, column=2)
    button.bind("<Enter>", func=lambda e: button.config(
        background='grey40',))
    button.bind("<Leave>", func=lambda e: button.config(
        background='grey20'))

def dif():
    n1 = num1.get()
    n2 = num2.get()
    differ = n1 - n2
    answer = tk.Label(frame,bg='black', fg='white', font=('ARIAL',15),) 
    answer.grid(row=3, column=2)   
    answer["text"] = differ
    

def clear_frame():
    for widgets in frame.winfo_children():
        widgets.destroy()

grafmenu = Menu(mainmenu, tearoff=0)
grafmenu.add_command(label="Сложение", command=sum_menu,)
grafmenu.add_command(label="Вычитание", command=dif_menu)

mainmenu.add_cascade(label="Математические опрерации", menu=grafmenu,)

frame = Frame(
   win, #Обязательный параметр, который указывает окно для размещения Frame.
   padx = 10, #Задаём отступ по горизонтали.
   pady = 10, #Задаём отступ по вертикали.
   bg = 'black',
)

frame.pack(expand=True)
 
win.mainloop()
