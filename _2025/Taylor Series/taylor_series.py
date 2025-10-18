from manim_imports_ext import *
sys.path.append("D:/Visualization/")
from helper import *

class TaylorSeriesIntroWithCosXExample(Template):
    title = "Taylor Series"
    page_no = 1

    def construct(self):
        self.embed()
        # taylor series of cos(x)
        tex_kw = dict(font_size=36, t2c={"x": YELLOW})
        cosx_tex  = R"\cos x = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n}}{(2n)!}"        
        cosx_equation = get_formula_and_rect(cosx_tex , tex_kw, corner_radius=0.08)
        cosx_equation.move_to(ORIGIN, DOWN)
        self.add(cosx_equation)

        # But how ?
        morty = Mortimer(mode="thinking")
        morty.set_color(PURPLE_B)
        morty.scale(0.5)
        morty.next_to(self.template[2].get_end(), UL, buff=SMALL_BUFF)
        but_how = morty.get_bubble("But How?")
        but_how.scale(0.6)
        but_how.pin_to(morty, True)
        self.add(morty, but_how)
        self.play(morty.animate.look_at(cosx_equation))

class IntroductionTaylorSeries(Template):
    title = "Taylor Series"
    page_no = 2

    def construct(self):
        self.embed()
        # Definitation
        definition = TexText(R"""
            \section*{What is Taylor Series?}
            The Taylor series of a function is an infinite sum of \\
            terms that are calculated from the values of the function's \\
            derivatives at a single point. It represents the function as a \\
            power series basically an infinite polynomial that approximates \\
            the function near that point.
        """, isolate=[R"\section*{What is Taylor Series?}"], alignment=R"\flushleft")
        definition.set_width(FRAME_WIDTH - 1)
        definition.set_x(0)
        definition.set_y(2)

        underline = Underline(definition[R"\section*{What is Taylor Series?}"], stretch_factor=1.05)
        underline.set_stroke(width=[1, 2, 2, 1])
        underline.set_color(BLUE)
        self.add(definition, underline)

        # Equation
        tex_config = dict(font_size=24, t2c={"x": YELLOW, "a": PINK})
        taylor_series_tex = R"f(x) = &\ f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \dots"
        taylor_series_equation = get_formula_and_rect(taylor_series_tex, tex_config, corner_radius=0.05)
        self.add(taylor_series_equation)

        explanation = BulletedList(
            "$f(x)$: The original function we want to approximate.",
            "$f(a)$: The value of the function at the expansion point $a$.",
            "$f'(a)(x-a)$: The linear term which adjusts the slope.",
            R"$\frac{f''(a)}{2!}(x-a)^2$: Adds the curvature (second derivative).",
            R"$\frac{f'''(a)}{3!}(x-a)^3$: Adds the inflection detail (third derivative)."
        )

        explanation.set_width(FRAME_WIDTH - 1)
        explanation.match_x(definition, LEFT)
        explanation.next_to(equation, DOWN)
        explanation.tex_text["f(x)"][0][-2].set_color(YELLOW)
        explanation.tex_text["f(a)"][0][-2].set_color(PINK)
        explanation.tex_text["f'(a)(x-a)"][0][-2].set_color(PINK)
        explanation.tex_text["f'(a)(x-a)"][0][3].set_color(PINK)
        explanation.tex_text["f'(a)(x-a)"][0][6].set_color(YELLOW)
        explanation.tex_text[R"\frac{f''(a)}{2!}(x-a)^2"][0][3].set_color(PINK)
        explanation.tex_text[R"\frac{f''(a)}{2!}(x-a)^2"][0][9].set_color(YELLOW)
        explanation.tex_text[R"\frac{f''(a)}{2!}(x-a)^2"][0][11].set_color(PINK)
        explanation.tex_text[R"\frac{f'''(a)}{3!}(x-a)^3"][0][2].set_color(PINK)
        explanation.tex_text[R"\frac{f'''(a)}{3!}(x-a)^3"][0][8].set_color(YELLOW)
        explanation.tex_text[R"\frac{f'''(a)}{3!}(x-a)^3"][0][10].set_color(PINK)
        self.add(explanation)

