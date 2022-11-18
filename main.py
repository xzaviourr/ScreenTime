import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from modules.pyplot_designer import WidgetPlot
from ui.main_ui import Ui_MainWindow

class window(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.stats_grapher = WidgetPlot()
        self.StatsGraph_QHBoxLaybout.addWidget(self.stats_grapher)
        self.stats_grapher.plot_stats_pie_chart()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = window()
    main.show()
    app.exec_()