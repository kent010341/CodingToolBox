import numpy as _np
from ..Math import norm_p

def MSE(real, predict):
    return ((real - predict)**2).mean()

def RMSE(real, predict):
    return MSE(real, predict) ** 0.5

def MAE(real, predict, lib=_np):
    return lib.abs(real - predict).mean()

def MAPE(real, predict, lib=_np):
    return lib.abs((real - predict)/real).mean() * 100

def SNR(real, predict, lib=_np):
    norm_real = norm_p(real, 2, lib)
    norm_noise = norm_p(real-predict, 2, lib)

    return 20*lib.log10(norm_real/norm_noise)

def SSIM(real, predict, c1=1e-4, c2=3e-4):
    mean_real = real.mean()
    mean_predict = predict.mean()
    var_real = real.var()
    var_predict = predict.var()

    cov = ((predict - mean_predict) * (real - mean_real)).mean()

    ssim_val = (2*mean_predict*mean_real+c1)*(2*cov+c2)
    ssim_val /= (mean_predict**2+mean_real**2+c1)*(var_predict+var_real+c2)

    return ssim_val