from scipy.signal import windows
from scipy.fftpack import fft
from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg
import sys
import pandas as pd
import pywt
import numpy as np
from scipy import signal


def rrt_cal(data, fs):
    peaks, _ = signal.find_peaks(data, height=[30, 60])
    peak_interval_sum = 0
    if len(peaks) >= 2:
        for i in range(1, len(peaks)):
            interval = peaks[i] - peaks[i - 1]
            peak_interval_sum += interval
            peak_interval_sum = int(peak_interval_sum / (len(peaks) - 1))
            Rrt = int(fs * 60 / peak_interval_sum)
            Rrt_valid = True
    else:
        Rrt = -999  # unable to calculate because # of peaks are too small
        Rrt_valid = False

    return Rrt, Rrt_valid


app = QApplication(sys.argv)
win = pg.GraphicsLayoutWidget(show=True)
win.resize(1000, 600)
win.setWindowTitle('WAVELET ANALYSIS (RESPIRATORY RATE DATA)')

pg.setConfigOptions(antialias=True)
sdata = pd.read_csv("Data/erotu/Front_L.csv", usecols=[0], names=['colA'])
data = sdata['colA'].values.tolist()[0:1000]
tm = tm = range(0, 1000)

coeff = pywt.wavedec(data, "db3", mode="symmetric", level=4)

CA4, CD4, CD3, CD2, CD1 = coeff

f = [np.zeros(len(CA4)), CD4, CD3, CD2, CD1]
filtered = pywt.waverec(f, "db3", mode="periodic")

fs = float("{0:2.1f}".format(1.0/np.mean(np.abs(np.diff(tm)))))
print(fs)

mean = int(np.mean(data))
data = -1*(np.array(data)-mean)
p = win.addPlot(title="Original Data")
curve = p.plot(data, pen="y")


win.nextRow()
p5 = win.addPlot(title="Using hanning window")
w = windows.hann(1000)
wn = w*filtered
curve5 = p5.plot(wn, pen="y")
# #-----------------------------------------------------------------------------------------------
win.nextRow()
p6 = win.addPlot(title="Magnitude Frequency Plot")
y = fft(wn)
mg = (2/len(tm))*np.abs(y)
fr = (round(fs)/len(tm))*np.array(range(0, len(tm)))
curve6 = p6.plot(fr[0:int(len(y)/2)], mg[0:int(len(y)/2)], pen="g")


win.nextRow()
p7 = win.addPlot(title="Filtered(bessel filter)")
# sos = signal.butter(4, [0.9, 2.5], 'bp', fs=fs, output = 'sos')
# sos = signal.bessel(4, [0.16, 0.8], 'bp', fs=round(fs), output = 'sos')

sos = signal.bessel(4, [0.2, 0.4], 'bp', fs=round(fs), output='sos')
filt = signal.sosfilt(sos, data)
curve7 = p7.plot(filt, pen='r')


win.nextRow()
p8 = win.addPlot(title="Magnitude Frequency Plot")
wn2 = w*filt
y2 = fft(wn2)
mg2 = (2/len(tm))*np.abs(y2)
fr2 = (round(fs)/len(tm))*np.array(range(0, len(tm)))
curve8 = p8.plot(fr2[0:int(len(y2)/2)], mg2[0:int(len(y2)/2)], pen="g")


win.nextRow()
p9 = win.addPlot(title="Filtered(bessel filter)")
sos2 = signal.bessel(4, [0.23, 0.255], 'bs', fs=round(fs), output='sos')
filt2 = signal.sosfilt(sos2, filt)
curve9 = p9.plot(filt2, pen='r')


# sos = signal.iirnotch(0.04, 25,output='sos')

peaks, _ = signal.find_peaks(filt, height=[0.2, 3])
p7.plot(peaks, filt[peaks], pen='r', symbolBrush=(255, 0, 0), symbolPen='w')
print(rrt_cal(filt, round(fs)))

win.nextRow()
p1 = win.addPlot(title="Filtered")
curve1 = p1.plot(filtered, pen="g")

# win.nextRow()
# p1 = win.addPlot(title="Approximate Coefficients(CA4)")
# curve1 = p1.plot(CA4, pen="g")
# win.nextRow()
# p2 = win.addPlot(title="Detailed Coefficients(CD4)")
# curve2 = p2.plot(CD4, pen="r")
# win.nextRow()
# p3 = win.addPlot(title="(CD3)")
# curve3 = p3.plot(CD3, pen="r")
# win.nextRow()
# p4 = win.addPlot(title="(CD2)")
# curve4 = p4.plot(CD2, pen="r")
# win.nextRow()
# p5 = win.addPlot(title="(CD1)")
# curve4 = p5.plot(CD1, pen="r")

win.show()
sys.exit(app.exec_())

# win.nextRow()
# p6 = win.addPlot(title="Magnitude Frequency Plot")
# y = fft(wn)
# mg = (2/len(tm))*np.abs(y)
# fr = (fs/len(tm))*np.array(range(0,len(tm)))
# curve6 = p6.plot(fr[0:int(len(y)/2)], mg[0:int(len(y)/2)], pen="g")
