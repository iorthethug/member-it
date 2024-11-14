from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QColorDialog, QFontDialog, QHBoxLayout, QMenu
from PyQt5.QtGui import QFont, QColor, QMouseEvent, QIcon, QFontDatabase
from PyQt5.QtCore import Qt, QPoint
import sys
import json

class MemberItWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.text_edit = QTextEdit(self)
        self.text_edit.setFont(QFont("Arial",12))
        self.setStyleSheet("""
            QWidget {
                background-color: #FFEB3B;
                border-radius: 10px;
                padding: 5px;
            }
            QTextEdit {
                font-family: "Comic Sans MS";
                font-size: 14px;
                color: #333; 
            }
            QPushButton {
                background-color: #FFC107;
                border: none;
                color: white;
                padding: 4px 8px;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #FFA000;
            }
        """)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        self.setLayout(layout)

        self.setWindowTitle("Note")
        self.resize(200, 200)


        button_layout = QHBoxLayout()

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def close_note(self):
        self.close()

    def minimize_window(self):
        self.showMinimized()

    def mousePressEvent(self, event: QMouseEvent):
        self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event: QMouseEvent):
        delta = QPoint(event.globalPos() - self.old_pos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_pos = event.globalPos()


    def contextMenuEvent(self, event):
        context_menu = QMenu(self)

        close_icon = QIcon(self.style().standardIcon(self.style().SP_TitleBarCloseButton))
        min_icon = QIcon(self.style().standardIcon(self.style().SP_TitleBarMinButton))

        context_menu.setFixedSize(25, 62)

        close_action = context_menu.addAction(close_icon, "")
        close_action.triggered.connect(self.close_note)
        min_action = context_menu.addAction(min_icon, "")
        min_action.triggered.connect(self.minimize_window)

        menu_pos = self.rect().topRight()

        adjusted_pos = QPoint(menu_pos.x()-25, menu_pos.y())
       
        global_pos = self.mapToGlobal(adjusted_pos)

        context_menu.setStyleSheet("""
            QMenu {
                background-color: #FFEB3B;
                padding: 0px;
            }
            QMenu::item {
                font-size: 14px;
                padding: 5px;
                margin-left: 5px;
            }
            QMenu::item:selected {
                background-color: #FFC107;
            }
            QMenu::separator {
                height: 0px;
                margin: 5px 0;
            }
        """)

        print(global_pos)
        context_menu.exec_(global_pos)

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
        self.setWindowTitle("Member It")
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