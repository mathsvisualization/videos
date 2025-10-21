from manim_imports_ext import *
sys.path.append("D:/Visualization/")
from helper import *

class IntroductionEtoX(Template):
    title = "Taylor Series"
    page_no = 1

    def construct(self):
        self.embed()
        # title
        title = TexText("Taylor Series of $e^x$", t2c=dict(x=YELLOW), font_size=36)
        title.next_to(self.template[-2], DOWN)
        title.set_x(0)

        underline = Underline(title, stretch_factor=1.1)
        underline.set_stroke(PINK, width=[1, 2, 2, 1])

        self.add(title, underline)

        # Equation
        kw = dict(font_size=36, t2c=dict(x=YELLOW))
        raw_tex = R"e^{x} = \sum_{n=0}^{\infty} \frac{x^{n}}{n!}"
        equation = get_formula_and_rect(raw_tex, kw, corner_radius=0.05)
        self.add(equation)


class RememberMaclaurinSeries(Template):
    title = "Taylor Series"
    page_no = 2

    def construct(self):
        self.embed()
        # Remember Maclaurin Series
        series = TexText("Maclaurin Series", font_size=36)
        series.next_to(self.template[-2], DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        series.shift(LEFT*0.5)
        self.add(series)

        # MaclaurinSeries
        tex_config = dict(font_size=24, t2c={"x": YELLOW})
        raw_tex = R"f(x) = &\ f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \dots"
        maclaurin = get_formula_and_rect(raw_tex, tex_config, corner_radius=0.05)
        maclaurin.next_to(series, DOWN, buff=MED_LARGE_BUFF)
        maclaurin.set_x(0)
        self.add(maclaurin)

        bullet = Tex("\\bullet", **tex_config)
        bullet.next_to(maclaurin, LEFT)
        self.add(bullet)

        # ApplyMaclaurinSeries
        apply = TexText("Apply Maclaurin Series", font_size=36)
        apply.next_to(maclaurin, DOWN, buff=MED_LARGE_BUFF)
        apply.match_x(series, LEFT)
        self.add(apply)

        # Table (e^x) Derivative
        table = Tex(R"""            
            \begin{tabular}{|c|c|c|c|}
            \hline
            Term Number $n$ & Derivative $f^{(n)}(x)$ & Value at $x=0$ & Maclaurin Term $\frac{f^{(n)}(0)}{n!}x^n$ \\[0.5em]
            \hline
            0 & $f(x) = e^x$ & 1 & $1$ \\[0.5em]
            1 & $f'(x) = e^x$ & 1 & $x$ \\[0.5em]
            2 & $f''(x) = e^x$ & 1 & $\frac{x^2}{2!} = \frac{x^2}{2}$ \\[0.5em]
            3 & $f'''(x) = e^x$ & 1 & $\frac{x^3}{3!} = \frac{x^3}{6}$ \\[0.5em]
            4 & $f^{(4)}(x) = e^x$ & 1 & $\frac{x^4}{4!} = \frac{x^4}{24}$ \\[0.5em]
            5 & $f^{(5)}(x) = e^x$ & 1 & $\frac{x^5}{5!} = \frac{x^5}{120}$ \\[0.5em]
            \hline
            \end{tabular}
        """, t2c=dict(x=YELLOW))
        table.set_width(FRAME_WIDTH - 1)
        table.next_to(apply, DOWN)
        table.set_x(0)
        self.add(table)

        # formula
        raw_tex = R"e^{x} = 1 + x + \frac{x^{2}}{2!} + \frac{x^{3}}{3!} + \frac{x^{4}}{4!} + \frac{x^{5}}{5!} \cdots"
        formula = get_formula_and_rect(raw_tex, tex_config, corner_radius=0.05)
        formula.next_to(table, DOWN)
        self.add(formula)

class VisualizationOfExpX(Template):
    title = "Visualization of $e^x$"
    page_no = 3

    def construct(self):
        self.embed()
        # Setup
        axes = Axes(
            (-1, 3, 1), (0, 15, 5),
            width=6, height=4,
            axis_config=dict(
                tick_size=0.05,
            )
        )
        axes.shift(UP)
        self.add(axes)

        # Actual e^x graph
        graph_actual = axes.get_graph(lambda x: np.exp(x))
        graph_actual.set_stroke(BLUE, 2)

        # Taylor approximation function for e^x
        def taylor_exp(x, n_terms):
            result = 0
            for k in range(n_terms):
                result += x**k / math.factorial(k)
            return result

        graph_label = Tex(
            "y = 1 + x + \\frac{x^2}{2!} + \\frac{x^3}{3!} + \\frac{x^4}{4!} + \\frac{x^5}{5!} + \\frac{x^6}{6!}",
            t2c=dict(x=YELLOW),
            font_size=19
        )
        graph_label.next_to(axes.y_axis.get_top(), RIGHT, aligned_edge=UP)

        label = Tex(
            "e^x = 1 + x + \\frac{x^2}{2!} + \\frac{x^3}{3!} + \\frac{x^4}{4!} + \\frac{x^5}{5!} + \\frac{x^6}{6!}",
            t2c=dict(x=YELLOW),
            font_size=24
        )
        label.set_flat_stroke(False)
        label.shift(DOWN * 2.5)
        self.add(label, graph_label["y ="][0])

        # equation
        tex_kw = dict(font_size=36, t2c={"x": YELLOW})
        tex = R"e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}"
        equ = Tex(tex, **tex_kw)
        equ.shift(2 * DOWN)

        rect = SurroundingRectangle(equ)
        rect.set_stroke(WHITE, 1.5)
        rect.set_fill("#191919", 1.0)
        rect.round_corners(0.05)

        # Generate all partial graphs for visualization
        graphs = VGroup()
        for i in range(1, 8):
            graph = axes.get_graph(lambda x, i=i: taylor_exp(x, i))
            graph.set_stroke(YELLOW, 2)
            graphs.add(graph)

        # Animate base graph and first approximation
        self.play(ShowCreation(graph_actual, run_time=2, rate_func=linear))
        self.wait()
        self.play(ShowCreation(graphs[0]), Write(graph_label["1"][0]), run_time=2)
        curr = graphs[0]

        for graph, term in zip(
            graphs[1:], 
            ["+ x", "+ \\frac{x^2}{2!}", "+ \\frac{x^3}{3!}", "+ \\frac{x^4}{4!}", "+ \\frac{x^5}{5!}", "+ \\frac{x^6}{6!}"]
        ):
            self.play(
                ReplacementTransform(curr, graph),
                ReplacementTransform(label[term][0].copy(), graph_label[term][0]),
                rate_func=smooth,
                run_time=2
            )
            self.wait(1.0)
            curr = graph

        self.play(
            LaggedStart(
                ReplacementTransform(curr, graph_actual, time_span=(0.5, 2)),
                FadeOut(label, shift=DOWN * 0.5),
                DrawBorderThenFill(rect),
                TransformMatchingStrings(graph_label, equ),
                lag_ratio=0.1,
                rate_func=smooth,
                run_time=2
            )
        )
        self.wait(3)
