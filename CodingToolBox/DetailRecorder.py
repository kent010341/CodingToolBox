import os
import numpy as np
from datetime import datetime

from .RawVar import raw_var
from .core.Checker import auto_mkdir_checker
from .core.MsgCore import current_time
from .core.FileWriter import write_str

class DetailRecorder:
    def __init__(self, detail_dir, file_name=None, show_time=False):
        auto_mkdir_checker(detail_dir)

        # If use_time_as_name is true, using current time as file name.
        if file_name == None:
            file_name = current_time()

        self.__full_dir__ = '{}/{}.txt'.format(detail_dir, file_name)
        self.__show_time__ = show_time

    def dprint(self, *strings, end=' ', raw=True):
        opt = ''
        for string in strings:
            if raw:
                string = raw_var(string)

            opt += str(string) + end

        opt = opt[:-1]
        self.__write_to_file__(opt)

    def __write_to_file__(self, string):
        if self.__show_time__:
            string = '<{:}> {:}'.format(current_time('%Y/%m/%d %H:%M:%S.%f'), string)

        write_str(string, self.__full_dir__)