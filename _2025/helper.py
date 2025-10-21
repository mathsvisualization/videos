from manimlib import *

class Template(InteractiveScene):
    title = ""
    page_no = 1
    def setup(self):
        super().setup()
        template = get_post_template(self.title, self.page_no)
        template[-2].set_fill(border_width=0.35)
        self.add(template)
        self.template = template

def get_post_template(text: str, post_no: str | int) -> VGroup:
    logo = Tex(r"\left< \phi\right>", font_size=24).set_color(PURPLE_A)
    logo.to_edge(UL, buff=0.25)
    logo.set_backstroke(BLACK, 3)
    v_line = Line(UP, DOWN, stroke_width=1.1)
    v_line.set_height(logo.get_height() + MED_SMALL_BUFF)
    v_line.next_to(logo, RIGHT, buff=MED_SMALL_BUFF)

    title = TexText(text, font_size=36)
    title.next_to(v_line, RIGHT)

    h_line = Line(LEFT, RIGHT)
    h_line.set_width(FRAME_WIDTH - 1)
    h_line.set_stroke(width=1.1)
    h_line.to_edge(DOWN, buff=MED_LARGE_BUFF)

    # Page Number Setup
    N_1 = Tex(str(post_no))
    W_1 = N_1.get_width() + 0.1
    H_1 = N_1.get_height() + 0.2        
    radius = max(W_1, H_1) / 2.0
    C = Circle(
        radius=radius,
        stroke_width=1.1,
        fill_color="#191919",
        stroke_color=WHITE,
        fill_opacity=1,
    )       
    N_1.move_to(C.get_center())
    page_no = VGroup(C, N_1)
    page_no.scale(0.5)
    page_no.next_to(h_line, DOWN, buff=SMALL_BUFF)
    return VGroup(logo, v_line, h_line, title, page_no)

def get_formula_and_rect(tex, tex_kw, corner_radius=0.05):
    formula = Tex(str(tex), **tex_kw)
    formula.set_backstroke(BLACK, 3)

    rect = SurroundingRectangle(formula)
    rect.set_stroke(WHITE, 1.5)
    rect.set_fill("#191919", 1,0)
    rect.round_corners(corner_radius)
    return VGroup(rect, formula)

def get_rect(mob, corner_radius=0.05):
    rect = SurroundingRectangle(mob)
    rect.set_stroke(WHITE, 1.5)
    rect.set_fill("#191919", 1.0)
    rect.round_corners(0.05)
    return rect
