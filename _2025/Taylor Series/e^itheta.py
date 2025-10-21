from manim_imports_ext import *
sys.path.append("D:/Visualization/")
from helper import *

class IntroductionToEtoITheta(Template):
    title = "Euler's Formula"
    page_no = 1

    def construct(self):
        self.embed()
        # Equation
        taylor = TexText(R"Why $e^{i\theta} =\; ???$", t2c={"x": YELLOW, R"\theta": GREEN})
        taylor.set_y(2.8)

        underline = Underline(taylor, stretch_factor=1.2)
        underline.set_stroke(BLUE, width=[0, 2, 2, 2, 2, 0])
        self.add(taylor, underline)

        tex_config = dict(font_size=36, t2c={R"\theta": GREEN})
        raw_equation = R"e^{i \theta} = \cos(\theta) + i \sin(\theta)"
        equation = get_formula_and_rect(raw_equation, tex_config, corner_radius=0.05)
        self.add(equation)

        # Other Examples
        morty = Mortimer(mode="thinking")
        morty.scale(0.6)
        morty.next_to(self.template[-3].get_end(), UL, buff=SMALL_BUFF)
        morty.set_color(PURPLE_B)
        self.add(morty)

        bubble = morty.get_bubble(R"$e^{i \pi} = -1$ ?", bubble_type=SpeechBubble, math_mode=True)
        bubble.scale(0.6)
        bubble.pin_to(morty, False)
        morty.look_at(equation)
        self.add(bubble)

class TheTaylorSeriesOFEtoTheiTheta(Template):
    title = "Taylor Series"
    page_no = 2

    def construct(self):
        self.embed()
        # Taylor Series
        kw = dict(font_size=36, t2c={R"\theta": GREEN, "x": YELLOW})
        title = TexText("The Taylor Series for $e^{i\\theta}$", **kw)
        title.next_to(self.template[-2], DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)

        underline = Underline(title, buff=-0.01)
        underline.set_stroke(BLUE, width=[0, 2, 2, 2, 0])

        self.add(underline, title)

        # Substitues
        tex_kw = dict(font_size=24, t2c={R"\theta": GREEN, "x": YELLOW})
        substitues = TexText(R"We simply substitute $x = i\theta$ into the series\\ for $e^{x}$: ", **tex_kw, alignment=R"\flushleft")
        substitues.next_to(title, DOWN, aligned_edge=LEFT)
        self.add(substitues)

        # Series
        series = Tex(R"e^{i \theta} &= 1 + (i \theta) + \frac{(i \theta)^2}{2!} + \frac{(i \theta)^3}{3!} + \frac{(i \theta)^4}{4!} + \frac{(i \theta)^5}{5!} + \cdots", **tex_kw)
        series.next_to(substitues, DOWN, buff=MED_LARGE_BUFF)
        series.set_x(0)
        self.add(series)

        # Simplify
        simplify = TexText("Simplify the Powers of $i$: ", **kw)
        simplify.next_to(series, DOWN, buff=MED_LARGE_BUFF - 0.1)
        simplify.match_x(substitues, LEFT)
        self.add(simplify)

        # Key
        propertyy = TexText("The key to simplifying this is to use the property $i^2 = -1$", **tex_kw)
        propertyy.next_to(simplify, DOWN, aligned_edge=LEFT)
        self.add(propertyy)

        # Solve i
        solve = Tex(R"""
            (i \theta)^1 &= i \theta \\
            (i \theta)^2 &= i^2 \theta^2 = (-1) \theta^2 \\
            (i \theta)^3 &= i^2 \cdot i \cdot \theta^3 = (-1) \cdot i \cdot \theta^3 = -i \theta^3 \\
            (i \theta)^4 &= (i^2)^2 \theta^4 = (-1)^2 \theta^4 = (1) \theta^4 \\
            (i \theta)^5 &= (i^4) \cdot i \cdot \theta^5 = (1) \cdot i \cdot \theta^5 = i \theta^5
        """, **tex_kw)
        solve.next_to(propertyy, DOWN, aligned_edge=LEFT)
        self.add(solve)

        # Notice
        notice = TexText(R"Do you see the pattern? The powers of $i$ cycle every \\4 steps: i, -1, -i, 1, i, -1, -i, 1, \ldots", **tex_kw, alignment=R"\flushleft")
        notice.next_to(solve, DOWN, aligned_edge=LEFT)
        self.add(notice)

        bullets = VGroup(
            Tex("\\bullet", font_size=24)
            for _ in range(2)
        )
        bullets[0].next_to(substitues, LEFT)
        bullets[1].next_to(propertyy, LEFT)
        self.add(bullets)

