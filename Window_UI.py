# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import random
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from algorithm import Object, ColorOrder, InputOrderCheck


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 200)
        MainWindow.setMinimumSize(QtCore.QSize(600, 200))
        MainWindow.setMaximumSize(QtCore.QSize(600, 200))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ButtonRandom = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ButtonRandom.setGeometry(QtCore.QRect(440, 20, 100, 20))
        self.ButtonRandom.setObjectName("ButtonRandom")
        self.ButtonRandom.clicked.connect(self.on_ButtonRandom_clicked)
        self.Edit_Input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Edit_Input.setGeometry(QtCore.QRect(30, 20, 380, 20))
        self.Edit_Input.setObjectName("Edit_Input")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 60, 16, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 60, 16, 16))
        self.label_2.setObjectName("label_2")
        self.Edit_Output = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Edit_Output.setGeometry(QtCore.QRect(30, 100, 380, 20))
        self.Edit_Output.setObjectName("Edit_Output")
        self.Edit_Output.setReadOnly(True)
        self.ButtonSort = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ButtonSort.setGeometry(QtCore.QRect(220, 60, 100, 20))
        self.ButtonSort.setObjectName("ButtonRandom_2")
        self.ButtonSort.clicked.connect(self.on_ButtonSort_clicked)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 60, 20, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMaxLength(1)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 60, 20, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setMaxLength(1)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 60, 20, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setMaxLength(1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Automiq Sorting"))
        self.ButtonRandom.setText(_translate("MainWindow", "Сгенерировать"))
        self.label.setText(_translate("MainWindow", "<"))
        self.label_2.setText(_translate("MainWindow", "<"))
        self.ButtonSort.setText(_translate("MainWindow", "Отсортировать"))

    # Event на нажатие кнопки 'Отсортировать'
    def on_ButtonSort_clicked(self):
        objects = []
        order = [self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text()]
        check = InputOrderCheck(order)

        for c in self.Edit_Input.text():
            objects.append(Object(c))

        # Проверка на правильность ввода последовательности сортировки(может быть можно было написать это читабельнее)
        if check.check() == "Error: Неверный формат ввода последовательности сортировки":
            # Каждый раз при обработке ошибки писать этот вызов, конечно, не лучшее решение, так как при возможном
            # расширении программы этот код будет занимать много места, это можно было бы исправить создав кастомный
            # MessageBox
            dlg = QMessageBox()
            dlg.setWindowTitle("Ошибка")
            dlg.setText("Error: Неверный формат ввода последовательности сортировки")
            dlg.setIcon(QMessageBox.Icon.Critical)
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.exec()
            return

        # Сортировка
        color_order = ColorOrder(objects, order)
        sorted_objects = color_order.sort()
        if sorted_objects == "Error: Неверный формат ввода данных для сортировки":
            dlg = QMessageBox()
            dlg.setWindowTitle("Ошибка")
            dlg.setText("Error: Неверный формат ввода данных для сортировки")
            dlg.setIcon(QMessageBox.Icon.Critical)
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.exec()
            return

        # Вывод
        output = ""
        for obj in sorted_objects:
            output += obj.color
        self.Edit_Output.setText(output)

    # Константа(последовательность цветов не имеет значения)
    INDEXCOLOR = ["з", "с", "к"]

    # Event на нажатие кнопки 'Сгенерировать'
    def on_ButtonRandom_clicked(self):
        # Генерация поля ввода
        str = ""
        for c in range(0, random.randint(5, 20), 1):
            str += self.INDEXCOLOR[random.randint(0, len(self.INDEXCOLOR)-1)]

        self.Edit_Input.setText(str)

        # Генерация полей последовательности сортировки
        self.lineEdit.setText(self.INDEXCOLOR[random.randint(0, len(self.INDEXCOLOR)-1)])

        while True:
            temp = self.INDEXCOLOR[random.randint(0, len(self.INDEXCOLOR)-1)]
            if temp != self.lineEdit.text():
                self.lineEdit_2.setText(temp)
                break

        while True:
            temp = self.INDEXCOLOR[random.randint(0, len(self.INDEXCOLOR)-1)]
            if temp != self.lineEdit_2.text() and temp != self.lineEdit.text():
                self.lineEdit_3.setText(temp)
                break


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
