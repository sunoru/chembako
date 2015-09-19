# coding=utf-8
import sys
import datetime
from chembako.bases import Config


class CommandSet(object):
    _log_file = None
    _log_filename = None

    class CommandError(Exception):
        pass

    def __del__(self):
        if not (self._log_file is None or (sys is not None and self._log_file is sys.stdin)):
            self._log_file.close()

    def _init_logfile(self):
        self._log_file = Config.get_log_file(self._log_filename)

    def _log(self, log_str, print_on_screen=False, newline=True):
        if self._log_file is None:
            self._init_logfile()
        log_str = '%s%s' % (log_str, '\n' if newline else "")
        log_str = "[%s] " % datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S') + log_str
        self._log_file.write(log_str)
        if print_on_screen:
            sys.stdout.write(log_str)

    def _log_screen(self, log_str, newline=True):
        self._log(log_str, True, newline)

    @staticmethod
    def _command(func):
        # make sure a command is supposed to return a boolean.
        def acommand(self, *args, **kwargs):
            self._log("Running %s." % func.func_name)
            result = func(self, *args, **kwargs)
            if result:
                self._log("%s completed." % func.func_name)
            else:
                self._log("%s failed." % func.func_name)
            return result

        return acommand
