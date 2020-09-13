import numpy as _np
from .core.Checker import dim_checker as _dim_checker
from .core.Checker import iter_checher as _iter_checher
from .core.Checker import assert_seq_checker as _assert_seq_checker
from .core.MsgCore import msg_form as _msg_form

def fft_smooth(arr, fs, filter_f, filter_type):
    # check input
    _dim_checker(arr, dim=1, msg=_msg_form('arr must be 1-D.'))
    _assert_seq_checker(filter_type, 'filter_type', ('lowpass', 'bandpass', 'highpass'))

    # fft and generate 0~fs array
    fft_arr = _np.fft.fft(arr)
    vector_f = _np.linspace(0, fs, arr.shape[0])

    if filter_type == 'lowpass':
        filtered_arr = _np.where(vector_f <= filter_f, fft_arr, 0)

    elif filter_type == 'highpass':
        filtered_arr = _np.where(vector_f >= filter_f, fft_arr, 0)

    elif filter_type == 'bandpass':
        # raise exceptions
        assert _iter_checher(filter_f), 'filter_f must be iterable if filter_type is bandpass.'
        assert filter_f.shape == (2,), 'filter_f must only have two elements if filter_type is bandpass.'
        assert filter_f[0] != filter_f[1], 'filter_f must have different elements.'

        lb, ub = filter_f
        if lb > ub:
            lb, ub = ub, lb

        filtered_arr = _np.where(vector_f >= lb and vector_f <= ub, fft_arr, 0)

    return _np.fft.ifft(filtered_arr)

def MA_smooth(arr, avg_len, smooth_type='middle'):
    # check input
    arr = _np.array(arr)
    _dim_checker(arr, dim=1, msg=_msg_form('arr must be 1-D.'))
    _assert_seq_checker(smooth_type, 'smooth_type', ('middle', 'start', 'end'))

    # smooth
    opt = arr.copy()

    if smooth_type == 'middle':
        if avg_len % 2 == 0:
            print('Warning: avg_len ({}) is suggest to be odd when smooth_type is \'middle\'.'.format(avg_len))
        avg_len = int(avg_len/2)

        for i in range(len(arr)):
            start_i, end_i = max(0, i-avg_len), min(len(arr), i+avg_len+1)
            opt[i] = arr[start_i: end_i].mean()

    elif smooth_type == 'start':
    	for i in range(len(arr)):
            end_i = min(len(arr), i + avg_len + 1)
            opt[i] = _np.mean(arr[i: end_i])

    elif smooth_type == 'end':
        for i in range(len(arr)):
            start_i = max(0, i - avg_len)
            opt[i] = _np.mean(arr[start_i: i])

    return opt