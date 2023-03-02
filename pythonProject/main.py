import tkinter as tk

def calculate_flow():
    n = float(n_entry.get())
    S = float(s_entry.get())
    R = float(r_entry.get())
    I = float(i_entry.get())

    Q = (1.49/n) * (R ** (2/3)) * S ** 0.5 * I ** (5/3)
    flow_result_label.config(text=f"Przepływ wody: {Q:.2f} m^3/s")

root = tk.Tk()
root.title("Obliczanie przepływu wody")

n_label = tk.Label(root, text="Współczynnik Manninga (n):")
s_label = tk.Label(root, text="Spad (S):")
r_label = tk.Label(root, text="Promień krzywizny (R):")
i_label = tk.Label(root, text="Nachylenie (I):")

n_entry = tk.Entry(root)
s_entry = tk.Entry(root)
r_entry = tk.Entry(root)
i_entry = tk.Entry(root)

calculate_button = tk.Button(root, text="Oblicz", command=calculate_flow)
flow_result_label = tk.Label(root, text="")

n_label.grid(row=0, column=0, sticky="W")
s_label.grid(row=1, column=0, sticky="W")
r_label.grid(row=2, column=0, sticky="W")
i_label.grid(row=3, column=0, sticky="W")

n_entry.grid(row=0, column=1)
s_entry.grid(row=1, column=1)
r_entry.grid(row=2, column=1)
i_entry.grid(row=3, column=1)

calculate_button.grid(row=4, column=0, columnspan=2, pady=10)
flow_result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
