from manim import *
import numpy as np

class RotateRectangleScene(Scene):
    def construct(self):
        # 添加坐标系
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            axis_config={"color": WHITE}
        )
        self.play(Create(axes))
        
        # 修正矩形绘制（添加闭合边）
        original_vertices = [
            np.array([0, 0, 0]),
            np.array([2, 0, 0]),
            np.array([2, 1, 0]), 
            np.array([0, 1, 0]),
            np.array([0, 0, 0])  # 闭合图形
        ]
        rect = Polygon(*original_vertices, color=BLUE, fill_opacity=0.3, stroke_width=4)
        self.play(Create(rect))

        # 添加文字说明
        text = Text("Original Rectangle").next_to(rect, UP)
        self.play(Write(text))

        # 定义角度跟踪器
        angle_tracker = ValueTracker(0)

        # 定义更新函数
        # 更新函数增加顶点闭合处理
        def update_rect(mob):
            angle = angle_tracker.get_value()
            new_vertices = []
            for vertex in original_vertices[:4]:  # 使用前四个原始顶点
                x, y = vertex[0], vertex[1]
                new_x = x * np.cos(angle) - y * np.sin(angle)
                new_y = x * np.sin(angle) + y * np.cos(angle)
                new_vertices.append(np.array([new_x, new_y, 0]))
            new_vertices.append(new_vertices[0])  # 添加闭合顶点
            mob.set_points_as_corners(new_vertices)

        rect.add_updater(update_rect)

        # 显示旋转矩阵
        # 修正后的动态矩阵显示（约分后的π分数格式）
        # 显示旋转矩阵（60等分π显示）
        matrix = always_redraw(lambda: MathTex(
            r"\begin{bmatrix}"
            r"\cos\left(\frac{" + str(int(angle_tracker.get_value()/PI*60)) + r"}{60}\pi\right) & "
            r"-\sin\left(\frac{" + str(int(angle_tracker.get_value()/PI*60)) + r"}{60}\pi\right) \\ "
            r"\sin\left(\frac{" + str(int(angle_tracker.get_value()/PI*60)) + r"}{60}\pi\right) & "
            r"\cos\left(\frac{" + str(int(angle_tracker.get_value()/PI*60)) + r"}{60}\pi\right)"
            r"\end{bmatrix}"
        ).to_edge(UP))
        
        self.add(matrix)
        self.play(Write(matrix))

        # 开始旋转
        self.play(angle_tracker.animate.set_value(2 * PI), run_time=4, rate_func=linear)
        self.wait()

        # 移除updater
        rect.remove_updater(update_rect)

        # 清理画面
        self.play(FadeOut(text), FadeOut(matrix))
        self.wait()