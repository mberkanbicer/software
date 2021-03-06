# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StripmapCV.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 680)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/python_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.x_span = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.x_span.sizePolicy().hasHeightForWidth())
        self.x_span.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.x_span.setFont(font)
        self.x_span.setObjectName("x_span")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.x_span)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label)
        self.y_span = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.y_span.sizePolicy().hasHeightForWidth())
        self.y_span.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.y_span.setFont(font)
        self.y_span.setObjectName("y_span")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.y_span)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.nx_ny = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nx_ny.sizePolicy().hasHeightForWidth())
        self.nx_ny.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.nx_ny.setFont(font)
        self.nx_ny.setObjectName("nx_ny")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.nx_ny)
        self.azimuth = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.azimuth.setFont(font)
        self.azimuth.setObjectName("azimuth")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.azimuth)
        self.aperture_length = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aperture_length.sizePolicy().hasHeightForWidth())
        self.aperture_length.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.aperture_length.setFont(font)
        self.aperture_length.setObjectName("aperture_length")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.aperture_length)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.dynamic_range = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dynamic_range.sizePolicy().hasHeightForWidth())
        self.dynamic_range.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dynamic_range.setFont(font)
        self.dynamic_range.setObjectName("dynamic_range")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.dynamic_range)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.target = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.target.sizePolicy().hasHeightForWidth())
        self.target.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.target.setFont(font)
        self.target.setObjectName("target")
        self.target.addItem("")
        self.target.addItem("")
        self.target.addItem("")
        self.target.addItem("")
        self.target.addItem("")
        self.target.addItem("")
        self.target.addItem("")
        self.target.addItem("")
        self.target.addItem("")
        self.target.addItem("")
        self.target.addItem("")
        self.target.addItem("")
        self.target.addItem("")
        self.target.addItem("")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.target)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.window_type = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.window_type.sizePolicy().hasHeightForWidth())
        self.window_type.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.window_type.setFont(font)
        self.window_type.setObjectName("window_type")
        self.window_type.addItem("")
        self.window_type.addItem("")
        self.window_type.addItem("")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.window_type)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.polarization = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.polarization.sizePolicy().hasHeightForWidth())
        self.polarization.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.polarization.setFont(font)
        self.polarization.setObjectName("polarization")
        self.polarization.addItem("")
        self.polarization.addItem("")
        self.polarization.addItem("")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.polarization)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.range_center = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.range_center.sizePolicy().hasHeightForWidth())
        self.range_center.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.range_center.setFont(font)
        self.range_center.setObjectName("range_center")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.range_center)
        self.squint_angle = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.squint_angle.sizePolicy().hasHeightForWidth())
        self.squint_angle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.squint_angle.setFont(font)
        self.squint_angle.setObjectName("squint_angle")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.squint_angle)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.antenna_width = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.antenna_width.sizePolicy().hasHeightForWidth())
        self.antenna_width.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.antenna_width.setFont(font)
        self.antenna_width.setObjectName("antenna_width")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.antenna_width)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.horizontalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(14, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 20)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stripmap"))
        self.label_6.setText(_translate("MainWindow", "Input"))
        self.label_3.setText(_translate("MainWindow", "Image Span-X (m)"))
        self.x_span.setText(_translate("MainWindow", "10"))
        self.label.setText(_translate("MainWindow", "Image Span-Y (m)"))
        self.y_span.setText(_translate("MainWindow", "10"))
        self.label_9.setText(_translate("MainWindow", "Number of Pixels (nx, ny)"))
        self.nx_ny.setText(_translate("MainWindow", "200, 200"))
        self.azimuth.setText(_translate("MainWindow", "Aperture Length (m)"))
        self.aperture_length.setText(_translate("MainWindow", "100"))
        self.label_12.setText(_translate("MainWindow", "Dynamic Range (dB)"))
        self.dynamic_range.setText(_translate("MainWindow", "50"))
        self.label_2.setText(_translate("MainWindow", "Target"))
        self.target.setItemText(0, _translate("MainWindow", "Jeep Elevation 30"))
        self.target.setItemText(1, _translate("MainWindow", "Jeep Elevation 40"))
        self.target.setItemText(2, _translate("MainWindow", "Jeep Elevation 50"))
        self.target.setItemText(3, _translate("MainWindow", "Jeep Elevation 60"))
        self.target.setItemText(4, _translate("MainWindow", "Camry Elevation 30"))
        self.target.setItemText(5, _translate("MainWindow", "Camry Elevation 40"))
        self.target.setItemText(6, _translate("MainWindow", "Camry Elevation 50"))
        self.target.setItemText(7, _translate("MainWindow", "Camry Elevation 60"))
        self.target.setItemText(8, _translate("MainWindow", "Tacoma Elevation 30"))
        self.target.setItemText(9, _translate("MainWindow", "Tacoma Elevation 40"))
        self.target.setItemText(10, _translate("MainWindow", "Tacoma Elevation 50"))
        self.target.setItemText(11, _translate("MainWindow", "Tacoma Elevation 60"))
        self.target.setItemText(12, _translate("MainWindow", "Backhoe Elevation 30"))
        self.target.setItemText(13, _translate("MainWindow", "Backhoe Elevation 0"))
        self.label_5.setText(_translate("MainWindow", "Window Type"))
        self.window_type.setItemText(0, _translate("MainWindow", "Rectangular"))
        self.window_type.setItemText(1, _translate("MainWindow", "Hanning"))
        self.window_type.setItemText(2, _translate("MainWindow", "Hamming"))
        self.label_4.setText(_translate("MainWindow", "Polarization"))
        self.polarization.setItemText(0, _translate("MainWindow", "VV"))
        self.polarization.setItemText(1, _translate("MainWindow", "HH"))
        self.polarization.setItemText(2, _translate("MainWindow", "HV"))
        self.label_7.setText(_translate("MainWindow", "Range to Scene Center (m)"))
        self.range_center.setText(_translate("MainWindow", "1000"))
        self.squint_angle.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "Squint Angle (deg)"))
        self.antenna_width.setText(_translate("MainWindow", "2"))
        self.label_10.setText(_translate("MainWindow", "Antenna Width (m)"))

import Libs.resources_rc
