import sys
from PyQt5 import QtWidgets, uic, QtCore
import numpy as np
import serial
import time
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("graph.ui", self)
        self.graph = self.findChild(QtWidgets.QGraphicsView, 'graphicsView')
        self.graph2 = self.findChild(QtWidgets.QGraphicsView, 'graphicsView_2')

        self.start = self.findChild(QtWidgets.QPushButton, 'start')
        self.pause = self.findChild(QtWidgets.QPushButton, 'pause')

        self.daire1_0 = self.findChild(QtWidgets.QLabel, 'daire1_0')
        self.daire1_1 = self.findChild(QtWidgets.QLabel, 'daire1_1')
        self.daire1_2 = self.findChild(QtWidgets.QLabel, 'daire1_2')
        self.daire1_3 = self.findChild(QtWidgets.QLabel, 'daire1_3')
        self.daire1_4 = self.findChild(QtWidgets.QLabel, 'daire1_4')
        self.daire1_5 = self.findChild(QtWidgets.QLabel, 'daire1_5')
        self.daire1_6 = self.findChild(QtWidgets.QLabel, 'daire1_6')
        self.daire1_7 = self.findChild(QtWidgets.QLabel, 'daire1_7')
        self.daire1_8 = self.findChild(QtWidgets.QLabel, 'daire1_8')
        self.daire1_9 = self.findChild(QtWidgets.QLabel, 'daire1_9')
        self.daire1_10 = self.findChild(QtWidgets.QLabel, 'daire1_10')
        self.daire1_11 = self.findChild(QtWidgets.QLabel, 'daire1_11')
        self.daire1_12 = self.findChild(QtWidgets.QLabel, 'daire1_12')
        self.daire1_13 = self.findChild(QtWidgets.QLabel, 'daire1_13')
        self.daire1_14 = self.findChild(QtWidgets.QLabel, 'daire1_14')
        self.daire1_sebeked = self.findChild(QtWidgets.QLabel, 'daire1_sebeke')
        self.daire1_paneld = self.findChild(QtWidgets.QLabel, 'daire1_panel')
        self.daire1_faturad = self.findChild(QtWidgets.QLabel, 'daire1_fatura')

        self.daire2_0 = self.findChild(QtWidgets.QLabel, 'daire2_0')
        self.daire2_1 = self.findChild(QtWidgets.QLabel, 'daire2_1')
        self.daire2_2 = self.findChild(QtWidgets.QLabel, 'daire2_2')
        self.daire2_3 = self.findChild(QtWidgets.QLabel, 'daire2_3')
        self.daire2_4 = self.findChild(QtWidgets.QLabel, 'daire2_4')
        self.daire2_5 = self.findChild(QtWidgets.QLabel, 'daire2_5')
        self.daire2_6 = self.findChild(QtWidgets.QLabel, 'daire2_6')
        self.daire2_7 = self.findChild(QtWidgets.QLabel, 'daire2_7')
        self.daire2_8 = self.findChild(QtWidgets.QLabel, 'daire2_8')
        self.daire2_9 = self.findChild(QtWidgets.QLabel, 'daire2_9')
        self.daire2_10 = self.findChild(QtWidgets.QLabel, 'daire2_10')
        self.daire2_11 = self.findChild(QtWidgets.QLabel, 'daire2_11')
        self.daire2_12 = self.findChild(QtWidgets.QLabel, 'daire2_12')
        self.daire2_13 = self.findChild(QtWidgets.QLabel, 'daire2_13')
        self.daire2_14 = self.findChild(QtWidgets.QLabel, 'daire2_14')
        self.daire2_sebeked = self.findChild(QtWidgets.QLabel, 'daire2_sebeke')
        self.daire2_paneld = self.findChild(QtWidgets.QLabel, 'daire2_panel')
        self.daire2_faturad = self.findChild(QtWidgets.QLabel, 'daire2_fatura')

        self.daire1_0.setText('320000 kW')
        self.daire1_senaryo = np.loadtxt("daire1.txt")
        self.daire2_senaryo = np.loadtxt("daire2.txt")
        self.isimler = ["Laptop Computer", "LED TV", "Fridge", "Dishwasher", "Washing Machine", "Heather",
                        "Oven", "Vacuum Cleaner", "Gas Water Heater", "Air Condition",
                        "Internet Router", "Phone Charger", "Florescent Lamp", "LED Lamb", "Iron"]
        self.daire1_enerji_tuketimi = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.daire2_enerji_tuketimi = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cihazlarin_gucleri = [18.0, 9.8, 4.4, 51.0, 30.3, 250.0, 250.0, 75.0,
                                   50.0, 108.0, 1.0, 2.4, 9.2, 4.8, 260.0]
        self.enerji_temp1 = 0
        self.enerji_temp2 = 0
        self.daire1_anlik_enerji = []
        self.daire1_anlik_enerji.append(0)
        self.daire2_anlik_enerji = []
        self.daire2_anlik_enerji.append(0)
        self.daire1_toplam_enerji = []
        self.daire1_toplam_enerji.append(self.enerji_temp1)
        self.daire2_toplam_enerji = []
        self.daire2_toplam_enerji.append(self.enerji_temp2)

        self.graph.setTitle("Toplam Enerji Tüketimi")
        self.graph.setLabel('left', 'kWatt')
        self.graph.setLabel('bottom', 'Saniye (10 sn = 1 saat)')

        self.graph2.setTitle("Anlık Enerji Tüketimi")
        self.graph2.setLabel('left', 'Watt')
        self.graph2.setLabel('bottom', 'Saniye (10 sn = 1 saat)')

        self.graph.plotItem.showGrid(True, True, 1.0)
        self.graph2.plotItem.showGrid(True, True, 1.0)

        self.timeArray = []
        self.time = 0
        self.timeArray.append(self.time)

        self.daire1_sebeke = "0"
        self.daire1_panel = "0"
        self.daire2_sebeke = "0"
        self.daire2_panel = "0"
        self.daire1_fatura = 0
        self.daire2_fatura = 0
        self.flag = False

        self.start.clicked.connect(self.startF)
        self.pause.clicked.connect(self.pauseF)

    def startF(self):
        self.flag = True

    def pauseF(self):
        self.flag = False

    def textleriGuncelle(self):
        self.daire1_0.setText(str(format(round(self.daire1_enerji_tuketimi[0], 2))) + " W")
        self.daire1_1.setText(str(format(round(self.daire1_enerji_tuketimi[1], 2))) + " W")
        self.daire1_2.setText(str(format(round(self.daire1_enerji_tuketimi[2], 2))) + " W")
        self.daire1_3.setText(str(format(round(self.daire1_enerji_tuketimi[3], 2))) + " W")
        self.daire1_4.setText(str(format(round(self.daire1_enerji_tuketimi[4], 2))) + " W")
        self.daire1_5.setText(str(format(round(self.daire1_enerji_tuketimi[5], 2))) + " W")
        self.daire1_6.setText(str(format(round(self.daire1_enerji_tuketimi[6], 2))) + " W")
        self.daire1_7.setText(str(format(round(self.daire1_enerji_tuketimi[7], 2))) + " W")
        self.daire1_8.setText(str(format(round(self.daire1_enerji_tuketimi[8], 2))) + " W")
        self.daire1_9.setText(str(format(round(self.daire1_enerji_tuketimi[9], 2))) + " W")
        self.daire1_10.setText(str(format(round(self.daire1_enerji_tuketimi[10], 2))) + " W")
        self.daire1_11.setText(str(format(round(self.daire1_enerji_tuketimi[11], 2))) + " W")
        self.daire1_12.setText(str(format(round(self.daire1_enerji_tuketimi[12], 2))) + " W")
        self.daire1_13.setText(str(format(round(self.daire1_enerji_tuketimi[13], 2))) + " W")
        self.daire1_14.setText(str(format(round(self.daire1_enerji_tuketimi[14], 2))) + " W")
        self.daire1_sebeked.setText(self.daire1_sebeke + " W")
        self.daire1_paneld.setText(self.daire1_panel + " W")
        self.daire1_faturad.setText(str(format(round(self.daire1_fatura, 2))) + " ₺")

        self.daire2_0.setText(str(format(round(self.daire2_enerji_tuketimi[0], 2))) + " W")
        self.daire2_1.setText(str(format(round(self.daire2_enerji_tuketimi[1], 2))) + " W")
        self.daire2_2.setText(str(format(round(self.daire2_enerji_tuketimi[2], 2))) + " W")
        self.daire2_3.setText(str(format(round(self.daire2_enerji_tuketimi[3], 2))) + " W")
        self.daire2_4.setText(str(format(round(self.daire2_enerji_tuketimi[4], 2))) + " W")
        self.daire2_5.setText(str(format(round(self.daire2_enerji_tuketimi[5], 2))) + " W")
        self.daire2_6.setText(str(format(round(self.daire2_enerji_tuketimi[6], 2))) + " W")
        self.daire2_7.setText(str(format(round(self.daire2_enerji_tuketimi[7], 2))) + " W")
        self.daire2_8.setText(str(format(round(self.daire2_enerji_tuketimi[8], 2))) + " W")
        self.daire2_9.setText(str(format(round(self.daire2_enerji_tuketimi[9], 2))) + " W")
        self.daire2_10.setText(str(format(round(self.daire2_enerji_tuketimi[10], 2))) + " W")
        self.daire2_11.setText(str(format(round(self.daire2_enerji_tuketimi[11], 2))) + " W")
        self.daire2_12.setText(str(format(round(self.daire2_enerji_tuketimi[12], 2))) + " W")
        self.daire2_13.setText(str(format(round(self.daire2_enerji_tuketimi[13], 2))) + " W")
        self.daire2_14.setText(str(format(round(self.daire2_enerji_tuketimi[14], 2))) + " W")
        self.daire2_sebeked.setText(self.daire2_sebeke + " W")
        self.daire2_paneld.setText(self.daire2_panel + " W")
        self.daire2_faturad.setText(str(format(round(self.daire2_fatura, 2))) + " ₺")

    def guncelle(self):
        index = int(self.time / 10)

        for i in range(15):
            if int(self.daire1_senaryo[i][index]) == 1:
                self.daire1_enerji_tuketimi[i] += self.cihazlarin_gucleri[i]
            if int(self.daire2_senaryo[i][index]) == 1:
                self.daire2_enerji_tuketimi[i] += self.cihazlarin_gucleri[i]
        for i in range(15):
            self.enerji_temp1 += self.daire1_enerji_tuketimi[i]
            self.enerji_temp2 += self.daire2_enerji_tuketimi[i]

        self.enerji_temp1 /= 1000
        self.enerji_temp2 /= 1000
        self.daire1_toplam_enerji.append(self.enerji_temp1)
        self.daire2_toplam_enerji.append(self.enerji_temp2)
        self.daire1_anlik_enerji.append(
            self.daire1_toplam_enerji[int(self.time)] - self.daire1_toplam_enerji[int(self.time) - 1])
        self.daire2_anlik_enerji.append(
            self.daire2_toplam_enerji[int(self.time)] - self.daire2_toplam_enerji[int(self.time) - 1])
        self.timeArray.append(self.time)

    def update(self):
        # ARDUNIO DAN TIME I OKU VE self.time a setle

        if(self.flag):
            data = arduino.readline()
            data = data.decode("utf-8")
            if data != "":
                data = data.split('*')
                self.time = int(data[0])
                self.daire1_sebeke = data[1]
                self.daire1_panel = data[2]
                self.daire2_sebeke = data[3]
                self.daire2_panel = data[4]
                self.daire1_fatura = int(self.daire1_sebeke.split('.')[0]) * 0.0004 + int(
                    self.daire1_panel.split('.')[0]) * 0.0002
                self.daire2_fatura = int(self.daire2_sebeke.split('.')[0]) * 0.0004 + int(
                    self.daire2_panel.split('.')[0]) * 0.0002
            self.guncelle()
            self.textleriGuncelle()

            self.graph.plot(self.timeArray, self.daire1_toplam_enerji, pen=(255, 0, 0), clear=True)
            self.graph.plot(self.timeArray, self.daire2_toplam_enerji, pen=(0, 255, 0), name="Green curve")

            self.graph2.plot(self.timeArray, self.daire1_anlik_enerji, pen=(255, 0, 0), clear=True)
            self.graph2.plot(self.timeArray, self.daire2_anlik_enerji, pen=(0, 255, 0), name="Green curve")

            QtCore.QTimer.singleShot(1000, self.update)
        else:
            self.graph.plot(self.timeArray, self.daire1_toplam_enerji, pen=(255, 0, 0), clear=True)
            self.graph.plot(self.timeArray, self.daire2_toplam_enerji, pen=(0, 255, 0), name="Green curve")

            self.graph2.plot(self.timeArray, self.daire1_anlik_enerji, pen=(255, 0, 0), clear=True)
            self.graph2.plot(self.timeArray, self.daire2_anlik_enerji, pen=(0, 255, 0), name="Green curve")
            QtCore.QTimer.singleShot(1000, self.update)


if __name__ == "__main__":
    arduino = serial.Serial('COM4', 115200, timeout=.1)

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.update()
    app.exec_()
