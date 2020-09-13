import numpy as np
try:
	import matplotlib.pyplot as plt
	has_plt = True
except:
	has_plt = False

from CodingToolBox.AMPD import get_peak

t = np.linspace(-30, 30, 9000)
sin_t = np.sin(t)
sin_t += np.random.normal(0, 0.01, sin_t.shape)

index_peaks, value_peaks = get_peak(sin_t)

plt.plot(t, sin_t)
plt.scatter(t[index_peaks], value_peaks)
plt.show()