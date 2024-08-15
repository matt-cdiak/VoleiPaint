import tkinter as tk
from model import Model
from view import View
from controller import Controller

def main():
    root = tk.Tk()
    model = Model()
    view = View(root)
    controller = Controller(model, view)
    root.mainloop()

if __name__ == "__main__":
    main()
