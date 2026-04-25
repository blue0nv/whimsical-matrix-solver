def run():
    import tkinter as tk
    import functions

    root = tk.Tk()

    root.title("الاله الذكيه لحساب المصفوفه الشقيه")
    root.geometry("600x500")

    def hide_results():
        results_frame.pack_forget()

    def show_results():
        results_frame.pack()

    def calculate():
        m = method.get()
        matrix = functions.matrix_generator(entries)
        match m:
            case "gauss":
                result = functions.gauss(matrix)

            case "cramer":
                result = functions.cramer(matrix)

            case "gje":
                result = functions.gauss_jordan(matrix)

            case "lu":
                result = functions.lu(matrix)

        if result == None:
            x1_var.set("")
            x2_var.set("")
            x3_var.set("")
            results.config(text="No Solution")
            show_results()
            return

        results.config(text="Results")
        x1_var.set(f"X1 = {result[0]}")
        x2_var.set(f"X2 = {result[1]}")
        x3_var.set(f"X3 = {result[2]}")
        show_results()

    def on_edit(event):
        hide_results()

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

    method = tk.StringVar()

    radio1 = tk.Radiobutton(root, text="Gauss Elimination", variable=method, value="gauss")
    radio2 = tk.Radiobutton(root, text="Gauss Jordan Elimination", variable=method, value="gje")
    radio3 = tk.Radiobutton(root, text="LU Decomposition", variable=method, value="lu")
    radio4 = tk.Radiobutton(root, text="Cramer's Rule", variable=method, value="cramer")

    radio1.pack()
    radio2.pack()
    radio3.pack()
    radio4.pack()

    tk.Button(root, text="Solve", command=calculate).pack(pady=15)

    x1_var = tk.StringVar()
    x2_var = tk.StringVar()
    x3_var = tk.StringVar()

    results_frame = tk.Frame(root)

    results = tk.Label(results_frame, text="Results", font=("Arial", 12))
    results.pack()
    x1 = tk.Label(results_frame, textvariable=x1_var)
    x1.pack()
    x2 = tk.Label(results_frame, textvariable=x2_var)
    x2.pack()
    x3 = tk.Label(results_frame, textvariable=x3_var)
    x3.pack()

    for row in entries:
        for entry in row:
            entry.bind("<KeyRelease>", on_edit)

    radio1.bind("<Button-1>", on_edit)
    radio2.bind("<Button-1>", on_edit)
    radio3.bind("<Button-1>", on_edit)
    radio4.bind("<Button-1>", on_edit)

    root.mainloop()