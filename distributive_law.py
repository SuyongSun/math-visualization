from manim import *

class DistributiveLaw(Scene):
    def construct(self):
        # 复用中文LaTeX配置
        tex_template = TexTemplate(
            documentclass=r"\documentclass{article}",
            tex_compiler="pdflatex",
            output_format=".pdf"
        )
        tex_template.add_to_preamble(r"""
            \usepackage{amsmath}
            \usepackage{amssymb}
        """)

        # 创建坐标系
        grid = NumberPlane(
            x_range=[0, 8, 1],
            y_range=[0, 5, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 2,
                "stroke_opacity": 0.8
            },
            axis_config={
                "stroke_width": 2,
                "include_numbers": True
            }
        )
        self.play(Create(grid))

        # 添加坐标轴标签
        config.tex_template = tex_template
        x_label = Text("Length", color=BLUE, font_size=36).next_to(grid.x_axis, RIGHT, buff=0.3)
        y_label = Text("Width", color=GREEN, font_size=36).next_to(grid.y_axis, UP, buff=0.3)
        self.play(Write(x_label), Write(y_label))

        # 初始矩形 (a=3, b+c=2+1)
        a, b, c = 3, 2, 1
        # 精确生成完整矩形
        rect_full = Rectangle(
            height=a,
            width=b+c,
            color=WHITE,
            fill_opacity=0.5
        ).move_to(grid.c2p(0, 0, 0), DL)
        
        # 提前创建a的标注
        brace_a = Brace(rect_full, LEFT)
        label_a = MathTex(r"a = ", f"{a}").next_to(brace_a, LEFT)
        
        # 公式显示
        formula = MathTex(r"a \times (b + c)").to_edge(UP)
        area_full = MathTex(f"{a}", r"\times", f"{b+c}", "=", f"{a*(b+c)}").next_to(rect_full, UP, buff=0.3)
        self.play(Create(rect_full), Write(formula), Write(area_full))
        self.wait()

        # 分割动画
        line = DashedLine(
            grid.c2p(b,0),
            grid.c2p(b,a),
            color=YELLOW
        )
        self.play(Create(line))
        
        # 创建两个分块
        # 精确生成分块矩形
        rect_left = Rectangle(
            height=a,
            width=b,
            color=BLUE,
            fill_opacity=0.3
        ).move_to(grid.c2p(0, 0, 0), DL)
        
        rect_right = Rectangle(
            height=a,
            width=c,
            color=RED,
            fill_opacity=0.3
        ).move_to(grid.c2p(b, 0, 0), DL)
        
        # 公式展开
        formula_expanded = MathTex(r"a \times b + a \times c").to_edge(UP)
        area_left = MathTex(f"{a}", r"\times", f"{b}", "=", f"{a*b}").next_to(rect_left, LEFT, buff=0.3)
        area_right = MathTex(f"{a}", r"\times", f"{c}", "=", f"{a*c}").next_to(rect_right, RIGHT, buff=0.3)
        # 添加面积对比动画
        self.play(
            Transform(rect_full, rect_left),
            Transform(formula, formula_expanded),
            FadeIn(rect_right),
            run_time=1.5
        )
        self.play(
            area_full.animate.become(VGroup(area_left, area_right)),
            run_time=1.5
        )
        self.wait(2)

        # 数值标注
        brace_a = Brace(rect_left, LEFT)
        brace_b = Brace(rect_left, DOWN)
        brace_c = Brace(rect_right, DOWN)
        
        # 动态绑定数值标签
        label_a = MathTex(r"a = ", f"{a}").next_to(rect_left, LEFT)
        label_b = MathTex(r"b = ", f"{b}").next_to(brace_b, DOWN)
        label_c = MathTex(r"c = ", f"{c}").next_to(brace_c, DOWN)
        
        self.play(
            GrowFromCenter(brace_a),
            Write(label_a),
            GrowFromCenter(brace_b),
            Write(label_b),
            GrowFromCenter(brace_c),
            Write(label_c)
        )
        self.wait(3)