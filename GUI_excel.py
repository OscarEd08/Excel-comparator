import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import pandas as pd

#Root window
root = tk.Tk()
root.geometry("700x600") 
root.resizable(0, 0) 

#Frame for ExcelFile 
frame1 = ttk.LabelFrame(root, text="Archivo excel")
frame1.place(height=500, width=700, rely=0.20, relx=0)

# Frame for open_file dialog
file_frame = ttk.LabelFrame(root, text="Archivos")
file_frame.place(height=100, width=700)

#Buttons
btn1 = ttk.Button(file_frame, text="Subir archivos", command=lambda: open_file())
btn1.place(rely=0.45, relx=0.30)

btn2 = ttk.Button(file_frame, text="Comparar archivos", command=lambda: load_excel())
btn2.place(rely=0.45, relx=0.50)

label_file1 = ttk.Label(file_frame, text="Archivo 1")
label_file1.grid(column=0, row=0)
label_file2 = ttk.Label(file_frame, text="Archivo 2")
label_file2.grid(column=1, row=0)


#Treeview Widget
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1) 

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) 
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
treescrollx.pack(side="bottom", fill="x") 
treescrolly.pack(side="right", fill="y") 


def open_file():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Seleccione archivo",
                                          filetype=(("xlsx files", "*.xlsx"),("All Files", "*.*")))
    label_file1["text"] = filename
    label_file2["text"] = filename
    return None


def load_excel():
    file_path1 = label_file1["text"]
    file_path2 = label_file2["text"]
    try:
        excel_file1 = r"{}".format(file_path1)
        excel_file2 = r"{}".format(file_path2)
        df1 = pd.read_excel(excel_file1, header=None)
        df2 = pd.read_excel(excel_file2, header=None)

    except ValueError:
        tk.messagebox.showerror("Information", "Formato incorrecto")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No encontrado {file_path1}")
        return None

    clear()
    tv1["column"] = list(df1.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column) 

    df_rows = df1.to_numpy().tolist()
    for row in df_rows:
        tv1.insert("", "end", values=row) 
    return None


def clear():
    tv1.delete(*tv1.get_children())
    return None


root.mainloop()