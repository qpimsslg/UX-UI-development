import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class CubicFunctionApp:
    def __init__(self, master):
        # cоздание всех виджетов для ввода параметров, инициация графиков
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

        self.fig = Figure(figsize=(5, 5))
        self.ax = self.fig.add_subplot(1, 1, 1)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.ax.grid(True, which='both', color='lightgray')

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

    def update_plot(self, event=None):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            c = float(self.entry_c.get())
            d = float(self.entry_d.get())

            self.ax.clear()

            x = range(-10, 11)
            y = [a * i ** 3 + b * i ** 2 + c * i + d for i in x]
            self.ax.plot(x, y)

            self.ax.set_title(f"y = {a}x^3 + {b}x^2 + {c}x + {d}")

            self.ax.set_xlabel("x")
            self.ax.set_ylabel("y")

            self.ax.grid(True, which='both', color='lightgray')

            self.canvas.draw()

            equation = f"y = {a}x^3 + {b}x^2 + {c}x + {d}"

        except ValueError:
            pass

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

if __name__ == "__main__":
    root = tk.Tk()
    app = CubicFunctionApp(root)
    root.mainloop()
