from hebi import GroupCommand
from time import sleep


def retry_on_error(func, on_error_func=None, sleep_time=0.1):
  while True:
    try:
      ret = func()
      return ret
    except Exception as e:
      if on_error_func != None:
        on_error_func()
      sleep(sleep_time)
