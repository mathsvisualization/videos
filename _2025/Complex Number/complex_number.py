from manimlib import *
sys.path.append("D:/Visualization/")
from helper import *

class Why90Rotate(Template):
    title = "Complex Number $i$"
    page_no = 1
    def construct(self):
        self.embed()
        # Question ?
        question = TexText("Why does multiplying any complex\\\\ number by $i$ rotate it by $90^\\circ$ ?")
        question.set_width(5)
        question.move_to(2.5 * UP)
        plane = ComplexPlane(
            (-4, 4), (0, 3),
            width=FRAME_WIDTH - 1, height=3,
            background_line_style=dict(
                stroke_width=2,
                stroke_color=GREY_C,
                stroke_opacity=0.5
            )
        )
        plane.add_coordinate_labels(font_size=24)
        plane.next_to(question, DOWN, buff=MED_LARGE_BUFF)

        timesi = Tex("\\times i", font_size=35)
        timesi.next_to(plane.get_bounding_box_point(UR), DL, buff=SMALL_BUFF)

        vector = Vector(RIGHT)
        vector.put_start_and_end_on(plane.c2p(0, 0, 0), plane.c2p(2, 2, 0))

        h_line = Line(plane.c2p(0, 0, 0), plane.c2p(2, 0, 0))
        h_line.set_color(YELLOW)

        v_line = h_line.copy()
        v_line.put_start_and_end_on(plane.c2p(2, 0, 0), plane.c2p(2, 2, 0))
        v_line.set_color(PINK)

        kw = dict(a=YELLOW, b=PINK)
        vect_label = Tex("a + bi", t2c=kw, font_size=24)
        vect_label.next_to(vector, UR, buff=SMALL_BUFF)
        labels = VGroup(
            Tex("a", t2c=kw, font_size=24),
            Tex("bi", t2c=kw, font_size=24)
        )
        for line, label, vect in zip([h_line, v_line], labels, [UP, RIGHT]):
            label.next_to(line, vect)

        new_vect = Vector(RIGHT)
        new_vect.put_start_and_end_on(plane.c2p(0, 0, 0), plane.c2p(-2, 2, 0))

        kw = dict(a=YELLOW, b=PINK)
        new_label = Tex("ai - b", t2c=kw, font_size=24)
        new_label.next_to(new_vect, UL, buff=SMALL_BUFF)

        p1 = new_vect.point_from_proportion(0.05)
        p2 = vector.point_from_proportion(0.05)
        origin = vector.get_start()
        mid_point = origin + np.array([0, 0.41, 0])

        temp_angle = VMobject()
        temp_angle.set_points_as_corners([p1, mid_point, p2])
        self.frame.reorient(0, 0, 0, (0, 0, 0))

        new_v_line = Line(plane.c2p(0, 0, 0), plane.c2p(0, 2, 0))
        new_v_line.set_color(YELLOW)

        new_h_line = Line(plane.c2p(0, 2, 0), plane.c2p(-2, 2, 0))
        new_h_line.set_color(PINK)

        new_labels = VGroup(
            Tex("bi \\cdot i = -b", t2c=kw, font_size=24),
            Tex("ai", t2c=kw, font_size=24),
        )
        for line, label, vect in zip([new_h_line, new_v_line], new_labels, [UP, RIGHT]):
            label.next_to(line, vect)

        elbo = Elbow(angle=45*DEG)
        elbo.replace(temp_angle)

        self.add(question)
        self.add(plane)
        self.add(timesi)
        self.add(vector)
        self.add(h_line)
        self.add(v_line)
        self.add(labels)
        self.add(vect_label)
        self.add(new_vect)
        self.add(new_label)
        self.add(new_v_line)
        self.add(new_h_line)
        self.add(new_labels)
        self.add(elbo)

