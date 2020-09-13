import numpy as np
import os
from importlib.util import find_spec

from .MsgCore import msg_form, assert_msg

def ipt_eq_opt(ipt, opt):
    return ipt.shape[0] == opt.shape[0]

def dim_checker(arr, dim, msg=None):
    flag = len(arr.shape) == dim
    if not flag and msg != None:
        raise ValueError(msg)

    return flag

def iter_checher(arr):
    return hasattr(arr, '__getitem__')

def assert_seq_checker(var, var_label, seq):
    assert var in seq, assert_msg(var_label, seq)

def auto_mkdir_checker(folder_dir):
    assert isinstance(folder_dir, str), 'The path of folder should be a string.'
    if not os.path.exists(folder_dir):
        os.makedirs(folder_dir)