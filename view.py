import tkinter as tk

class View:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=800, height=600, bg='white')
        self.canvas.pack()
        self.eraser_button = tk.Button(root, text="Borracha")
        self.eraser_button.pack(side=tk.LEFT)
        self.pencil_button = tk.Button(root, text="Lapis")
        self.pencil_button.pack(side=tk.LEFT)
        