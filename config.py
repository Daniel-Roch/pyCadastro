import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Cadastro Cliente")

root.geometry("500x200")

tkFrame = ttk.Frame(root)
tkFrame.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

root.grid()