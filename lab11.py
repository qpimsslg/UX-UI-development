import dearpygui.dearpygui as dpg
import numpy as np
import time

class CubicFunctionApp:
    def __init__(self):
        self.a, self.b, self.c, self.d = 1, 0, 0, 0
        self.prev_a, self.prev_b, self.prev_c, self.prev_d = self.a, self.b, self.c, self.d
        self.frames = 120
        self.target_fps = 100000
        self.frame_duration = 1 / self.target_fps

        dpg.create_context()
        dpg.create_viewport(title='Cubic Function Plotter', width=800, height=600, vsync=False)

        with dpg.window(label="Parameters", width=150, height=600, pos=(0, 0)):
            dpg.add_text("a =")
            self.input_a = dpg.add_input_text(default_value=str(self.a), callback=self.on_input_change, width=50)
            dpg.add_text("b =")
            self.input_b = dpg.add_input_text(default_value=str(self.b), callback=self.on_input_change, width=50)
            dpg.add_text("c =")
            self.input_c = dpg.add_input_text(default_value=str(self.c), callback=self.on_input_change, width=50)
            dpg.add_text("d =")
            self.input_d = dpg.add_input_text(default_value=str(self.d), callback=self.on_input_change, width=50)
            dpg.add_text("")
            self.fps_display = dpg.add_text("FPS: calculating...")

        with dpg.window(label="Graph", pos=(160, 0), width=600, height=600):
            with dpg.plot(label="Cubic Function", height=500, width=600):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvXAxis, label="x", tag="x_axis")
                dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis")
                self.plot_series = dpg.add_line_series([], [], label="y = ax^3 + bx^2 + cx + d", parent="y_axis")


        dpg.setup_dearpygui()
        dpg.show_viewport()

    def generate_plot_data(self, a, b, c, d):
        x = np.linspace(-10, 10, 400)
        y = a * x ** 3 + b * x ** 2 + c * x + d
        return x, y

    def update_plot(self, a, b, c, d):
        x, y = self.generate_plot_data(a, b, c, d)
        dpg.set_value(self.plot_series, [x.tolist(), y.tolist()])
        dpg.set_axis_limits("x_axis", -10, 10)
        dpg.set_axis_limits("y_axis", -100, 100)

    def animate_transition(self):
        last_time = time.time()
        for frame in range(self.frames):
            t = frame / (self.frames - 1)
            a = (1 - t) * self.prev_a + t * self.a
            b = (1 - t) * self.prev_b + t * self.b
            c = (1 - t) * self.prev_c + t * self.c
            d = (1 - t) * self.prev_d + t * self.d

            # раньше были закомментированные строки и не было current и elapsed time

            # self.update_plot(a, b, c, d)
            # time.sleep(0.01)
            # dpg.render_dearpygui_frame()

            self.update_plot(a, b, c, d)
            current_time = time.time()
            elapsed_time = current_time - last_time

            if elapsed_time < self.frame_duration:
                time.sleep(self.frame_duration - elapsed_time)

            dpg.set_value(self.fps_display, f"FPS: {int(1 / max(elapsed_time, self.frame_duration))}")
            last_time = time.time()
            # dpg.render_dearpygui_frame()

        self.prev_a, self.prev_b, self.prev_c, self.prev_d = self.a, self.b, self.c, self.d

    def on_input_change(self, sender, app_data):
        try:
            self.a = float(dpg.get_value(self.input_a))
            self.b = float(dpg.get_value(self.input_b))
            self.c = float(dpg.get_value(self.input_c))
            self.d = float(dpg.get_value(self.input_d))
            self.animate_transition()
        except ValueError:
            pass

    def run(self):
        self.update_plot(self.a, self.b, self.c, self.d)
        while dpg.is_dearpygui_running():
            dpg.render_dearpygui_frame()
        dpg.destroy_context()

if __name__ == "__main__":
    app = CubicFunctionApp()
    app.run()
