from manim import *

class ChickenRabbitCage(Scene):
    def construct(self):
        # 配置中文LaTeX模板（解决中文编译问题）
        tex_template = TexTemplate(
            tex_compiler="xelatex",
            output_format=".pdf"
        )
        tex_template.add_to_preamble(r"\usepackage{ctex}")
        config.tex_template = tex_template

        # 问题描述
        # 在construct方法中修改以下部分：
        
        # 原问题描述保持顶部位置
        problem = Text('鸡兔同笼：共有8个头，26只脚，问鸡兔各几只？', font_size=36).to_edge(UP)
        
        # 定义右侧信息面板元素
        assume_explanation = Text("假设所有都是鸡：", font_size=28, color=BLUE)
        chicken_legs = MathTex("2 \\times 8 = 16", color=YELLOW)
        rabbit_legs = MathTex("4 \\times 5 = 20", color=GREEN)
        leg_diff = MathTex("26 - 16 = 10", color=RED)
        
        # 创建右侧信息面板
        info_panel = VGroup(
            assume_explanation,
            chicken_legs,
            leg_diff,
            rabbit_legs
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.8).to_edge(RIGHT, buff=1)  # 调整元素顺序为：假设→鸡腿数→腿差→兔腿数
        
        # 主推导流程使用VGroup组织
        # 使用Text对象显示中文
        assume = Text("假设全是鸡 ⇒", font_size=32, color=BLUE)
        # 分离数学公式和中文文本
        diff_math = MathTex("26 - 16 = 10", color=RED)
        diff_text = Text("条腿差", font_size=28, color=RED).next_to(diff_math, RIGHT)
        # 拆分数学计算和中文说明
        rabbit_math = MathTex("10 \\div 2 = 5", color=GREEN)
        rabbit_text = Text("只兔", font_size=28, color=GREEN).next_to(rabbit_math, RIGHT)
        rabbit_num = VGroup(rabbit_math, rabbit_text)

        derivation = VGroup(
            assume,
            VGroup(diff_math, diff_text),
            rabbit_num
        ).arrange(DOWN, buff=0.6).shift(LEFT*0.2)  # 增加行间距，减少左移量，优化布局
        
        # 调整动画时序（示例修改）
        # 分步显示动画元素
        self.play(FadeIn(problem), run_time=0.5)
        self.wait(0.3)
        self.play(Write(assume), run_time=1)  # 展示假设步骤
        self.play(FadeIn(info_panel[0]), run_time=0.8)  # 显示假设说明
        self.play(Write(info_panel[1]), run_time=1)  # 显示鸡的腿数计算（2×8=16）
        self.wait(0.5)
        self.play(Write(info_panel[2]), run_time=1)  # 显示腿差计算（26-16=10）
        self.wait(0.5)
        self.play(Write(info_panel[3]), run_time=1)  # 显示兔的腿数计算（4×5=20）
        
        # 计算鸡的数量并展示结果
        chicken_num = 8 - 5
        # 调整结果位置避免遮挡
        result = VGroup(
            MathTex(f"{chicken_num}", color=PURPLE),
            Text("只鸡", font_size=28, color=PURPLE),
            MathTex("+", color=PURPLE),
            MathTex("5", color=PURPLE),
            Text("只兔", font_size=28, color=PURPLE)
        ).arrange(RIGHT, aligned_edge=DOWN, buff=0.2).next_to(derivation, DOWN, buff=1.5).shift(LEFT*0.3)  # 调整位置避免遮挡
        self.play(Write(result))
        self.wait(2)