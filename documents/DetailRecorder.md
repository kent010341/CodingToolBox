# DetailRecorder Document

## Description
DetailRecorder can help developer recording anything including the time when it's recorded.

## class parameters
* detail_dir: str
  * Folder path.
* file_name: str, optional (default=None)
  * File name, defaultly using time format.
* show_time: bool, optional (default=False)
  * If true, string of current time will be added before each line.

## class method
* dprint(self, \*strings, end=' ', raw=True)
  * Similar to python built-in function 'print'.
  * parameters:
    * \*strings: any type
      * Variables needed to be written in file.
    * end: str, optional (default=' ')
      * All of \*strings will be separated by this parameter.
    * raw: bool, optional (default=True)
      * If true, every variable of \*strings will pass by method [CodingToolBox.raw_var()](https://github.com/kent010341/CodingToolBox/blob/master/documents/raw_var.md).
