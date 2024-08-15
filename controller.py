class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.canvas.bind("<Button-1>", self.start_draw)
        self.view.canvas.bind("<B1-Motion>", self.draw)
        self.view.canvas.bind("<ButtonRelease-1>", self.stop_draw)
        self.view.eraser_button.config(command=self.toggle_eraser)
        self.view.pencil_button.config(command=self.toggle_pencil)

    def start_draw(self, event):
        self.model.drawing_data["draw"] = True
        self.model.drawing_data["x"] = event.x
        self.model.drawing_data["y"] = event.y

    def draw(self, event):
        if self.model.drawing_data["draw"]:

            if self.model.drawing_data["color"] == self.view.canvas.cget("bg"):
                self.view.canvas.create_line(self.model.drawing_data["x"], self.model.drawing_data["y"], event.x, event.y, fill=self.model.drawing_data["color"], width=50, smooth=True)
            else:
                self.view.canvas.create_line(self.model.drawing_data["x"], self.model.drawing_data["y"], event.x, event.y, fill=self.model.drawing_data["color"], width=5, smooth=True)

            self.model.drawing_data["x"] = event.x
            self.model.drawing_data["y"] = event.y
    
    def stop_draw(self, event):
        self.model.drawing_data["draw"] = False

    def toggle_eraser(self):
        self.model.drawing_data["color"] = self.view.canvas.cget("bg")

    def toggle_pencil(self):
        self.model.drawing_data["color"] = "black"