class WhatExactlyFx(Template):
    title = "Taylor Series"
    page_no = 3

    def construct(self):
        self.embed()
        # What exactly f(x) and f(a)
        idea = TexText("What exactly $f(x)$ and $f(a)$?")
        idea["x"][1].set_color(YELLOW)
        idea["a"][-1].set_color(PINK)
        idea.match_x(self.template[3], LEFT)
        idea.shift(UP*3)

        underline = Underline(idea)
        underline.set_stroke(BLUE, width=[0, 2, 2, 0])

        self.add(underline)
        self.add(idea)
        
        # f(x)
        kw = dict(font_size=36, t2c={"x": YELLOW, "a": PINK})
        f = Tex("f(x)", **kw)
        f.next_to(underline, DOWN, aligned_edge=LEFT)
        fx = BulletedList(
            "$f$: is the name of a function (such as $\\sine$, $\\cosine$, exponential,\\\\or any other function).",
            "$x$: is input variable",
            "$f(x)$ means: The value of the function $f$ when its input is $x$.",
            "This is a general formula or rule.",
            t2c=dict(x=YELLOW)
        )
        fx.scale(0.5)
        fx.tex_text["exponential"].set_color(WHITE)
        fx.next_to(f, DOWN, buff=MED_SMALL_BUFF, aligned_edge=LEFT)
        fx.shift(0.3*RIGHT)
        self.add(f, fx)

        # Example
        example = VGroup(
            Text("Example:", font_size=36),
            Tex(R"f(x) = x^2 + 3", **kw),
            Text("Here f(x) states a rule: Take any number, \nsquare it, and then add 3 to the result", font_size=36)
        )
        example.arrange(DOWN, aligned_edge=LEFT)
        example.next_to(fx, DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT)
        example[0].match_x(f, LEFT)
        example[-1]["f(x)"][0][2].set_color(YELLOW)
        example[-1].shift(0.2*DOWN)
        self.add(example)

class WhatExactlyFA(Template):
    title = "Taylor Series"
    page_no = 4

    def construct(self):
        self.embed()
        # f(a)
        kw = dict(font_size=36, t2c={"x": YELLOW, "a": PINK})
        f = Tex("f(a)", **kw)
        f.next_to(self.template[0], DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT)
        fa = BulletedList(
            "$a$: is a specific value, a fixed number (e.g. 2, 5, 0, 3.14, etc.).",
            "$f(a)$ means: The value of the function $f$ when its input is $a$ \\\\instead of $x$.",
            "The process of finding $f(a)$ is very simple: replace $x$ with a in\\\\ the function $f(x)$.",
            t2c={"$a$": PINK, "$x$": YELLOW}
        )
        fa.scale(0.5)
        fa[1][3].set_color(PINK)
        fa[2][len("The process of finding") - 1].set_color(YELLOW)
        fa[2][-3].set_color(YELLOW)
        fa.next_to(f, DOWN, buff=MED_SMALL_BUFF, aligned_edge=LEFT)
        fa.shift(0.3*RIGHT)
        self.add(f, fa)

        # Example
        example = VGroup(
            TexText("Example: Let us find $f(a)$ for the above function $f(x) = x^2 + 3$.", font_size=24, isolate=["$f(a)$", "$f(x) = x^2 + 3$"]),
            TexText(R"$f(x) = x^2 + 3$", font_size=24, t2c=dict(x=YELLOW)),
            TexText("To find $f(a)$, replace every $x$ in the function with $a$.", t2c={"$a$": PINK, "$x$": YELLOW}, font_size=24, isolate=["$f(a)$"]),
            TexText("$f(a) = a^2 + 3$", font_size=24, t2c=dict(a=PINK)),
            TexText("When the value of $a$ is known, we can calculate the exact output", isolate=["$a$"], t2c={"$a$": PINK}, font_size=24),
            TexText("For $a$ = 2: $f(a)$ = 7", font_size=24, t2c={"a": PINK}),
            TexText("For $a$ = 0: $f(a)$ = 3", font_size=24, t2c={"a": PINK}),
            TexText("For $a$ = 5: $f(a)$ = 28", font_size=24, t2c={"a": PINK}),
        )
        example.arrange(DOWN, aligned_edge=LEFT)
        example.next_to(fa, DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT)
        example[0]["$f(a)$"][0][2].set_color(PINK)
        example[0]["$f(x) = x^2 + 3$"][0][2].set_color(YELLOW)
        example[0]["$f(x) = x^2 + 3$"][0][5].set_color(YELLOW)
        example[0].match_x(f, LEFT)
        self.add(example)

