# get_peak Document
## Description
Get indices and values of peaks of periodical signal by **automatic multiscale-based peak detection (AMPD)** algorithm.

## Method parameter
* data: list or numpy.ndarray
  * Periodical data.
* find_button: bool (optional=False)
  * If true, return buttom of data.
* scan_range: int (optional=1000)
  * Somtimes data is too large to directly calculate by AMPD. Therefore, this method will seperate data to pieces with legth scan_range.
