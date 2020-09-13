import numpy as np

def raw_var(var):
	# this function will return a raw string of variable
    if isinstance(var, (list, np.ndarray, tuple)):
        if isinstance(var, list):
            opt_str, end_str = '[', ']'
        elif isinstance(var, np.ndarray):
            opt_str, end_str = 'np.array([', '])'
        elif isinstance(var, tuple):
            opt_str, end_str = '(', ')'

        if len(var) != 0:
            for v in var:
                if isinstance(var, np.ndarray):
                    opt_str += raw_var(v.tolist()) + ', '
                else:
                    opt_str += raw_var(v) + ', '
            opt_str = opt_str[:-2] + end_str
        else:
            opt_str += end_str

    # check dict
    elif isinstance(var, dict):
        if len(var) != 0:
            opt_str = '{'
            for key, value in var.items():
                opt_str += '{:}: {:}, '.format(raw_var(key), raw_var(value))
            opt_str = opt_str[:-2] + '}'
        else:
            opt_str = '{}'
    else:
        opt_str = str(var)

    return opt_str