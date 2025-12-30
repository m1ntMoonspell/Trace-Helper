from PySide6.QtWidgets import (QPushButton,QFileDialog,
                               QMessageBox,QApplication,QVBoxLayout,
                               QLabel,QDialog)
import csv,os
from pathlib import Path
from slice_dialog import SliceDia


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
        layout.addWidget(self.slice_button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.slicer = SliceDia()

    def slice_phrase(self):
        self.slicer.exec()

    def open_files(self):
        fileName,_ = QFileDialog.getOpenFileName(self)
        suffix = os.path.splitext(fileName)[1]
        if fileName and suffix == ".csv":
            self.get_data(fileName)
        elif fileName and suffix != ".csv":
            QMessageBox.critical(self,"Error","please choose trace sheet")
        else:
            pass

    def get_data(self,fileName):
        ID_dict = {}
        lines = Path(fileName).read_text(encoding="utf-8").splitlines()
        reader = csv.reader(lines)
        reader_head = next(reader)
        for index,colum in enumerate(reader_head):
            if colum == "ID":
                index_for_ID = int(index)
            if colum == "链接":
                index_for_link = int(index)
            if colum == "所属系统":
                index_for_title = int(index)
            if colum == "负责程序":
                index_for_code = int(index)
            if colum == "负责qa":
                index_for_qa = int(index)

        for row in reader:
            try:
                ID = row[index_for_ID]
                link = row[index_for_link]
                title = row[index_for_title]
                code = row[index_for_code]
                qa = row[index_for_qa]
            except ValueError:
                print(f"Missing for {ID}")
            else:
                ID_dict[ID] = [link,title,code,qa]

        for k,v in ID_dict.copy().items():
            if not v[1] or not v[2] or not v[3]:
                del ID_dict[k]

if __name__ == "__main__":
    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()