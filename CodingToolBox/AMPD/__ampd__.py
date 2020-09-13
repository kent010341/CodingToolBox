import numpy as np

def ampd(sig_input, LSM_limit = 1):
    """Find the peaks in the signal with the AMPD algorithm.
    
        Original implementation by Felix Scholkmann et al. in
        "An Efficient Algorithm for Automatic Peak Detection in 
        Noisy Periodic and Quasi-Periodic Signals", Algorithms 2012,
         5, 588-603

        Parameters
        ----------
        sig_input: ndarray
            The 1D signal given as input to the algorithm
        LSM_limit: float
            Wavelet transform limit as a ratio of full signal length.
            Valid values: 0-1, the LSM array will no longer be calculated after this point
              which results in the inability to find peaks at a scale larger than this factor.
              For example a value of .5 will be unable to find peaks that are of period 
              1/2 * signal length, a default value of 1 will search all LSM sizes.

        Returns
        -------
        pks: ndarray
            The ordered array of peaks found in sig_input
    """
        
    # Create preprocessing linear fit    
    sig_time = np.arange(0, len(sig_input))
    
    # Detrend
    dtr_signal = (sig_input - np.polyval(np.polyfit(sig_time, sig_input, 1), sig_time)).astype(float)
    
    N = len(dtr_signal)
    L = int(np.ceil(N*LSM_limit / 2.0)) - 1
    
    # Generate random matrix
    LSM = np.ones([L, N], dtype='uint8')
    
    # Local minima extraction
    for k in range(1, L):
        LSM[k - 1, np.where((dtr_signal[k:N - k - 1] > dtr_signal[0: N - 2 * k - 1]) & (dtr_signal[k:N - k - 1] > dtr_signal[2 * k: N - 1]))[0]+k] = 0
    
    pks = np.where(np.sum(LSM[0:np.argmin(np.sum(LSM, 1)), :], 0)==0)[0]
    return pks


def AMPD_avoid_MemoryError(data):
    try:
        all_index = ampd(data)
        all_data = data[all_index]

    except Exception:
        start_index = 0
        all_index = np.array([])
        all_data = np.array([])

        while end_index != len(data):
            # ampd
            end_index = min(start_index + scan_range, len(data))
            arr_data = data[start_index:end_index]
            arr_index = ampd(np.array(arr_data))

            # get real index and value
            real_index = arr_index + start_index
            real_data = arr_data[arr_index]

            # append
            if len(all_index) != 0:
                append_i = np.argwhere(real_index>all_index[-1]).reshape(-1)
                real_index = real_index[append_i]
                real_data = real_data[append_i]
                
            all_index = np.append(all_index, real_index)
            all_data = np.append(all_data, real_data)

    return all_index, all_data