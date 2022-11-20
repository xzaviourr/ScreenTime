import numpy as np

from PyQt5.QtWidgets import QSizePolicy, QWidget, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib as plt

class PieChartCanvas(FigureCanvas):
    """
    Instance that plots all graphs on the UI
    """
    def __init__(self, parent=None, height=12, width=20, dpi=100):
        self.figure = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, self.figure)
        self.setParent(parent)

        # Set width and size to be expanding to cover up the widget
        FigureCanvas.setSizePolicy(
            self,
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

    def plot_stats_pie_chart(self, daily_status:dict, weekly_stats:dict, monthly_stats:dict):
        """
        Plots pie charts for daily, weekly and monthly stats

        Args :
            daily_stats : dict[values, labels] : daily stats
            weekly_stats : dict[values, labels] : weekly stats
            monthly_stats : dict[values, labels] : monthly stats
        """
        def get_sector(x, values):
            abs_value = int(x / 100.*np.sum(values))
            return "{:.1f}%\n({:d} mins)".format(x, abs_value)

        self.figure.clear(True)
        idx_mapping = {0:daily_status, 1:weekly_stats, 2:monthly_stats}
        
        for idx, chart in enumerate(['Daily Stats', "Weekly Stats", "Monthly Stats"]):
            ax = self.figure.add_subplot(1, 3, idx+1)
            
            values = list(idx_mapping[idx]['values'])
            labels = list(idx_mapping[idx]['labels'])
            highest_time_consuming_index = values.index(max(values))
            explode = [0 for x in range(len(values))]
            explode[highest_time_consuming_index] = 0.2

            w, t, at = ax.pie(
                x = values,
                autopct = lambda pct: get_sector(pct, values),
                explode = explode,
                labels = labels,
                shadow = True,
                startangle = 90, 
                radius = 1.35,
                wedgeprops = {'linewidth': 1, 'edgecolor': "black"},
                textprops = dict(color = "black", size = 10)
            )

            ax.set_title(chart, pad = 15)

        self.figure.tight_layout(pad=6)
        self.draw()


class PieChartsWidgetPlot(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setLayout(QVBoxLayout())
        self.canvas = PieChartCanvas(self)
        self.layout().addWidget(self.canvas)

    def plot_stats_pie_chart(self, daily_status:dict, weekly_stats:dict, monthly_stats:dict):
        self.canvas.plot_stats_pie_chart(daily_status, weekly_stats, monthly_stats)


class BarChartCanvas(FigureCanvas):
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

    def plot_stats_bar_chart(self, today_stats:dict):
        """
        Plots pie charts for daily, weekly and monthly stats

        Args :
            today_stats : dict[values, labels] : today's stats
        """
        self.figure.clear(True)
        ax = self.figure.add_subplot(1, 1, 1)
        
        values = list(today_stats['values'])
        labels = list(today_stats['labels'])
        
        colors = []
        for i in range(0, len(labels)+1):
            colors.append(np.random.rand(1, 3))

        ax.bar(
            x = labels,
            height = values,
            width = 0.8,
            color = colors
        )

        ax.set_xlabel("Application")
        ax.set_ylabel("Minutes")
        ax.set_title("Time Spent Today", pad = 15)

        self.figure.tight_layout(pad=8)
        self.draw()


class BarChartsWidgetPlot(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setLayout(QVBoxLayout())
        self.canvas = BarChartCanvas(self)
        self.layout().addWidget(self.canvas)

    def plot_stats_bar_chart(self, today_stats:dict):
        self.canvas.plot_stats_bar_chart(today_stats)


class LineChartCanvas(FigureCanvas):
    """
    Instance that plots all graphs on the UI
    """
    def __init__(self, parent=None, height=20, width=20, dpi=100):
        self.figure = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, self.figure)
        self.setParent(parent)

        # Set width and size to be expanding to cover up the widget
        FigureCanvas.setSizePolicy(
            self,
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

    def plot_stats_line_chart(self, weekly_stats:list, monthly_stats:list):
        """
        Plots line chart for weekly and monthly stats

        Args :
            weekly_stats : [values] : weekly stats
            monthly_stats : [values] : monthly stats
        """
        self.figure.clear(True)
        
        idx_mapping = {0: weekly_stats, 1:monthly_stats}
        for idx, grp in enumerate(["Last Week", "Last Month"]):
            ax = self.figure.add_subplot(2, 1, idx+1)
            values = list(idx_mapping[idx])
            indices = [i+1 for i in range(len(values))]
            ax.plot(indices, values, marker='o')
            ax.fill_between(indices, values, alpha=0.3)
            ax.set_xlabel("Day")
            ax.set_ylabel("Time")
            ax.set_title(grp, pad = 8)

        self.figure.tight_layout(pad=15)
        self.draw()


class LineChartsWidgetPlot(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setLayout(QVBoxLayout())
        self.canvas = LineChartCanvas(self)
        self.layout().addWidget(self.canvas)

    def plot_stats_line_chart(self, weekly_stats:list, monthly_stats:list):
        self.canvas.plot_stats_line_chart(weekly_stats, monthly_stats)
