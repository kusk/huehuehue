#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, getopt
from PyQt4 import QtGui, QtCore
from phue import Bridge

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def show_controls(self, lamp, brightness, hue, saturation, count):
        btn1_left = 10 + (count * 100)
        sld_left = 15 + (count * 100)
        btn1 = QtGui.QPushButton(lamp, self)
        btn1.move(btn1_left, 10)
        btn1.setToolTip('Turn lamp <b>' + lamp + '</b> on/off')
        btn1.clicked.connect(self.set_lamp_state)

        #brightness label
        brightness_label = QtGui.QLabel("Brightness", self)
        brightness_label.move(10, 40)

        #Brightness slider
        brightness_slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        brightness_slider.setFocusPolicy(QtCore.Qt.NoFocus)
        brightness_slider.setToolTip('Brightness controller for lamp: <b>' + lamp + '</b>')
        brightness_slider.setRange(0, 254)
        brightness_slider.setValue(brightness)
        brightness_slider.setGeometry(sld_left, 60, 90, 30)
        brightness_slider.sliderReleased.connect(lambda: self.set_lamp_brightness(lamp))

        #Hue label
        hue_label = QtGui.QLabel("Hue", self)
        hue_label.move(10, 80)

        #Hue slider
        hue_slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        hue_slider.setFocusPolicy(QtCore.Qt.NoFocus)
        hue_slider.setToolTip('Hue controller for lamp: <b>' + lamp + '</b>')
        hue_slider.setRange(0, 65535)
        hue_slider.setValue(hue)
        hue_slider.setGeometry(sld_left, 100, 90, 30)
        hue_slider.sliderReleased.connect(lambda: self.set_lamp_hue(lamp))

        #Saturation label
        saturation_label = QtGui.QLabel("Saturation", self)
        saturation_label.move(10, 120)

        #Hue slider
        saturation_slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        saturation_slider.setFocusPolicy(QtCore.Qt.NoFocus)
        saturation_slider.setToolTip('Saturation controller for lamp: <b>' + lamp + '</b>')
        saturation_slider.setRange(0, 254)
        saturation_slider.setValue(saturation)
        saturation_slider.setGeometry(sld_left, 140, 90, 30)
        saturation_slider.sliderReleased.connect(lambda: self.set_lamp_saturation(lamp))


    def initUI(self):
        global b
        b = Bridge("192.168.0.17")
        b.connect()
        count = 0
        for l in b.lights:
            self.show_controls(l.name, l.brightness, l.hue, l.saturation, count)
            count += 1
        self.statusBar()
        self.setGeometry(100, 400, 320, 185)
        self.setWindowTitle('hueqt')
        self.show()



    def set_lamp_state(self):
        sender = self.sender()
        if b.get_light(str(sender.text()), 'on'):
            self.statusBar().showMessage(sender.text() + ' is off')
            b.set_light(str(sender.text()), 'on', False)
        else:
            self.statusBar().showMessage(sender.text() + ' is on')
            b.set_light(str(sender.text()), 'on', True)

    def set_lamp_brightness(self, value):
        sender = self.sender()
        b.set_light(value, 'bri', sender.value())

    def set_lamp_hue(self, value):
        sender = self.sender()
        b.set_light(value, 'hue', sender.value())

    def set_lamp_saturation(self, value):
        sender = self.sender()
        b.set_light(value, 'sat', sender.value())

    def check_lamp_id(id):
        if id.isdigit():
            return int(id)
        else:
            return id


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()