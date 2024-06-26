# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testeui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(565, 597)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(565, 597))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 561, 561))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.AddP = QtWidgets.QWidget()
        self.AddP.setObjectName("AddP")
        self.NameL = QtWidgets.QLabel(self.AddP)
        self.NameL.setGeometry(QtCore.QRect(10, 20, 51, 21))
        self.NameL.setObjectName("NameL")
        self.PhoneL = QtWidgets.QLabel(self.AddP)
        self.PhoneL.setGeometry(QtCore.QRect(10, 50, 51, 21))
        self.PhoneL.setObjectName("PhoneL")
        self.EarningL = QtWidgets.QLabel(self.AddP)
        self.EarningL.setGeometry(QtCore.QRect(10, 80, 51, 21))
        self.EarningL.setObjectName("EarningL")
        self.ninput = QtWidgets.QLineEdit(self.AddP)
        self.ninput.setGeometry(QtCore.QRect(60, 20, 113, 20))
        self.ninput.setObjectName("ninput")
        self.pinput = QtWidgets.QLineEdit(self.AddP)
        self.pinput.setGeometry(QtCore.QRect(60, 50, 113, 20))
        self.pinput.setObjectName("pinput")
        self.einput = QtWidgets.QLineEdit(self.AddP)
        self.einput.setGeometry(QtCore.QRect(60, 80, 113, 20))
        self.einput.setObjectName("einput")
        self.SButton = QtWidgets.QPushButton(self.AddP)
        self.SButton.setGeometry(QtCore.QRect(60, 110, 111, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SButton.setFont(font)
        self.SButton.setObjectName("SButton")
        self.TButton = QtWidgets.QPushButton(self.AddP)
        self.TButton.setGeometry(QtCore.QRect(40, 230, 141, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TButton.setFont(font)
        self.TButton.setObjectName("TButton")
        self.TotalEarning = QtWidgets.QLabel(self.AddP)
        self.TotalEarning.setGeometry(QtCore.QRect(50, 300, 121, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TotalEarning.setFont(font)
        self.TotalEarning.setAlignment(QtCore.Qt.AlignCenter)
        self.TotalEarning.setObjectName("TotalEarning")
        self.RefreshButton = QtWidgets.QPushButton(self.AddP)
        self.RefreshButton.setGeometry(QtCore.QRect(60, 150, 111, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.RefreshButton.setFont(font)
        self.RefreshButton.setObjectName("RefreshButton")
        self.tabWidget.addTab(self.AddP, "")
        self.ImportP = QtWidgets.QWidget()
        self.ImportP.setEnabled(True)
        self.ImportP.setObjectName("ImportP")
        self.DentalChartImage = QtWidgets.QLabel(self.ImportP)
        self.DentalChartImage.setGeometry(QtCore.QRect(0, 120, 231, 301))
        self.DentalChartImage.setText("")
        self.DentalChartImage.setPixmap(QtGui.QPixmap(":/DentalChart/Downloads/dents.png"))
        self.DentalChartImage.setScaledContents(True)
        self.DentalChartImage.setObjectName("DentalChartImage")
        self.DentalChartLabel = QtWidgets.QLabel(self.ImportP)
        self.DentalChartLabel.setGeometry(QtCore.QRect(-10, 10, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.DentalChartLabel.setFont(font)
        self.DentalChartLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DentalChartLabel.setObjectName("DentalChartLabel")
        self.tabWidget.addTab(self.ImportP, "")
        self.IOTab = QtWidgets.QWidget()
        self.IOTab.setObjectName("IOTab")
        self.AddImage = QtWidgets.QPushButton(self.IOTab)
        self.AddImage.setGeometry(QtCore.QRect(60, 40, 101, 41))
        self.AddImage.setObjectName("AddImage")
        self.ViewImage = QtWidgets.QPushButton(self.IOTab)
        self.ViewImage.setGeometry(QtCore.QRect(60, 90, 101, 41))
        self.ViewImage.setObjectName("ViewImage")
        self.tabWidget.addTab(self.IOTab, "")
        self.Ptable = QtWidgets.QTableWidget(self.centralwidget)
        self.Ptable.setGeometry(QtCore.QRect(230, 20, 321, 531))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Ptable.setFont(font)
        self.Ptable.setRowCount(1)
        self.Ptable.setColumnCount(3)
        self.Ptable.setObjectName("Ptable")
        item = QtWidgets.QTableWidgetItem()
        self.Ptable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Ptable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Ptable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Ptable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Ptable.setItem(0, 1, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setEnabled(True)
        self.menuOptions.setGeometry(QtCore.QRect(269, 125, 135, 72))
        self.menuOptions.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuOptions.addAction(self.actionExit)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "King and Queen Dental Clinic"))
        self.NameL.setText(_translate("MainWindow", "Name"))
        self.PhoneL.setText(_translate("MainWindow", "Phone"))
        self.EarningL.setText(_translate("MainWindow", "Earning"))
        self.SButton.setText(_translate("MainWindow", "Submit"))
        self.TButton.setText(_translate("MainWindow", "Calculate Total Earning"))
        self.TotalEarning.setText(_translate("MainWindow", "0Rs"))
        self.RefreshButton.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AddP), _translate("MainWindow", "Add Patients"))
        self.DentalChartLabel.setText(_translate("MainWindow", "Dental Chart"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ImportP), _translate("MainWindow", "Dental Chart"))
        self.AddImage.setText(_translate("MainWindow", "Add new image"))
        self.ViewImage.setText(_translate("MainWindow", "View Images"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.IOTab), _translate("MainWindow", "Intra oral Camera"))
        item = self.Ptable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Patient Name"))
        item = self.Ptable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Phone Number"))
        item = self.Ptable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Earning"))
        __sortingEnabled = self.Ptable.isSortingEnabled()
        self.Ptable.setSortingEnabled(False)
        self.Ptable.setSortingEnabled(__sortingEnabled)
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
import DentalImage_rc
