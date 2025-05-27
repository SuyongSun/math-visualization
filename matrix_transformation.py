from manim import *

class MatrixTransformation(Scene):
    def construct(self):
        # 统一中文LaTeX配置
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

        # 创建原点正方形
        square = Square(side_length=2, color=BLUE)
        square.move_to(ORIGIN).shift(-LEFT - DOWN)

        # 添加网格线
        grid = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )
        
        # 添加坐标轴
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-3, 3, 1],
            axis_config={
                "include_numbers": True,
                "font_size": 24,
                "color": WHITE
            }
        )
        axes.set_aspect_ratio(1.0)
        self.play(Create(grid), Create(axes))
        config.tex_template = tex_template
        x_label = Text("X轴", font="SimHei", color=RED, font_size=36).next_to(axes.x_axis, RIGHT, buff=0.3)
        y_label = Text("Y轴", font="SimHei", color=GREEN, font_size=36).next_to(axes.y_axis, UP, buff=0.3)
        axes.add(x_label, y_label)
        # 旋转变换
        rotation_matrix = np.array([[0, -1], [1, 0]])
        rotation_text = MathTex(r"\text{旋转矩阵: } \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}", tex_template=tex_template)
        rotation_text.shift(LEFT*0.5 + DOWN*0.1)

        # 显示初始状态（最后添加文字层）
        self.play(Create(square))
        self.play(Write(rotation_text))
        self.wait(1)

        # 应用旋转变换
        self.play(
            square.animate.apply_matrix(rotation_matrix),
            run_time=2
        )
        self.wait(2)
        
        # 剪切变换
        shear_matrix = np.array([[1, -0.5], [0, 1]])
        shear_text = MathTex(r"\text{剪切矩阵: } \begin{bmatrix} 1 & -0.5 \\ 0 & 1 \end{bmatrix}", tex_template=tex_template)
        shear_text.shift(LEFT*0.5 + DOWN*0.1)

        self.remove(rotation_text)
        self.play(Write(shear_text))
        self.wait(1)
        
        # 应用剪切变换
        self.play(
            square.animate.apply_matrix(shear_matrix),
            run_time=2
        )
        self.wait(2)
