import simpy.core
from matplotlib import pyplot as plt
from simulacao import Simulacao
from manim import *


class NaviosCargueiros(Scene):
    def construct(self):
        plt.ion()
        fig, axs = plt.subplots(1, 3)
        simulacao = Simulacao(self, num_navios=5)
        simulacao.plot_cummulative_hist_in_axes(axs)
        plt.show()
        while simulacao.peek() != simpy.core.Infinity:
            simulacao.step()
            # for event_time, priority, algo, event in simulacao._queue:  # verifica estado dos eventos na fila
            #     if event.triggered:
            #         if hasattr(event, '_generator') and event._generator.gi_code.co_name == 'chegada':
            #             print(f"Evento disparado: {event}")


class SinAndCosFunctionPlot(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        cos_graph = axes.plot(lambda x: np.cos(x), color=RED)

        sin_label = axes.get_graph_label(
            sin_graph, "\\sin(x)", x_val=-10, direction=UP / 2
        )
        cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)")

        vert_line = axes.get_vertical_line(
            axes.i2gp(TAU, cos_graph), color=YELLOW, line_func=Line
        )
        line_label = axes.get_graph_label(
            cos_graph, "x=2\pi", x_val=TAU, direction=UR, color=WHITE
        )

        plot = VGroup(axes, sin_graph, cos_graph, vert_line)
        labels = VGroup(axes_labels, sin_label, cos_label, line_label)
        self.wait()
        self.play(Create(axes))
        self.play(Create(axes_labels))
        self.wait()
        self.play(Create(sin_graph))
        self.play(Create(sin_label))
        self.wait()
        self.play(Create(cos_graph))
        self.play(Create(cos_label))
        self.wait()
        self.play(Create(vert_line))
        self.play(Create(line_label))
        self.wait()


if __name__=="__main__":
    teste = Teste()
    teste.construct()