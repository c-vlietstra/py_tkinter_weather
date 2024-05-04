import tkinter as tk

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1, x1+radius, y1, x2-radius, y1, x2-radius, y1, x2, y1,
              x2, y1+radius, x2, y1+radius, x2, y2-radius, x2, y2-radius, x2, y2,
              x2-radius, y2, x2-radius, y2, x1+radius, y2, x1+radius, y2, x1, y2,
              x1, y2-radius, x1, y2-radius, x1, y1+radius, x1, y1+radius, x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

class SearchBar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.canvas = tk.Canvas(self, height=50, width=300, bd=0, highlightthickness=0, bg='white')
        self.canvas.pack(fill='both', expand=True)

        create_rounded_rectangle(self.canvas, 10, 10, 290, 40, radius=15, fill='darkgrey')

        self.entry = tk.Entry(self, bd=0, font=('Arial', 14), fg='white', bg='darkgrey')
        self.entry.place(x=20, y=15, width=260, height=20)