class SolveTaylorSeries(Template):
    title = "Taylor Series"
    page_no = 3

    def construct(self):
        self.embed()
        # Pulg
        kw = dict(font_size=36, t2c={R"\theta": GREEN, "x": YELLOW})
        tex_kw = dict(font_size=24, t2c={R"\theta": GREEN, "x": YELLOW})
        plug = TexText("Now, plug these back into the series:", **tex_kw)
        plug.next_to(self.template[-2], DOWN, aligned_edge=LEFT)
        self.add(plug)

        # series
        series = Tex(R"e^{i \theta} &= 1 + i \theta + \frac{(-1) \theta^2}{2!} + \frac{(-i) \theta^3}{3!} + \frac{(1) \theta^4}{4!} + \frac{i \theta^5}{5!} + \cdots", **tex_kw)
        series.next_to(plug, DOWN)
        series.set_x(0)
        self.add(series)

        # finalpart
        final_part = Tex(R"e^{i \theta} &= 1 + i \theta - \frac{\theta^2}{2!} - i \frac{\theta^3}{3!} + \frac{\theta^4}{4!} + i \frac{\theta^5}{5!} + \cdots", **tex_kw)
        final_part.next_to(series, DOWN, aligned_edge=LEFT)
        self.add(final_part)

        # Group
        group = TexText(R"Group Real and Imaginary Terms:", **tex_kw)
        group.next_to(final_part, DOWN, buff=MED_LARGE_BUFF)
        group.match_x(plug, LEFT)
        self.add(group)

        # Real and Imaginary Part
        real_imag = TexText(R"Now, we separate the terms without $i$ (real parts) and \\with $i$ (imaginary parts):", **tex_kw, alignment=R"\flushleft")
        real_imag.next_to(group, DOWN)
        real_imag.match_x(series, LEFT)
        self.add(real_imag)

        # Bullet form
        real_and_imag = BulletedList(
            R"Real terms:  $1, -\dfrac{\theta^2}{2!}, \dfrac{\theta^4}{4!}, -\dfrac{\theta^6}{6!}, \cdots$",
            R"Imaginary terms:  $i \theta, -i \dfrac{\theta^3}{3!}, i \dfrac{\theta^5}{5!}, -i \dfrac{\theta^7}{7!}, \ldots$",
            buff=SMALL_BUFF,
            **tex_kw
        )
        real_and_imag.next_to(real_imag, DOWN, aligned_edge=LEFT)
        self.add(real_and_imag)

        # Expantion Become
        expansion = Tex(R"e^{i \theta} &= \left( 1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \frac{\theta^6}{6!} + \cdots \right) + i \left( \theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \frac{\theta^7}{7!} + \cdots \right)", **tex_kw)
        expansion.next_to(real_and_imag, DOWN)
        expansion.set_x(0)
        self.add(expansion)

        # Brace
        real_brace = Brace(expansion[R"1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \frac{\theta^6}{6!} + \cdots"][0], DOWN)
        real_content = real_brace.get_tex(R"\text{Real Parts}", font_size=24)
        self.add(real_brace, real_content)

        imag_brace = Brace(expansion[R"i \left( \theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \frac{\theta^7}{7!} + \cdots \right)"][0], DOWN)
        imag_content = imag_brace.get_tex(R"\text{Imaginary Parts}", font_size=24)
        self.add(imag_brace, imag_content)

        # Bullets
        bullets = VGroup(
            Tex(R"\bullet", font_size=24)
            for _ in range(2)
        )
        for bullet, label in zip(bullets, [plug, group]):
            bullet.next_to(label, LEFT)
        self.add(bullets)

