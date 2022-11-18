import numpy as np

from PyQt5.QtWidgets import QSizePolicy, QWidget, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib as plt

class PlotCanvas(FigureCanvas):
    """
    Instance that plots all graphs on the UI
    """
    def __init__(self, parent=None, height=10, width=20, dpi=100):
        self.figure = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, self.figure)
        self.setParent(parent)

        # Set width and size to be expanding to cover up the widget
        FigureCanvas.setSizePolicy(
            self,
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

    def plot_stats_pie_chart(self, daily_status, weekly_stats, monthly_stats):
        def get_sector(x, values):
            abs_value = int(x / 100.*np.sum(values))
            return "{:.1f}%\n({:d} mins)".format(x, abs_value)

        self.figure.clear(True)
        idx_mapping = {0:daily_status, 1:weekly_stats, 2:monthly_stats}
        
        for idx, chart in enumerate(['Daily Stats', "Weekly Stats", "Monthly Stats"]):
            ax = self.figure.add_subplot(1, 3, idx+1)
            
            values = [10, 20, 15]
            labels = ["Moodle", "Chrome", "Teams"]
            explode = (0.1, 0.0, 0.2)

            w, t, at = ax.pie(
                x = values,
                autopct = lambda pct: get_sector(pct, values),
                explode = explode,
                labels = labels,
                shadow = True,
                startangle = 90, 
                radius = 1.3,
                wedgeprops = {'linewidth': 1, 'edgecolor': "black"},
                textprops = dict(color = "black", size = 8)
            )

            # if idx == 2:
            #     ax.legend(w, labels, title = "Stats", loc = "center right")
            ax.set_title(chart)

        self.figure.tight_layout(pad=10)
        self.draw()



class WidgetPlot(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setLayout(QVBoxLayout())
        self.canvas = PlotCanvas(self)
        self.layout().addWidget(self.canvas)

    def plot_stats_pie_chart(self):
        self.canvas.plot_stats_pie_chart()