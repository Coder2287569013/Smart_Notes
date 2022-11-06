from PyQt5.QtWidgets import QApplication
from smart import *
import json 

notes = {
    "Ласкаво просимо!": {
        "text": "Це программа для створення заміток...",
        "tegs": ["інструкція", "про программу"]
    }
}

with open("notes.json", "w", encoding="utf-8") as file:
    json.dump(notes, file)

app = QApplication([])

win = Ui_Form()
win.setupUi(win)
win.show()
app.exec_()