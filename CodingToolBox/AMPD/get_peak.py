import numpy as np

from .__ampd__ import AMPD_avoid_MemoryError

def get_peak(data, find_button=False, scan_range=1000):
    data = np.array(data)

    if find_button:
        data = -data

    index_peaks, value_peaks = AMPD_avoid_MemoryError(data)

    if find_button:
        return index_peaks, -value_peaks
    else:
        return index_peaks, value_peaks