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
      * Variable p in formula: 
        ![](https://latex.codecogs.com/svg.latex?||\textbf{x}||_p%20=%20\left(\sum_i{x_i}%20\right)^{\frac{1}{p}})
