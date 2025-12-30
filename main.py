from PySide6.QtWidgets import QApplication
from main_window import MyWindow

if __name__ == "__main__":
    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()