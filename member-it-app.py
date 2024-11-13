from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QColorDialog, QFontDialog
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt
import sys
import json

class MemberItWidget(QWidget):
    def __init__(self):
        super().__init__()


class MemberItApp(QWidget):
    def __init__(self):
        super().__init__()
        self.notes = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MemberItApp()
    window.show()
    sys.exit(app.exec())