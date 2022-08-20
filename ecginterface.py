#!/bin/python3
import csv
import os
import serial
import time
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    directory = 'Data'
    port = '/dev/ttyACM0'

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(551, 397)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 515, 337))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 18, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onCreate)
        self.horizontalLayout_4.addWidget(self.pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(
            18, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_12 = QtWidgets.QPushButton(self.widget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.onTest)
        self.horizontalLayout_5.addWidget(self.pushButton_12)
        spacerItem5 = QtWidgets.QSpacerItem(
            18, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem6 = QtWidgets.QSpacerItem(
            20, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        spacerItem7 = QtWidgets.QSpacerItem(
            20, 18, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.on_click)
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.on_click)
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.on_click)
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.on_click)
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.on_click)
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(
            20, 30, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        spacerItem9 = QtWidgets.QSpacerItem(
            20, 18, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.on_click)
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.on_click)
        self.horizontalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.on_click)
        self.horizontalLayout_3.addWidget(self.pushButton_11)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.on_click)
        self.horizontalLayout_3.addWidget(self.pushButton_10)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.on_click)
        self.horizontalLayout_3.addWidget(self.pushButton_9)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ECG options"))
        self.label.setText(_translate("Form", "Enter Port"))
        self.label_2.setText(_translate("Form", "Sample Name"))
        self.pushButton.setText(_translate("Form", "Connect"))
        self.label_3.setText(_translate("Form", ""))
        self.pushButton_12.setText(_translate("Form", "Test"))
        self.label_6.setText(_translate("Form", ""))
        self.label_4.setText(_translate("Form", "Light Environment"))
        self.pushButton_2.setText(_translate("Form", "Front_L"))
        self.pushButton_3.setText(_translate("Form", "Left_L"))
        self.pushButton_4.setText(_translate("Form", "Right_L"))
        self.pushButton_5.setText(_translate("Form", "Up_L"))
        self.pushButton_6.setText(_translate("Form", "Down_L"))
        self.label_5.setText(_translate("Form", "Dark Environment"))
        self.pushButton_7.setText(_translate("Form", "Front_D"))
        self.pushButton_8.setText(_translate("Form", "Left_D"))
        self.pushButton_11.setText(_translate("Form", "Right_D"))
        self.pushButton_10.setText(_translate("Form", "Up_D"))
        self.pushButton_9.setText(_translate("Form", "Down_D"))

    def on_click(self):
        button = self.widget.sender()
        self.logdata(button.text())

    def onCreate(self):
        if(self.lineEdit.text() != ''):
            self.port = self.lineEdit.text()
        # check the device if it is connected
        try:
            ser = serial.Serial(self.port, 115200, timeout=1)
            time.sleep(2)
            self.label_3.setText("Device detected")
            # device detected
            ser.close()
        except:
            self.label_3.setText('No device on port '+self.port)

    def logdata(self, name):
        text2 = self.lineEdit_2.text()
        if(text2 != ''):
            self.directory = text2
        current_directory = os.getcwd()
        final_directory = os.path.join(
            current_directory, 'Data', self.directory)
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)

        ##file = open(name+".csv", 'w', newline='')
        file = open(os.path.join(
            final_directory, name)+'.csv', 'w', newline='')
        writer = csv.writer(file)
        try:
            arduino = serial.Serial(self.port, 115200, timeout=1)
            time.sleep(1)
            self.label_3.setText("Device detected")
            time.sleep(1)
            arduino.write(bytes('9', 'utf-8'))
        except:
            self.label_3.setText('No device on port '+self.port)
            return

        while True:
            try:
                while (arduino.inWaiting() == 0):  # Wait here until there is data
                    pass  # do nothing

                try:
                    line = arduino.readline().decode().strip()
                except:
                    line = arduino.readline().decode().strip()

                if (line == 'end'):
                    arduino.close()
                    file.close()
                    break
                writer.writerow([line, ])

            except:
                self.label_3.setText('Device disconnected')
                return

    def onTest(self):
        try:
            arduino = serial.Serial(self.port, 115200, timeout=1)
            time.sleep(2)
        except:
            self.label_6.setText('No device on port '+self.port)
            return

        arduino.write(bytes('9', 'utf-8'))
        while True:
            try:
                while (arduino.inWaiting() == 0):  # Wait here until there is data
                    pass  # do nothing

                try:
                    line = arduino.readline().decode().strip()
                except:
                    line = arduino.readline().decode().strip()

                if (line == 'end'):
                    arduino.close()
                    break

                self.label_6.setText(line)

            except:
                self.label_3.setText('Device disconnected')
                return


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
