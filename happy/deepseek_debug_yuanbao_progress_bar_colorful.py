import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QProgressBar,
                             QVBoxLayout, QWidget, QPushButton, QSlider)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QLinearGradient, QColor


class SegmentedProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.segments = []  # 存储颜色分段：[开始%, 结束%, 颜色]
        self.setStyleSheet("""
            QProgressBar {
                border: 2px solid #c0c0c0;
                border-radius: 8px;
                background: #f8f8f8;
                text-align: center;
                font-weight: bold;
            }
        """)

    def add_segment(self, start, end, color):
        """添加新的颜色分段"""
        if 0 <= start < end <= 100:
            self.segments.append((start, end, color))

    def paintEvent(self, event):
        # 使用上下文管理器确保QPainter正确释放
        with QPainter(self) as painter:
            # 获取当前值占范围的百分比
            value_percent = (self.value() - self.minimum()) * 100.0 / (self.maximum() - self.minimum())

            # 绘制基础背景
            painter.fillRect(self.rect(), QColor(240, 240, 240))

            # 绘制总进度背景
            bg_rect = self.rect().adjusted(2, 2, -2, -2)
            painter.fillRect(bg_rect, QColor(220, 220, 220))

            # 计算当前进度宽度（转换为整数）
            progress_width = int(bg_rect.width() * value_percent / 100)
            progress_rect = bg_rect.adjusted(0, 0, progress_width - bg_rect.width(), 0)

            # 绘制各分段（确保使用整数坐标）
            for start, end, color in self.segments:
                # 计算分段位置（转换为整数）
                segment_start = int(bg_rect.width() * start / 100)
                segment_end = int(bg_rect.width() * min(end, value_percent) / 100)

                if segment_end > segment_start:
                    # 创建分段矩形区域（使用整数坐标）
                    segment_rect = progress_rect.adjusted(
                        segment_start, 0,
                        segment_end - bg_rect.width(), 0
                    )

                    # 创建渐变效果
                    gradient = QLinearGradient(
                        segment_rect.topLeft(),
                        segment_rect.bottomRight()
                    )
                    gradient.setColorAt(0, QColor(color).lighter(130))
                    gradient.setColorAt(1, QColor(color))

                    # 绘制分段
                    painter.fillRect(segment_rect, gradient)

            # 绘制文本
            painter.setPen(Qt.black)
            painter.drawText(self.rect(), Qt.AlignCenter,
                             f"{self.value()}%")


class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('分段式进度条演示')
        self.setGeometry(100, 100, 500, 300)

        # 创建主组件
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        # 创建进度条
        self.progress_bar = SegmentedProgressBar()
        self.progress_bar.setRange(0, 100)

        # 添加颜色分段
        self.progress_bar.add_segment(0, 30, '#FF4136')  # 红色：0-30%
        self.progress_bar.add_segment(30, 70, '#FFB700')  # 橙色：30-70%
        self.progress_bar.add_segment(70, 100, '#2ECC40')  # 绿色：70-100%

        layout.addWidget(self.progress_bar)

        # 添加滑块控制
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.valueChanged.connect(self.progress_bar.setValue)
        layout.addWidget(self.slider)

        # 添加控制按钮
        self.reset_btn = QPushButton('重置 (0%)')
        self.reset_btn.clicked.connect(lambda: self.slider.setValue(0))
        layout.addWidget(self.reset_btn)

        self.mid_btn = QPushButton('中段 (50%)')
        self.mid_btn.clicked.connect(lambda: self.slider.setValue(50))
        layout.addWidget(self.mid_btn)

        self.complete_btn = QPushButton('完成 (100%)')
        self.complete_btn.clicked.connect(lambda: self.slider.setValue(100))
        layout.addWidget(self.complete_btn)

        # 初始化滑块值
        self.slider.setValue(25)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DemoWindow()
    window.show()
    sys.exit(app.exec_())