# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LiveScreenTime_Widget = QtWidgets.QWidget(self.centralwidget)
        self.LiveScreenTime_Widget.setGeometry(QtCore.QRect(50, 20, 541, 351))
        self.LiveScreenTime_Widget.setAutoFillBackground(False)
        self.LiveScreenTime_Widget.setStyleSheet("background-color: white")
        self.LiveScreenTime_Widget.setObjectName("LiveScreenTime_Widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.LiveScreenTime_Widget)
        self.verticalLayout_2.setContentsMargins(23, 15, 24, 15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.LiveScreenTime_Widget)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.LiveScreenTime_Widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.TimeToday_Label = QtWidgets.QLabel(self.LiveScreenTime_Widget)
        self.TimeToday_Label.setObjectName("TimeToday_Label")
        self.horizontalLayout_2.addWidget(self.TimeToday_Label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.LiveScreenTime_Widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.TimeWeek_Label = QtWidgets.QLabel(self.LiveScreenTime_Widget)
        self.TimeWeek_Label.setObjectName("TimeWeek_Label")
        self.horizontalLayout_3.addWidget(self.TimeWeek_Label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.LiveScreenTime_Widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.TimeMonth_Label = QtWidgets.QLabel(self.LiveScreenTime_Widget)
        self.TimeMonth_Label.setObjectName("TimeMonth_Label")
        self.horizontalLayout_4.addWidget(self.TimeMonth_Label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(50, 400, 541, 591))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.HBarChartStats_QHBoxLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.HBarChartStats_QHBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.HBarChartStats_QHBoxLayout.setObjectName("HBarChartStats_QHBoxLayout")
        self.main_stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.main_stackedWidget.setGeometry(QtCore.QRect(610, 10, 1291, 981))
        self.main_stackedWidget.setObjectName("main_stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 390, 1271, 561))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.BarChartStats_QHBoxLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.BarChartStats_QHBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.BarChartStats_QHBoxLayout.setObjectName("BarChartStats_QHBoxLayout")
        self.weekGraph_pushButton = QtWidgets.QPushButton(self.page)
        self.weekGraph_pushButton.setGeometry(QtCore.QRect(1090, 940, 89, 41))
        self.weekGraph_pushButton.setObjectName("weekGraph_pushButton")
        self.monthGraph_pushButton = QtWidgets.QPushButton(self.page)
        self.monthGraph_pushButton.setGeometry(QtCore.QRect(1000, 940, 89, 41))
        self.monthGraph_pushButton.setObjectName("monthGraph_pushButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 1271, 371))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.StatsGraph_QHBoxLaybout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.StatsGraph_QHBoxLaybout.setContentsMargins(0, 0, 0, 0)
        self.StatsGraph_QHBoxLaybout.setObjectName("StatsGraph_QHBoxLaybout")
        self.dayGraph_pushButton = QtWidgets.QPushButton(self.page)
        self.dayGraph_pushButton.setGeometry(QtCore.QRect(1180, 940, 89, 41))
        self.dayGraph_pushButton.setObjectName("dayGraph_pushButton")
        self.viewDetailedReport_pushButton = QtWidgets.QPushButton(self.page)
        self.viewDetailedReport_pushButton.setGeometry(QtCore.QRect(30, 940, 221, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.viewDetailedReport_pushButton.setFont(font)
        self.viewDetailedReport_pushButton.setObjectName("viewDetailedReport_pushButton")
        self.main_stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.page_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 10, 611, 971))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.timestampPlot_QHBoxLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.timestampPlot_QHBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.timestampPlot_QHBoxLayout.setObjectName("timestampPlot_QHBoxLayout")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(680, 30, 341, 51))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(690, 90, 211, 31))
        self.label_6.setObjectName("label_6")
        self.chooseApplication_comboBox = QtWidgets.QComboBox(self.page_2)
        self.chooseApplication_comboBox.setGeometry(QtCore.QRect(900, 90, 311, 31))
        self.chooseApplication_comboBox.setObjectName("chooseApplication_comboBox")
        self.pandasViewer_QtableWidget = QtWidgets.QTableWidget(self.page_2)
        self.pandasViewer_QtableWidget.setGeometry(QtCore.QRect(660, 130, 631, 791))
        self.pandasViewer_QtableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pandasViewer_QtableWidget.setLineWidth(2)
        self.pandasViewer_QtableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.pandasViewer_QtableWidget.setObjectName("pandasViewer_QtableWidget")
        self.pandasViewer_QtableWidget.setColumnCount(0)
        self.pandasViewer_QtableWidget.setRowCount(0)
        self.pandasViewer_QtableWidget.horizontalHeader().setVisible(False)
        self.pandasViewer_QtableWidget.verticalHeader().setVisible(False)
        self.backToDailyReport_pushButton = QtWidgets.QPushButton(self.page_2)
        self.backToDailyReport_pushButton.setGeometry(QtCore.QRect(1040, 930, 241, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.backToDailyReport_pushButton.setFont(font)
        self.backToDailyReport_pushButton.setObjectName("backToDailyReport_pushButton")
        self.main_stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.main_stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Screen Time Tracker"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt; font-weight:600;\">Screen Time</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Today -</span></p></body></html>"))
        self.TimeToday_Label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:72pt; font-weight:600;\">01h 25m</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">This week -</span></p></body></html>"))
        self.TimeWeek_Label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:48pt; font-weight:600;\">08h 20m</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">This month -</span></p></body></html>"))
        self.TimeMonth_Label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:36pt; font-weight:600;\">24h 10m</span></p></body></html>"))
        self.weekGraph_pushButton.setText(_translate("MainWindow", "WEEK"))
        self.monthGraph_pushButton.setText(_translate("MainWindow", "MONTH"))
        self.dayGraph_pushButton.setText(_translate("MainWindow", "DAY"))
        self.viewDetailedReport_pushButton.setText(_translate("MainWindow", "VIEW DETAILED REPORT"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600;\">Get Detailed Report</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Choose Application</span></p></body></html>"))
        self.backToDailyReport_pushButton.setText(_translate("MainWindow", "BACK TO DAILY REPORT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
