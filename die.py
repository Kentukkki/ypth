import tkinter as tk
from tkinter import *

def sum_number(num1,num2):
    sumary = int(num1) + int(num2)
    result_text = "Сумма", num1 ,"и", num2, "Равна" , sumary
    result_lb = Label(frame,text=result_text)# создаем подпись к второму textbox
    result_lb.grid(row=4, column=1 , columnspan=3) #указываем расположение элемента

def sum_number():
    clear_frame()
    number_one_lb = Label(frame,text="Число 1")# создаем подпись к первому textbox
    number_one_lb.grid(row=1, column=1) #указываем расположение элемента
    number_one_tb = Entry(frame) # создаем первый textbox
    number_one_tb.grid(row=1, column=2) # аналогично размещаем
    number_two_lb = Label(frame,text="Число 2")# создаем подпись к второму textbox
    number_two_lb.grid(row=2, column=1) #указываем расположение элемента
    number_two_tb = Entry(frame) # создаем второй textbox
    number_two_tb.grid(row=2, column=2) # аналогично размещаем
    btn = Button(
       frame,
       text='Посчитать', #Надпись на кнопке.
       command= lambda: sum_number(number_one_tb.get(),number_two_tb.get())
    )
    btn.grid(row=3, column=1, columnspan=3)
    
def clear_frame():
    for widgets in frame.winfo_children():
        widgets.destroy()
        
window = Tk() #Создаём окно приложения.
window.title("Построение параболы") #Добавляем название приложения.
window.geometry('600x500+10+10')#Указываем размеры окна

mainmenu = Menu(window) 
window.config(menu=mainmenu)

grafmenu = Menu(mainmenu, tearoff=0)
grafmenu.add_command(label="Сложение",command=sum_number)
grafmenu.add_command(label="Вычитание")

mainmenu.add_cascade(label="Математические опрерации",
                     menu=grafmenu)

frame = Frame(
   window, #Обязательный параметр, который указывает окно для размещения Frame.
   padx = 10, #Задаём отступ по горизонтали.
   pady = 10 #Задаём отступ по вертикали.
)

frame.pack(expand=True)

window.mainloop()