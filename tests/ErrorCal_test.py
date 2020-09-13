import numpy as np
import math

def test_NpLoss():
    from CodingToolBox.NpLoss import MSE, RMSE, MAE, MAPE, SNR, SSIM

    t = np.linspace(-4*np.pi, 4*np.pi, 400)
    sin_t = np.sin(t)
    noisy_sin_t = sin_t + np.random.normal(0, 0.1, t.shape)

    for loss in (MSE, RMSE, MAE, MAPE, SNR, SSIM):
        print(loss(t, noisy_sin_t))

def test_TorchLoss():
    import torch
    from CodingToolBox.TorchLoss import MSE, RMSE, MAE, MAPE, SNR, SSIM

    t = torch.linspace(-4*math.pi, 4*math.pi, 400)
    sin_t = torch.sin(t)
    noisy_sin_t = sin_t + torch.normal(0, 0.1, t.shape)

    for loss in (MSE, RMSE, MAE, MAPE, SNR, SSIM):
        print(loss(t, noisy_sin_t))

if __name__ == '__main__':
	test_NpLoss()
	test_TorchLoss()