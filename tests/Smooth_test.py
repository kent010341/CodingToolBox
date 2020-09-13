import numpy as np

from CodingToolBox.SmoothTools import fft_smooth, MA_smooth

t = np.linspace(-4*np.pi, 4*np.pi, 400)
noisy_sin_t = np.sin(t) + np.random.normal(0, 1, t.shape) * 0.1
ma_smooth_sin_t = MA_smooth(noisy_sin_t, 11)
fft_smooth_sin_t = fft_smooth(noisy_sin_t, fs=400, filter_f=30, filter_type='lowpass')

import matplotlib.pyplot as plt
plt.subplot(311)
plt.plot(noisy_sin_t, label='noisy sine')
plt.legend()

plt.subplot(312)
plt.plot(ma_smooth_sin_t, label='ma')
plt.legend()

plt.subplot(313)
plt.plot(fft_smooth_sin_t, label='fft')
plt.legend()
plt.show()