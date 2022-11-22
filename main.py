import sys
import pandas as pd

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QHeaderView
from PyQt5 import QtCore
from PyQt5.QtGui import QFont

from modules.pyplot_designer import PieChartsWidgetPlot, BarChartsWidgetPlot, LineChartsWidgetPlot, StepChartsWidgetPlot
from ui.main_ui import Ui_MainWindow


class window(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.pie_chart_stats_grapher = PieChartsWidgetPlot()
        self.StatsGraph_QHBoxLaybout.addWidget(self.pie_chart_stats_grapher)

        self.bar_chart_stats_grapher = BarChartsWidgetPlot()
        self.BarChartStats_QHBoxLayout.addWidget(self.bar_chart_stats_grapher)

        self.line_chart_stats_grapher = LineChartsWidgetPlot()
        self.HBarChartStats_QHBoxLayout.addWidget(self.line_chart_stats_grapher)

        self.step_chart_stats_grapher = StepChartsWidgetPlot()
        self.timestampPlot_QHBoxLayout.addWidget(self.step_chart_stats_grapher)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.handle_timer_event)
        self.timer.start(2000)

        self.plot_category_stats()
        self.plot_graph_timeline("DAY")
        self.change_live_stats()
        self.plot_application_stats()
        self.plot_day_timeline()
        self.fill_table()

        self.connectSignalSlots()
        self.main_stackedWidget.setCurrentIndex(0)

    def handle_timer_event(self):
        self.change_live_stats()
        self.plot_graph_timeline(interval=self.last_interval_plotted)
        self.plot_category_stats()
        self.plot_day_timeline()
        self.fill_table()

    def connectSignalSlots(self):
        self.monthGraph_pushButton.clicked.connect(lambda: self.plot_graph_timeline("MONTH"))
        self.weekGraph_pushButton.clicked.connect(lambda: self.plot_graph_timeline("WEEK"))
        self.dayGraph_pushButton.clicked.connect(lambda: self.plot_graph_timeline("DAY"))

        self.main_stackedWidget.currentChanged.connect(self.change_main_stack_widget)
        self.chooseApplication_comboBox.currentIndexChanged.connect(self.fill_table)
        self.viewDetailedReport_pushButton.clicked.connect(lambda: self.main_stackedWidget.setCurrentIndex(1))

        self.backToDailyReport_pushButton.clicked.connect(lambda: self.main_stackedWidget.setCurrentIndex(0))

    def change_main_stack_widget(self):
        if self.main_stackedWidget.currentIndex() == 1:
            self.chooseApplication_comboBox.clear()
            applications = ["ALL", "PRIME VIDEO"]

            for app in applications:
                self.chooseApplication_comboBox.addItem(app)

    def plot_category_stats(self):
        """
        Plots user category stats pie charts
        """
        daily_stats = {
            "values": [10, 20, 15],
            "labels": ["Entertainment", "Work", "College"]
        }

        weekly_stats = {
            "values": [10, 30, 5, 20],
            "labels": ["Shopping", "Work", "Entertainment", "College"]
        }

        monthly_stats = {
            "values": [80, 10, 20, 40],
            "labels": ["Entertainment", "Coding", "Work", "College"]
        }

        self.pie_chart_stats_grapher.plot_stats_pie_chart(
            daily_status = daily_stats,
            weekly_stats = weekly_stats,
            monthly_stats = monthly_stats
        )

    def plot_graph_timeline(self, interval:str):
        """
        Plots user stats for today
        interval : MONTH, WEEK, DAY
        """
        self.last_interval_plotted = interval
        if interval == "DAY":
            stats = {
                "values": [10, 20, 15, 40, 15, 20],
                "labels": ["Teams", "Moodle", "Chrome", "VS Code", "Counter Strike", "Notepad"]
            }
            self.dayGraph_pushButton.setStyleSheet("font-weight: bold;")
            self.weekGraph_pushButton.setStyleSheet("font-weight: light;")
            self.monthGraph_pushButton.setStyleSheet("font-weight: light;")

        elif interval == "WEEK":
            stats = {
                "values": [25, 40, 100, 85, 150, 100],
                "labels": ["Teams", "Moodle", "VS Code", "Chrome", "Counter Strike", "Notepad"]
            }
            self.dayGraph_pushButton.setStyleSheet("font-weight: light;")
            self.weekGraph_pushButton.setStyleSheet("font-weight: bold;")
            self.monthGraph_pushButton.setStyleSheet("font-weight: light;")

        else:
            stats = {
                "values": [400, 375, 260, 850, 370, 200],
                "labels": ["Teams", "VS Code", "Moodle", "Chrome", "Notepad", "Counter Strike"]
            }
            self.dayGraph_pushButton.setStyleSheet("font-weight: light;")
            self.weekGraph_pushButton.setStyleSheet("font-weight: light;")
            self.monthGraph_pushButton.setStyleSheet("font-weight: bold;")

        self.bar_chart_stats_grapher.plot_stats_bar_chart(
            stats = stats,
            interval = interval
        )

    def change_live_stats(self):
        """
        Updates live stats of screen time
        """
        today = "01h 25m"
        week = "08h 20m"
        month = "24h 15m"

        self.TimeToday_Label.setText(today)
        self.TimeWeek_Label.setText(week)
        self.TimeMonth_Label.setText(month)

        self.TimeToday_Label.setStyleSheet("font-size: 72pt; font-weight: bold; text-align: right")
        self.TimeWeek_Label.setStyleSheet("font-size: 48pt; font-weight: bold; text-align: right")
        self.TimeMonth_Label.setStyleSheet("font-size: 36pt; font-weight: bold; text-align: right")
        
        self.TimeToday_Label.setAlignment(QtCore.Qt.AlignRight)
        self.TimeWeek_Label.setAlignment(QtCore.Qt.AlignRight)
        self.TimeMonth_Label.setAlignment(QtCore.Qt.AlignRight)

    def plot_application_stats(self):
        """
        Plots weekly and monthly line chart stats
        """
        weekly_stats = [10, 20, 5, 30, 40, 15, 20]
        monthly_stats = [100, 120, 200, 130, 80, 40, 50, 27, 48, 12, 23, 235, 123, 23, 235, 23, 234, 23,4 ,23, 234]
        self.line_chart_stats_grapher.plot_stats_line_chart(
            weekly_stats = weekly_stats,
            monthly_stats = monthly_stats
        )

    def plot_day_timeline(self):
        stats = {
            "values": [10, 20, 15, 50, 40, 28, 55, 100],
            "labels": ["visual studio", "Teams", "moodle", "cs go", "youtube", "chrome", "firefox", "inkspace"]
        }
        self.step_chart_stats_grapher.plot_step_chart(
            stats = stats
        )

    def fill_table(self):
        columns = ['DATE', 'APPLICATION', 'TIME SPENT']
        selected_application = self.chooseApplication_comboBox.currentText()
        if selected_application == "ALL":
            data = pd.DataFrame([
                ["22-11-2022", "PRIME VIDEO", "60"], 
                ["21-11-2022", "GOOGLE CHROME", "90"], 
                ["20-11-2022", "TEAMS", "30"]], 
                columns=columns)
        else:
            data = pd.DataFrame([
                ["22-11-2022", selected_application, "60"], 
                ["21-11-2022", selected_application, "90"], 
                ["20-11-2022", selected_application, "30"]], 
                columns=columns)

        row, column = data.shape
        self.pandasViewer_QtableWidget.setRowCount(row+1)
        self.pandasViewer_QtableWidget.setColumnCount(column)
        
        font = QFont()
        font.setBold(True)
        font.setPointSize(15)

        for i in range(column):
            itm = QTableWidgetItem(str(columns[i]))
            self.pandasViewer_QtableWidget.setItem(0, i, itm)
            self.pandasViewer_QtableWidget.item(0, i).setFont(font)

        for i in range(row):
            for j in range(column):
                self.pandasViewer_QtableWidget.setItem(i+1, j, QTableWidgetItem(str(data.iloc[i][columns[j]])))

        self.pandasViewer_QtableWidget.horizontalHeader().setStretchLastSection(True)
        self.pandasViewer_QtableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = window()
    main.show()
    app.exec_()