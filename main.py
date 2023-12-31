import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sqlite3


class Espresso(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.InitUI()
    
    def InitUI(self):
        self.update_table(self.do_query())
    
    def do_query(self, query="SELECT * from coffee"):
        res = ''
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        if 'SELECT' in query:
            res = cur.execute(query).fetchall()
        else:
            cur.execute(query)
            con.commit()
        con.close()
        if res:
            return res

    def update_table(self, data):
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))
        labels = ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса',
                  'цена', 'объем упаковки']
        self.tableWidget.setHorizontalHeaderLabels(labels)
        for row in range(len(data)):
            for column in range(len(data[0])):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(data[row][column])))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    espresso = Espresso()
    espresso.show()
    sys.exit(app.exec())