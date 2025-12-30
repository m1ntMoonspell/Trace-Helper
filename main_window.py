from PySide6.QtWidgets import (QPushButton,QFileDialog,
                               QMessageBox,QApplication,QVBoxLayout,
                               QLabel,QDialog)
import csv,os
from pathlib import Path


class MyWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.creat_subwidgets()
        self.setWindowTitle("Trace Helper")

    def creat_subwidgets(self):
        self.file_button = QPushButton("Select...",self)
        self.file_button.clicked.connect(self.open_files)
        self.slice_button = QPushButton("Slice...",self)
        self.slice_button.clicked.connect(self.slice_phrase)
        self.label = QLabel("All Rights Reserved" \
        "<a href='https://github.com/m1ntMoonspell?tab=repositories'>@m1nt</a>",
        self)
        self.label.setOpenExternalLinks(True)
        layout = QVBoxLayout(self)
        layout.addWidget(self.file_button)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def slice_phrase(self):
        

    def open_files(self):
        fileName,_ = QFileDialog.getOpenFileName(self)
        suffix = os.path.splitext(".")[1]
        if fileName and suffix == ".csv":
            pass
        elif fileName and suffix != ".csv":
            QMessageBox.critical(self,"Error","please choose trace sheet")
        else:
            pass

if __name__ == "__main__":
    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()