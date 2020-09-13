import os

def write_str(string, file_dir, newline=True):
	if newline:
		if os.path.exists(file_dir):
			string = '\n' + string

	with open(file_dir, 'a', encoding='utf-8') as fp:
		fp.write(string)