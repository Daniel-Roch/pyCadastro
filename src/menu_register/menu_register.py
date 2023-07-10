from menu_register_config import root_register
from menu_register_config import tk

def confirm():
    print("Confirm!")

def cancel():
    print("Cancel")
    root_register.destroy()

def open_wind_register():
    # ID
    id = tk.Label(root_register, text="ID (opcional):")
    id.grid(row=0, column=0, padx=10, pady=10)

    label_id = tk.Entry(root_register)
    label_id.grid(row=0, column=1)

    # First name
    first_name = tk.Label(root_register, text="Primeiro Nome:")
    first_name.grid(row=1, column=0, padx=10, pady=10)

    label_fName = tk.Entry(root_register)
    label_fName.grid(row=1, column=1)

    # Last name
    last_name = tk.Label(root_register, text="Sobrenome:")
    last_name.grid(row=2, column=0, padx=10, pady=10)

    label_lName = tk.Entry(root_register)
    label_lName.grid(row=2, column=1)

    # CPF
    cpf = tk.Label(root_register, text="CPF:")
    cpf.grid(row=3, column=0, padx=10, pady=10)

    label_cpf = tk.Entry(root_register)
    label_cpf.grid(row=3, column=1)

    # Nasc
    date = tk.Label(root_register, text="Data Nascimento:")
    date.grid(row=4, column=0, padx=10, pady=10)

    label_date = tk.Entry(root_register)
    label_date.grid(row=4, column=1)

    root_register.mainloop()

