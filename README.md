:no_entry: [DEPRECATED]
# CodingToolBox

## github:
[CodingToolBox](https://github.com/kent010341/CodingToolBox)

## Requires:
* Python 3.6 (or above)
* numpy

## Update dialog
* 1.0.0: Upload package.
* 1.1.0: Add two methods: ask_file_popup, ask_folder_popup
* 1.2.0: Add method: install_checker
  * 1.2.1: Edit copy in var_form.
  * 1.2.2: Fix init bug.
  * 1.2.3: Fix bug at DetailRecorder.
  * 1.2.4: Fix bug at DetailRecorder.
* 1.3.0: Add method: cal_SNR.
  * 1.3.1: Fix bug at cal_SNR.
  * 1.3.2: Use importlib.util.find_spec instead of ModuleNotFoundError. 
* 1.4.0: Add module: TorchLoss, contains various of loss function including MSE, RMSE, MAPE, MAE, SNR and SSIM.
* 2.0.0: Rewrite library, remove AnimatedPlot.
  * 2.0.1: fix bug.

## Lib Description
* Most of the functions are elaborated at my another repository [useful_coding_tools](https://github.com/kent010341/useful_coding_tools). 
* There're some demo at [CodingToolBox](https://github.com/kent010341/CodingToolBox).

## Lib Structure
* CodingToolBox
  * get_peak: Get indices and values of peaks of periodical signal by **automatic multiscale-based peak detection (AMPD)** algorithm.
  * DetailRecorder: Convenient recording tool.
  * raw_var: Return raw variable string that can easily be used in another script.
  * TkMethods: Methods based on tkinter.
    * ask_file: Popup menu for asking file location.
    * ask_folder: Popup menu for asking folder location.
  * Math: Math module.
    * norm_p: Return norm.
    * sqrt: Support negative value.
  * NpLoss: Loss function (NumPy version).
    * MAE: mean absulate error.
    * MAPE: mean absolute percentage error.
    * MSE: mean square error.
    * RMSE: root mean square error.
    * SNR: signal-to-noise ratio.
    * SSIM: structural similarity index.
  * TorchLoss: Loss function (PyTorch version).
    * MAE: mean absulate error.
    * MAPE: mean absolute percentage error.
    * MSE: mean square error.
    * RMSE: root mean square error.
    * SNR: signal-to-noise ratio.
    * SSIM: structural similarity index.
