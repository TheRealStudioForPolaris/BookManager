from PyQt5.QtWidgets import QProgressBar, QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class CustomProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRange(0, 100)
        self.setValue(50)

    def paintEvent(self, event):
        # 使用上下文管理器确保QPainter自动释放
        with QPainter(self) as painter:
            # 绘制背景
            painter.fillRect(self.rect(), Qt.lightGray)

            # 手动绘制进度块（替代SE_ProgressBarChunk）
            progress_width = int(self.width() * self.value() / self.maximum())
            progress_rect = self.rect().adjusted(0, 0, progress_width - self.width(), 0)
            painter.fillRect(progress_rect, Qt.blue)


if __name__ == "__main__":
    app = QApplication([])
    bar = CustomProgressBar()
    bar.show()
    app.exec_()