from manim import *

class DistributiveLawV2(Scene):
    def construct(self):
        # 创建坐标系
        grid = NumberPlane(
            x_range=[0, 8, 1],
            y_range=[0, 5, 1],
            background_line_style={"stroke_color": GREY, "stroke_opacity": 0.6},
            axis_config={"include_numbers": True}
        ).scale(0.9)
        self.play(Create(grid))
        
        # 添加坐标轴标签
        x_label = Text("Length", color=BLUE, font_size=32).next_to(grid.x_axis, RIGHT, buff=0.3)
        y_label = Text("Width", color=GREEN, font_size=32).next_to(grid.y_axis, UP, buff=0.3)
        self.play(Write(x_label), Write(y_label))
        
        # 定义参数
        a, b, c = 3, 2, 1
        print(f'坐标校验: rect_full位置={grid.c2p(0,0,0)} 尺寸={a}x{b+c} 实际宽度={(b+c)*grid.get_x_unit_size()}')
        # 创建初始矩形
        rect_full = Rectangle(height=a, width=b+c, fill_opacity=0.3, color=PURPLE)
        rect_full.move_to(grid.c2p(0, 0, 0), DL)
        
        # 初始公式
        formula = MathTex(f"a\\times({b}+{c}) = {a*(b+c)}", color=PURPLE, font_size=36).to_edge(UP)
        self.play(Create(rect_full), Write(formula))
        
        # 创建左右子矩形（提前初始化）
        rect_left = Rectangle(height=a, width=b, fill_opacity=0.3, color=BLUE).move_to(grid.c2p(0, 0, 0), DL)
        rect_right = Rectangle(height=a, width=c, fill_opacity=0.3, color=RED).move_to(grid.c2p(b, 0, 0), DL)

        # 分割动画
        split_line = DashedLine(
            start=grid.c2p(b, 0, 0),
            end=grid.c2p(b, a, 0),
            color=YELLOW
        )
        print(f'Debug坐标: 分割线起点={grid.c2p(b,0,0)} 终点={grid.c2p(b,a,0)}')
        
        # 在正确位置创建标注
        brace_a = Brace(rect_left, LEFT)
        label_a = MathTex("a = ", f"{a}").next_to(brace_a, LEFT)
        
        self.play(Create(split_line))
        
        # 公式变换
        formula_expanded = MathTex(f"{a}\\times{b} + {a}\\times{c} = {a*b + a*c}").set_color_by_tex_to_color({
            "a\times b": BLUE,
            "a\times c": RED
        }).to_edge(UP)
        self.play(
            Transform(formula, formula_expanded),
            FadeOut(rect_full),
            FadeIn(VGroup(rect_left, rect_right)),
            GrowFromCenter(brace_a),
            Write(label_a),
            # 移除重复的标注动画
            run_time=1.5
        )
        
        # 删除重复的标注动画代码块（原54-62行）
        
        
        # 添加数值标注
        brace_b = Brace(rect_left, DOWN)
        label_b = MathTex("b = ", f"{b}").next_to(brace_b, DOWN)
        brace_c = Brace(rect_right, DOWN)
        label_c = MathTex("c = ", f"{c}").next_to(brace_c, DOWN)
        self.play(
            GrowFromCenter(brace_b), Write(label_b),
            GrowFromCenter(brace_c), Write(label_c),
            run_time=1.2
        )
        self.wait(2)