# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AVR32-config.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from lxml import etree as ET

import sys

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(873, 613)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.AVR_ATMEGA32_CONFIG = QTabWidget(Form)
        self.AVR_ATMEGA32_CONFIG.setObjectName(u"AVR_ATMEGA32_CONFIG")
        self.AVR_ATMEGA32_CONFIG.setEnabled(True)
        self.AVR_ATMEGA32_CONFIG.setMaximumSize(QSize(16777215, 16777215))
        self.AVR_ATMEGA32_CONFIG.setAcceptDrops(False)
        self.AVR_ATMEGA32_CONFIG.setStyleSheet(u"background-color: rgb(26, 79, 79);\n"
"border-color: rgb(0, 0, 0);\n"
"border-color: rgb(170, 161, 111);\n"
"font: 75 9pt \"Rockwell\";\n"
"color: rgb(218, 197, 144);")
        self.PortA = QWidget()
        self.PortA.setObjectName(u"PortA")
        self.PortA.setEnabled(True)
        self.PortA.setAcceptDrops(False)
        self.BoxA0 = QGroupBox(self.PortA)
        self.BoxA0.setObjectName(u"BoxA0")
        self.BoxA0.setGeometry(QRect(30, 10, 151, 61))
        self.outputA0 = QRadioButton(self.BoxA0)
        self.outputA0.setObjectName(u"outputA0")
        self.outputA0.setGeometry(QRect(10, 20, 82, 17))
        self.inputA0 = QRadioButton(self.BoxA0)
        self.inputA0.setObjectName(u"inputA0")
        self.inputA0.setGeometry(QRect(10, 40, 82, 17))
        self.inputConfidA0 = QGroupBox(self.PortA)
        self.inputConfidA0.setObjectName(u"inputConfidA0")
        self.inputConfidA0.setGeometry(QRect(440, 10, 211, 61))
        self.pul_upA0 = QRadioButton(self.inputConfidA0)
        self.pul_upA0.setObjectName(u"pul_upA0")
        self.pul_upA0.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceA0 = QRadioButton(self.inputConfidA0)
        self.high_impedenceA0.setObjectName(u"high_impedenceA0")
        self.high_impedenceA0.setGeometry(QRect(110, 30, 101, 17))
        self.outputConfigA0 = QGroupBox(self.PortA)
        self.outputConfigA0.setObjectName(u"outputConfigA0")
        self.outputConfigA0.setEnabled(True)
        self.outputConfigA0.setGeometry(QRect(210, 10, 211, 61))
        self.highA0 = QRadioButton(self.outputConfigA0)
        self.highA0.setObjectName(u"highA0")
        self.highA0.setGeometry(QRect(30, 30, 82, 17))
        self.lowA0 = QRadioButton(self.outputConfigA0)
        self.lowA0.setObjectName(u"lowA0")
        self.lowA0.setGeometry(QRect(120, 30, 82, 17))
        self.BoxA1 = QGroupBox(self.PortA)
        self.BoxA1.setObjectName(u"BoxA1")
        self.BoxA1.setGeometry(QRect(30, 80, 151, 61))
        self.outputA1 = QRadioButton(self.BoxA1)
        self.outputA1.setObjectName(u"outputA1")
        self.outputA1.setGeometry(QRect(10, 20, 82, 17))
        self.inputA1 = QRadioButton(self.BoxA1)
        self.inputA1.setObjectName(u"inputA1")
        self.inputA1.setGeometry(QRect(10, 40, 82, 17))
        self.BoxA6 = QGroupBox(self.PortA)
        self.BoxA6.setObjectName(u"BoxA6")
        self.BoxA6.setGeometry(QRect(30, 430, 151, 61))
        self.outputA6 = QRadioButton(self.BoxA6)
        self.outputA6.setObjectName(u"outputA6")
        self.outputA6.setGeometry(QRect(10, 20, 82, 17))
        self.inputA6 = QRadioButton(self.BoxA6)
        self.inputA6.setObjectName(u"inputA6")
        self.inputA6.setGeometry(QRect(10, 40, 82, 17))
        self.BoxA2 = QGroupBox(self.PortA)
        self.BoxA2.setObjectName(u"BoxA2")
        self.BoxA2.setGeometry(QRect(30, 150, 151, 61))
        self.outputA2 = QRadioButton(self.BoxA2)
        self.outputA2.setObjectName(u"outputA2")
        self.outputA2.setGeometry(QRect(10, 20, 82, 17))
        self.inputA2 = QRadioButton(self.BoxA2)
        self.inputA2.setObjectName(u"inputA2")
        self.inputA2.setGeometry(QRect(10, 40, 82, 17))
        self.BoxA3 = QGroupBox(self.PortA)
        self.BoxA3.setObjectName(u"BoxA3")
        self.BoxA3.setGeometry(QRect(30, 220, 151, 61))
        self.outputA3 = QRadioButton(self.BoxA3)
        self.outputA3.setObjectName(u"outputA3")
        self.outputA3.setGeometry(QRect(10, 20, 82, 17))
        self.inputA3 = QRadioButton(self.BoxA3)
        self.inputA3.setObjectName(u"inputA3")
        self.inputA3.setGeometry(QRect(10, 40, 82, 17))
        self.BoxA5 = QGroupBox(self.PortA)
        self.BoxA5.setObjectName(u"BoxA5")
        self.BoxA5.setGeometry(QRect(30, 360, 151, 61))
        self.outputA5 = QRadioButton(self.BoxA5)
        self.outputA5.setObjectName(u"outputA5")
        self.outputA5.setGeometry(QRect(10, 20, 82, 17))
        self.inputA5 = QRadioButton(self.BoxA5)
        self.inputA5.setObjectName(u"inputA5")
        self.inputA5.setGeometry(QRect(10, 40, 82, 17))
        self.BoxA4 = QGroupBox(self.PortA)
        self.BoxA4.setObjectName(u"BoxA4")
        self.BoxA4.setGeometry(QRect(30, 290, 151, 61))
        self.outputA4 = QRadioButton(self.BoxA4)
        self.outputA4.setObjectName(u"outputA4")
        self.outputA4.setGeometry(QRect(10, 20, 82, 17))
        self.inputA4 = QRadioButton(self.BoxA4)
        self.inputA4.setObjectName(u"inputA4")
        self.inputA4.setGeometry(QRect(10, 40, 82, 17))
        self.BoxA7 = QGroupBox(self.PortA)
        self.BoxA7.setObjectName(u"BoxA7")
        self.BoxA7.setGeometry(QRect(30, 500, 151, 61))
        self.outputA7 = QRadioButton(self.BoxA7)
        self.outputA7.setObjectName(u"outputA7")
        self.outputA7.setGeometry(QRect(10, 20, 82, 17))
        self.inputA7 = QRadioButton(self.BoxA7)
        self.inputA7.setObjectName(u"inputA7")
        self.inputA7.setGeometry(QRect(10, 40, 82, 17))
        self.outputConfigA1 = QGroupBox(self.PortA)
        self.outputConfigA1.setObjectName(u"outputConfigA1")
        self.outputConfigA1.setEnabled(True)
        self.outputConfigA1.setGeometry(QRect(210, 80, 211, 61))
        self.highA1 = QRadioButton(self.outputConfigA1)
        self.highA1.setObjectName(u"highA1")
        self.highA1.setGeometry(QRect(30, 30, 82, 17))
        self.lowA1 = QRadioButton(self.outputConfigA1)
        self.lowA1.setObjectName(u"lowA1")
        self.lowA1.setGeometry(QRect(120, 30, 82, 17))
        self.outputConfigA2 = QGroupBox(self.PortA)
        self.outputConfigA2.setObjectName(u"outputConfigA2")
        self.outputConfigA2.setEnabled(True)
        self.outputConfigA2.setGeometry(QRect(210, 150, 211, 61))
        self.highA2 = QRadioButton(self.outputConfigA2)
        self.highA2.setObjectName(u"highA2")
        self.highA2.setGeometry(QRect(30, 30, 82, 17))
        self.lowA2 = QRadioButton(self.outputConfigA2)
        self.lowA2.setObjectName(u"lowA2")
        self.lowA2.setGeometry(QRect(120, 30, 82, 17))
        self.outputConfigA5 = QGroupBox(self.PortA)
        self.outputConfigA5.setObjectName(u"outputConfigA5")
        self.outputConfigA5.setEnabled(True)
        self.outputConfigA5.setGeometry(QRect(210, 360, 211, 61))
        self.highA5 = QRadioButton(self.outputConfigA5)
        self.highA5.setObjectName(u"highA5")
        self.highA5.setGeometry(QRect(30, 30, 82, 17))
        self.lowA5 = QRadioButton(self.outputConfigA5)
        self.lowA5.setObjectName(u"lowA5")
        self.lowA5.setGeometry(QRect(120, 30, 82, 17))
        self.outputConfigA4 = QGroupBox(self.PortA)
        self.outputConfigA4.setObjectName(u"outputConfigA4")
        self.outputConfigA4.setEnabled(True)
        self.outputConfigA4.setGeometry(QRect(210, 290, 211, 61))
        self.highA4 = QRadioButton(self.outputConfigA4)
        self.highA4.setObjectName(u"highA4")
        self.highA4.setGeometry(QRect(30, 30, 82, 17))
        self.lowA4 = QRadioButton(self.outputConfigA4)
        self.lowA4.setObjectName(u"lowA4")
        self.lowA4.setGeometry(QRect(120, 30, 82, 17))
        self.outputConfigA3 = QGroupBox(self.PortA)
        self.outputConfigA3.setObjectName(u"outputConfigA3")
        self.outputConfigA3.setEnabled(True)
        self.outputConfigA3.setGeometry(QRect(210, 220, 211, 61))
        self.highA3 = QRadioButton(self.outputConfigA3)
        self.highA3.setObjectName(u"highA3")
        self.highA3.setGeometry(QRect(30, 30, 82, 17))
        self.lowA3 = QRadioButton(self.outputConfigA3)
        self.lowA3.setObjectName(u"lowA3")
        self.lowA3.setGeometry(QRect(120, 30, 82, 17))
        self.outputConfigA6 = QGroupBox(self.PortA)
        self.outputConfigA6.setObjectName(u"outputConfigA6")
        self.outputConfigA6.setEnabled(True)
        self.outputConfigA6.setGeometry(QRect(210, 430, 211, 61))
        self.highA6 = QRadioButton(self.outputConfigA6)
        self.highA6.setObjectName(u"highA6")
        self.highA6.setGeometry(QRect(30, 30, 82, 17))
        self.lowA6 = QRadioButton(self.outputConfigA6)
        self.lowA6.setObjectName(u"lowA6")
        self.lowA6.setGeometry(QRect(120, 30, 82, 17))
        self.outputConfigA7 = QGroupBox(self.PortA)
        self.outputConfigA7.setObjectName(u"outputConfigA7")
        self.outputConfigA7.setEnabled(True)
        self.outputConfigA7.setGeometry(QRect(210, 500, 211, 61))
        self.highA7 = QRadioButton(self.outputConfigA7)
        self.highA7.setObjectName(u"highA7")
        self.highA7.setGeometry(QRect(30, 30, 82, 17))
        self.lowA7 = QRadioButton(self.outputConfigA7)
        self.lowA7.setObjectName(u"lowA7")
        self.lowA7.setGeometry(QRect(120, 30, 82, 17))
        self.inputConfidA1 = QGroupBox(self.PortA)
        self.inputConfidA1.setObjectName(u"inputConfidA1")
        self.inputConfidA1.setGeometry(QRect(440, 80, 211, 61))
        self.pul_upA1 = QRadioButton(self.inputConfidA1)
        self.pul_upA1.setObjectName(u"pul_upA1")
        self.pul_upA1.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceA1 = QRadioButton(self.inputConfidA1)
        self.high_impedenceA1.setObjectName(u"high_impedenceA1")
        self.high_impedenceA1.setGeometry(QRect(110, 30, 101, 17))
        self.inputConfidA2 = QGroupBox(self.PortA)
        self.inputConfidA2.setObjectName(u"inputConfidA2")
        self.inputConfidA2.setGeometry(QRect(440, 150, 211, 61))
        self.pul_upA2 = QRadioButton(self.inputConfidA2)
        self.pul_upA2.setObjectName(u"pul_upA2")
        self.pul_upA2.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceA2 = QRadioButton(self.inputConfidA2)
        self.high_impedenceA2.setObjectName(u"high_impedenceA2")
        self.high_impedenceA2.setGeometry(QRect(110, 30, 101, 17))
        self.inputConfidA3 = QGroupBox(self.PortA)
        self.inputConfidA3.setObjectName(u"inputConfidA3")
        self.inputConfidA3.setGeometry(QRect(440, 220, 211, 61))
        self.pul_upA3 = QRadioButton(self.inputConfidA3)
        self.pul_upA3.setObjectName(u"pul_upA3")
        self.pul_upA3.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceA3 = QRadioButton(self.inputConfidA3)
        self.high_impedenceA3.setObjectName(u"high_impedenceA3")
        self.high_impedenceA3.setGeometry(QRect(110, 30, 101, 17))
        self.inputConfidA4 = QGroupBox(self.PortA)
        self.inputConfidA4.setObjectName(u"inputConfidA4")
        self.inputConfidA4.setGeometry(QRect(440, 290, 211, 61))
        self.pul_upA4 = QRadioButton(self.inputConfidA4)
        self.pul_upA4.setObjectName(u"pul_upA4")
        self.pul_upA4.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceA4 = QRadioButton(self.inputConfidA4)
        self.high_impedenceA4.setObjectName(u"high_impedenceA4")
        self.high_impedenceA4.setGeometry(QRect(110, 30, 101, 17))
        self.inputConfidA5 = QGroupBox(self.PortA)
        self.inputConfidA5.setObjectName(u"inputConfidA5")
        self.inputConfidA5.setGeometry(QRect(440, 360, 211, 61))
        self.pul_upA5 = QRadioButton(self.inputConfidA5)
        self.pul_upA5.setObjectName(u"pul_upA5")
        self.pul_upA5.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceA5 = QRadioButton(self.inputConfidA5)
        self.high_impedenceA5.setObjectName(u"high_impedenceA5")
        self.high_impedenceA5.setGeometry(QRect(110, 30, 101, 17))
        self.inputConfidA6 = QGroupBox(self.PortA)
        self.inputConfidA6.setObjectName(u"inputConfidA6")
        self.inputConfidA6.setGeometry(QRect(440, 430, 211, 61))
        self.pul_upA6 = QRadioButton(self.inputConfidA6)
        self.pul_upA6.setObjectName(u"pul_upA6")
        self.pul_upA6.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceA6 = QRadioButton(self.inputConfidA6)
        self.high_impedenceA6.setObjectName(u"high_impedenceA6")
        self.high_impedenceA6.setGeometry(QRect(110, 30, 101, 17))
        self.inputConfidA7 = QGroupBox(self.PortA)
        self.inputConfidA7.setObjectName(u"inputConfidA7")
        self.inputConfidA7.setGeometry(QRect(440, 500, 211, 61))
        self.pul_upA7 = QRadioButton(self.inputConfidA7)
        self.pul_upA7.setObjectName(u"pul_upA7")
        self.pul_upA7.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceA7 = QRadioButton(self.inputConfidA7)
        self.high_impedenceA7.setObjectName(u"high_impedenceA7")
        self.high_impedenceA7.setGeometry(QRect(110, 30, 101, 17))
        self.AVR_ATMEGA32_CONFIG.addTab(self.PortA, "")
        self.PortB = QWidget()
        self.PortB.setObjectName(u"PortB")
        self.PortB.setEnabled(True)
        self.PortB.setAcceptDrops(False)
        self.BoxB6 = QGroupBox(self.PortB)
        self.BoxB6.setObjectName(u"BoxB6")
        self.BoxB6.setGeometry(QRect(30, 430, 151, 61))
        self.outputB6 = QRadioButton(self.BoxB6)
        self.outputB6.setObjectName(u"outputB6")
        self.outputB6.setGeometry(QRect(10, 20, 82, 17))
        self.inputB6 = QRadioButton(self.BoxB6)
        self.inputB6.setObjectName(u"inputB6")
        self.inputB6.setGeometry(QRect(10, 40, 82, 17))
        self.BoxB2 = QGroupBox(self.PortB)
        self.BoxB2.setObjectName(u"BoxB2")
        self.BoxB2.setGeometry(QRect(30, 150, 151, 61))
        self.outputB2 = QRadioButton(self.BoxB2)
        self.outputB2.setObjectName(u"outputB2")
        self.outputB2.setGeometry(QRect(10, 20, 82, 17))
        self.inputB2 = QRadioButton(self.BoxB2)
        self.inputB2.setObjectName(u"inputB2")
        self.inputB2.setGeometry(QRect(10, 40, 82, 17))
        self.outputConfigB0 = QGroupBox(self.PortB)
        self.outputConfigB0.setObjectName(u"outputConfigB0")
        self.outputConfigB0.setEnabled(True)
        self.outputConfigB0.setGeometry(QRect(210, 10, 211, 61))
        self.highB0 = QRadioButton(self.outputConfigB0)
        self.highB0.setObjectName(u"highB0")
        self.highB0.setGeometry(QRect(30, 30, 82, 17))
        self.lowB0 = QRadioButton(self.outputConfigB0)
        self.lowB0.setObjectName(u"lowB0")
        self.lowB0.setGeometry(QRect(120, 30, 82, 17))
        self.BoxB5 = QGroupBox(self.PortB)
        self.BoxB5.setObjectName(u"BoxB5")
        self.BoxB5.setGeometry(QRect(30, 360, 151, 61))
        self.outputB5 = QRadioButton(self.BoxB5)
        self.outputB5.setObjectName(u"outputB5")
        self.outputB5.setGeometry(QRect(10, 20, 82, 17))
        self.inputB5 = QRadioButton(self.BoxB5)
        self.inputB5.setObjectName(u"inputB5")
        self.inputB5.setGeometry(QRect(10, 40, 82, 17))
        self.BoxB4 = QGroupBox(self.PortB)
        self.BoxB4.setObjectName(u"BoxB4")
        self.BoxB4.setGeometry(QRect(30, 290, 151, 61))
        self.outputB4 = QRadioButton(self.BoxB4)
        self.outputB4.setObjectName(u"outputB4")
        self.outputB4.setGeometry(QRect(10, 20, 82, 17))
        self.inputB4 = QRadioButton(self.BoxB4)
        self.inputB4.setObjectName(u"inputB4")
        self.inputB4.setGeometry(QRect(10, 40, 82, 17))
        self.inputConfidB2 = QGroupBox(self.PortB)
        self.inputConfidB2.setObjectName(u"inputConfidB2")
        self.inputConfidB2.setGeometry(QRect(440, 150, 211, 61))
        self.pul_upB2 = QRadioButton(self.inputConfidB2)
        self.pul_upB2.setObjectName(u"pul_upB2")
        self.pul_upB2.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceB2 = QRadioButton(self.inputConfidB2)
        self.high_impedenceB2.setObjectName(u"high_impedenceB2")
        self.high_impedenceB2.setGeometry(QRect(110, 30, 101, 17))
        self.outputConfigB3 = QGroupBox(self.PortB)
        self.outputConfigB3.setObjectName(u"outputConfigB3")
        self.outputConfigB3.setEnabled(True)
        self.outputConfigB3.setGeometry(QRect(210, 220, 211, 61))
        self.highB3 = QRadioButton(self.outputConfigB3)
        self.highB3.setObjectName(u"highB3")
        self.highB3.setGeometry(QRect(30, 30, 82, 17))
        self.lowB3 = QRadioButton(self.outputConfigB3)
        self.lowB3.setObjectName(u"lowB3")
        self.lowB3.setGeometry(QRect(120, 30, 82, 17))
        self.inputConfidB6 = QGroupBox(self.PortB)
        self.inputConfidB6.setObjectName(u"inputConfidB6")
        self.inputConfidB6.setGeometry(QRect(440, 430, 211, 61))
        self.pul_upB6 = QRadioButton(self.inputConfidB6)
        self.pul_upB6.setObjectName(u"pul_upB6")
        self.pul_upB6.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceB6 = QRadioButton(self.inputConfidB6)
        self.high_impedenceB6.setObjectName(u"high_impedenceB6")
        self.high_impedenceB6.setGeometry(QRect(110, 30, 101, 17))
        self.outputConfigB5 = QGroupBox(self.PortB)
        self.outputConfigB5.setObjectName(u"outputConfigB5")
        self.outputConfigB5.setEnabled(True)
        self.outputConfigB5.setGeometry(QRect(210, 360, 211, 61))
        self.highB5 = QRadioButton(self.outputConfigB5)
        self.highB5.setObjectName(u"highB5")
        self.highB5.setGeometry(QRect(30, 30, 82, 17))
        self.lowB5 = QRadioButton(self.outputConfigB5)
        self.lowB5.setObjectName(u"lowB5")
        self.lowB5.setGeometry(QRect(120, 30, 82, 17))
        self.BoxB7 = QGroupBox(self.PortB)
        self.BoxB7.setObjectName(u"BoxB7")
        self.BoxB7.setGeometry(QRect(30, 500, 151, 61))
        self.outputB7 = QRadioButton(self.BoxB7)
        self.outputB7.setObjectName(u"outputB7")
        self.outputB7.setGeometry(QRect(10, 20, 82, 17))
        self.inputB7 = QRadioButton(self.BoxB7)
        self.inputB7.setObjectName(u"inputB7")
        self.inputB7.setGeometry(QRect(10, 40, 82, 17))
        self.inputConfidB5 = QGroupBox(self.PortB)
        self.inputConfidB5.setObjectName(u"inputConfidB5")
        self.inputConfidB5.setGeometry(QRect(440, 360, 211, 61))
        self.pul_upB5 = QRadioButton(self.inputConfidB5)
        self.pul_upB5.setObjectName(u"pul_upB5")
        self.pul_upB5.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceB5 = QRadioButton(self.inputConfidB5)
        self.high_impedenceB5.setObjectName(u"high_impedenceB5")
        self.high_impedenceB5.setGeometry(QRect(110, 30, 101, 17))
        self.BoxB3 = QGroupBox(self.PortB)
        self.BoxB3.setObjectName(u"BoxB3")
        self.BoxB3.setGeometry(QRect(30, 220, 151, 61))
        self.outputB3 = QRadioButton(self.BoxB3)
        self.outputB3.setObjectName(u"outputB3")
        self.outputB3.setGeometry(QRect(10, 20, 82, 17))
        self.inputB3 = QRadioButton(self.BoxB3)
        self.inputB3.setObjectName(u"inputB3")
        self.inputB3.setGeometry(QRect(10, 40, 82, 17))
        self.inputConfidB0 = QGroupBox(self.PortB)
        self.inputConfidB0.setObjectName(u"inputConfidB0")
        self.inputConfidB0.setGeometry(QRect(440, 10, 211, 61))
        self.pul_upB0 = QRadioButton(self.inputConfidB0)
        self.pul_upB0.setObjectName(u"pul_upB0")
        self.pul_upB0.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceB0 = QRadioButton(self.inputConfidB0)
        self.high_impedenceB0.setObjectName(u"high_impedenceB0")
        self.high_impedenceB0.setGeometry(QRect(110, 30, 101, 17))
        self.outputConfigB2 = QGroupBox(self.PortB)
        self.outputConfigB2.setObjectName(u"outputConfigB2")
        self.outputConfigB2.setEnabled(True)
        self.outputConfigB2.setGeometry(QRect(210, 150, 211, 61))
        self.highB2 = QRadioButton(self.outputConfigB2)
        self.highB2.setObjectName(u"highB2")
        self.highB2.setGeometry(QRect(30, 30, 82, 17))
        self.lowB2 = QRadioButton(self.outputConfigB2)
        self.lowB2.setObjectName(u"lowB2")
        self.lowB2.setGeometry(QRect(120, 30, 82, 17))
        self.BoxB0 = QGroupBox(self.PortB)
        self.BoxB0.setObjectName(u"BoxB0")
        self.BoxB0.setGeometry(QRect(30, 10, 151, 61))
        self.outputB0 = QRadioButton(self.BoxB0)
        self.outputB0.setObjectName(u"outputB0")
        self.outputB0.setGeometry(QRect(10, 20, 82, 17))
        self.inputB0 = QRadioButton(self.BoxB0)
        self.inputB0.setObjectName(u"inputB0")
        self.inputB0.setGeometry(QRect(10, 40, 82, 17))
        self.BoxB1 = QGroupBox(self.PortB)
        self.BoxB1.setObjectName(u"BoxB1")
        self.BoxB1.setGeometry(QRect(30, 80, 151, 61))
        self.outputB1 = QRadioButton(self.BoxB1)
        self.outputB1.setObjectName(u"outputB1")
        self.outputB1.setGeometry(QRect(10, 20, 82, 17))
        self.inputB1 = QRadioButton(self.BoxB1)
        self.inputB1.setObjectName(u"inputB1")
        self.inputB1.setGeometry(QRect(10, 40, 82, 17))
        self.inputConfidB1 = QGroupBox(self.PortB)
        self.inputConfidB1.setObjectName(u"inputConfidB1")
        self.inputConfidB1.setGeometry(QRect(440, 80, 211, 61))
        self.pul_upB1 = QRadioButton(self.inputConfidB1)
        self.pul_upB1.setObjectName(u"pul_upB1")
        self.pul_upB1.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceB1 = QRadioButton(self.inputConfidB1)
        self.high_impedenceB1.setObjectName(u"high_impedenceB1")
        self.high_impedenceB1.setGeometry(QRect(110, 30, 101, 17))
        self.inputConfidB4 = QGroupBox(self.PortB)
        self.inputConfidB4.setObjectName(u"inputConfidB4")
        self.inputConfidB4.setGeometry(QRect(440, 290, 211, 61))
        self.pul_upB4 = QRadioButton(self.inputConfidB4)
        self.pul_upB4.setObjectName(u"pul_upB4")
        self.pul_upB4.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceB4 = QRadioButton(self.inputConfidB4)
        self.high_impedenceB4.setObjectName(u"high_impedenceB4")
        self.high_impedenceB4.setGeometry(QRect(110, 30, 101, 17))
        self.outputConfigB1 = QGroupBox(self.PortB)
        self.outputConfigB1.setObjectName(u"outputConfigB1")
        self.outputConfigB1.setEnabled(True)
        self.outputConfigB1.setGeometry(QRect(210, 80, 211, 61))
        self.highB1 = QRadioButton(self.outputConfigB1)
        self.highB1.setObjectName(u"highB1")
        self.highB1.setGeometry(QRect(30, 30, 82, 17))
        self.lowB1 = QRadioButton(self.outputConfigB1)
        self.lowB1.setObjectName(u"lowB1")
        self.lowB1.setGeometry(QRect(120, 30, 82, 17))
        self.inputConfidB7 = QGroupBox(self.PortB)
        self.inputConfidB7.setObjectName(u"inputConfidB7")
        self.inputConfidB7.setGeometry(QRect(440, 500, 211, 61))
        self.pul_upB7 = QRadioButton(self.inputConfidB7)
        self.pul_upB7.setObjectName(u"pul_upB7")
        self.pul_upB7.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceB7 = QRadioButton(self.inputConfidB7)
        self.high_impedenceB7.setObjectName(u"high_impedenceB7")
        self.high_impedenceB7.setGeometry(QRect(110, 30, 101, 17))
        self.outputConfigB6 = QGroupBox(self.PortB)
        self.outputConfigB6.setObjectName(u"outputConfigB6")
        self.outputConfigB6.setEnabled(True)
        self.outputConfigB6.setGeometry(QRect(210, 430, 211, 61))
        self.highB6 = QRadioButton(self.outputConfigB6)
        self.highB6.setObjectName(u"highB6")
        self.highB6.setGeometry(QRect(30, 30, 82, 17))
        self.lowB6 = QRadioButton(self.outputConfigB6)
        self.lowB6.setObjectName(u"lowB6")
        self.lowB6.setGeometry(QRect(120, 30, 82, 17))
        self.outputConfigB4 = QGroupBox(self.PortB)
        self.outputConfigB4.setObjectName(u"outputConfigB4")
        self.outputConfigB4.setEnabled(True)
        self.outputConfigB4.setGeometry(QRect(210, 290, 211, 61))
        self.highB4 = QRadioButton(self.outputConfigB4)
        self.highB4.setObjectName(u"highB4")
        self.highB4.setGeometry(QRect(30, 30, 82, 17))
        self.lowB4 = QRadioButton(self.outputConfigB4)
        self.lowB4.setObjectName(u"lowB4")
        self.lowB4.setGeometry(QRect(120, 30, 82, 17))
        self.outputConfigB7 = QGroupBox(self.PortB)
        self.outputConfigB7.setObjectName(u"outputConfigB7")
        self.outputConfigB7.setEnabled(True)
        self.outputConfigB7.setGeometry(QRect(210, 500, 211, 61))
        self.highB7 = QRadioButton(self.outputConfigB7)
        self.highB7.setObjectName(u"highB7")
        self.highB7.setGeometry(QRect(30, 30, 82, 17))
        self.lowB7 = QRadioButton(self.outputConfigB7)
        self.lowB7.setObjectName(u"lowB7")
        self.lowB7.setGeometry(QRect(120, 30, 82, 17))
        self.inputConfidB3 = QGroupBox(self.PortB)
        self.inputConfidB3.setObjectName(u"inputConfidB3")
        self.inputConfidB3.setGeometry(QRect(440, 220, 211, 61))
        self.pul_upB3 = QRadioButton(self.inputConfidB3)
        self.pul_upB3.setObjectName(u"pul_upB3")
        self.pul_upB3.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceB3 = QRadioButton(self.inputConfidB3)
        self.high_impedenceB3.setObjectName(u"high_impedenceB3")
        self.high_impedenceB3.setGeometry(QRect(110, 30, 101, 17))
        self.AVR_ATMEGA32_CONFIG.addTab(self.PortB, "")
        self.PortC = QWidget()
        self.PortC.setObjectName(u"PortC")
        self.PortC.setEnabled(True)
        self.PortC.setAcceptDrops(False)
        self.BoxC6 = QGroupBox(self.PortC)
        self.BoxC6.setObjectName(u"BoxC6")
        self.BoxC6.setGeometry(QRect(30, 430, 151, 61))
        self.outputC6 = QRadioButton(self.BoxC6)
        self.outputC6.setObjectName(u"outputC6")
        self.outputC6.setGeometry(QRect(10, 20, 82, 17))
        self.inputC6 = QRadioButton(self.BoxC6)
        self.inputC6.setObjectName(u"inputC6")
        self.inputC6.setGeometry(QRect(10, 40, 82, 17))
        self.BoxC2 = QGroupBox(self.PortC)
        self.BoxC2.setObjectName(u"BoxC2")
        self.BoxC2.setGeometry(QRect(30, 150, 151, 61))
        self.outputC2 = QRadioButton(self.BoxC2)
        self.outputC2.setObjectName(u"outputC2")
        self.outputC2.setGeometry(QRect(10, 20, 82, 17))
        self.inputC2 = QRadioButton(self.BoxC2)
        self.inputC2.setObjectName(u"inputC2")
        self.inputC2.setGeometry(QRect(10, 40, 82, 17))
        self.outputConfigC0 = QGroupBox(self.PortC)
        self.outputConfigC0.setObjectName(u"outputConfigC0")
        self.outputConfigC0.setEnabled(True)
        self.outputConfigC0.setGeometry(QRect(210, 10, 211, 61))
        self.highC0 = QRadioButton(self.outputConfigC0)
        self.highC0.setObjectName(u"highC0")
        self.highC0.setGeometry(QRect(30, 30, 82, 17))
        self.lowC0 = QRadioButton(self.outputConfigC0)
        self.lowC0.setObjectName(u"lowC0")
        self.lowC0.setGeometry(QRect(120, 30, 82, 17))
        self.BoxC5 = QGroupBox(self.PortC)
        self.BoxC5.setObjectName(u"BoxC5")
        self.BoxC5.setGeometry(QRect(30, 360, 151, 61))
        self.outputC5 = QRadioButton(self.BoxC5)
        self.outputC5.setObjectName(u"outputC5")
        self.outputC5.setGeometry(QRect(10, 20, 82, 17))
        self.inputC5 = QRadioButton(self.BoxC5)
        self.inputC5.setObjectName(u"inputC5")
        self.inputC5.setGeometry(QRect(10, 40, 82, 17))
        self.BoxC4 = QGroupBox(self.PortC)
        self.BoxC4.setObjectName(u"BoxC4")
        self.BoxC4.setGeometry(QRect(30, 290, 151, 61))
        self.outputC4 = QRadioButton(self.BoxC4)
        self.outputC4.setObjectName(u"outputC4")
        self.outputC4.setGeometry(QRect(10, 20, 82, 17))
        self.inputC4 = QRadioButton(self.BoxC4)
        self.inputC4.setObjectName(u"inputC4")
        self.inputC4.setGeometry(QRect(10, 40, 82, 17))
        self.inputConfidC2 = QGroupBox(self.PortC)
        self.inputConfidC2.setObjectName(u"inputConfidC2")
        self.inputConfidC2.setGeometry(QRect(440, 150, 211, 61))
        self.pul_upC2 = QRadioButton(self.inputConfidC2)
        self.pul_upC2.setObjectName(u"pul_upC2")
        self.pul_upC2.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceC2 = QRadioButton(self.inputConfidC2)
        self.high_impedenceC2.setObjectName(u"high_impedenceC2")
        self.high_impedenceC2.setGeometry(QRect(110, 30, 101, 17))
        self.outputConfigC3 = QGroupBox(self.PortC)
        self.outputConfigC3.setObjectName(u"outputConfigC3")
        self.outputConfigC3.setEnabled(True)
        self.outputConfigC3.setGeometry(QRect(210, 220, 211, 61))
        self.highC3 = QRadioButton(self.outputConfigC3)
        self.highC3.setObjectName(u"highC3")
        self.highC3.setGeometry(QRect(30, 30, 82, 17))
        self.lowC3 = QRadioButton(self.outputConfigC3)
        self.lowC3.setObjectName(u"lowC3")
        self.lowC3.setGeometry(QRect(120, 30, 82, 17))
        self.inputConfidC6 = QGroupBox(self.PortC)
        self.inputConfidC6.setObjectName(u"inputConfidC6")
        self.inputConfidC6.setGeometry(QRect(440, 430, 211, 61))
        self.pul_upC6 = QRadioButton(self.inputConfidC6)
        self.pul_upC6.setObjectName(u"pul_upC6")
        self.pul_upC6.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceC6 = QRadioButton(self.inputConfidC6)
        self.high_impedenceC6.setObjectName(u"high_impedenceC6")
        self.high_impedenceC6.setGeometry(QRect(110, 30, 101, 17))
        self.outputConfigC5 = QGroupBox(self.PortC)
        self.outputConfigC5.setObjectName(u"outputConfigC5")
        self.outputConfigC5.setEnabled(True)
        self.outputConfigC5.setGeometry(QRect(210, 360, 211, 61))
        self.highC5 = QRadioButton(self.outputConfigC5)
        self.highC5.setObjectName(u"highC5")
        self.highC5.setGeometry(QRect(30, 30, 82, 17))
        self.lowC5 = QRadioButton(self.outputConfigC5)
        self.lowC5.setObjectName(u"lowC5")
        self.lowC5.setGeometry(QRect(120, 30, 82, 17))
        self.BoxC7 = QGroupBox(self.PortC)
        self.BoxC7.setObjectName(u"BoxC7")
        self.BoxC7.setGeometry(QRect(30, 500, 151, 61))
        self.outputC7 = QRadioButton(self.BoxC7)
        self.outputC7.setObjectName(u"outputC7")
        self.outputC7.setGeometry(QRect(10, 20, 82, 17))
        self.inputC7 = QRadioButton(self.BoxC7)
        self.inputC7.setObjectName(u"inputC7")
        self.inputC7.setGeometry(QRect(10, 40, 82, 17))
        self.inputConfidC5 = QGroupBox(self.PortC)
        self.inputConfidC5.setObjectName(u"inputConfidC5")
        self.inputConfidC5.setGeometry(QRect(440, 360, 211, 61))
        self.pul_upC5 = QRadioButton(self.inputConfidC5)
        self.pul_upC5.setObjectName(u"pul_upC5")
        self.pul_upC5.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceC5 = QRadioButton(self.inputConfidC5)
        self.high_impedenceC5.setObjectName(u"high_impedenceC5")
        self.high_impedenceC5.setGeometry(QRect(110, 30, 101, 17))
        self.BoxC3 = QGroupBox(self.PortC)
        self.BoxC3.setObjectName(u"BoxC3")
        self.BoxC3.setGeometry(QRect(30, 220, 151, 61))
        self.outputC3 = QRadioButton(self.BoxC3)
        self.outputC3.setObjectName(u"outputC3")
        self.outputC3.setGeometry(QRect(10, 20, 82, 17))
        self.inputC3 = QRadioButton(self.BoxC3)
        self.inputC3.setObjectName(u"inputC3")
        self.inputC3.setGeometry(QRect(10, 40, 82, 17))
        self.inputConfidC0 = QGroupBox(self.PortC)
        self.inputConfidC0.setObjectName(u"inputConfidC0")
        self.inputConfidC0.setGeometry(QRect(440, 10, 211, 61))
        self.pul_upC0 = QRadioButton(self.inputConfidC0)
        self.pul_upC0.setObjectName(u"pul_upC0")
        self.pul_upC0.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceC0 = QRadioButton(self.inputConfidC0)
        self.high_impedenceC0.setObjectName(u"high_impedenceC0")
        self.high_impedenceC0.setGeometry(QRect(110, 30, 101, 17))
        self.outputConfigC2 = QGroupBox(self.PortC)
        self.outputConfigC2.setObjectName(u"outputConfigC2")
        self.outputConfigC2.setEnabled(True)
        self.outputConfigC2.setGeometry(QRect(210, 150, 211, 61))
        self.highC2 = QRadioButton(self.outputConfigC2)
        self.highC2.setObjectName(u"highC2")
        self.highC2.setGeometry(QRect(30, 30, 82, 17))
        self.lowC2 = QRadioButton(self.outputConfigC2)
        self.lowC2.setObjectName(u"lowC2")
        self.lowC2.setGeometry(QRect(120, 30, 82, 17))
        self.BoxC0 = QGroupBox(self.PortC)
        self.BoxC0.setObjectName(u"BoxC0")
        self.BoxC0.setGeometry(QRect(30, 10, 151, 61))
        self.outputC0 = QRadioButton(self.BoxC0)
        self.outputC0.setObjectName(u"outputC0")
        self.outputC0.setGeometry(QRect(10, 20, 82, 17))
        self.inputC0 = QRadioButton(self.BoxC0)
        self.inputC0.setObjectName(u"inputC0")
        self.inputC0.setGeometry(QRect(10, 40, 82, 17))
        self.BoxC1 = QGroupBox(self.PortC)
        self.BoxC1.setObjectName(u"BoxC1")
        self.BoxC1.setGeometry(QRect(30, 80, 151, 61))
        self.outputC1 = QRadioButton(self.BoxC1)
        self.outputC1.setObjectName(u"outputC1")
        self.outputC1.setGeometry(QRect(10, 20, 82, 17))
        self.inputC1 = QRadioButton(self.BoxC1)
        self.inputC1.setObjectName(u"inputC1")
        self.inputC1.setGeometry(QRect(10, 40, 82, 17))
        self.inputConfidC1 = QGroupBox(self.PortC)
        self.inputConfidC1.setObjectName(u"inputConfidC1")
        self.inputConfidC1.setGeometry(QRect(440, 80, 211, 61))
        self.pul_upC1 = QRadioButton(self.inputConfidC1)
        self.pul_upC1.setObjectName(u"pul_upC1")
        self.pul_upC1.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceC1 = QRadioButton(self.inputConfidC1)
        self.high_impedenceC1.setObjectName(u"high_impedenceC1")
        self.high_impedenceC1.setGeometry(QRect(110, 30, 101, 17))
        self.inputConfidC4 = QGroupBox(self.PortC)
        self.inputConfidC4.setObjectName(u"inputConfidC4")
        self.inputConfidC4.setGeometry(QRect(440, 290, 211, 61))
        self.pul_upC4 = QRadioButton(self.inputConfidC4)
        self.pul_upC4.setObjectName(u"pul_upC4")
        self.pul_upC4.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceC4 = QRadioButton(self.inputConfidC4)
        self.high_impedenceC4.setObjectName(u"high_impedenceC4")
        self.high_impedenceC4.setGeometry(QRect(110, 30, 101, 17))
        self.outputConfigC1 = QGroupBox(self.PortC)
        self.outputConfigC1.setObjectName(u"outputConfigC1")
        self.outputConfigC1.setEnabled(True)
        self.outputConfigC1.setGeometry(QRect(210, 80, 211, 61))
        self.highC1 = QRadioButton(self.outputConfigC1)
        self.highC1.setObjectName(u"highC1")
        self.highC1.setGeometry(QRect(30, 30, 82, 17))
        self.lowC1 = QRadioButton(self.outputConfigC1)
        self.lowC1.setObjectName(u"lowC1")
        self.lowC1.setGeometry(QRect(120, 30, 82, 17))
        self.inputConfidC7 = QGroupBox(self.PortC)
        self.inputConfidC7.setObjectName(u"inputConfidC7")
        self.inputConfidC7.setGeometry(QRect(440, 500, 211, 61))
        self.pul_upC7 = QRadioButton(self.inputConfidC7)
        self.pul_upC7.setObjectName(u"pul_upC7")
        self.pul_upC7.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceC7 = QRadioButton(self.inputConfidC7)
        self.high_impedenceC7.setObjectName(u"high_impedenceC7")
        self.high_impedenceC7.setGeometry(QRect(110, 30, 101, 17))
        self.outputConfigC6 = QGroupBox(self.PortC)
        self.outputConfigC6.setObjectName(u"outputConfigC6")
        self.outputConfigC6.setEnabled(True)
        self.outputConfigC6.setGeometry(QRect(210, 430, 211, 61))
        self.highC6 = QRadioButton(self.outputConfigC6)
        self.highC6.setObjectName(u"highC6")
        self.highC6.setGeometry(QRect(30, 30, 82, 17))
        self.lowC6 = QRadioButton(self.outputConfigC6)
        self.lowC6.setObjectName(u"lowC6")
        self.lowC6.setGeometry(QRect(120, 30, 82, 17))
        self.outputConfigC4 = QGroupBox(self.PortC)
        self.outputConfigC4.setObjectName(u"outputConfigC4")
        self.outputConfigC4.setEnabled(True)
        self.outputConfigC4.setGeometry(QRect(210, 290, 211, 61))
        self.highC4 = QRadioButton(self.outputConfigC4)
        self.highC4.setObjectName(u"highC4")
        self.highC4.setGeometry(QRect(30, 30, 82, 17))
        self.lowC4 = QRadioButton(self.outputConfigC4)
        self.lowC4.setObjectName(u"lowC4")
        self.lowC4.setGeometry(QRect(120, 30, 82, 17))
        self.outputConfigC7 = QGroupBox(self.PortC)
        self.outputConfigC7.setObjectName(u"outputConfigC7")
        self.outputConfigC7.setEnabled(True)
        self.outputConfigC7.setGeometry(QRect(210, 500, 211, 61))
        self.highC7 = QRadioButton(self.outputConfigC7)
        self.highC7.setObjectName(u"highC7")
        self.highC7.setGeometry(QRect(30, 30, 82, 17))
        self.lowC7 = QRadioButton(self.outputConfigC7)
        self.lowC7.setObjectName(u"lowC7")
        self.lowC7.setGeometry(QRect(120, 30, 82, 17))
        self.inputConfidC3 = QGroupBox(self.PortC)
        self.inputConfidC3.setObjectName(u"inputConfidC3")
        self.inputConfidC3.setGeometry(QRect(440, 220, 211, 61))
        self.pul_upC3 = QRadioButton(self.inputConfidC3)
        self.pul_upC3.setObjectName(u"pul_upC3")
        self.pul_upC3.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceC3 = QRadioButton(self.inputConfidC3)
        self.high_impedenceC3.setObjectName(u"high_impedenceC3")
        self.high_impedenceC3.setGeometry(QRect(110, 30, 101, 17))
        self.AVR_ATMEGA32_CONFIG.addTab(self.PortC, "")
        self.PortD = QWidget()
        self.PortD.setObjectName(u"PortD")
        self.PortD.setEnabled(True)
        self.PortD.setAcceptDrops(False)
        self.BoxD6 = QGroupBox(self.PortD)
        self.BoxD6.setObjectName(u"BoxD6")
        self.BoxD6.setGeometry(QRect(30, 430, 151, 61))
        self.outputD6 = QRadioButton(self.BoxD6)
        self.outputD6.setObjectName(u"outputD6")
        self.outputD6.setGeometry(QRect(10, 20, 82, 17))
        self.inputD6 = QRadioButton(self.BoxD6)
        self.inputD6.setObjectName(u"inputD6")
        self.inputD6.setGeometry(QRect(10, 40, 82, 17))
        self.BoxD2 = QGroupBox(self.PortD)
        self.BoxD2.setObjectName(u"BoxD2")
        self.BoxD2.setGeometry(QRect(30, 150, 151, 61))
        self.outputD2 = QRadioButton(self.BoxD2)
        self.outputD2.setObjectName(u"outputD2")
        self.outputD2.setGeometry(QRect(10, 20, 82, 17))
        self.inputD2 = QRadioButton(self.BoxD2)
        self.inputD2.setObjectName(u"inputD2")
        self.inputD2.setGeometry(QRect(10, 40, 82, 17))
        self.outputConfigD0 = QGroupBox(self.PortD)
        self.outputConfigD0.setObjectName(u"outputConfigD0")
        self.outputConfigD0.setEnabled(True)
        self.outputConfigD0.setGeometry(QRect(210, 10, 211, 61))
        self.outputConfigD0.setStyleSheet(u"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.highD0 = QRadioButton(self.outputConfigD0)
        self.highD0.setObjectName(u"highD0")
        self.highD0.setGeometry(QRect(30, 30, 82, 17))
        self.lowD0 = QRadioButton(self.outputConfigD0)
        self.lowD0.setObjectName(u"lowD0")
        self.lowD0.setGeometry(QRect(120, 30, 82, 17))
        self.BoxD5 = QGroupBox(self.PortD)
        self.BoxD5.setObjectName(u"BoxD5")
        self.BoxD5.setGeometry(QRect(30, 360, 151, 61))
        self.outputD5 = QRadioButton(self.BoxD5)
        self.outputD5.setObjectName(u"outputD5")
        self.outputD5.setGeometry(QRect(10, 20, 82, 17))
        self.inputD5 = QRadioButton(self.BoxD5)
        self.inputD5.setObjectName(u"inputD5")
        self.inputD5.setGeometry(QRect(10, 40, 82, 17))
        self.BoxD4 = QGroupBox(self.PortD)
        self.BoxD4.setObjectName(u"BoxD4")
        self.BoxD4.setGeometry(QRect(30, 290, 151, 61))
        self.outputD4 = QRadioButton(self.BoxD4)
        self.outputD4.setObjectName(u"outputD4")
        self.outputD4.setGeometry(QRect(10, 20, 82, 17))
        self.inputD4 = QRadioButton(self.BoxD4)
        self.inputD4.setObjectName(u"inputD4")
        self.inputD4.setGeometry(QRect(10, 40, 82, 17))
        self.inputConfidD2 = QGroupBox(self.PortD)
        self.inputConfidD2.setObjectName(u"inputConfidD2")
        self.inputConfidD2.setGeometry(QRect(440, 150, 211, 61))
        self.pul_upD2 = QRadioButton(self.inputConfidD2)
        self.pul_upD2.setObjectName(u"pul_upD2")
        self.pul_upD2.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceD2 = QRadioButton(self.inputConfidD2)
        self.high_impedenceD2.setObjectName(u"high_impedenceD2")
        self.high_impedenceD2.setGeometry(QRect(110, 30, 101, 17))
        self.outputConfigD3 = QGroupBox(self.PortD)
        self.outputConfigD3.setObjectName(u"outputConfigD3")
        self.outputConfigD3.setEnabled(True)
        self.outputConfigD3.setGeometry(QRect(210, 220, 211, 61))
        self.highD3 = QRadioButton(self.outputConfigD3)
        self.highD3.setObjectName(u"highD3")
        self.highD3.setGeometry(QRect(30, 30, 82, 17))
        self.lowD3 = QRadioButton(self.outputConfigD3)
        self.lowD3.setObjectName(u"lowD3")
        self.lowD3.setGeometry(QRect(120, 30, 82, 17))
        self.inputConfidD6 = QGroupBox(self.PortD)
        self.inputConfidD6.setObjectName(u"inputConfidD6")
        self.inputConfidD6.setGeometry(QRect(440, 430, 211, 61))
        self.pul_upD6 = QRadioButton(self.inputConfidD6)
        self.pul_upD6.setObjectName(u"pul_upD6")
        self.pul_upD6.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceD6 = QRadioButton(self.inputConfidD6)
        self.high_impedenceD6.setObjectName(u"high_impedenceD6")
        self.high_impedenceD6.setGeometry(QRect(110, 30, 101, 17))
        self.outputConfigD5 = QGroupBox(self.PortD)
        self.outputConfigD5.setObjectName(u"outputConfigD5")
        self.outputConfigD5.setEnabled(True)
        self.outputConfigD5.setGeometry(QRect(210, 360, 211, 61))
        self.highD5 = QRadioButton(self.outputConfigD5)
        self.highD5.setObjectName(u"highD5")
        self.highD5.setGeometry(QRect(30, 30, 82, 17))
        self.lowD5 = QRadioButton(self.outputConfigD5)
        self.lowD5.setObjectName(u"lowD5")
        self.lowD5.setGeometry(QRect(120, 30, 82, 17))
        self.BoxD7 = QGroupBox(self.PortD)
        self.BoxD7.setObjectName(u"BoxD7")
        self.BoxD7.setGeometry(QRect(30, 500, 151, 61))
        self.outputD7 = QRadioButton(self.BoxD7)
        self.outputD7.setObjectName(u"outputD7")
        self.outputD7.setGeometry(QRect(10, 20, 82, 17))
        self.inputD7 = QRadioButton(self.BoxD7)
        self.inputD7.setObjectName(u"inputD7")
        self.inputD7.setGeometry(QRect(10, 40, 82, 17))
        self.inputConfidD5 = QGroupBox(self.PortD)
        self.inputConfidD5.setObjectName(u"inputConfidD5")
        self.inputConfidD5.setGeometry(QRect(440, 360, 211, 61))
        self.pul_upD5 = QRadioButton(self.inputConfidD5)
        self.pul_upD5.setObjectName(u"pul_upD5")
        self.pul_upD5.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceD5 = QRadioButton(self.inputConfidD5)
        self.high_impedenceD5.setObjectName(u"high_impedenceD5")
        self.high_impedenceD5.setGeometry(QRect(110, 30, 101, 17))
        self.BoxD3 = QGroupBox(self.PortD)
        self.BoxD3.setObjectName(u"BoxD3")
        self.BoxD3.setGeometry(QRect(30, 220, 151, 61))
        self.outputD3 = QRadioButton(self.BoxD3)
        self.outputD3.setObjectName(u"outputD3")
        self.outputD3.setGeometry(QRect(10, 20, 82, 17))
        self.inputD3 = QRadioButton(self.BoxD3)
        self.inputD3.setObjectName(u"inputD3")
        self.inputD3.setGeometry(QRect(10, 40, 82, 17))
        self.inputConfidD0 = QGroupBox(self.PortD)
        self.inputConfidD0.setObjectName(u"inputConfidD0")
        self.inputConfidD0.setGeometry(QRect(440, 10, 211, 61))
        self.pul_upD0 = QRadioButton(self.inputConfidD0)
        self.pul_upD0.setObjectName(u"pul_upD0")
        self.pul_upD0.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceD0 = QRadioButton(self.inputConfidD0)
        self.high_impedenceD0.setObjectName(u"high_impedenceD0")
        self.high_impedenceD0.setGeometry(QRect(110, 30, 101, 17))
        self.outputConfigD2 = QGroupBox(self.PortD)
        self.outputConfigD2.setObjectName(u"outputConfigD2")
        self.outputConfigD2.setEnabled(True)
        self.outputConfigD2.setGeometry(QRect(210, 150, 211, 61))
        self.highD2 = QRadioButton(self.outputConfigD2)
        self.highD2.setObjectName(u"highD2")
        self.highD2.setGeometry(QRect(30, 30, 82, 17))
        self.lowD2 = QRadioButton(self.outputConfigD2)
        self.lowD2.setObjectName(u"lowD2")
        self.lowD2.setGeometry(QRect(120, 30, 82, 17))
        self.BoxD0 = QGroupBox(self.PortD)
        self.BoxD0.setObjectName(u"BoxD0")
        self.BoxD0.setGeometry(QRect(30, 10, 151, 61))
        self.outputD0 = QRadioButton(self.BoxD0)
        self.outputD0.setObjectName(u"outputD0")
        self.outputD0.setGeometry(QRect(10, 20, 82, 17))
        self.inputD0 = QRadioButton(self.BoxD0)
        self.inputD0.setObjectName(u"inputD0")
        self.inputD0.setGeometry(QRect(10, 40, 82, 17))
        self.BoxD1 = QGroupBox(self.PortD)
        self.BoxD1.setObjectName(u"BoxD1")
        self.BoxD1.setGeometry(QRect(30, 80, 151, 61))
        self.outputD1 = QRadioButton(self.BoxD1)
        self.outputD1.setObjectName(u"outputD1")
        self.outputD1.setGeometry(QRect(10, 20, 82, 17))
        self.inputD1 = QRadioButton(self.BoxD1)
        self.inputD1.setObjectName(u"inputD1")
        self.inputD1.setGeometry(QRect(10, 40, 82, 17))
        self.inputConfidD1 = QGroupBox(self.PortD)
        self.inputConfidD1.setObjectName(u"inputConfidD1")
        self.inputConfidD1.setGeometry(QRect(440, 80, 211, 61))
        self.pul_upD1 = QRadioButton(self.inputConfidD1)
        self.pul_upD1.setObjectName(u"pul_upD1")
        self.pul_upD1.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceD1 = QRadioButton(self.inputConfidD1)
        self.high_impedenceD1.setObjectName(u"high_impedenceD1")
        self.high_impedenceD1.setGeometry(QRect(110, 30, 101, 17))
        self.inputConfidD4 = QGroupBox(self.PortD)
        self.inputConfidD4.setObjectName(u"inputConfidD4")
        self.inputConfidD4.setGeometry(QRect(440, 290, 211, 61))
        self.pul_upD4 = QRadioButton(self.inputConfidD4)
        self.pul_upD4.setObjectName(u"pul_upD4")
        self.pul_upD4.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceD4 = QRadioButton(self.inputConfidD4)
        self.high_impedenceD4.setObjectName(u"high_impedenceD4")
        self.high_impedenceD4.setGeometry(QRect(110, 30, 101, 17))
        self.outputConfigD1 = QGroupBox(self.PortD)
        self.outputConfigD1.setObjectName(u"outputConfigD1")
        self.outputConfigD1.setEnabled(True)
        self.outputConfigD1.setGeometry(QRect(210, 80, 211, 61))
        self.highD1 = QRadioButton(self.outputConfigD1)
        self.highD1.setObjectName(u"highD1")
        self.highD1.setGeometry(QRect(30, 30, 82, 17))
        self.lowD1 = QRadioButton(self.outputConfigD1)
        self.lowD1.setObjectName(u"lowD1")
        self.lowD1.setGeometry(QRect(120, 30, 82, 17))
        self.inputConfidD7 = QGroupBox(self.PortD)
        self.inputConfidD7.setObjectName(u"inputConfidD7")
        self.inputConfidD7.setGeometry(QRect(440, 500, 211, 61))
        self.pul_upD7 = QRadioButton(self.inputConfidD7)
        self.pul_upD7.setObjectName(u"pul_upD7")
        self.pul_upD7.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceD7 = QRadioButton(self.inputConfidD7)
        self.high_impedenceD7.setObjectName(u"high_impedenceD7")
        self.high_impedenceD7.setGeometry(QRect(110, 30, 101, 17))
        self.outputConfigD6 = QGroupBox(self.PortD)
        self.outputConfigD6.setObjectName(u"outputConfigD6")
        self.outputConfigD6.setEnabled(True)
        self.outputConfigD6.setGeometry(QRect(210, 430, 211, 61))
        self.highD6 = QRadioButton(self.outputConfigD6)
        self.highD6.setObjectName(u"highD6")
        self.highD6.setGeometry(QRect(30, 30, 82, 17))
        self.lowD6 = QRadioButton(self.outputConfigD6)
        self.lowD6.setObjectName(u"lowD6")
        self.lowD6.setGeometry(QRect(120, 30, 82, 17))
        self.outputConfigD4 = QGroupBox(self.PortD)
        self.outputConfigD4.setObjectName(u"outputConfigD4")
        self.outputConfigD4.setEnabled(True)
        self.outputConfigD4.setGeometry(QRect(210, 290, 211, 61))
        self.highD4 = QRadioButton(self.outputConfigD4)
        self.highD4.setObjectName(u"highD4")
        self.highD4.setGeometry(QRect(30, 30, 82, 17))
        self.lowD4 = QRadioButton(self.outputConfigD4)
        self.lowD4.setObjectName(u"lowD4")
        self.lowD4.setGeometry(QRect(120, 30, 82, 17))
        self.outputConfigD7 = QGroupBox(self.PortD)
        self.outputConfigD7.setObjectName(u"outputConfigD7")
        self.outputConfigD7.setEnabled(True)
        self.outputConfigD7.setGeometry(QRect(210, 500, 211, 61))
        self.highD7 = QRadioButton(self.outputConfigD7)
        self.highD7.setObjectName(u"highD7")
        self.highD7.setGeometry(QRect(30, 30, 82, 17))
        self.lowD7 = QRadioButton(self.outputConfigD7)
        self.lowD7.setObjectName(u"lowD7")
        self.lowD7.setGeometry(QRect(120, 30, 82, 17))
        self.inputConfidD3 = QGroupBox(self.PortD)
        self.inputConfidD3.setObjectName(u"inputConfidD3")
        self.inputConfidD3.setGeometry(QRect(440, 220, 211, 61))
        self.pul_upD3 = QRadioButton(self.inputConfidD3)
        self.pul_upD3.setObjectName(u"pul_upD3")
        self.pul_upD3.setGeometry(QRect(30, 30, 82, 17))
        self.high_impedenceD3 = QRadioButton(self.inputConfidD3)
        self.high_impedenceD3.setObjectName(u"high_impedenceD3")
        self.high_impedenceD3.setGeometry(QRect(110, 30, 101, 17))
        self.AVR_ATMEGA32_CONFIG.addTab(self.PortD, "")
        self.configcheck = QWidget()
        self.configcheck.setObjectName(u"configcheck")
        self.groupBox_2 = QGroupBox(self.configcheck)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(140, 100, 391, 61))
        self.groupBox_2.setStyleSheet(u"font: 81 14pt \"Rockwell Extra Bold\";\n"
"text-decoration: underline;\n"
"font: 81 14pt \"Rockwell Extra Bold\";")
        self.path = QLineEdit(self.groupBox_2)
        self.path.setObjectName(u"path")
        self.path.setGeometry(QRect(0, 20, 391, 41))
        self.path.setStyleSheet(u"font: 81 6pt \"Rockwell Extra Bold\";")
        self.Generate = QPushButton(self.configcheck)
        self.Generate.setObjectName(u"Generate")
        self.Generate.setGeometry(QRect(50, 300, 171, 41))
        self.Generate.setStyleSheet(u"font: 81 14pt \"Rockwell Extra Bold\";")
        self.load = QPushButton(self.configcheck)
        self.load.setObjectName(u"load")
        self.load.setGeometry(QRect(470, 300, 171, 41))
        self.load.setStyleSheet(u"font: 81 14pt \"Rockwell Extra Bold\";")
        self.save = QPushButton(self.configcheck)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(260, 300, 171, 41))
        self.save.setStyleSheet(u"font: 81 14pt \"Rockwell Extra Bold\";")
        self.AVR_ATMEGA32_CONFIG.addTab(self.configcheck, "")

        self.verticalLayout.addWidget(self.AVR_ATMEGA32_CONFIG)


        self.retranslateUi(Form)
        self.outputA0.toggled.connect(self.outputConfigA0.setEnabled)
        self.outputA7.toggled.connect(self.inputConfidA7.setDisabled)
        self.outputA7.toggled.connect(self.outputConfigA7.setEnabled)
        self.inputA7.toggled.connect(self.outputConfigA7.setDisabled)
        self.inputA7.toggled.connect(self.inputConfidA7.setEnabled)
        self.outputA6.toggled.connect(self.inputConfidA6.setDisabled)
        self.outputA6.toggled.connect(self.outputConfigA6.setEnabled)
        self.inputA6.toggled.connect(self.outputConfigA6.setDisabled)
        self.inputA6.toggled.connect(self.inputConfidA6.setEnabled)
        self.outputA5.toggled.connect(self.inputConfidA5.setDisabled)
        self.outputA5.toggled.connect(self.outputConfigA5.setEnabled)
        self.inputA5.toggled.connect(self.outputConfigA5.setDisabled)
        self.inputA5.toggled.connect(self.inputConfidA5.setEnabled)
        self.outputA4.toggled.connect(self.inputConfidA4.setDisabled)
        self.outputA4.toggled.connect(self.outputConfigA4.setEnabled)
        self.inputA4.toggled.connect(self.outputConfigA4.setDisabled)
        self.inputA4.toggled.connect(self.inputConfidA4.setEnabled)
        self.outputA3.toggled.connect(self.outputConfigA3.setEnabled)
        self.outputA3.toggled.connect(self.inputConfidA3.setDisabled)
        self.inputA3.toggled.connect(self.outputConfigA3.setDisabled)
        self.inputA3.toggled.connect(self.inputConfidA3.setEnabled)
        self.outputA2.toggled.connect(self.inputConfidA2.setDisabled)
        self.outputA2.toggled.connect(self.outputConfigA2.setEnabled)
        self.inputA2.toggled.connect(self.outputConfigA2.setDisabled)
        self.inputA2.toggled.connect(self.inputConfidA2.setEnabled)
        self.inputA1.toggled.connect(self.outputConfigA1.setDisabled)
        self.inputA1.toggled.connect(self.inputConfidA1.setEnabled)
        self.outputA1.toggled.connect(self.outputConfigA1.setEnabled)
        self.outputA1.toggled.connect(self.inputConfidA1.setDisabled)
        self.inputA0.toggled.connect(self.outputConfigA0.setDisabled)
        self.inputA0.toggled.connect(self.inputConfidA0.setEnabled)
        self.outputA0.toggled.connect(self.inputConfidA0.setDisabled)
        self.outputB7.toggled.connect(self.inputConfidB7.setDisabled)
        self.outputB7.toggled.connect(self.outputConfigB7.setEnabled)
        self.inputB7.toggled.connect(self.outputConfigB7.setDisabled)
        self.inputB7.toggled.connect(self.inputConfidB7.setEnabled)
        self.outputB6.toggled.connect(self.inputConfidB6.setDisabled)
        self.outputB6.toggled.connect(self.outputConfigB6.setEnabled)
        self.inputB6.toggled.connect(self.outputConfigB6.setDisabled)
        self.inputB6.toggled.connect(self.inputConfidB6.setEnabled)
        self.outputB5.toggled.connect(self.inputConfidB5.setDisabled)
        self.outputB5.toggled.connect(self.outputConfigB5.setEnabled)
        self.inputB5.toggled.connect(self.outputConfigB5.setDisabled)
        self.inputB5.toggled.connect(self.inputConfidB5.setEnabled)
        self.outputB4.toggled.connect(self.inputConfidB4.setDisabled)
        self.outputB4.toggled.connect(self.outputConfigB4.setEnabled)
        self.inputB4.toggled.connect(self.outputConfigB4.setDisabled)
        self.inputB4.toggled.connect(self.inputConfidB4.setEnabled)
        self.outputB3.toggled.connect(self.inputConfidB3.setDisabled)
        self.outputB3.toggled.connect(self.outputConfigB3.setEnabled)
        self.inputB3.toggled.connect(self.outputConfigB3.setDisabled)
        self.inputB3.toggled.connect(self.inputConfidB3.setEnabled)
        self.outputB2.toggled.connect(self.inputConfidB2.setDisabled)
        self.outputB2.toggled.connect(self.outputConfigB2.setEnabled)
        self.inputB2.toggled.connect(self.outputConfigB2.setDisabled)
        self.inputB2.toggled.connect(self.inputConfidB2.setEnabled)
        self.outputB1.toggled.connect(self.inputConfidB1.setDisabled)
        self.outputB1.toggled.connect(self.outputConfigB1.setEnabled)
        self.inputB1.toggled.connect(self.outputConfigB1.setDisabled)
        self.inputB1.toggled.connect(self.inputConfidB1.setEnabled)
        self.outputB0.toggled.connect(self.inputConfidB0.setDisabled)
        self.outputB0.toggled.connect(self.outputConfigB0.setEnabled)
        self.inputB0.toggled.connect(self.outputConfigB0.setDisabled)
        self.inputB0.toggled.connect(self.inputConfidB0.setEnabled)
        self.inputC0.toggled.connect(self.inputConfidC0.setEnabled)
        self.inputC0.toggled.connect(self.outputConfigC0.setDisabled)
        self.inputC1.toggled.connect(self.inputConfidC1.setEnabled)
        self.outputC0.toggled.connect(self.outputConfigC0.setEnabled)
        self.inputC2.toggled.connect(self.outputConfigC2.setDisabled)
        self.inputD1.toggled.connect(self.inputConfidD1.setEnabled)
        self.inputC1.toggled.connect(self.outputConfigC1.setDisabled)
        self.inputC3.toggled.connect(self.inputConfidC3.setEnabled)
        self.inputC5.toggled.connect(self.inputConfidC5.setEnabled)
        self.outputD1.toggled.connect(self.outputConfigD1.setEnabled)
        self.inputC7.toggled.connect(self.outputConfigC7.setDisabled)
        self.outputC4.toggled.connect(self.inputConfidC4.setDisabled)
        self.inputC3.toggled.connect(self.outputConfigC3.setDisabled)
        self.inputC2.toggled.connect(self.inputConfidC2.setEnabled)
        self.inputC6.toggled.connect(self.outputConfigC6.setDisabled)
        self.inputC7.toggled.connect(self.inputConfidC7.setEnabled)
        self.inputC5.toggled.connect(self.outputConfigC5.setDisabled)
        self.outputC2.toggled.connect(self.outputConfigC2.setEnabled)
        self.outputC3.toggled.connect(self.outputConfigC3.setEnabled)
        self.inputD3.toggled.connect(self.inputConfidD3.setEnabled)
        self.outputC5.toggled.connect(self.outputConfigC5.setEnabled)
        self.inputD4.toggled.connect(self.inputConfidD4.setEnabled)
        self.inputC6.toggled.connect(self.inputConfidC6.setEnabled)
        self.outputC4.toggled.connect(self.outputConfigC4.setEnabled)
        self.outputC5.toggled.connect(self.inputConfidC5.setDisabled)
        self.inputC4.toggled.connect(self.inputConfidC4.setEnabled)
        self.inputD4.toggled.connect(self.outputConfigD4.setDisabled)
        self.outputC0.toggled.connect(self.inputConfidC0.setDisabled)
        self.outputC1.toggled.connect(self.outputConfigC1.setEnabled)
        self.inputC4.toggled.connect(self.outputConfigC4.setDisabled)
        self.outputC1.toggled.connect(self.inputConfidC1.setDisabled)
        self.outputC7.toggled.connect(self.outputConfigC7.setEnabled)
        self.outputC7.toggled.connect(self.inputConfidC7.setDisabled)
        self.outputC6.toggled.connect(self.outputConfigC6.setEnabled)
        self.outputC2.toggled.connect(self.inputConfidC2.setDisabled)
        self.outputC6.toggled.connect(self.inputConfidC6.setDisabled)
        self.outputC3.toggled.connect(self.inputConfidC3.setDisabled)
        self.outputD2.toggled.connect(self.outputConfigD2.setEnabled)
        self.inputD7.toggled.connect(self.inputConfidD7.setEnabled)
        self.inputD1.toggled.connect(self.outputConfigD1.setDisabled)
        self.inputD5.toggled.connect(self.outputConfigD5.setDisabled)
        self.inputD2.toggled.connect(self.outputConfigD2.setDisabled)
        self.inputD2.toggled.connect(self.inputConfidD2.setEnabled)
        self.inputD0.toggled.connect(self.outputConfigD0.setDisabled)
        self.inputD6.toggled.connect(self.inputConfidD6.setEnabled)
        self.inputD6.toggled.connect(self.outputConfigD6.setDisabled)
        self.inputD5.toggled.connect(self.inputConfidD5.setEnabled)
        self.inputD3.toggled.connect(self.outputConfigD3.setDisabled)
        self.outputD1.toggled.connect(self.inputConfidD1.setDisabled)
        self.outputD6.toggled.connect(self.inputConfidD6.setDisabled)
        self.outputD2.toggled.connect(self.inputConfidD2.setDisabled)
        self.inputD7.toggled.connect(self.outputConfigD7.setDisabled)
        self.outputD4.toggled.connect(self.outputConfigD4.setEnabled)
        self.outputD4.toggled.connect(self.inputConfidD4.setDisabled)
        self.outputD3.toggled.connect(self.inputConfidD0.setEnabled)
        self.outputD3.toggled.connect(self.inputConfidD3.setDisabled)
        self.outputD5.toggled.connect(self.outputConfigD5.setEnabled)
        self.outputD7.toggled.connect(self.inputConfidD7.setDisabled)
        self.outputD6.toggled.connect(self.outputConfigD7.setEnabled)
        self.outputD0.toggled.connect(self.outputConfigD0.setEnabled)
        self.outputD0.toggled.connect(self.inputConfidD0.setDisabled)
        self.Generate.clicked.connect(self.GenerateFunction)
        self.save.clicked.connect(self.saveFunction)
        self.load.clicked.connect(self.loadFunction)

        self.AVR_ATMEGA32_CONFIG.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def GenerateFunction(self):
      output_path =self.path.text()+r'\DioTEST_cfg.h'
      File_Handler = open (output_path,'w')
      File_Handler.write("#ifndef_DIO_CFG_H\n")
      File_Handler.write("#define_DIO_CFG_H\n")
      File_Handler.write("\n")
      File_Handler.write("\n")
       
       
      File_Handler.write("#PORTA_CONFIG\n")
      File_Handler.write("\n")
      
      if self.outputA0.isChecked():
        if self.highA0.isChecked():
          File_Handler.write("#define DIO_PINA0_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINA0_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upA0.isChecked():
          File_Handler.write('#define DIO_PINA0_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINA0_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################      
      if self.outputA1.isChecked():
        if self.highA1.isChecked():
          File_Handler.write("#define DIO_PINA1_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINA1_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upA1.isChecked():
          File_Handler.write('#define DIO_PINA1_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINA1_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputA2.isChecked():
        if self.highA2.isChecked():
          File_Handler.write("#define DIO_PINA2_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINA2_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upA2.isChecked():
          File_Handler.write('#define DIO_PINA2_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINA2_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputA3.isChecked():
        if self.highA3.isChecked():
          File_Handler.write("#define DIO_PINA3_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINA3_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upA3.isChecked():
          File_Handler.write('#define DIO_PINA3_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINA3_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputA4.isChecked():
        if self.highA4.isChecked():
          File_Handler.write("#define DIO_PINA4_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINA4_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upA4.isChecked():
          File_Handler.write('#define DIO_PINA4_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINA4_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputA5.isChecked():
        if self.highA5.isChecked():
          File_Handler.write("#define DIO_PINA5_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINA5_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upA5.isChecked():
          File_Handler.write('#define DIO_PINA5_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINA5_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputA6.isChecked():
        if self.highA6.isChecked():
          File_Handler.write("#define DIO_PINA6_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINA6_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upA6.isChecked():
          File_Handler.write('#define DIO_PINA6_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINA6_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputA7.isChecked():
        if self.highA7.isChecked():
          File_Handler.write("#define DIO_PINA7_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINA7_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upA7.isChecked():
          File_Handler.write('#define DIO_PINA7_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINA7_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################


      File_Handler.write("\n")
      File_Handler.write("#PORTB_CONFIG\n")
      File_Handler.write("\n")
      if self.outputB0.isChecked():
        if self.highB0.isChecked():
          File_Handler.write("#define DIO_PINB0_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINB0_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upB0.isChecked():
          File_Handler.write('#define DIO_PINB0_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINB0_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################      
      if self.outputB1.isChecked():
        if self.highB1.isChecked():
          File_Handler.write("#define DIO_PINB1_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINB1_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upB1.isChecked():
          File_Handler.write('#define DIO_PINB1_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINB1_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputB2.isChecked():
        if self.highB2.isChecked():
          File_Handler.write("#define DIO_PINB2_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINB2_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upB2.isChecked():
          File_Handler.write('#define DIO_PINB2_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINB2_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputB3.isChecked():
        if self.highB3.isChecked():
          File_Handler.write("#define DIO_PINB3_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINB3_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upB3.isChecked():
          File_Handler.write('#define DIO_PINB3_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINB3_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputB4.isChecked():
        if self.highB4.isChecked():
          File_Handler.write("#define DIO_PINB4_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINB4_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upB4.isChecked():
          File_Handler.write('#define DIO_PINB4_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINB4_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputB5.isChecked():
        if self.highB5.isChecked():
          File_Handler.write("#define DIO_PINB5_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINA5_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upB5.isChecked():
          File_Handler.write('#define DIO_PINB5_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINB5_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputB6.isChecked():
        if self.highB6.isChecked():
          File_Handler.write("#define DIO_PINB6_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINB6_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upB6.isChecked():
          File_Handler.write('#define DIO_PINB6_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINB6_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputB7.isChecked():
        if self.highB7.isChecked():
          File_Handler.write("#define DIO_PINB7_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINB7_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upB7.isChecked():
          File_Handler.write('#define DIO_PINB7_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINB7_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
    
    
    
      File_Handler.write("\n")
      File_Handler.write("#PORTC_CONFIG\n")
      File_Handler.write("\n")
      if self.outputC0.isChecked():
        if self.highC0.isChecked():
          File_Handler.write("#define DIO_PINC0_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINC0_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upC0.isChecked():
          File_Handler.write('#define DIO_PINC0_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINC0_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################      
      if self.outputC1.isChecked():
        if self.highC1.isChecked():
          File_Handler.write("#define DIO_PINC1_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINC1_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upC1.isChecked():
          File_Handler.write('#define DIO_PINC1_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINC1_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputC2.isChecked():
        if self.highC2.isChecked():
          File_Handler.write("#define DIO_PINC2_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINC2_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upC2.isChecked():
          File_Handler.write('#define DIO_PINC2_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINC2_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputC3.isChecked():
        if self.highC3.isChecked():
          File_Handler.write("#define DIO_PINC3_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINC3_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upC3.isChecked():
          File_Handler.write('#define DIO_PINC3_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINC3_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputC4.isChecked():
        if self.highC4.isChecked():
          File_Handler.write("#define DIO_PINC4_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINC4_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upC4.isChecked():
          File_Handler.write('#define DIO_PINC4_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINC4_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputC5.isChecked():
        if self.highC5.isChecked():
          File_Handler.write("#define DIO_PINC5_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINC5_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upC5.isChecked():
          File_Handler.write('#define DIO_PINC5_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINC5_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputC6.isChecked():
        if self.highC6.isChecked():
          File_Handler.write("#define DIO_PINC6_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINC6_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upC6.isChecked():
          File_Handler.write('#define DIO_PINC6_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINC6_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputC7.isChecked():
        if self.highC7.isChecked():
          File_Handler.write("#define DIO_PINC7_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINC7_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upC7.isChecked():
          File_Handler.write('#define DIO_PINC7_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PINC7_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
    
    
    
      File_Handler.write("\n")
      File_Handler.write("#PORTD_CONFIG\n")
      File_Handler.write("\n")      
      if self.outputD0.isChecked():
        if self.highD0.isChecked():
          File_Handler.write("#define DIO_PIND0_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PIND0_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upD0.isChecked():
          File_Handler.write('#define DIO_PIND0_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PIND0_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ############################################################################## 
      if self.outputD1.isChecked():
        if self.highD1.isChecked():
          File_Handler.write("#define DIO_PIND1_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PINC1_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upD1.isChecked():
          File_Handler.write('#define DIO_PIND1_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PIND1_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputD2.isChecked():
        if self.highD2.isChecked():
          File_Handler.write("#define DIO_PIND2_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PIND2_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upD2.isChecked():
          File_Handler.write('#define DIO_PIND2_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PIND2_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputD3.isChecked():
        if self.highD3.isChecked():
          File_Handler.write("#define DIO_PIND3_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PIND3_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upD3.isChecked():
          File_Handler.write('#define DIO_PIND3_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PIND3_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputD4.isChecked():
        if self.highD4.isChecked():
          File_Handler.write("#define DIO_PIND4_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PIND4_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upD4.isChecked():
          File_Handler.write('#define DIO_PIND4_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#efine DIO_PIND4_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputD5.isChecked():
        if self.highD5.isChecked():
          File_Handler.write("#define DIO_PIND5_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PIND5_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upD5.isChecked():
          File_Handler.write('#define DIO_PIND5_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PIND5_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputD6.isChecked():
        if self.highD6.isChecked():
          File_Handler.write("#define DIO_PIND6_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PIND6_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upD6.isChecked():
          File_Handler.write('#define DIO_PIND6_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PIND6_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      if self.outputD7.isChecked():
        if self.highD7.isChecked():
          File_Handler.write("#define DIO_PIND7_MODE     DIO_OUTPUT_HIGH\n")
        else:
          File_Handler.write("#define DIO_PIND7_MODE     DIO_OUTPUT_LOW\n")
      else:
        if self.pul_upD7.isChecked():
          File_Handler.write('#define DIO_PIND7_MODE     DIO_INPUT_PULLUP\n')
        else:
          File_Handler.write('#define DIO_PIND7_MODE     DIO_INPUT_HIGH_IMPEDANCE\n')
    ##############################################################################
      File_Handler.write("\n")
      File_Handler.write("\n")
      File_Handler.write("#endef _DIO_CFG_H\n")
      File_Handler.close()
      
     
     
     
    def saveFunction(self): 
      DIO = ET.Element("DIO")
      ##############################################################################
      
      PORTA= ET.Element("PORTA")
      PORTA_PIN0 = ET.Element("PINA0")
      PORTA_PIN1 = ET.Element("PINA1")
      PORTA_PIN2 = ET.Element("PINA2")
      PORTA_PIN3 = ET.Element("PINA3")
      PORTA_PIN4 = ET.Element("PINA4")
      PORTA_PIN5 = ET.Element("PINA5")
      PORTA_PIN6 = ET.Element("PINA6")
      PORTA_PIN7 = ET.Element("PINA7")
      
      PORTA_PIN0_DIR = ET.Element("DIR")      
      PORTA_PIN0_CONFIG = ET.Element("CONFIG")
      PORTA_PIN1_DIR = ET.Element("DIR")      
      PORTA_PIN1_CONFIG = ET.Element("CONFIG")
      PORTA_PIN2_DIR = ET.Element("DIR")      
      PORTA_PIN2_CONFIG = ET.Element("CONFIG")
      PORTA_PIN3_DIR = ET.Element("DIR")      
      PORTA_PIN3_CONFIG = ET.Element("CONFIG")
      PORTA_PIN4_DIR = ET.Element("DIR")      
      PORTA_PIN4_CONFIG = ET.Element("CONFIG")
      PORTA_PIN5_DIR = ET.Element("DIR")      
      PORTA_PIN5_CONFIG = ET.Element("CONFIG")
      PORTA_PIN6_DIR = ET.Element("DIR")      
      PORTA_PIN6_CONFIG = ET.Element("CONFIG")
      PORTA_PIN7_DIR = ET.Element("DIR")      
      PORTA_PIN7_CONFIG = ET.Element("CONFIG")
      
      
      if self.outputA0.isChecked():
        PORTA_PIN0_DIR.text = "OUTPUT"
        if self.highA0.isChecked():
          PORTA_PIN0_CONFIG.text = "HIGH"
        else:
          PORTA_PIN0_CONFIG.text = "LOW"
      else:		
        PORTA_PIN0_DIR.text = "INPUT"
        if self.pul_upA0.isChecked():
          PORTA_PIN0_CONFIG.text = "PULL_UP"
        else:
          PORTA_PIN0_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputA1.isChecked():
        PORTA_PIN1_DIR.text = "OUTPUT"
        if self.highA1.isChecked():
          PORTA_PIN1_CONFIG.text = "HIGH"
        else:
          PORTA_PIN1_CONFIG.text = "LOW"
      else:		
        PORTA_PIN1_DIR.text = "INPUT"
        if self.pul_upA1.isChecked():
          PORTA_PIN1_CONFIG.text = "PULL_UP"
        else:
          PORTA_PIN1_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputA2.isChecked():
        PORTA_PIN2_DIR.text = "OUTPUT"
        if self.highA2.isChecked():
          PORTA_PIN2_CONFIG.text = "HIGH"
        else:
          PORTA_PIN2_CONFIG.text = "LOW"
      else:		
        PORTA_PIN2_DIR.text = "INPUT"
        if self.pul_upA2.isChecked():
          PORTA_PIN2_CONFIG.text = "PULL_UP"
        else:
          PORTA_PIN2_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputA3.isChecked():
        PORTA_PIN3_DIR.text = "OUTPUT"
        if self.highA3.isChecked():
          PORTA_PIN2_CONFIG.text = "HIGH"
        else:
          PORTA_PIN3_CONFIG.text = "LOW"
      else:		
        PORTA_PIN3_DIR.text = "INPUT"
        if self.pul_upA3.isChecked():
          PORTA_PIN3_CONFIG.text = "PULL_UP"
        else:
          PORTA_PIN3_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputA4.isChecked():
        PORTA_PIN4_DIR.text = "OUTPUT"
        if self.highA4.isChecked():
          PORTA_PIN4_CONFIG.text = "HIGH"
        else:
          PORTA_PIN4_CONFIG.text = "LOW"
      else:		
        PORTA_PIN4_DIR.text = "INPUT"
        if self.pul_upA4.isChecked():
          PORTA_PIN4_CONFIG.text = "PULL_UP"
        else:
          PORTA_PIN4_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputA5.isChecked():
        PORTA_PIN5_DIR.text = "OUTPUT"
        if self.highA5.isChecked():
          PORTA_PIN5_CONFIG.text = "HIGH"
        else:
          PORTA_PIN5_CONFIG.text = "LOW"
      else:		
        PORTA_PIN5_DIR.text = "INPUT"
        if self.pul_upA5.isChecked():
          PORTA_PIN5_CONFIG.text = "PULL_UP"
        else:
          PORTA_PIN5_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputA6.isChecked():
        PORTA_PIN6_DIR.text = "OUTPUT"
        if self.highA6.isChecked():
          PORTA_PIN6_CONFIG.text = "HIGH"
        else:
          PORTA_PIN6_CONFIG.text = "LOW"
      else:		
        PORTA_PIN6_DIR.text = "INPUT"
        if self.pul_upA6.isChecked():
          PORTA_PIN6_CONFIG.text = "PULL_UP"
        else:
          PORTA_PIN6_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputA7.isChecked():
        PORTA_PIN7_DIR.text = "OUTPUT"
        if self.highA7.isChecked():
          PORTA_PIN7_CONFIG.text = "HIGH"
        else:
          PORTA_PIN7_CONFIG.text = "LOW"
      else:		
        PORTA_PIN7_DIR.text = "INPUT"
        if self.pul_upA7.isChecked():
          PORTA_PIN7_CONFIG.text = "PULL_UP"
        else:
          PORTA_PIN7_CONFIG.text = "HIGH_IMP"
      #################################################
      DIO.append(PORTA)
      PORTA.append(PORTA_PIN0)
      PORTA_PIN0.append(PORTA_PIN0_DIR)
      PORTA_PIN0.append(PORTA_PIN0_CONFIG)
      PORTA.append(PORTA_PIN1)
      PORTA_PIN1.append(PORTA_PIN1_DIR)
      PORTA_PIN1.append(PORTA_PIN1_CONFIG)
      PORTA.append(PORTA_PIN2)
      PORTA_PIN2.append(PORTA_PIN2_DIR)
      PORTA_PIN2.append(PORTA_PIN2_CONFIG)
      PORTA.append(PORTA_PIN3)
      PORTA_PIN3.append(PORTA_PIN3_DIR)
      PORTA_PIN3.append(PORTA_PIN3_CONFIG)
      PORTA.append(PORTA_PIN4)
      PORTA_PIN4.append(PORTA_PIN4_DIR)
      PORTA_PIN4.append(PORTA_PIN4_CONFIG)
      PORTA.append(PORTA_PIN5)
      PORTA_PIN5.append(PORTA_PIN5_DIR)
      PORTA_PIN5.append(PORTA_PIN5_CONFIG)
      PORTA.append(PORTA_PIN6)
      PORTA_PIN6.append(PORTA_PIN6_DIR)
      PORTA_PIN6.append(PORTA_PIN6_CONFIG)
      PORTA.append(PORTA_PIN7)
      PORTA_PIN7.append(PORTA_PIN7_DIR)
      PORTA_PIN7.append(PORTA_PIN7_CONFIG)
      
      
      ############################################################################################################
      
      PORTB = ET.Element("PORTB")
      PORTB_PIN0 = ET.Element("PINB0")
      PORTB_PIN1 = ET.Element("PINB1")
      PORTB_PIN2 = ET.Element("PINB2")
      PORTB_PIN3 = ET.Element("PINB3")
      PORTB_PIN4 = ET.Element("PINB4")
      PORTB_PIN5 = ET.Element("PINB5")
      PORTB_PIN6 = ET.Element("PINB6")
      PORTB_PIN7 = ET.Element("PINB7")
      
      PORTB_PIN0_DIR = ET.Element("DIR")      
      PORTB_PIN0_CONFIG = ET.Element("CONFIG")
      PORTB_PIN1_DIR = ET.Element("DIR")      
      PORTB_PIN1_CONFIG = ET.Element("CONFIG")
      PORTB_PIN2_DIR = ET.Element("DIR")      
      PORTB_PIN2_CONFIG = ET.Element("CONFIG")
      PORTB_PIN3_DIR = ET.Element("DIR")      
      PORTB_PIN3_CONFIG = ET.Element("CONFIG")
      PORTB_PIN4_DIR = ET.Element("DIR")      
      PORTB_PIN4_CONFIG = ET.Element("CONFIG")
      PORTB_PIN5_DIR = ET.Element("DIR")      
      PORTB_PIN5_CONFIG = ET.Element("CONFIG")
      PORTB_PIN6_DIR = ET.Element("DIR")      
      PORTB_PIN6_CONFIG = ET.Element("CONFIG")
      PORTB_PIN7_DIR = ET.Element("DIR")      
      PORTB_PIN7_CONFIG = ET.Element("CONFIG")
      
      
      if self.outputB0.isChecked():
        PORTB_PIN0_DIR.text = "OUTPUT"
        if self.highB0.isChecked():
          PORTB_PIN0_CONFIG.text = "HIGH"
        else:
          PORTB_PIN0_CONFIG.text = "LOW"
      else:		
        PORTB_PIN0_DIR.text = "INPUT"
        if self.pul_upB0.isChecked():
          PORTB_PIN0_CONFIG.text = "PULL_UP"
        else:
          PORTB_PIN0_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputB1.isChecked():
        PORTB_PIN1_DIR.text = "OUTPUT"
        if self.highB1.isChecked():
          PORTB_PIN1_CONFIG.text = "HIGH"
        else:
          PORTB_PIN1_CONFIG.text = "LOW"
      else:		
        PORTB_PIN1_DIR.text = "INPUT"
        if self.pul_upB1.isChecked():
          PORTB_PIN1_CONFIG.text = "PULL_UP"
        else:
          PORTB_PIN1_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputB2.isChecked():
        PORTB_PIN2_DIR.text = "OUTPUT"
        if self.highB2.isChecked():
          PORTB_PIN2_CONFIG.text = "HIGH"
        else:
          PORTB_PIN2_CONFIG.text = "LOW"
      else:		
        PORTB_PIN2_DIR.text = "INPUT"
        if self.pul_upB2.isChecked():
          PORTB_PIN2_CONFIG.text = "PULL_UP"
        else:
          PORTB_PIN2_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputB3.isChecked():
        PORTB_PIN3_DIR.text = "OUTPUT"
        if self.highB3.isChecked():
          PORTB_PIN2_CONFIG.text = "HIGH"
        else:
          PORTB_PIN3_CONFIG.text = "LOW"
      else:		
        PORTB_PIN3_DIR.text = "INPUT"
        if self.pul_upB3.isChecked():
          PORTB_PIN3_CONFIG.text = "PULL_UP"
        else:
          PORTB_PIN3_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputB4.isChecked():
        PORTB_PIN4_DIR.text = "OUTPUT"
        if self.highB4.isChecked():
          PORTB_PIN4_CONFIG.text = "HIGH"
        else:
          PORTB_PIN4_CONFIG.text = "LOW"
      else:		
        PORTB_PIN4_DIR.text = "INPUT"
        if self.pul_upB4.isChecked():
          PORTB_PIN4_CONFIG.text = "PULL_UP"
        else:
          PORTB_PIN4_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputB5.isChecked():
        PORTB_PIN5_DIR.text = "OUTPUT"
        if self.highB5.isChecked():
          PORTB_PIN5_CONFIG.text = "HIGH"
        else:
          PORTB_PIN5_CONFIG.text = "LOW"
      else:		
        PORTB_PIN5_DIR.text = "INPUT"
        if self.pul_upB5.isChecked():
          PORTB_PIN5_CONFIG.text = "PULL_UP"
        else:
          PORTB_PIN5_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputB6.isChecked():
        PORTB_PIN6_DIR.text = "OUTPUT"
        if self.highB6.isChecked():
          PORTB_PIN6_CONFIG.text = "HIGH"
        else:
          PORTB_PIN6_CONFIG.text = "LOW"
      else:		
        PORTB_PIN6_DIR.text = "INPUT"
        if self.pul_upB6.isChecked():
          PORTB_PIN6_CONFIG.text = "PULL_UP"
        else:
          PORTB_PIN6_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputB7.isChecked():
        PORTB_PIN7_DIR.text = "OUTPUT"
        if self.highB7.isChecked():
          PORTB_PIN7_CONFIG.text = "HIGH"
        else:
          PORTB_PIN7_CONFIG.text = "LOW"
      else:		
        PORTB_PIN7_DIR.text = "INPUT"
        if self.pul_upB7.isChecked():
          PORTB_PIN7_CONFIG.text = "PULL_UP"
        else:
          PORTB_PIN7_CONFIG.text = "HIGH_IMP"
          ###############################################3
      DIO.append(PORTB)
      PORTB.append(PORTB_PIN0)
      PORTB_PIN0.append(PORTB_PIN0_DIR)
      PORTB_PIN0.append(PORTB_PIN0_CONFIG)
      PORTB.append(PORTB_PIN1)
      PORTB_PIN1.append(PORTB_PIN1_DIR)
      PORTB_PIN1.append(PORTB_PIN1_CONFIG)
      PORTB.append(PORTB_PIN2)
      PORTB_PIN2.append(PORTB_PIN2_DIR)
      PORTB_PIN2.append(PORTB_PIN2_CONFIG)
      PORTB.append(PORTB_PIN3)
      PORTB_PIN3.append(PORTB_PIN3_DIR)
      PORTB_PIN3.append(PORTB_PIN3_CONFIG)
      PORTB.append(PORTB_PIN4)
      PORTB_PIN4.append(PORTB_PIN4_DIR)
      PORTB_PIN4.append(PORTB_PIN4_CONFIG)
      PORTB.append(PORTB_PIN5)
      PORTB_PIN5.append(PORTB_PIN5_DIR)
      PORTB_PIN5.append(PORTB_PIN5_CONFIG)
      PORTB.append(PORTB_PIN6)
      PORTB_PIN6.append(PORTB_PIN6_DIR)
      PORTB_PIN6.append(PORTB_PIN6_CONFIG)
      PORTB.append(PORTB_PIN7)
      PORTB_PIN7.append(PORTB_PIN7_DIR)
      PORTB_PIN7.append(PORTB_PIN7_CONFIG)
      ##############################################################################
      
      PORTC = ET.Element("PORTC")
      PORTC_PIN0 = ET.Element("PINC0")
      PORTC_PIN1 = ET.Element("PINC1")
      PORTC_PIN2 = ET.Element("PINC2")
      PORTC_PIN3 = ET.Element("PINC3")
      PORTC_PIN4 = ET.Element("PINC4")
      PORTC_PIN5 = ET.Element("PINC5")
      PORTC_PIN6 = ET.Element("PINC6")
      PORTC_PIN7 = ET.Element("PINC7")
          
      PORTC_PIN0_DIR = ET.Element("DIR")      
      PORTC_PIN0_CONFIG = ET.Element("CONFIG")
      PORTC_PIN1_DIR = ET.Element("DIR")      
      PORTC_PIN1_CONFIG = ET.Element("CONFIG")
      PORTC_PIN2_DIR = ET.Element("DIR")      
      PORTC_PIN2_CONFIG = ET.Element("CONFIG")
      PORTC_PIN3_DIR = ET.Element("DIR")      
      PORTC_PIN3_CONFIG = ET.Element("CONFIG")
      PORTC_PIN4_DIR = ET.Element("DIR")      
      PORTC_PIN4_CONFIG = ET.Element("CONFIG")
      PORTC_PIN5_DIR = ET.Element("DIR")      
      PORTC_PIN5_CONFIG = ET.Element("CONFIG")
      PORTC_PIN6_DIR = ET.Element("DIR")      
      PORTC_PIN6_CONFIG = ET.Element("CONFIG")
      PORTC_PIN7_DIR = ET.Element("DIR")      
      PORTC_PIN7_CONFIG = ET.Element("CONFIG")
      
      
      if self.outputC0.isChecked():
        PORTC_PIN0_DIR.text = "OUTPUT"
        if self.highC0.isChecked():
          PORTC_PIN0_CONFIG.text = "HIGH"
        else:
          PORTC_PIN0_CONFIG.text = "LOW"
      else:		
        PORTC_PIN0_DIR.text = "INPUT"
        if self.pul_upC0.isChecked():
          PORTC_PIN0_CONFIG.text = "PULL_UP"
        else:
          PORTC_PIN0_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputC1.isChecked():
        PORTC_PIN1_DIR.text = "OUTPUT"
        if self.highC1.isChecked():
          PORTC_PIN1_CONFIG.text = "HIGH"
        else:
          PORTC_PIN1_CONFIG.text = "LOW"
      else:		
        PORTC_PIN1_DIR.text = "INPUT"
        if self.pul_upC1.isChecked():
          PORTC_PIN1_CONFIG.text = "PULL_UP"
        else:
          PORTC_PIN1_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputC2.isChecked():
        PORTC_PIN2_DIR.text = "OUTPUT"
        if self.highC2.isChecked():
          PORTC_PIN2_CONFIG.text = "HIGH"
        else:
          PORTC_PIN2_CONFIG.text = "LOW"
      else:		
        PORTC_PIN2_DIR.text = "INPUT"
        if self.pul_upC2.isChecked():
          PORTC_PIN2_CONFIG.text = "PULL_UP"
        else:
          PORTC_PIN2_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputC3.isChecked():
        PORTC_PIN3_DIR.text = "OUTPUT"
        if self.highC3.isChecked():
          PORTC_PIN2_CONFIG.text = "HIGH"
        else:
          PORTC_PIN3_CONFIG.text = "LOW"
      else:		
        PORTC_PIN3_DIR.text = "INPUT"
        if self.pul_upC3.isChecked():
          PORTC_PIN3_CONFIG.text = "PULL_UP"
        else:
          PORTC_PIN3_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputC4.isChecked():
        PORTC_PIN4_DIR.text = "OUTPUT"
        if self.highC4.isChecked():
          PORTC_PIN4_CONFIG.text = "HIGH"
        else:
          PORTC_PIN4_CONFIG.text = "LOW"
      else:		
        PORTC_PIN4_DIR.text = "INPUT"
        if self.pul_upC4.isChecked():
          PORTC_PIN4_CONFIG.text = "PULL_UP"
        else:
          PORTC_PIN4_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputC5.isChecked():
        PORTC_PIN5_DIR.text = "OUTPUT"
        if self.highC5.isChecked():
          PORTC_PIN5_CONFIG.text = "HIGH"
        else:
          PORTC_PIN5_CONFIG.text = "LOW"
      else:		
        PORTC_PIN5_DIR.text = "INPUT"
        if self.pul_upC5.isChecked():
          PORTC_PIN5_CONFIG.text = "PULL_UP"
        else:
          PORTC_PIN5_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputC6.isChecked():
        PORTC_PIN6_DIR.text = "OUTPUT"
        if self.highC6.isChecked():
          PORTC_PIN6_CONFIG.text = "HIGH"
        else:
          PORTC_PIN6_CONFIG.text = "LOW"
      else:		
        PORTC_PIN6_DIR.text = "INPUT"
        if self.pul_upC6.isChecked():
          PORTC_PIN6_CONFIG.text = "PULL_UP"
        else:
          PORTC_PIN6_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputC7.isChecked():
        PORTC_PIN7_DIR.text = "OUTPUT"
        if self.highC7.isChecked():
          PORTC_PIN7_CONFIG.text = "HIGH"
        else:
          PORTC_PIN7_CONFIG.text = "LOW"
      else:		
        PORTC_PIN7_DIR.text = "INPUT"
        if self.pul_upC7.isChecked():
          PORTC_PIN7_CONFIG.text = "PULL_UP"
        else:
          PORTC_PIN7_CONFIG.text = "HIGH_IMP"
      ##############################################
      DIO.append(PORTC)
      PORTC.append(PORTC_PIN0)
      PORTC_PIN0.append(PORTC_PIN0_DIR)
      PORTC_PIN0.append(PORTC_PIN0_CONFIG)
      PORTC.append(PORTC_PIN1)
      PORTC_PIN1.append(PORTC_PIN1_DIR)
      PORTC_PIN1.append(PORTC_PIN1_CONFIG)
      PORTC.append(PORTC_PIN2)
      PORTC_PIN2.append(PORTC_PIN2_DIR)
      PORTC_PIN2.append(PORTC_PIN2_CONFIG)
      PORTC.append(PORTC_PIN3)
      PORTC_PIN3.append(PORTC_PIN3_DIR)
      PORTC_PIN3.append(PORTC_PIN3_CONFIG)
      PORTC.append(PORTC_PIN4)
      PORTC_PIN4.append(PORTC_PIN4_DIR)
      PORTC_PIN4.append(PORTC_PIN4_CONFIG)
      PORTC.append(PORTC_PIN5)
      PORTC_PIN5.append(PORTC_PIN5_DIR)
      PORTC_PIN5.append(PORTC_PIN5_CONFIG)
      PORTC.append(PORTC_PIN6)
      PORTC_PIN6.append(PORTC_PIN6_DIR)
      PORTC_PIN6.append(PORTC_PIN6_CONFIG)
      PORTC.append(PORTC_PIN7)
      PORTC_PIN7.append(PORTC_PIN7_DIR)
      PORTC_PIN7.append(PORTC_PIN7_CONFIG)
      ##############################################################################
      
      PORTD = ET.Element("PORTD")
      PORTD_PIN0 = ET.Element("PIND0")
      PORTD_PIN1 = ET.Element("PIND1")
      PORTD_PIN2 = ET.Element("PIND2")
      PORTD_PIN3 = ET.Element("PIND3")
      PORTD_PIN4 = ET.Element("PIND4")
      PORTD_PIN5 = ET.Element("PIND5")
      PORTD_PIN6 = ET.Element("PIND6")
      PORTD_PIN7 = ET.Element("PIND7")
          
      PORTD_PIN0_DIR = ET.Element("DIR")      
      PORTD_PIN0_CONFIG = ET.Element("CONFIG")
      PORTD_PIN1_DIR = ET.Element("DIR")      
      PORTD_PIN1_CONFIG = ET.Element("CONFIG")
      PORTD_PIN2_DIR = ET.Element("DIR")      
      PORTD_PIN2_CONFIG = ET.Element("CONFIG")
      PORTD_PIN3_DIR = ET.Element("DIR")      
      PORTD_PIN3_CONFIG = ET.Element("CONFIG")
      PORTD_PIN4_DIR = ET.Element("DIR")      
      PORTD_PIN4_CONFIG = ET.Element("CONFIG")
      PORTD_PIN5_DIR = ET.Element("DIR")      
      PORTD_PIN5_CONFIG = ET.Element("CONFIG")
      PORTD_PIN6_DIR = ET.Element("DIR")      
      PORTD_PIN6_CONFIG = ET.Element("CONFIG")
      PORTD_PIN7_DIR = ET.Element("DIR")      
      PORTD_PIN7_CONFIG = ET.Element("CONFIG")
      

      if self.outputD0.isChecked():
        PORTD_PIN0_DIR.text = "OUTPUT"
        if self.highD0.isCheCked():
          PORTD_PIN0_CONFIG.text = "HIGH"
        else:
          PORTD_PIN0_CONFIG.text = "LOW"
      else:		
        PORTD_PIN0_DIR.text = "INPUT"
        if self.pul_upD0.isChecked():
          PORTD_PIN0_CONFIG.text = "PULL_UP"
        else:
          PORTD_PIN0_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputD1.isChecked():
        PORTD_PIN1_DIR.text = "OUTPUT"
        if self.highD1.isChecked():
          PORTD_PIN1_CONFIG.text = "HIGH"
        else:
          PORTD_PIN1_CONFIG.text = "LOW"
      else:		
        PORTD_PIN1_DIR.text = "INPUT"
        if self.pul_upD1.isChecked():
          PORTD_PIN1_CONFIG.text = "PULL_UP"
        else:
          PORTD_PIN1_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputD2.isChecked():
        PORTD_PIN2_DIR.text = "OUTPUT"
        if self.highD2.isChecked():
          PORTD_PIN2_CONFIG.text = "HIGH"
        else:
          PORTD_PIN2_CONFIG.text = "LOW"
      else:		
        PORTD_PIN2_DIR.text = "INPUT"
        if self.pul_upD2.isChecked():
          PORTD_PIN2_CONFIG.text = "PULL_UP"
        else:
          PORTD_PIN2_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputD3.isChecked():
        PORTD_PIN3_DIR.text = "OUTPUT"
        if self.highD3.isChecked():
          PORTD_PIN2_CONFIG.text = "HIGH"
        else:
          PORTD_PIN3_CONFIG.text = "LOW"
      else:		
        PORTD_PIN3_DIR.text = "INPUT"
        if self.pul_upD3.isChecked():
          PORTD_PIN3_CONFIG.text = "PULL_UP"
        else:
          PORTD_PIN3_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputD4.isChecked():
        PORTD_PIN4_DIR.text = "OUTPUT"
        if self.highD4.isChecked():
          PORTD_PIN4_CONFIG.text = "HIGH"
        else:
          PORTD_PIN4_CONFIG.text = "LOW"
      else:		
        PORTD_PIN4_DIR.text = "INPUT"
        if self.pul_upD4.isChecked():
          PORTD_PIN4_CONFIG.text = "PULL_UP"
        else:
          PORTD_PIN4_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputD5.isChecked():
        PORTD_PIN5_DIR.text = "OUTPUT"
        if self.highD5.isChecked():
          PORTD_PIN5_CONFIG.text = "HIGH"
        else:
          PORTD_PIN5_CONFIG.text = "LOW"
      else:		
        PORTD_PIN5_DIR.text = "INPUT"
        if self.pul_upD5.isChecked():
          PORTD_PIN5_CONFIG.text = "PULL_UP"
        else:
          PORTD_PIN5_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputD6.isChecked():
        PORTD_PIN6_DIR.text = "OUTPUT"
        if self.highD6.isChecked():
          PORTD_PIN6_CONFIG.text = "HIGH"
        else:
          PORTD_PIN6_CONFIG.text = "LOW"
      else:		
        PORTD_PIN6_DIR.text = "INPUT"
        if self.pul_upD6.isChecked():
          PORTD_PIN6_CONFIG.text = "PULL_UP"
        else:
          PORTD_PIN6_CONFIG.text = "HIGH_IMP"
		  ######################################################
      if self.outputD7.isChecked():
        PORTD_PIN7_DIR.text = "OUTPUT"
        if self.highD7.isChecked():
          PORTD_PIN7_CONFIG.text = "HIGH"
        else:
          PORTD_PIN7_CONFIG.text = "LOW"
      else:		
        PORTD_PIN7_DIR.text = "INPUT"
        if self.pul_upD7.isChecked():
          PORTD_PIN7_CONFIG.text = "PULL_UP"
        else:
          PORTD_PIN7_CONFIG.text = "HIGH_IMP"
      #####################################################
      DIO.append(PORTD)
      PORTD.append(PORTD_PIN0)
      PORTD_PIN0.append(PORTD_PIN0_DIR)
      PORTD_PIN0.append(PORTD_PIN0_CONFIG)
      PORTD.append(PORTD_PIN1)
      PORTD_PIN1.append(PORTD_PIN1_DIR)
      PORTD_PIN1.append(PORTD_PIN1_CONFIG)
      PORTD.append(PORTD_PIN2)
      PORTD_PIN2.append(PORTD_PIN2_DIR)
      PORTD_PIN2.append(PORTD_PIN2_CONFIG)
      PORTD.append(PORTD_PIN3)
      PORTD_PIN3.append(PORTD_PIN3_DIR)
      PORTD_PIN3.append(PORTD_PIN3_CONFIG)
      PORTD.append(PORTD_PIN4)
      PORTD_PIN4.append(PORTD_PIN4_DIR)
      PORTD_PIN4.append(PORTD_PIN4_CONFIG)
      PORTD.append(PORTD_PIN5)
      PORTD_PIN5.append(PORTD_PIN5_DIR)
      PORTD_PIN5.append(PORTD_PIN5_CONFIG)
      PORTD.append(PORTD_PIN6)
      PORTD_PIN6.append(PORTD_PIN6_DIR)
      PORTD_PIN6.append(PORTD_PIN6_CONFIG)
      PORTD.append(PORTD_PIN7)
      PORTD_PIN7.append(PORTD_PIN7_DIR)
      PORTD_PIN7.append(PORTD_PIN7_CONFIG)
      #################################################################
      
      output_path =self.path.text()+r'\DioTEST_cfg.xml'
      File_Handler2 = open (output_path,'w')
      File_Handler2.write(ET.tostring(DIO,pretty_print=True).decode())
      File_Handler2.close()
      
      
      
      
      
      
    def loadFunction(self):  
    
      output_path =self.path.text()+r'\DioTEST_cfg.xml'
      tree = ET.parse(output_path)
      DIO=tree.getroot()
      
      port=DIO.find('PORTA')
      pin=port.find('PINA0')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir == "OUTPUT":
        self.outputA0.setChecked(True)
        self.outputConfigA0.setEnabled(True)
        self.inputConfidA0.setDisabled(True)
        if config == "HIGH":
          self.highA0.setChecked(True)
        else:
          self.lowA0.setChecked(True)	
      else:
        self.inputA0.setChecked(True)
        self.outputConfigA0.setDisabled(True)
        self.inputConfidA0.setEnabled(True)
        if config == "PULL_UP":
          self.pul_upA0.setChecked(True)
        else:
          self.high_impedenceA0.setChecked(True)
      ###################################################
      port=DIO.find('PORTA')
      pin=port.find('PINA1')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputA1.setChecked(True)
        self.outputConfigA1.setEnabled(True)
        self.inputConfidA1.setDisabled(True)
        if config =='HIGH':
          self.highA1.setChecked(True)
        else:
          self.lowA1.setChecked(True)	
      else:
        self.inputA1.setChecked(True)
        self.outputConfigA1.setDisabled(True)
        self.inputConfidA1.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upA1.setChecked(True)
        else:
          self.high_impedenceA1.setChecked(True)
      ###################################################
      port=DIO.find('PORTA')
      pin=port.find('PINA2')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputA2.setChecked(True)
        self.outputConfigA2.setEnabled(True)
        self.inputConfidA2.setDisabled(True)
        if config =='HIGH':
          self.highA2.setChecked(True)
        else:
          self.lowA2.setChecked(True)	
      else:
        self.inputA2.setChecked(True)
        self.outputConfigA2.setDisabled(True)
        self.inputConfidA2.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upA2.setChecked(True)
        else:
          self.high_impedenceA2.setChecked(True)
      ###################################################
      port=DIO.find('PORTA')
      pin=port.find('PINA3')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputA3.setChecked(True)
        self.outputConfigA3.setEnabled(True)
        self.inputConfidA3.setDisabled(True)
        if config =='HIGH':
          self.highA3.setChecked(True)
        else:
          self.lowA3.setChecked(True)	
      else:
        self.inputA3.setChecked(True)
        self.outputConfigA3.setDisabled(True)
        self.inputConfidA3.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upA3.setChecked(True)
        else:
          self.high_impedenceA3.setChecked(True)
      ###################################################
      port=DIO.find('PORTA')
      pin=port.find('PINA4')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputA4.setChecked(True)
        self.outputConfigA4.setEnabled(True)
        self.inputConfidA4.setDisabled(True)
        if config =='HIGH':
          self.highA4.setChecked(True)
        else:
          self.lowA4.setChecked(True)	
      else:
        self.inputA4.setChecked(True)
        self.outputConfigA4.setDisabled(True)
        self.inputConfidA4.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upA4.setChecked(True)
        else:
          self.high_impedenceA4.setChecked(True)
      ###################################################
      port=DIO.find('PORTA')
      pin=port.find('PINA5')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputA5.setChecked(True)
        self.outputConfigA5.setEnabled(True)
        self.inputConfidA5.setDisabled(True)
        if config =='HIGH':
          self.highA5.setChecked(True)
        else:
          self.lowA5.setChecked(True)	
      else:
        self.inputA5.setChecked(True)
        self.outputConfigA5.setDisabled(True)
        self.inputConfidA5.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upA5.setChecked(True)
        else:
          self.high_impedenceA5.setChecked(True)
      ###################################################
      port=DIO.find('PORTA')
      pin=port.find('PINA6')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputA6.setChecked(True)
        self.outputConfigA6.setEnabled(True)
        self.inputConfidA6.setDisabled(True)
        if config =='HIGH':
          self.highA6.setChecked(True)
        else:
          self.lowA6.setChecked(True)	
      else:
        self.inputA6.setChecked(True)
        self.outputConfigA6.setDisabled(True)
        self.inputConfidA6.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upA6.setChecked(True)
        else:
          self.high_impedenceA6.setChecked(True)
      ###################################################
      port=DIO.find('PORTA')
      pin=port.find('PINA7')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputA7.setChecked(True)
        self.outputConfigA7.setEnabled(True)
        self.inputConfidA7.setDisabled(True)
        if config =='HIGH':
          self.highA7.setChecked(True)
        else:
          self.lowA7.setChecked(True)	
      else:
        self.inputA7.setChecked(True)
        self.outputConfigA7.setDisabled(True)
        self.inputConfidA7.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upA7.setChecked(True)
        else:
          self.high_impedenceA7.setChecked(True)
      ###################################################
      ###################################################
      ###################################################
      port=DIO.find('PORTB')
      pin=port.find('PINB0')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir == "OUTPUT":
        self.outputB0.setChecked(True)
        self.outputConfigB0.setEnabled(True)
        self.inputConfidB0.setDisabled(True)
        if config == "HIGH":
          self.highB0.setChecked(True)
        else:
          self.lowB0.setChecked(True)	
      else:
        self.inputB0.setChecked(True)
        self.outputConfigB0.setDisabled(True)
        self.inputConfidB0.setEnabled(True)
        if config == "PULL_UP":
          self.pul_upB0.setChecked(True)
        else:
          self.high_impedenceB0.setChecked(True)
      ###################################################
      port=DIO.find('PORTB')
      pin=port.find('PINB1')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputB1.setChecked(True)
        self.outputConfigB1.setEnabled(True)
        self.inputConfidB1.setDisabled(True)
        if config =='HIGH':
          self.highB1.setChecked(True)
        else:
          self.lowB1.setChecked(True)	
      else:
        self.inputB1.setChecked(True)
        self.outputConfigB1.setDisabled(True)
        self.inputConfidB1.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upB1.setChecked(True)
        else:
          self.high_impedenceB1.setChecked(True)
      ###################################################
      port=DIO.find('PORTB')
      pin=port.find('PINB2')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputB2.setChecked(True)
        self.outputConfigB2.setEnabled(True)
        self.inputConfidB2.setDisabled(True)
        if config =='HIGH':
          self.highB2.setChecked(True)
        else:
          self.lowB2.setChecked(True)	
      else:
        self.inputB2.setChecked(True)
        self.outputConfigB2.setDisabled(True)
        self.inputConfidB2.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upB2.setChecked(True)
        else:
          self.high_impedenceB2.setChecked(True)
      ###################################################
      port=DIO.find('PORTB')
      pin=port.find('PINB3')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputB3.setChecked(True)
        self.outputConfigB3.setEnabled(True)
        self.inputConfidB3.setDisabled(True)
        if config =='HIGH':
          self.highB3.setChecked(True)
        else:
          self.lowB3.setChecked(True)	
      else:
        self.inputB3.setChecked(True)
        self.outputConfigB3.setDisabled(True)
        self.inputConfidB3.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upB3.setChecked(True)
        else:
          self.high_impedenceB3.setChecked(True)
      ###################################################
      port=DIO.find('PORTB')
      pin=port.find('PINB4')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputB4.setChecked(True)
        self.outputConfigB4.setEnabled(True)
        self.inputConfidB4.setDisabled(True)
        if config =='HIGH':
          self.highB4.setChecked(True)
        else:
          self.lowB4.setChecked(True)	
      else:
        self.inputB4.setChecked(True)
        self.outputConfigB4.setDisabled(True)
        self.inputConfidB4.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upB4.setChecked(True)
        else:
          self.high_impedenceB4.setChecked(True)
      ###################################################
      port=DIO.find('PORTB')
      pin=port.find('PINB5')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputB5.setChecked(True)
        self.outputConfigB5.setEnabled(True)
        self.inputConfidB5.setDisabled(True)
        if config =='HIGH':
          self.highB5.setChecked(True)
        else:
          self.lowB5.setChecked(True)	
      else:
        self.inputB5.setChecked(True)
        self.outputConfigB5.setDisabled(True)
        self.inputConfidB5.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upB5.setChecked(True)
        else:
          self.high_impedenceB5.setChecked(True)
      ###################################################
      port=DIO.find('PORTB')
      pin=port.find('PINB6')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputB6.setChecked(True)
        self.outputConfigB6.setEnabled(True)
        self.inputConfidB6.setDisabled(True)
        if config =='HIGH':
          self.highB6.setChecked(True)
        else:
          self.lowB6.setChecked(True)	
      else:
        self.inputB6.setChecked(True)
        self.outputConfigB6.setDisabled(True)
        self.inputConfidB6.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upB6.setChecked(True)
        else:
          self.high_impedenceB6.setChecked(True)
      ###################################################
      port=DIO.find('PORTB')
      pin=port.find('PINB7')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputB7.setChecked(True)
        self.outputConfigB7.setEnabled(True)
        self.inputConfidB7.setDisabled(True)
        if config =='HIGH':
          self.highB7.setChecked(True)
        else:
          self.lowB7.setChecked(True)	
      else:
        self.inputB7.setChecked(True)
        self.outputConfigB7.setDisabled(True)
        self.inputConfidB7.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upB7.setChecked(True)
        else:
          self.high_impedenceB7.setChecked(True)
      ###################################################
      ###################################################
      ###################################################
      port=DIO.find('PORTC')
      pin=port.find('PINC0')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir == "OUTPUT":
        self.outputC0.setChecked(True)
        self.outputConfigC0.setEnabled(True)
        self.inputConfidC0.setDisabled(True)
        if config == "HIGH":
          self.highC0.setChecked(True)
        else:
          self.lowC0.setChecked(True)	
      else:
        self.inputC0.setChecked(True)
        self.outputConfigC0.setDisabled(True)
        self.inputConfidC0.setEnabled(True)
        if config == "PULL_UP":
          self.pul_upC0.setChecked(True)
        else:
          self.high_impedenceC0.setChecked(True)
      ###################################################
      port=DIO.find('PORTC')
      pin=port.find('PINC1')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputC1.setChecked(True)
        self.outputConfigC1.setEnabled(True)
        self.inputConfidC1.setDisabled(True)
        if config =='HIGH':
          self.highC1.setChecked(True)
        else:
          self.lowC1.setChecked(True)	
      else:
        self.inputC1.setChecked(True)
        self.outputConfigC1.setDisabled(True)
        self.inputConfidC1.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upC1.setChecked(True)
        else:
          self.high_impedenceC1.setChecked(True)
      ###################################################
      port=DIO.find('PORTC')
      pin=port.find('PINC2')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputC2.setChecked(True)
        self.outputConfigC2.setEnabled(True)
        self.inputConfidC2.setDisabled(True)
        if config =='HIGH':
          self.highC2.setChecked(True)
        else:
          self.lowC2.setChecked(True)	
      else:
        self.inputC2.setChecked(True)
        self.outputConfigC2.setDisabled(True)
        self.inputConfidC2.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upC2.setChecked(True)
        else:
          self.high_impedenceC2.setChecked(True)
      ###################################################
      port=DIO.find('PORTC')
      pin=port.find('PINC3')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputC3.setChecked(True)
        self.outputConfigC3.setEnabled(True)
        self.inputConfidC3.setDisabled(True)
        if config =='HIGH':
          self.highC3.setChecked(True)
        else:
          self.lowC3.setChecked(True)	
      else:
        self.inputC3.setChecked(True)
        self.outputConfigC3.setDisabled(True)
        self.inputConfidC3.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upC3.setChecked(True)
        else:
          self.high_impedenceC3.setChecked(True)
      ###################################################
      port=DIO.find('PORTC')
      pin=port.find('PINC4')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputC4.setChecked(True)
        self.outputConfigC4.setEnabled(True)
        self.inputConfidC4.setDisabled(True)
        if config =='HIGH':
          self.highC4.setChecked(True)
        else:
          self.lowC4.setChecked(True)	
      else:
        self.inputC4.setChecked(True)
        self.outputConfigC4.setDisabled(True)
        self.inputConfidC4.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upC4.setChecked(True)
        else:
          self.high_impedenceC4.setChecked(True)
      ###################################################
      port=DIO.find('PORTC')
      pin=port.find('PINC5')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputC5.setChecked(True)
        self.outputConfigC5.setEnabled(True)
        self.inputConfidC5.setDisabled(True)
        if config =='HIGH':
          self.highC5.setChecked(True)
        else:
          self.lowC5.setChecked(True)	
      else:
        self.inputC5.setChecked(True)
        self.outputConfigC5.setDisabled(True)
        self.inputConfidC5.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upC5.setChecked(True)
        else:
          self.high_impedenceC5.setChecked(True)
      ###################################################
      port=DIO.find('PORTC')
      pin=port.find('PINC6')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputC6.setChecked(True)
        self.outputConfigC6.setEnabled(True)
        self.inputConfidC6.setDisabled(True)
        if config =='HIGH':
          self.highC6.setChecked(True)
        else:
          self.lowC6.setChecked(True)	
      else:
        self.inputC6.setChecked(True)
        self.outputConfigC6.setDisabled(True)
        self.inputConfidC6.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upC6.setChecked(True)
        else:
          self.high_impedenceC6.setChecked(True)
      ###################################################
      port=DIO.find('PORTC')
      pin=port.find('PINC7')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputC7.setChecked(True)
        self.outputConfigC7.setEnabled(True)
        self.inputConfidC7.setDisabled(True)
        if config =='HIGH':
          self.highC7.setChecked(True)
        else:
          self.lowC7.setChecked(True)	
      else:
        self.inputC7.setChecked(True)
        self.outputConfigC7.setDisabled(True)
        self.inputConfidC7.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upC7.setChecked(True)
        else:
          self.high_impedenceC7.setChecked(True)
      ###################################################
      port=DIO.find('PORTD')
      pin=port.find('PIND0')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir == "OUTPUT":
        self.outputD0.setChecked(True)
        self.outputConfigD0.setEnabled(True)
        self.inputConfidD0.setDisabled(True)
        if config == "HIGH":
          self.highD0.setChecked(True)
        else:
          self.lowD0.setChecked(True)	
      else:
        self.inputD0.setChecked(True)
        self.outputConfigD0.setDisabled(True)
        self.inputConfidD0.setEnabled(True)
        if config == "PULL_UP":
          self.pul_upD0.setChecked(True)
        else:
          self.high_impedenceD0.setChecked(True)
      ###################################################
      port=DIO.find('PORTD')
      pin=port.find('PIND1')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputD1.setChecked(True)
        self.outputConfigD1.setEnabled(True)
        self.inputConfidD1.setDisabled(True)
        if config =='HIGH':
          self.highD1.setChecked(True)
        else:
          self.lowD1.setChecked(True)	
      else:
        self.inputD1.setChecked(True)
        self.outputConfigD1.setDisabled(True)
        self.inputConfidD1.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upD1.setChecked(True)
        else:
          self.high_impedenceD1.setChecked(True)
      ###################################################
      port=DIO.find('PORTD')
      pin=port.find('PIND2')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputD2.setChecked(True)
        self.outputConfigD2.setEnabled(True)
        self.inputConfidD2.setDisabled(True)
        if config =='HIGH':
          self.highD2.setChecked(True)
        else:
          self.lowD2.setChecked(True)	
      else:
        self.inputD2.setChecked(True)
        self.outputConfigD2.setDisabled(True)
        self.inputConfidD2.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upD2.setChecked(True)
        else:
          self.high_impedenceD2.setChecked(True)
      ###################################################
      port=DIO.find('PORTD')
      pin=port.find('PIND3')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputD3.setChecked(True)
        self.outputConfigD3.setEnabled(True)
        self.inputConfidD3.setDisabled(True)
        if config =='HIGH':
          self.highD3.setChecked(True)
        else:
          self.lowD3.setChecked(True)	
      else:
        self.inputD3.setChecked(True)
        self.outputConfigD3.setDisabled(True)
        self.inputConfidD3.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upD3.setChecked(True)
        else:
          self.high_impedenceD3.setChecked(True)
      ###################################################
      port=DIO.find('PORTD')
      pin=port.find('PIND4')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputD4.setChecked(True)
        self.outputConfigD4.setEnabled(True)
        self.inputConfidD4.setDisabled(True)
        if config =='HIGH':
          self.highD4.setChecked(True)
        else:
          self.lowD4.setChecked(True)	
      else:
        self.inputD4.setChecked(True)
        self.outputConfigD4.setDisabled(True)
        self.inputConfidD4.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upD4.setChecked(True)
        else:
          self.high_impedenceD4.setChecked(True)
      ###################################################
      port=DIO.find('PORTD')
      pin=port.find('PIND5')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputD5.setChecked(True)
        self.outputConfigD5.setEnabled(True)
        self.inputConfidD5.setDisabled(True)
        if config =='HIGH':
          self.highD5.setChecked(True)
        else:
          self.lowD5.setChecked(True)	
      else:
        self.inputD5.setChecked(True)
        self.outputConfigD5.setDisabled(True)
        self.inputConfidD5.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upD5.setChecked(True)
        else:
          self.high_impedenceD5.setChecked(True)
      ###################################################
      port=DIO.find('PORTD')
      pin=port.find('PIND6')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputD6.setChecked(True)
        self.outputConfigD6.setEnabled(True)
        self.inputConfidD6.setDisabled(True)
        if config =='HIGH':
          self.highD6.setChecked(True)
        else:
          self.lowD6.setChecked(True)	
      else:
        self.inputD6.setChecked(True)
        self.outputConfigD6.setDisabled(True)
        self.inputConfidD6.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upD6.setChecked(True)
        else:
          self.high_impedenceD6.setChecked(True)
      ###################################################
      port=DIO.find('PORTD')
      pin=port.find('PIND7')
      dir=pin.find('DIR').text
      config=pin.find('CONFIG').text
      if dir =='OUTPUT':
        self.outputD7.setChecked(True)
        self.outputConfigD7.setEnabled(True)
        self.inputConfidD7.setDisabled(True)
        if config =='HIGH':
          self.highD7.setChecked(True)
        else:
          self.lowD7.setChecked(True)	
      else:
        self.inputD7.setChecked(True)
        self.outputConfigD7.setDisabled(True)
        self.inputConfidD7.setEnabled(True)
        if config == 'PULL_UP':
          self.pul_upD7.setChecked(True)
        else:
          self.high_impedenceD7.setChecked(True)
      ###################################################











    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(whatsthis)
        self.AVR_ATMEGA32_CONFIG.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.BoxA0.setTitle(QCoreApplication.translate("Form", u"A0", None))
        self.outputA0.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputA0.setText(QCoreApplication.translate("Form", u"Input", None))
        self.inputConfidA0.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upA0.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceA0.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.outputConfigA0.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highA0.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowA0.setText(QCoreApplication.translate("Form", u"Low", None))
        self.BoxA1.setTitle(QCoreApplication.translate("Form", u"A1", None))
        self.outputA1.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputA1.setText(QCoreApplication.translate("Form", u"Input", None))
        self.BoxA6.setTitle(QCoreApplication.translate("Form", u"A6", None))
        self.outputA6.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputA6.setText(QCoreApplication.translate("Form", u"Input", None))
        self.BoxA2.setTitle(QCoreApplication.translate("Form", u"A2", None))
        self.outputA2.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputA2.setText(QCoreApplication.translate("Form", u"Input", None))
        self.BoxA3.setTitle(QCoreApplication.translate("Form", u"A3", None))
        self.outputA3.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputA3.setText(QCoreApplication.translate("Form", u"Input", None))
        self.BoxA5.setTitle(QCoreApplication.translate("Form", u"A5", None))
        self.outputA5.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputA5.setText(QCoreApplication.translate("Form", u"Input", None))
        self.BoxA4.setTitle(QCoreApplication.translate("Form", u"A4", None))
        self.outputA4.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputA4.setText(QCoreApplication.translate("Form", u"Input", None))
        self.BoxA7.setTitle(QCoreApplication.translate("Form", u"A7", None))
        self.outputA7.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputA7.setText(QCoreApplication.translate("Form", u"Input", None))
        self.outputConfigA1.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highA1.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowA1.setText(QCoreApplication.translate("Form", u"Low", None))
        self.outputConfigA2.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highA2.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowA2.setText(QCoreApplication.translate("Form", u"Low", None))
        self.outputConfigA5.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highA5.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowA5.setText(QCoreApplication.translate("Form", u"Low", None))
        self.outputConfigA4.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highA4.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowA4.setText(QCoreApplication.translate("Form", u"Low", None))
        self.outputConfigA3.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highA3.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowA3.setText(QCoreApplication.translate("Form", u"Low", None))
        self.outputConfigA6.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highA6.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowA6.setText(QCoreApplication.translate("Form", u"Low", None))
        self.outputConfigA7.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highA7.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowA7.setText(QCoreApplication.translate("Form", u"Low", None))
        self.inputConfidA1.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upA1.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceA1.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.inputConfidA2.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upA2.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceA2.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.inputConfidA3.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upA3.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceA3.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.inputConfidA4.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upA4.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceA4.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.inputConfidA5.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upA5.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceA5.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.inputConfidA6.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upA6.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceA6.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.inputConfidA7.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upA7.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceA7.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.AVR_ATMEGA32_CONFIG.setTabText(self.AVR_ATMEGA32_CONFIG.indexOf(self.PortA), QCoreApplication.translate("Form", u"PORT-A", None))
        self.BoxB6.setTitle(QCoreApplication.translate("Form", u"B6", None))
        self.outputB6.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputB6.setText(QCoreApplication.translate("Form", u"Input", None))
        self.BoxB2.setTitle(QCoreApplication.translate("Form", u"B2", None))
        self.outputB2.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputB2.setText(QCoreApplication.translate("Form", u"Input", None))
        self.outputConfigB0.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highB0.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowB0.setText(QCoreApplication.translate("Form", u"Low", None))
        self.BoxB5.setTitle(QCoreApplication.translate("Form", u"B5", None))
        self.outputB5.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputB5.setText(QCoreApplication.translate("Form", u"Input", None))
        self.BoxB4.setTitle(QCoreApplication.translate("Form", u"B4", None))
        self.outputB4.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputB4.setText(QCoreApplication.translate("Form", u"Input", None))
        self.inputConfidB2.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upB2.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceB2.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.outputConfigB3.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highB3.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowB3.setText(QCoreApplication.translate("Form", u"Low", None))
        self.inputConfidB6.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upB6.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceB6.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.outputConfigB5.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highB5.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowB5.setText(QCoreApplication.translate("Form", u"Low", None))
        self.BoxB7.setTitle(QCoreApplication.translate("Form", u"B7", None))
        self.outputB7.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputB7.setText(QCoreApplication.translate("Form", u"Input", None))
        self.inputConfidB5.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upB5.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceB5.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.BoxB3.setTitle(QCoreApplication.translate("Form", u"B3", None))
        self.outputB3.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputB3.setText(QCoreApplication.translate("Form", u"Input", None))
        self.inputConfidB0.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upB0.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceB0.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.outputConfigB2.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highB2.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowB2.setText(QCoreApplication.translate("Form", u"Low", None))
        self.BoxB0.setTitle(QCoreApplication.translate("Form", u"B0", None))
        self.outputB0.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputB0.setText(QCoreApplication.translate("Form", u"Input", None))
        self.BoxB1.setTitle(QCoreApplication.translate("Form", u"B1", None))
        self.outputB1.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputB1.setText(QCoreApplication.translate("Form", u"Input", None))
        self.inputConfidB1.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upB1.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceB1.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.inputConfidB4.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upB4.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceB4.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.outputConfigB1.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highB1.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowB1.setText(QCoreApplication.translate("Form", u"Low", None))
        self.inputConfidB7.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upB7.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceB7.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.outputConfigB6.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highB6.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowB6.setText(QCoreApplication.translate("Form", u"Low", None))
        self.outputConfigB4.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highB4.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowB4.setText(QCoreApplication.translate("Form", u"Low", None))
        self.outputConfigB7.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highB7.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowB7.setText(QCoreApplication.translate("Form", u"Low", None))
        self.inputConfidB3.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upB3.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceB3.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.AVR_ATMEGA32_CONFIG.setTabText(self.AVR_ATMEGA32_CONFIG.indexOf(self.PortB), QCoreApplication.translate("Form", u"PORT-B", None))
        self.BoxC6.setTitle(QCoreApplication.translate("Form", u"C6", None))
        self.outputC6.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputC6.setText(QCoreApplication.translate("Form", u"Input", None))
        self.BoxC2.setTitle(QCoreApplication.translate("Form", u"C2", None))
        self.outputC2.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputC2.setText(QCoreApplication.translate("Form", u"Input", None))
        self.outputConfigC0.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highC0.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowC0.setText(QCoreApplication.translate("Form", u"Low", None))
        self.BoxC5.setTitle(QCoreApplication.translate("Form", u"C5", None))
        self.outputC5.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputC5.setText(QCoreApplication.translate("Form", u"Input", None))
        self.BoxC4.setTitle(QCoreApplication.translate("Form", u"C4", None))
        self.outputC4.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputC4.setText(QCoreApplication.translate("Form", u"Input", None))
        self.inputConfidC2.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upC2.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceC2.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.outputConfigC3.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highC3.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowC3.setText(QCoreApplication.translate("Form", u"Low", None))
        self.inputConfidC6.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upC6.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceC6.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.outputConfigC5.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highC5.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowC5.setText(QCoreApplication.translate("Form", u"Low", None))
        self.BoxC7.setTitle(QCoreApplication.translate("Form", u"C7", None))
        self.outputC7.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputC7.setText(QCoreApplication.translate("Form", u"Input", None))
        self.inputConfidC5.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upC5.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceC5.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.BoxC3.setTitle(QCoreApplication.translate("Form", u"C3", None))
        self.outputC3.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputC3.setText(QCoreApplication.translate("Form", u"Input", None))
        self.inputConfidC0.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upC0.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceC0.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.outputConfigC2.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highC2.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowC2.setText(QCoreApplication.translate("Form", u"Low", None))
        self.BoxC0.setTitle(QCoreApplication.translate("Form", u"C0", None))
        self.outputC0.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputC0.setText(QCoreApplication.translate("Form", u"Input", None))
        self.BoxC1.setTitle(QCoreApplication.translate("Form", u"C1", None))
        self.outputC1.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputC1.setText(QCoreApplication.translate("Form", u"Input", None))
        self.inputConfidC1.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upC1.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceC1.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.inputConfidC4.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upC4.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceC4.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.outputConfigC1.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highC1.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowC1.setText(QCoreApplication.translate("Form", u"Low", None))
        self.inputConfidC7.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upC7.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceC7.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.outputConfigC6.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highC6.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowC6.setText(QCoreApplication.translate("Form", u"Low", None))
        self.outputConfigC4.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highC4.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowC4.setText(QCoreApplication.translate("Form", u"Low", None))
        self.outputConfigC7.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highC7.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowC7.setText(QCoreApplication.translate("Form", u"Low", None))
        self.inputConfidC3.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upC3.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceC3.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.AVR_ATMEGA32_CONFIG.setTabText(self.AVR_ATMEGA32_CONFIG.indexOf(self.PortC), QCoreApplication.translate("Form", u"PORT-C", None))
        self.BoxD6.setTitle(QCoreApplication.translate("Form", u"D6", None))
        self.outputD6.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputD6.setText(QCoreApplication.translate("Form", u"Input", None))
        self.BoxD2.setTitle(QCoreApplication.translate("Form", u"D2", None))
        self.outputD2.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputD2.setText(QCoreApplication.translate("Form", u"Input", None))
        self.outputConfigD0.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highD0.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowD0.setText(QCoreApplication.translate("Form", u"Low", None))
        self.BoxD5.setTitle(QCoreApplication.translate("Form", u"D5", None))
        self.outputD5.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputD5.setText(QCoreApplication.translate("Form", u"Input", None))
        self.BoxD4.setTitle(QCoreApplication.translate("Form", u"D4", None))
        self.outputD4.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputD4.setText(QCoreApplication.translate("Form", u"Input", None))
        self.inputConfidD2.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upD2.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceD2.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.outputConfigD3.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highD3.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowD3.setText(QCoreApplication.translate("Form", u"Low", None))
        self.inputConfidD6.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upD6.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceD6.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.outputConfigD5.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highD5.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowD5.setText(QCoreApplication.translate("Form", u"Low", None))
        self.BoxD7.setTitle(QCoreApplication.translate("Form", u"D7", None))
        self.outputD7.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputD7.setText(QCoreApplication.translate("Form", u"Input", None))
        self.inputConfidD5.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upD5.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceD5.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.BoxD3.setTitle(QCoreApplication.translate("Form", u"D3", None))
        self.outputD3.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputD3.setText(QCoreApplication.translate("Form", u"Input", None))
        self.inputConfidD0.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upD0.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceD0.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.outputConfigD2.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highD2.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowD2.setText(QCoreApplication.translate("Form", u"Low", None))
        self.BoxD0.setTitle(QCoreApplication.translate("Form", u"D0", None))
        self.outputD0.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputD0.setText(QCoreApplication.translate("Form", u"Input", None))
        self.BoxD1.setTitle(QCoreApplication.translate("Form", u"D1", None))
        self.outputD1.setText(QCoreApplication.translate("Form", u"Output", None))
        self.inputD1.setText(QCoreApplication.translate("Form", u"Input", None))
        self.inputConfidD1.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upD1.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceD1.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.inputConfidD4.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upD4.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceD4.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.outputConfigD1.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highD1.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowD1.setText(QCoreApplication.translate("Form", u"Low", None))
        self.inputConfidD7.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upD7.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceD7.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.outputConfigD6.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highD6.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowD6.setText(QCoreApplication.translate("Form", u"Low", None))
        self.outputConfigD4.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highD4.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowD4.setText(QCoreApplication.translate("Form", u"Low", None))
        self.outputConfigD7.setTitle(QCoreApplication.translate("Form", u"output Config", None))
        self.highD7.setText(QCoreApplication.translate("Form", u"High", None))
        self.lowD7.setText(QCoreApplication.translate("Form", u"Low", None))
        self.inputConfidD3.setTitle(QCoreApplication.translate("Form", u"input config", None))
        self.pul_upD3.setText(QCoreApplication.translate("Form", u"Pull up", None))
        self.high_impedenceD3.setText(QCoreApplication.translate("Form", u"High impedance", None))
        self.AVR_ATMEGA32_CONFIG.setTabText(self.AVR_ATMEGA32_CONFIG.indexOf(self.PortD), QCoreApplication.translate("Form", u"PORT-D", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"PATH:", None))
        self.path.setText(QCoreApplication.translate("Form", u"enter a path of the configuration :", None))
        self.Generate.setText(QCoreApplication.translate("Form", u"Gernerate", None))
        self.load.setText(QCoreApplication.translate("Form", u"Load", None))
        self.save.setText(QCoreApplication.translate("Form", u"Save", None))
        self.AVR_ATMEGA32_CONFIG.setTabText(self.AVR_ATMEGA32_CONFIG.indexOf(self.configcheck), QCoreApplication.translate("Form", u"config", None))
    # retranslateUi

app=QApplication(sys.argv)
Widget=QWidget()
Form=Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())