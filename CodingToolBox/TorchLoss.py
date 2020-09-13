import torch as _torch

from .core.ErrFunc import MSE, RMSE, SSIM
from .core.ErrFunc import MAE as __mae__
from .core.ErrFunc import MAPE as __mape__
from .core.ErrFunc import SNR as __snr__

MAE = lambda real, predict: __mae__(real, predict, lib=_torch)
MAPE = lambda real, predict: __mape__(real, predict, lib=_torch)
SNR = lambda real, predict: __snr__(real, predict, lib=_torch)