import numpy as _np

def norm_p(arr, p=1, lib=_np):
    if p == 2:
        return (arr**2).sum()**0.5
    else:
        abs_arr = lib.abs(arr)
        return (abs_arr**p).sum()**(1/p)

def sqrt(arr, lib=_np):
    return lib.where(arr > 0, arr**0.5, (-arr)**0.5*1j)