class MaclaurinSeries(Template):
    title = "Maclaurin Series"
    page_no = 5

    def construct(self):
        self.embed()
        # Equation
        tex_kw = dict(font_size=24, t2c={"x": YELLOW, "a": PINK})
        tex = R"f(x) = &\ f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \dots"
        equation = get_formula_and_rect(tex, tex_kw, corner_radius=0.05)
        equation.shift(UP * 2.5)
        self.add(equation)

        # Cases When a = 0
        kw = dict(t2c={"$a$": PINK, "$x$": YELLOW}, font_size=24)
        bullet = Tex("\\bullet", font_size=24)
        cases = VGroup(
            TexText("Special Case: When $a$ $=$ $0$", **kw),
            TexText("When the center is $a$ $=$ $0$, the Taylor series has a special name: \\\\the Maclaurin Series. The formula becomes simpler:", **kw, alignment=R"\flushleft"),

        )
        cases.arrange(DOWN, aligned_edge=LEFT)
        cases.next_to(equation, DOWN, aligned_edge=LEFT)
        cases[1].shift(RIGHT*0.3)
        bullet.next_to(cases[1]["W"][0], LEFT, buff=SMALL_BUFF)
        self.add(bullet)
        self.add(cases)

        # new equation
        tex_kw = dict(font_size=24, t2c={"x": YELLOW})
        tex = R"f(x) = &\ f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \dots"
        new_equation = get_formula_and_rect(tex, tex_kw, corner_radius=0.05)
        self.add(new_equation)

        notice = TexText("Notice how the ($x$ $-$ $a$) terms just become $x$", **kw)
        notice_bullet = bullet.copy()
        notice.next_to(new_equation, DOWN)
        notice.match_x(cases[1], LEFT)
        notice_bullet.next_to(notice["N"][0], LEFT, buff=SMALL_BUFF)
        self.add(notice, notice_bullet)
        
        # Notation
        therefore = TexText(R"Therefore", font_size=24)
        therefore.next_to(notice, DOWN, aligned_edge=LEFT)
        therefore_bullet = bullet.copy()
        therefore_bullet.next_to(therefore["T"][0], LEFT, buff=SMALL_BUFF)
        self.add(therefore, therefore_bullet)

        prime_notation = VGroup(
            Tex(R"f'(a) = \left. \frac{d f(x)}{d x} \right|_{x=a}", t2c=dict(a=PINK, x=YELLOW), font_size=24),
            Tex(R"f''(a) = \left. \frac{d^2 f(x)}{d x^2} \right|_{x=a}", t2c=dict(a=PINK, x=YELLOW), font_size=24),
            Tex(R"f'''(a) = \left. \frac{d^3 f(x)}{d x^3} \right|_{x=a}", t2c=dict(a=PINK, x=YELLOW), font_size=24),
        )
        prime_notation.scale(0.8)
        prime_notation.arrange(DOWN, aligned_edge=LEFT)
        prime_notation.next_to(therefore, DR, buff=SMALL_BUFF)
        self.add(prime_notation)

        # what about cos(x)?
        morty = Mortimer(mode="angry")
        morty.set_color(PURPLE_B)
        morty.scale(0.5)
        morty.next_to(self.template[-3].get_end(), UL, buff=SMALL_BUFF)
        self.add(morty)

        content = morty.get_bubble("what about $\\cos(x)$?", bubble_type=SpeechBubble, math_mode=True, tex_config=dict(t2c=dict(x=YELLOW)))
        content.scale(0.5)
        content.pin_to(morty, False)
        content.content["x"].set_color(YELLOW)
        self.add(content)

