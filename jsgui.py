import tkinter as tk

root = tk.Tk()

root.title("الاله الذكيه لحساب المصفوفه الشقيه")
root.geometry("600x500")

tk.Label(root, text="Enter Augmented Matrix (3x4)", font=("Arial", 14)).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

entries = []

labels = ["x1", "x2", "x3", "b"]
for j in range(4):
    tk.Label(frame, text=labels[j]).grid(row=0, column=j)

for i in range(3):
    row_entries = []
    for j in range(4):
        e = tk.Entry(frame, width=5)
        e.grid(row=i+1, column=j, padx=5, pady=5)
        row_entries.append(e)
    entries.append(row_entries)

tk.Label(root, text="Choose Method", font=("Arial", 12)).pack(pady=10)

tk.Radiobutton(root, text="Gauss Elimination").pack()
tk.Radiobutton(root, text="Gauss Jordan Elimination").pack()
tk.Radiobutton(root, text="LU Decomposition").pack()
tk.Radiobutton(root, text="Cramer's Rule").pack()

tk.Button(root, text="Solve").pack(pady=15)
tk.Label(root, text="Results", font=("Arial", 12)).pack()

x1_var = tk.StringVar()
x2_var = tk.StringVar()
x3_var = tk.StringVar()

tk.Label(root, text="X1 =").pack()
tk.Label(root, textvariable=x1_var).pack()

tk.Label(root, text="X2 =").pack()
tk.Label(root, textvariable=x2_var).pack()

tk.Label(root, text="X3 =").pack()
tk.Label(root, textvariable=x3_var).pack()

root.mainloop()