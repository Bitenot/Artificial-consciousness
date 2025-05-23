import tkinter as tk
from tkinter import Listbox, Button, END, EXTENDED
import matplotlib.pyplot as plt

# Дані
month = ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень']
sales = [11.0, 17.0, 18.0, 32.5, 22.5, 15.5]

# Головне вікно
root = tk.Tk()
root.title("Обсяг продажів")

# Віджет Listbox
box1 = Listbox(root, selectmode=EXTENDED)
box1.grid(row=0, column=0, rowspan=6)
for p in sales:
    box1.insert(END, p)

# Функція для стовпчикової діаграми
def btn1_cl():
    plt.title('Обсяг продажів')
    plt.xlabel('Місяці', color='gray')
    plt.ylabel('тис. грн', color='gray')
    plt.bar(month, sales, color='skyblue')
    plt.grid(axis='y', linestyle='--', linewidth=0.5)
    plt.show()

# Функція для графіка
def btn2_cl():
    plt.title('Обсяг продажів (лінійний графік)')
    plt.plot(month, sales, marker='o', linestyle='-', color='green')
    plt.xlabel('Місяці')
    plt.ylabel('тис. грн')
    plt.grid(True)
    plt.show()

# Функція для кругової діаграми
def btn3_cl():
    plt.title('Кругова діаграма обсягів продажів')
    plt.pie(sales, labels=month, autopct="%.1f%%", startangle=90)
    plt.axis('equal')
    plt.show()

# Кнопка для стовпчикової діаграми
btn1 = Button(root, text="Стовпчикова діаграма", command=btn1_cl)
btn1.grid(row=2, column=1)

# Кнопка для графіка
btn2 = Button(root, text="Графік", command=btn2_cl)
btn2.grid(row=4, column=1)

# Кнопка для кругової діаграми
btn3 = Button(root, text="Кругова діаграма", command=btn3_cl)
btn3.grid(row=6, column=1)

# Запуск головного циклу
root.mainloop()