class TaylorSeriesForCosX(Template):
    title = "Taylor Series for $\\cos(x)$"
    page_no = 6

    def construct(self):
        self.embed()
        # Taylor
        title = TexText("To construct the Taylor series for $\\cos(x)$, we calculate \\\\the derivatives at $x = 0$", t2c={"x": YELLOW}, font_size=24, alignment=R"\flushleft")
        title.next_to(self.template[-2], DOWN, aligned_edge=LEFT)
        self.add(title)

        equations = Tex(R"""
            &1. \quad f(x) = \cos x \\[0.3em]
            &\quad \circ \quad f(0) = \cos(0) = 1 \\[0.3em]
            &2. \quad \textbf{First derivative:} \\[0.3em]
            &\quad \circ \quad f'(x) = -\sin x \\[0.3em]
            &\quad \circ \quad f'(0) = -\sin(0) = 0 \\[0.3em]
            &3. \quad \textbf{Second derivative:} \\[0.3em]
            &\quad \circ \quad f''(x) = -\cos x \\[0.3em]
            &\quad \circ \quad f''(0) = -\cos(0) = -1 \\[0.3em]
            &4. \quad \textbf{Third derivative:} \\[0.3em]
            &\quad \circ \quad f'''(x) = sin(x) \\[0.3em]
            &\quad (\text{By using the product rule or simply following the pattern}) \\[0.3em]
            &\quad \circ \quad f'''(0) = sin(0) = 0
        """, font_size=24, t2c=dict(x=YELLOW))
        equations.next_to(title, DOWN, aligned_edge=LEFT)
        self.add(equations)

        pattern = TexText(R"A pattern is emerging here: the values of the derivatives \\at $x=0$ repeat every 4 steps. 1, 0, -1, 0, 1, 0, -1, 0, \ldots", font_size=24, t2c=dict(x=YELLOW), alignment=R"\flushleft")
        pattern.next_to(equations, DOWN)
        pattern.shift(0.6*LEFT)
        self.add(pattern)

class CosXFinall(Template):
    title = "Taylor Series for $\\cos(x)$"
    page_no = 7

    def construct(self):
        self.embed()
        # Values
        values = TexText("Substitute the values into the Maclaurin Series formula:", font_size=24)
        values.next_to(self.template[-2], DOWN, aligned_edge=LEFT)
        self.add(values)

        series = Tex(R"\cos x &= f(0) + f'(0)x + \frac{f''(0)}{2!} x^2 + \frac{f'''(0)}{3!} x^3 + \frac{f^{(4)}(0)}{4!} x^4 + \frac{f^{(5)}(0)}{5!} x^5 + \frac{f^{(6)}(0)}{6!} x^6 + \cdots", t2c=dict(x=YELLOW), font_size=19)
        series.next_to(values, DOWN, aligned_edge=LEFT)
        series.shift(0.3*LEFT)
        self.add(series)

        tex = TexText("After substituting the values:", font_size=24)
        tex.next_to(series, DOWN, aligned_edge=LEFT)
        self.add(tex)

        cosx = Tex(R"\cos x &= (1) + (0)x + \frac{(-1)}{2!} x^2 + \frac{(0)}{3!} x^3 + \frac{(1)}{4!} x^4 + \frac{(0)}{5!} x^5 + \frac{(-1)}{6!} x^6 + \cdots", t2c=dict(x=YELLOW), font_size=20)
        cosx.next_to(tex, DOWN, aligned_edge=LEFT)
        self.add(cosx)

        finall = Tex(R"\cos x &= 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \frac{x^8}{8!} - \cdots", font_size=19, t2c=dict(x=YELLOW))
        finall.next_to(cosx, DOWN, aligned_edge=LEFT)
        self.add(finall)

        observe = TexText("What can we observe here?", font_size=24)
        observe.next_to(finall, DOWN, aligned_edge=LEFT)
        self.add(observe)

        group = VGroup(
            TexText("Only even powers of $x$ are present: $x^0$, $x^2$, $x^4$, $x^6$, $x^8$ $\\ldots$", t2c=dict(x=YELLOW), font_size=24),
            TexText("The signs alternate: +, -, +, - $\\ldots$", font_size=24)
        )
        group.arrange(DOWN, aligned_edge=LEFT)
        group.next_to(observe, DOWN, aligned_edge=LEFT)
        group.shift(RIGHT*0.5)
        self.add(group)

        # taylor series of cos(x)
        tex_kw = dict(font_size=36, t2c={"x": YELLOW})
        tex = R"\cos x = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n}}{(2n)!}"        
        equation = get_formula_and_rect(tex, tex_kw, corner_radius=0.08)
        equation.shift(DOWN*2)
        self.add(equation)

