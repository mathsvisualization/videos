from manim_imports_ext import *
sys.path.append("D:/Visualization/")
from helper import *

class IntroductionOfTaylorSeriesSinX(Template):
    title = "Taylor Series"
    page_no = 1

    def construct(self):
        self.embed()
        # Equation
        taylor = TexText(R"Taylor Series of $\sin(x)$", t2c={"x": YELLOW})
        taylor.set_y(2.8)

        underline = Underline(taylor, stretch_factor=1.1)
        underline.set_stroke(PURPLE_B, width=[1, 2, 2, 1])
        self.add(taylor, underline)

        tex_config = dict(font_size=36, t2c=dict(x=YELLOW))
        equation_tex = R"\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots"
        equation = get_formula_and_rect(equation_tex, tex_config, corner_radius=0.05)
        self.add(equation)

class TaylorSeriesOfSinX(Template):
    title = "Taylor Series"
    page_no = 2

    def construct(self):
        self.embed()
        # Remember Maclaurin Series
        remember = TexText("Remember Maclaurin Series?", font_size=36)
        remember.next_to(self.template[-2], DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        remember.shift(LEFT*0.5)
        self.add(remember)

        # new equation
        tex_kw = dict(font_size=24, t2c={"x": YELLOW})
        tex = R"f(x) = &\ f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \dots"
        new_equation = get_formula_and_rect(tex, tex_kw, corner_radius=0.05)
        new_equation.next_to(remember, DOWN, buff=MED_LARGE_BUFF)
        new_equation.shift(RIGHT)
        self.add(new_equation)

        # Derivative of sin(x)
        derivative = TexText("$\\bullet$ Derivative of $\\sin(x)$", font_size=36, t2c={"x": YELLOW})
        derivative.next_to(new_equation, DOWN, buff=MED_LARGE_BUFF)
        derivative.match_x(remember, LEFT)
        self.add(derivative)

        # Table
        table = Tex(R"""
            \begin{array}{c@{\quad}|@{\quad}c@{\quad}|@{\quad}c}
            \text{Term} & \text{Derivative} & \text{Value at } x = 0 \\[0.3em] \hline
            f(x) & \sin x & 0 \\[0.5em]
            f'(x) & \cos x & 1 \\[0.5em]
            f''(x) & -\sin x & 0 \\[0.5em]
            f'''(x) & -\cos x & -1 \\[0.5em]
            \vdots & \vdots & \vdots
            \end{array}
        """, t2c={"x": YELLOW}, font_size=24)
        table.scale(1.2, about_edge=UP)
        table.next_to(derivative, DOWN, aligned_edge=LEFT)
        table.shift(RIGHT)
        self.add(table)

class Final(Template):
    title = "Taylor Series"
    page_no = 3

    def construct(self):
        self.embed()
        # Template
        substitues = TexText("$\\bullet$ Substitute in series formula", font_size=36)
        substitues.next_to(self.template[-2], DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        substitues.shift(0.5*LEFT)
        self.add(substitues)

        # Formula sin(x)
        sinx = Tex(R"\sin x = 0 + (1)x + \frac{0}{2!} x^2 + \frac{-1}{3!} x^3 + \frac{0}{4!} x^4 + \frac{1}{5!} x^5 - \cdots", font_size=24, t2c=dict(x=YELLOW))
        sinx.next_to(substitues, DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        sinx.shift(RIGHT)
        self.add(sinx)

        # become
        sinx_ = Tex(R"\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots", font_size=24, t2c=dict(x=YELLOW))
        sinx_.next_to(sinx, DOWN, aligned_edge=LEFT)
        self.add(sinx_)

        # Pattern
        pattern = TexText("$\\bullet$ notice x to the power is odd\\\\ $\\bullet$ alternate signs (+ - + - \\ldots)", alignment=R"\flushleft", font_size=24)
        pattern.next_to(sinx_, DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF).to_edge(LEFT)
        self.add(pattern)

        tex = R"\sin x = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!}"
        tex_config = dict(font_size=36, t2c=dict(x=YELLOW))
        equ_rect = get_formula_and_rect(tex, tex_config, corner_radius=0.05)
        equ_rect.set_y(-1.5)
        self.add(equ_rect)

class VisualizationOfSinX(Template):
    title = "Visualization of $\\sin(x)$"
    page_no = 4

    def construct(self):
        self.embed()
        # Setup
        axes = Axes(
            (-2 * PI, 2 * PI, PI / 2), (-3, 3),
            width=6, height=4,
            axis_config=dict(
                tick_size=0.05,
            )
        )
        axes.shift(UP)
        self.add(axes)

        # Actual sin(x) graph
        graph_actual = axes.get_graph(lambda x: np.sin(x))
        graph_actual.set_stroke(BLUE, 2)

        # Taylor approximation function for sin(x)
        def taylor_sin(x, n_terms):
            result = 0
            for k in range(n_terms):
                term = ((-1)**k * x**(2*k + 1)) / math.factorial(2*k + 1)
                result += term
            return result

        graph_label = Tex(
            "y = x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + \\frac{x^9}{9!} - \\frac{x^{11}}{11!}",
            t2c=dict(x=YELLOW),
            font_size=19
        )
        graph_label.next_to(axes.y_axis.get_top(), RIGHT, aligned_edge=UP)

        label = Tex(
            "\\sin(x) = x - \\frac{x^3}{3!} + \\frac{x^5}{5!} - \\frac{x^7}{7!} + \\frac{x^9}{9!} - \\frac{x^{11}}{11!}",
            t2c=dict(x=YELLOW),
            font_size=24
        )
        label.set_flat_stroke(False)
        label.shift(DOWN * 2.5)
        self.add(label, graph_label["y ="][0])

        # equation
        tex_kw = dict(font_size=36, t2c={"x": YELLOW})
        tex = R"\sin x = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!}"
        equ = Tex(tex, **tex_kw)
        equ.shift(2 * DOWN)

        rect = SurroundingRectangle(equ)
        rect.set_stroke(WHITE, 1.5)
        rect.set_fill("#191919", 1.0)
        rect.round_corners(0.05)

        # Generate all partial graphs for visualization
        graphs = VGroup()
        for i in range(1, 7):
            graph = axes.get_graph(lambda x, i=i: taylor_sin(x, i))
            graph.set_stroke(YELLOW, 2)
            graphs.add(graph)

        # Animate base graph and first approximation
        self.play(ShowCreation(graph_actual, run_time=2, rate_func=linear))
        self.play(ShowCreation(graphs[0]), Write(graph_label["x"][0]), run_time=2)
        curr = graphs[0]

        for graph, term in zip(
            graphs[1:], 
            ["- \\frac{x^3}{3!}", "+ \\frac{x^5}{5!}", "- \\frac{x^7}{7!}", "+ \\frac{x^9}{9!}", "- \\frac{x^{11}}{11!}"]
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
        self.wait(2)