class ExplainWhyRotate90DEG(Template):
    title = "Complex Number $i$"
    page_no = 2

    def construct(self):
        self.embed()
        # plane
        plane = ComplexPlane(
            (-4, 4), (0, 3),
            width=FRAME_WIDTH - 1, height=3.5,
            background_line_style=dict(
                stroke_width=2,
                stroke_color=GREY_C,
                stroke_opacity=0.5
            )
        )
        plane.add_coordinate_labels(font_size=24)
        plane.next_to(self.template[2], UP)
        plane.shift(UP)
        self.add(plane)

        # Vector
        vector = Vector(RIGHT)
        vector.put_start_and_end_on(plane.c2p(0, 0, 0), plane.c2p(2, 2, 0))

        lines = VGroup(
            Line(LEFT, RIGHT).set_color(color)
            for color in [YELLOW, PINK]
        )
        for line, vec in zip(lines, [(plane.c2p(0, 0, 0), plane.c2p(2, 0, 0)), (plane.c2p(2, 0, 0), plane.c2p(2, 2, 0))]):
            line.put_start_and_end_on(*vec)
        t2c = dict(a=YELLOW, b=PINK)
        aib = Tex("z = a + bi", t2c=t2c, font_size=24)
        aib.next_to(vector, UR, buff=SMALL_BUFF - 0.05)

        self.play(
            GrowArrow(vector),
            Write(aib, time_span=(0, 1.25))
        )
        self.wait()

        # Equations
        aligned_eqs = Tex(
            R"""
            z &= a + bi \\
            zi&= i(a + bi) \\
            zi&= ai + bi \cdot i \quad \therefore i\cdot i = -1\\
            zi&= ai -b
            """,
            font_size=30,
            t2c=t2c
        )
        aligned_eqs.move_to([-1.5, 2.5, 0], ORIGIN)
        aligned_eqs["\\therefore"][0].shift(0.05*UP)
        self.play(
            Write(aligned_eqs, run_time=2)
        )

        labels = VGroup(
            Tex(tex, t2c=t2c, font_size=24)
            for tex in ("a", "bi")
        )
        for label, line, vect in zip(labels, lines, [UP, RIGHT]):
            label.next_to(line, vect)

        multiplier = Tex("\\times i")
        multiplier.next_to(plane.get_bounding_box_point(UR), DL, buff=SMALL_BUFF)

        new_lines = VGroup(
            Line(LEFT, RIGHT).set_color(color)
            for color in [YELLOW, PINK]
        )
        for line, vec in zip(new_lines, [(plane.c2p(0, 0, 0), plane.c2p(0, 2, 0)), (plane.c2p(0, 0, 0), plane.c2p(-2, 0, 0))]):
            line.put_start_and_end_on(*vec)

        new_labels = VGroup(
            Tex(tex, t2c=t2c, font_size=24)
            for tex in ("ai", "bi \\cdot i")
        )
        for label, line, vect in zip(new_labels, new_lines, [RIGHT, UP]):
            label.next_to(line, vect)

        negb = Tex("bi \\cdot i = -b", t2c=t2c, font_size=24)
        negb.next_to(new_lines[1], UP)

        box_negb = SurroundingRectangle(negb, buff=SMALL_BUFF)
        box_negb.set_stroke(PINK, width=2)

        # Play the animation
        self.play(*(
            ShowCreation(line)
            for line in lines
            ),
            *(
                FadeIn(label, shift=shift * 0.5)
                for label, shift in zip(labels, [RIGHT, UP])
            )
        )
        self.wait()
        self.play(
            FadeIn(multiplier, lag_ratio=0.1)
        )
        self.wait()
        self.play(
            TransformFromCopy(
                lines[0], new_lines[0], path_arc=90*DEG
            ),
            ReplacementTransform(
                labels[0].copy(), new_labels[0]["a"][0]
            ),
            ReplacementTransform(
                multiplier["i"][0].copy(), new_labels[0]["i"][0]
            ),
            run_time=2,
        )
        self.wait()
        self.play(
            TransformFromCopy(
                lines[1], new_lines[1], path_arc=90*DEG
            ),
            ReplacementTransform(
                multiplier["i"][0].copy(), new_labels[1]["i"][1]
            ),
            ReplacementTransform(
                labels[1]["bi"][0].copy(), new_labels[1]["bi"][0]
            ),
            FadeIn(new_labels[1]["\\cdot"][0], time_span=(1, 2)),
            run_time=2,
        )
        self.wait()

        # Last
        self.play(
            ReplacementTransform(
                new_labels[1], negb["bi \\cdot i"][0]
            ),
            FadeIn(negb["= -b"][0], shift=RIGHT*0.1),
            VShowPassingFlash(box_negb.copy().set_stroke(width=5), time_width=5, run_time=3),
        )
        self.wait()

        self.play(
            new_lines[1].animate.move_to(plane.c2p(-2, 2, 0), LEFT),
            negb.animate.move_to([-0.875, 0.68493599, 0]),
            run_time=2
        )

        # next play
        rotate_vect = Vector(RIGHT)
        rotate_vect.put_start_and_end_on(plane.c2p(0, 0, 0), plane.c2p(-2, 2, 0))

        rotate_vect_label = Tex("z = ai -b", t2c=t2c, font_size=24)
        rotate_vect_label.next_to(rotate_vect, UL, buff=SMALL_BUFF)

        p1 = rotate_vect.point_from_proportion(0.05)
        p2 = vector.point_from_proportion(0.05)
        origin = vector.get_start()
        mid_point = origin + np.array([0, 0.41, 0])

        temp_angle = VMobject()
        temp_angle.set_points_as_corners([p1, mid_point, p2])
        elbo = Elbow(angle=45*DEG)
        elbo.replace(temp_angle)
        self.play(
            TransformFromCopy(vector, rotate_vect, path_arc=90*DEG),
            Write(rotate_vect_label, time_span=(0, 1.75)),
            run_time=2
        )
        self.play(ShowCreation(elbo))
        self.wait()

        # geo text
        geo_text = TexText(
            "So, multiplying by $i$ moves every point $90^\\circ$ \\\\ anti-clockwise "
            "around the origin.",
            font_size=26,
            color=YELLOW
        ).next_to(plane, DOWN)
        self.play(Write(geo_text, run_time=3))
        self.wait(2)