class VisualizationCosX(Template):
    title = "Visualization of $\\cos(x)$"
    page_no = 8

    def construct(self):
        self.embed()
        # Setup
        axes = Axes(
            (-2 * PI, 2 * PI, PI/2), (-3, 3),
            width=6, height=4,
            axis_config=dict(
                tick_size=0.05,
            )
        )
        axes.shift(UP)
        self.add(axes)

        graph_ = axes.get_graph(lambda x: np.cos(x))
        graph_.set_stroke(BLUE, 2)
        graph_label = Tex("y = 1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + \\frac{x^8}{8!} - \\frac{x^{10}}{10!}", t2c=dict(x=YELLOW), font_size=19)
        graph_label.next_to(axes.y_axis.get_top(), RIGHT, aligned_edge=UP)

        def taylor_cos(x, n_terms):
            result = 0
            for k in range(n_terms):
                term = ((-1)**k * x**(2*k)) / math.factorial(2*k)
                result += term
            return result

        label = Tex("\\cos(x) = 1 - \\frac{x^2}{2!} + \\frac{x^4}{4!} - \\frac{x^6}{6!} + \\frac{x^8}{8!} - \\frac{x^{10}}{10!}", t2c=dict(x=YELLOW), font_size=24)
        label.set_flat_stroke(False)
        label.shift(DOWN*2.5)
        self.add(label, graph_label["y ="][0])

        # taylor series of cos(x)
        tex_kw = dict(font_size=36, t2c={"x": YELLOW})
        tex = R"\cos x = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n}}{(2n)!}"
        equ = Tex(tex, **tex_kw)
        equ.shift(2*DOWN)

        rect = SurroundingRectangle(equ)
        rect.set_stroke(WHITE, 1.5)
        rect.set_fill("#191919", 1.0)
        rect.round_corners(0.05)

        graphs = VGroup()
        for i in range(1, 7):
            graph = axes.get_graph(lambda x, i=i: taylor_cos(x, i))
            graph.set_stroke(YELLOW, 2)
            graphs.add(graph)
        self.play(ShowCreation(graph_, run_time=2, rate_func=linear))
        self.play(ShowCreation(graphs[0]), Write(graph_label["1"][0]), run_time=2)
        curr = graphs[0]
        for graph, term in zip(graphs[1:], ["- \\frac{x^2}{2!}", "+ \\frac{x^4}{4!}", "- \\frac{x^6}{6!}", "+ \\frac{x^8}{8!}", "- \\frac{x^{10}}{10!}"]):
            self.play(
                ReplacementTransform(curr, graph),
                ReplacementTransform(label[term][0].copy(), graph_label[term][0]),
                rate_func=linear,
                run_time=2
            )
            self.wait(1.0)
            curr = graph
        # Last
        self.play(
            LaggedStart(
                ReplacementTransform(curr, graph_, time_span=(0.5, 1)),
                FadeOut(label, shift=DOWN*0.5),
                DrawBorderThenFill(rect),
                TransformMatchingStrings(graph_label, equ),
                lag_ratio=0.1,
                rate_func=linear,
                run_time=2
            )
        )
        self.wait()
