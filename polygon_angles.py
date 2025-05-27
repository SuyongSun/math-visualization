from manim import *

class PolygonAnglesSum(Scene):
    def construct(self):
        # 标题
        title = Text("多边形内角和", font="SimSun").scale(0.8)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 1. 三角形部分
        triangle = Polygon([-2, -1, 0], [2, -1, 0], [0, 2, 0])
        triangle_text = Text("三角形内角和 = 180°", font="SimSun").scale(0.6)
        triangle_text.next_to(triangle, DOWN)
        
        # 显示三角形
        self.play(Create(triangle))
        self.play(Write(triangle_text))
        
        # 标注三角形的角度
        angles = VGroup()
        dots = VGroup()
        vertices = triangle.get_vertices()
        for i in range(3):
            # 创建两条线段，用于构建角度
            line1 = Line(vertices[i], vertices[(i-1)%3])
            line2 = Line(vertices[i], vertices[(i+1)%3])
            angle = Angle(
                line1, line2,
                radius=0.5,
                color=YELLOW
            )
            angles.add(angle)
            dot = Dot(vertices[i])
            dots.add(dot)
        
        self.play(Create(angles), Create(dots))
        self.wait(1)

        # 2. 四边形部分
        self.play(
            FadeOut(triangle), 
            FadeOut(angles), 
            FadeOut(dots),
            FadeOut(triangle_text)
        )

        # 创建四边形
        square = Polygon(
            [-2, -1, 0], [2, -1, 0], 
            [1, 2, 0], [-1, 2, 0],
            color=BLUE
        )
        square_text = Text("四边形内角和 = 360°", font="SimSun").scale(0.6)
        square_text.next_to(square, DOWN)

        self.play(Create(square))
        
        # 画出对角线，展示可以分成两个三角形
        diagonal = Line(square.get_vertices()[0], square.get_vertices()[2])
        diagonal_text = Text("分成两个三角形\n2 × 180° = 360°", font="SimSun").scale(0.5)
        diagonal_text.next_to(square, RIGHT)

        self.play(Create(diagonal))
        self.play(Write(diagonal_text))
        self.play(Write(square_text))
        self.wait(1)

        # 3. 五边形部分
        self.play(
            FadeOut(square), 
            FadeOut(diagonal),
            FadeOut(diagonal_text),
            FadeOut(square_text)
        )

        # 创建正五边形
        pentagon = RegularPolygon(5, color=GREEN)
        pentagon.scale(2)
        pentagon_text = Text("五边形内角和 = 540°", font="SimSun").scale(0.6)
        pentagon_text.next_to(pentagon, DOWN)

        self.play(Create(pentagon))

        # 从一个顶点到其他顶点画线，展示可以分成三个三角形
        diagonals = VGroup()
        center = pentagon.get_center()
        vertices = pentagon.get_vertices()
        for i in range(2, 4):
            diagonal = Line(vertices[0], vertices[i])
            diagonals.add(diagonal)

        diagonal_text = Text("分成三个三角形\n3 × 180° = 540°", font="SimSun").scale(0.5)
        diagonal_text.next_to(pentagon, RIGHT)

        self.play(Create(diagonals))
        self.play(Write(diagonal_text))
        self.play(Write(pentagon_text))
        self.wait(1)

        # 4. 推广到n边形
        self.play(
            FadeOut(pentagon),
            FadeOut(diagonals),
            FadeOut(diagonal_text),
            FadeOut(pentagon_text)
        )

        # 创建公式
        tex_template = TexTemplate()
        tex_template.add_to_preamble(r'\usepackage{ctex}')
        tex_template.add_to_preamble(r'\usepackage{amsmath}')
        
        formula = MathTex(
            r"\text{n边形内角和} = (n-2) \times 180^\circ",
            tex_template=tex_template
        ).scale(1)
        explanation = Text(
            "n边形可以分成(n-2)个三角形\n每个三角形的内角和是180°", 
            font="SimSun"
        ).scale(0.6)
        
        formula.shift(UP)
        explanation.next_to(formula, DOWN)

        self.play(Write(formula))
        self.play(Write(explanation))
        self.wait(2)

        # 最后的总结
        final_box = SurroundingRectangle(formula, color=YELLOW)
        self.play(Create(final_box))
        self.wait(2)