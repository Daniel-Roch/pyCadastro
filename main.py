from config import root
from config import tk
from tkinter import ttk
from config import tkFrame

""" from src.menu_register import open_wind_register """

def click():
    print("Click!")

""" def win_register():
    open_wind_register() """




# Columns Table
nameColumns = ('id', 'name', 'cpf', 'nasc', 'age')
tableTitle = ttk.Treeview(tkFrame, columns=nameColumns, show='headings')

tableTitle.heading('id', text='id')
tableTitle.heading('name', text='Nome')
tableTitle.heading('cpf', text='CPF')
tableTitle.heading('nasc', text='Data Nascimento')
tableTitle.heading('age', text='Idade')

tableTitle.insert('', tk.END, values=['1', 'Fulano', '1111111111', '01/01/1990', 30])

# ScrollBar
screenScroll = tk.Scrollbar(tkFrame, orient=tk.VERTICAL, command=tableTitle.yview)

tableTitle.configure(yscroll=screenScroll.set)
screenScroll.grid(row=0, column=1, sticky='ns')

""" text = tk.Label(root, text="Nome:")
text.grid(row=0, column=0, padx=10, pady=10)

label = tk.Entry(root)
label.grid(row=0, column=1) """

""" btn = tk.Button(root, text="Cadastro", command=win_register)
btn.grid(row=1, column=0, columnspan=2) """

root.mainloop()