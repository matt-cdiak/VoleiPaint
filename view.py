import tkinter as tk

class View:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=800, height=600, bg='white')
        self.canvas.pack()
        self.eraser_button = tk.Button(root, text="Borracha", command=self.toggle_eraser)
        self.eraser_button.pack()
        self.pencil_button = tk.Button(root, text="Lápis", command=self.toggle_pencil)
        self.pencil_button.pack()
        
    def toggle_eraser(self):
        pass

    def toggle_pencil(self):
        pass
