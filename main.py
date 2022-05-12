import tkinter as tk
from tkinter import ttk

root = tk.Tk()

main = ttk.Frame(root)
main.pack(fill="both",expand=True, padx=1, pady=(4,0))

notebook= ttk.Notebook(main)

root.mainloop()

