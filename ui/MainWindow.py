# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(471, 251)
        MainWindow.setMinimumSize(QtCore.QSize(471, 251))
        MainWindow.setMaximumSize(QtCore.QSize(471, 251))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PreviewLabel = QtWidgets.QLabel(self.centralwidget)
        self.PreviewLabel.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.PreviewLabel.setObjectName("PreviewLabel")
        self.PreviewIcon = QtWidgets.QLabel(self.centralwidget)
        self.PreviewIcon.setGeometry(QtCore.QRect(10, 30, 141, 191))
        self.PreviewIcon.setAutoFillBackground(True)
        self.PreviewIcon.setText("")
        self.PreviewIcon.setScaledContents(True)
        self.PreviewIcon.setObjectName("PreviewIcon")
        self.Divider = QtWidgets.QFrame(self.centralwidget)
        self.Divider.setGeometry(QtCore.QRect(150, 10, 21, 211))
        self.Divider.setFrameShape(QtWidgets.QFrame.VLine)
        self.Divider.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Divider.setObjectName("Divider")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(170, 10, 291, 211))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.unfixedLabel = QtWidgets.QLabel(self.widget)
        self.unfixedLabel.setObjectName("unfixedLabel")
        self.gridLayout_2.addWidget(self.unfixedLabel, 0, 0, 1, 1)
        self.UnfixedInput = QtWidgets.QLineEdit(self.widget)
        self.UnfixedInput.setObjectName("UnfixedInput")
        self.gridLayout_2.addWidget(self.UnfixedInput, 1, 0, 1, 1)
        self.UnfixedButton = QtWidgets.QPushButton(self.widget)
        self.UnfixedButton.setObjectName("UnfixedButton")
        self.gridLayout_2.addWidget(self.UnfixedButton, 1, 1, 1, 1)
        self.LockedLabel = QtWidgets.QLabel(self.widget)
        self.LockedLabel.setObjectName("LockedLabel")
        self.gridLayout_2.addWidget(self.LockedLabel, 2, 0, 1, 1)
        self.LockedInput = QtWidgets.QLineEdit(self.widget)
        self.LockedInput.setObjectName("LockedInput")
        self.gridLayout_2.addWidget(self.LockedInput, 3, 0, 1, 1)
        self.LockedButton = QtWidgets.QPushButton(self.widget)
        self.LockedButton.setObjectName("LockedButton")
        self.gridLayout_2.addWidget(self.LockedButton, 3, 1, 1, 1)
        self.BinLabel = QtWidgets.QLabel(self.widget)
        self.BinLabel.setObjectName("BinLabel")
        self.gridLayout_2.addWidget(self.BinLabel, 4, 0, 1, 1)
        self.BinInput = QtWidgets.QLineEdit(self.widget)
        self.BinInput.setObjectName("BinInput")
        self.gridLayout_2.addWidget(self.BinInput, 5, 0, 1, 1)
        self.BinButton = QtWidgets.QPushButton(self.widget)
        self.BinButton.setObjectName("BinButton")
        self.gridLayout_2.addWidget(self.BinButton, 5, 1, 1, 1)
        self.WriteButton = QtWidgets.QPushButton(self.widget)
        self.WriteButton.setObjectName("WriteButton")
        self.gridLayout_2.addWidget(self.WriteButton, 6, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NFCiibo"))
        self.PreviewLabel.setText(_translate("MainWindow", "Preview"))
        self.unfixedLabel.setText(_translate("MainWindow", "Unfixed Key"))
        self.UnfixedButton.setText(_translate("MainWindow", "Select File"))
        self.LockedLabel.setText(_translate("MainWindow", "Locked Key"))
        self.LockedButton.setText(_translate("MainWindow", "Select File"))
        self.BinLabel.setText(_translate("MainWindow", "Amiibo .BIN"))
        self.BinButton.setText(_translate("MainWindow", "Select File"))
        self.WriteButton.setText(_translate("MainWindow", "Write to NFC"))

