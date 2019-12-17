import sys
from PyQt5 import QtWidgets, uic, QtCore
import numpy as np
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget


class Daire1(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi("daire1.ui", self)

        self.countb = self.findChild(QtWidgets.QPushButton, 'countartir')
        self.countb.clicked.connect(self.countArtir)

    def countArtir(self):
        print("test")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("graph.ui", self)
        self.graph = self.findChild(QtWidgets.QGraphicsView, 'graphicsView')
        self.graph2 = self.findChild(QtWidgets.QGraphicsView, 'graphicsView_2')

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


    def textleriGuncelle(self):
        self.daire1_0.setText(str(format(self.daire1_enerji_tuketimi[0])))
        self.daire1_1.setText(str(self.daire1_enerji_tuketimi[1]))
        self.daire1_2.setText(str(self.daire1_enerji_tuketimi[2]))
        self.daire1_3.setText(str(self.daire1_enerji_tuketimi[3]))
        self.daire1_4.setText(str(self.daire1_enerji_tuketimi[4]))
        self.daire1_5.setText(str(self.daire1_enerji_tuketimi[5]))
        self.daire1_6.setText(str(self.daire1_enerji_tuketimi[6]))
        self.daire1_7.setText(str(self.daire1_enerji_tuketimi[7]))
        self.daire1_8.setText(str(self.daire1_enerji_tuketimi[8]))
        self.daire1_9.setText(str(self.daire1_enerji_tuketimi[9]))
        self.daire1_10.setText(str(self.daire1_enerji_tuketimi[10]))
        self.daire1_11.setText(str(self.daire1_enerji_tuketimi[11]))
        self.daire1_12.setText(str(format(round(self.daire1_enerji_tuketimi[12], 2)))+" W")
        self.daire1_13.setText(str(format(round(self.daire1_enerji_tuketimi[13], 2))))
        self.daire1_14.setText(str(self.daire1_enerji_tuketimi[14]))

        self.daire2_0.setText(str(self.daire2_enerji_tuketimi[0]))
        self.daire2_1.setText(str(self.daire2_enerji_tuketimi[1]))
        self.daire2_2.setText(str(self.daire2_enerji_tuketimi[2]))
        self.daire2_3.setText(str(self.daire2_enerji_tuketimi[3]))
        self.daire2_4.setText(str(self.daire2_enerji_tuketimi[4]))
        self.daire2_5.setText(str(self.daire2_enerji_tuketimi[5]))
        self.daire2_6.setText(str(self.daire2_enerji_tuketimi[6]))
        self.daire2_7.setText(str(self.daire2_enerji_tuketimi[7]))
        self.daire2_8.setText(str(self.daire2_enerji_tuketimi[8]))
        self.daire2_9.setText(str(self.daire2_enerji_tuketimi[9]))
        self.daire2_10.setText(str(self.daire2_enerji_tuketimi[10]))
        self.daire2_11.setText(str(self.daire2_enerji_tuketimi[11]))
        self.daire2_12.setText(str(self.daire2_enerji_tuketimi[12]))
        self.daire2_13.setText(str(self.daire2_enerji_tuketimi[13]))
        self.daire2_14.setText(str(self.daire2_enerji_tuketimi[14]))

    def guncelle(self):
        index = int(self.time / 10)

        for i in range(15):
            if int(self.daire1_senaryo[index][i]) == 1:
                self.daire1_enerji_tuketimi[i] += self.cihazlarin_gucleri[i]
            if int(self.daire2_senaryo[index][i]) == 1:
                self.daire2_enerji_tuketimi[i] += self.cihazlarin_gucleri[i]
        for i in range(15):
            self.enerji_temp1 += self.daire1_enerji_tuketimi[i]
            self.enerji_temp2 += self.daire2_enerji_tuketimi[i]

        self.enerji_temp1 /= 1000
        self.enerji_temp2 /= 1000
        self.daire1_toplam_enerji.append(self.enerji_temp1)
        self.daire2_toplam_enerji.append(self.enerji_temp2)
        self.daire1_anlik_enerji.append(self.daire1_toplam_enerji[int(self.time)]-self.daire1_toplam_enerji[int(self.time)-1])
        self.daire2_anlik_enerji.append(self.daire2_toplam_enerji[int(self.time)]-self.daire2_toplam_enerji[int(self.time)-1])
        self.timeArray.append(self.time)
    def update(self):
        self.time += 1
        # ARDUNIO DAN TIME I OKU VE self.time a setle
        self.guncelle()
        self.textleriGuncelle()

        self.graph.plot(self.timeArray, self.daire1_toplam_enerji, pen=(255, 0, 0), clear=True)
        self.graph.plot(self.timeArray, self.daire2_toplam_enerji, pen=(0, 255, 0), name="Green curve")

        self.graph2.plot(self.timeArray, self.daire1_anlik_enerji, pen=(255, 0, 0), clear=True)
        self.graph2.plot(self.timeArray, self.daire2_anlik_enerji, pen=(0, 255, 0), name="Green curve")

        QtCore.QTimer.singleShot(1000, self.update)

    def testClicked(self):
        print("test")
        self.w = Daire1()
        self.w.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.update()
    app.exec_()
    print("finished")
