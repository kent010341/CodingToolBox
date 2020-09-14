# Math Document
## Description
Extension mathods that doesn't support by Numpy or Scipy.

## Methods
* norm_p(arr, p=1, lib=numpy)
  * Return norm of arr.
  * parameters:
    * arr: numpy.ndarray (or any calculating supported type)
      * Array that used to calculate norm.
    * p: int, optional (default=1)
      * Variable p in formula: $$\norm \textbf{x} \norm _p = \left(\sum_i{x_i} \right)^{\frac{1}{p}}$$
