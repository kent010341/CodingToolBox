from datetime import datetime

def msg_form(s, *args, **kwargs):
    return s.format(*args, **kwargs)

def assert_msg(var_name, lst, aux='should'):
    return '{} {} be in {}'.format(var_name, aux, lst)

def current_time(time_format='%Y%m%d_%H%M%S'):
	return datetime.now().strftime(time_format)