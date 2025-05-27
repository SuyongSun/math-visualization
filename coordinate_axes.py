from manim import *

class CoordinateAxesDemo(Scene):
    def construct(self):
        # 继承中文LaTeX配置
        tex_template = TexTemplate(
            documentclass=r"\documentclass[UTF8]{ctexart}",
            tex_compiler="xelatex",
            output_format=".xdv"
        )
        tex_template.add_to_preamble(r"""
            \usepackage{amsmath}
            \usepackage{amssymb}
            \usepackage{ctex}
            \setCJKmainfont{SimHei}
        """)

        # 创建带数字标注的坐标轴
        axes = Axes(
            y_range=[-3, 3, 1],
            x_range=[-6, 6, 1],
            axis_config={
                "include_numbers": True,
                "font_size": 28,
                "color": BLUE,
            },
            tips=False,
        )
        axes.set_aspect_ratio(1.0)
        self.play(Create(axes))
        
        # 添加坐标轴标签
        config.tex_template = tex_template
        x_label = Text("X轴", font="SimHei", color=RED, font_size=36).next_to(axes.x_axis, RIGHT, buff=0.3)
        y_label = Text("Y轴", font="SimHei", color=GREEN, font_size=36).next_to(axes.y_axis, UP, buff=0.3)
        axes.add(x_label, y_label)

        # 动画展示
        self.wait(1)
        
        # 添加单位圆动画
        circle = Circle(radius=1, color=YELLOW).move_to(axes.coords_to_point(0, 0))
        self.play(Create(circle))
        self.wait(1)