class PuttingSinXandCosX(Template):
    title = "Euler's Formula"
    page_no = 4

    def construct(self):
        self.embed()
        # Recognize
        kw = dict(font_size=36, t2c={R"\theta": GREEN, "x": YELLOW})
        tex_kw = dict(font_size=24, t2c={R"\theta": GREEN, "x": YELLOW})
        recognize = TexText("Recognize the Taylor Series for Cosine and Sine", **tex_kw)
        recognize.next_to(self.template[-2], DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        self.add(recognize)

        # cos and sin
        cos_label = TexText("The Taylor series for $\\cos(\\theta)$: ", **tex_kw)
        cos_label.next_to(recognize, DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        self.add(cos_label)

        cos = Tex(R"\cos \theta = 1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \frac{\theta^6}{6!} + \cdots", **tex_kw)
        cos.next_to(cos_label, DOWN)
        cos.set_x(0)
        self.add(cos)

        sin_label = TexText("The Taylor series for $\\sin(\\theta)$:", **tex_kw)
        sin_label.next_to(cos, DOWN, buff=MED_LARGE_BUFF)
        sin_label.match_x(cos_label, LEFT)
        self.add(sin_label)

        sin = Tex(R"\sin \theta = \theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \frac{\theta^7}{7!} + \cdots", **tex_kw)
        sin.next_to(sin_label, DOWN)
        sin.set_x(0)
        self.add(sin)

        # Expantion Become
        expansion = Tex(R"e^{i \theta} &= \left( 1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \frac{\theta^6}{6!} + \cdots \right) + i \left( \theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \frac{\theta^7}{7!} + \cdots \right)", **tex_kw)
        expansion.next_to(sin, DOWN)
        expansion.set_x(0)
        self.add(expansion)

        # Brace
        real_brace = Brace(expansion[R"1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \frac{\theta^6}{6!} + \cdots"][0], DOWN)
        real_content = real_brace.get_tex(R"\cos(\theta)", **tex_kw)
        self.add(real_brace, real_content)

        imag_brace = Brace(expansion[R"\theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \frac{\theta^7}{7!} + \cdots"][0], DOWN)
        imag_content = imag_brace.get_tex(R"\sin(\theta)", **tex_kw)
        self.add(imag_brace, imag_content)

        raw_equation = R"e^{i \theta} = \cos(\theta) + i \sin(\theta)"
        equation = get_formula_and_rect(raw_equation, tex_kw, corner_radius=0.05)
        equation.scale(1.5)
        equation.next_to(expansion, DOWN, buff=LARGE_BUFF+SMALL_BUFF)
        self.add(equation)

        # Bullets
        bullets = VGroup(
            Tex(R"\bullet", font_size=24)
            for _ in range(2)
        )
        for bullet, label in zip(bullets, [cos_label, sin_label]):
            bullet.next_to(label, LEFT)
        self.add(bullets)

class FinalFormOFEulersExample(Template):
    title = "Euler's Formula"
    page_no = 5

    def construct(self):
        self.embed()
        # Start
        kw = dict(font_size=18, t2c={R"\theta": GREEN})
        tex_kw = dict(font_size=18, t2c={R"\theta": GREEN})
        start = TexText(R"""
            \section*{Intuition and the Complex Plane}
                What does this formula mean? It provides a brilliant way to represent complex numbers.
            \begin{itemize}
                \item Any complex number can be represented as a point on a 2D plane (the \textbf{complex plane}), with a \textbf{real part} (x-axis) and an \textbf{imaginary part} (y-axis).                
                \item Euler's Formula,
                \[
                    e^{i\theta} = \cos(\theta) + i\sin(\theta),
                \]
                describes a point on the \textbf{unit circle} in the complex plane.
                
                \item The real part of this point is $\cos(\theta)$, and the imaginary part is $\sin(\theta)$.
                
                \item As $\theta$ increases, the point $e^{i\theta}$ \textbf{traces a circle} of radius 1 around the origin.
            \end{itemize}
            So, $e^{i\theta}$ is not just an abstract algebraic expression; it's a \textbf{rotation} in the complex plane.
        """, **tex_kw, alignment=R"\flushleft", isolate=["Intuition and the Complex Plane"])
        start.next_to(self.template[-2], DOWN, aligned_edge=LEFT)

        start_underline = Underline(start["Intuition and the Complex Plane"][0], buff=-0.001)
        start_underline.set_stroke(BLUE, width=[0, 2, 2, 2, 0])
        self.add(start_underline, start)


        example = TexText(R"""
            \section*{A Special Case: Euler's Identity}
            If we plug $\theta = \pi$ into Euler's Formula, we get:
            \[
            e^{i\pi} = \cos(\pi) + i\sin(\pi) = -1 + i(0) = -1
            \]
            Rewriting this gives the famous \textbf{Euler's Identity:}
            \[
            \fbox{$e^{i\pi} + 1 = 0$}
            \]
            This identity is celebrated because it links the five most fundamental constants in mathematics --- 
            $e$, $i$, $\pi$, $1$, and $0$ --- in a single, elegant equation.
        """, **kw, alignment=R"\flushleft", isolate=["A Special Case: Euler's Identity"])
        example.next_to(start, DOWN, aligned_edge=LEFT)

        example_underline = Underline(example["A Special Case: Euler's Identity"][0], buff=-0.001)
        example_underline.set_stroke(BLUE, width=[0, 2, 2, 2, 0])
        self.add(example_underline, example)
