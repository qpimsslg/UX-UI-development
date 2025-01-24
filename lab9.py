import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import numpy as np

class CubicFunctionApp:
    def __init__(self, master):
        self.master = master
        master.title("Cubic Function Plotter")

        self.input_frame = tk.Frame(master)
        self.input_frame.pack(side=tk.LEFT, padx=20, pady=20)

        self.plot_frame = tk.Frame(master)
        self.plot_frame.pack(side=tk.RIGHT, padx=20, pady=20)

        self.label_a = tk.Label(self.input_frame, text="a =")
        self.label_a.pack()
        self.entry_a = tk.Entry(self.input_frame)
        self.entry_a.pack()

        self.label_b = tk.Label(self.input_frame, text="b =")
        self.label_b.pack()
        self.entry_b = tk.Entry(self.input_frame)
        self.entry_b.pack()

        self.label_c = tk.Label(self.input_frame, text="c =")
        self.label_c.pack()
        self.entry_c = tk.Entry(self.input_frame)
        self.entry_c.pack()

        self.label_d = tk.Label(self.input_frame, text="d =")
        self.label_d.pack()
        self.entry_d = tk.Entry(self.input_frame)
        self.entry_d.pack()

        self.fig, self.ax = plt.subplots(figsize=(5, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.ax.grid(True, which='both', color='lightgray')

        self.animation = None

        self.entry_a.bind("<KeyRelease>", self.update_plot)
        self.entry_b.bind("<KeyRelease>", self.update_plot)
        self.entry_c.bind("<KeyRelease>", self.update_plot)
        self.entry_d.bind("<KeyRelease>", self.update_plot)

        self.canvas.mpl_connect('scroll_event', self.on_scroll)
        self.canvas.mpl_connect('button_press_event', self.on_click)
        self.canvas.mpl_connect('button_release_event', self.on_release)
        self.canvas.mpl_connect('motion_notify_event', self.on_motion)
        self.is_panning = False
        self.start_x = 0
        self.start_y = 0

        self.a = 0.0
        self.b = 0.0
        self.c = 0.0
        self.d = 0.0
        self.prev_a = 0.0
        self.prev_b = 0.0
        self.prev_c = 0.0
        self.prev_d = 0.0

        self.update_plot()

    def update_plot(self, event=None):
        # обновление параметров и инициирование анимации
        try:
            self.a = float(self.entry_a.get())
            self.b = float(self.entry_b.get())
            self.c = float(self.entry_c.get())
            self.d = float(self.entry_d.get())

            self.equation = f"y = {self.a}x^3 + {self.b}x^2 + {self.c}x + {self.d}"

            if self.animation is not None:
                self.animation.event_source.stop()

            self.ax.set_xlim(-10, 10)
            self.ax.set_ylim(-100, 100)

            self.animation = FuncAnimation(
                self.fig, self.animate_plot, frames=30, interval=20, blit=True
            )

            self.ax.set_title(self.equation)

        except ValueError:
            pass

    def animate_plot(self, frame):
        # анимация при изменении параметров графика
        a = (frame * self.a + (30 - frame) * self.prev_a) / 30
        b = (frame * self.b + (30 - frame) * self.prev_b) / 30
        c = (frame * self.c + (30 - frame) * self.prev_c) / 30
        d = (frame * self.d + (30 - frame) * self.prev_d) / 30

        x = np.linspace(-10, 10, 400)
        y = a * x ** 3 + b * x ** 2 + c * x + d

        if hasattr(self, 'line'):
            self.line.remove()
        self.line, = self.ax.plot(x, y, color='blue')

        # сетку и метки осей устанавливаем только на 1 кадре анимации
        if frame == 0:
            self.ax.grid(True, which='both', color='lightgray')
            self.ax.set_xlabel("x")
            self.ax.set_ylabel("y")

        self.canvas.draw()

        # на последнем кадре анимации переназначаем параметры
        if frame == 29:
            self.prev_a, self.prev_b, self.prev_c, self.prev_d = self.a, self.b, self.c, self.d

        return self.line,

    def plot_function(self):
        # построение графика с данными параметрами
        if self.ax.lines:
            self.ax.lines.pop()

        x = range(-10, 11)
        y = [self.a * i ** 3 + self.b * i ** 2 + self.c * i + self.d for i in x]

        equation = f"y = {self.a}x^3 + {self.b}x^2 + {self.c}x + {self.d}"
        self.ax.set_title(equation, fontsize=12)
        self.ax.plot(x, y)
        self.canvas.draw()

    def on_scroll(self, event):
        # масштабирование графика прокруткой колесика
        if event.button == 'up':
            base_scale = 1.1
        elif event.button == 'down':
            base_scale = 0.9
        else:
            return

        x_min, x_max = self.ax.get_xlim()
        y_min, y_max = self.ax.get_ylim()

        x_center = (x_min + x_max) / 2
        y_center = (y_min + y_max) / 2
        x_width = (x_max - x_min) * base_scale
        y_height = (y_max - y_min) * base_scale
        x_min = x_center - x_width / 2
        x_max = x_center + x_width / 2
        y_min = y_center - y_height / 2
        y_max = y_center + y_height / 2

        self.ax.set_xlim(x_min, x_max)
        self.ax.set_ylim(y_min, y_max)
        self.canvas.draw()

    def on_click(self, event):
        # передвижение графика
        if event.button == 1:
            self.is_panning = True
            self.start_x = event.xdata
            self.start_y = event.ydata

    def on_release(self, event):
        # перестаем перемешать график при отпускании мышки
        if event.button == 1:
            self.is_panning = False

    def on_motion(self, event):
        # реализация перемещения графика
        if self.is_panning:
            x_min, x_max = self.ax.get_xlim()
            y_min, y_max = self.ax.get_ylim()

            x_distance = event.xdata - self.start_x
            y_distance = event.ydata - self.start_y

            x_min -= x_distance
            x_max -= x_distance
            y_min -= y_distance
            y_max -= y_distance

            self.ax.set_xlim(x_min, x_max)
            self.ax.set_ylim(y_min, y_max)
            self.canvas.draw()

            self.start_x = event.xdata
            self.start_y = event.ydata

root = tk.Tk()
app = CubicFunctionApp(root)
root.mainloop()