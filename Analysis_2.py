from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg
import sys
import pandas as pd
import pywt
import numpy as np

app = QApplication(sys.argv)
win = pg.GraphicsLayoutWidget(show=True)
win.resize(1000, 600)
win.setWindowTitle('WAVELET ANALYSIS (HEART RATE DATA)')

pg.setConfigOptions(antialias=True)
sdata = pd.read_csv("Data/erotu/Front_L.csv", usecols=[0], names=['colA'])
data = sdata['colA'].values.tolist()[0:1000]
tm = tm = range(0, 1000)

coeff = pywt.wavedec(data, "bior3.3", mode="symmetric", level=5)

CA5, CD5, CD4, CD3, CD2, CD1, = coeff

f = [np.zeros(len(CA5)), CD5, CD4, CD3, np.zeros(len(CD2)), np.zeros(len(CD1))]
filtered = pywt.waverec(f, "bior3.3", mode="periodic")

p = win.addPlot(title="Original Data")
curve = p.plot(data, pen="r")

win.nextRow()
p1 = win.addPlot(title="Filtered Signal")
curve1 = p1.plot(filtered, pen="g")


# p1 = win.addPlot(title="Approximate Coefficients(CA5)")
# curve1 = p1.plot(CA5, pen="g")
# win.nextRow()
# p2 = win.addPlot(title="Detailed Coefficients(CD5)")
# curve2 = p2.plot(CD5, pen="g")
# win.nextRow()
# p3 = win.addPlot(title="(CD4)")
# curve3 = p3.plot(CD4, pen="g")
# win.nextRow()
# p4 = win.addPlot(title="(CD3)")
# curve4 = p4.plot(CD3, pen="g")
# win.nextRow()
# p4 = win.addPlot(title="(CD2)")
# curve4 = p4.plot(CD2, pen="g")
# win.nextRow()
# p4 = win.addPlot(title="(CD1)")
# curve4 = p4.plot(CD1, pen="g")

win.show()
sys.exit(app.exec_())
