from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QColorDialog, QFontDialog, QHBoxLayout
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt
import sys
import json

class MemberItWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.text_edit = QTextEdit(self)
        self.text_edit.setFont(QFont("Arial",12))
        self.text_edit.setStyleSheet("background-color: orange")

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        self.setLayout(layout)

        self.setWindowOpacity(0.9)
        self.setWindowTitle("Note")
        self.resize(200, 200)


        button_layout = QHBoxLayout()
        close_button = QPushButton("Close", self)
        close_button.clicked.connect(self.close_note)
        button_layout.addWidget(close_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def close_note(self):
        self.close()


class MemberItApp(QWidget):
    def __init__(self):
        super().__init__()
        self.notes = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        add_note_btn = QPushButton("New Note", self)
        add_note_btn.clicked.connect(self.add_note)
        layout.addWidget(add_note_btn)

        self.setLayout(layout)
        self.setWindowTitle("Sticky Notes")
        self.resize(400, 300)

    def add_note(self):
        note = MemberItWidget()
        note.show()
        self.notes.append(note)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MemberItApp()
    window.show()
    sys.exit(app.exec())