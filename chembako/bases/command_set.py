# coding=utf-8
import sys


class CommandSet(object):
    _log_file = None
    _log_filename = None

    class CommandError(Exception):
        pass

    def __del__(self):
        if not (self._log_file is None or (sys is not None and self._log_file is sys.stdin)):
            self._log_file.close()

    def _init_logfile(self):
        self._log_file = open(self._log_filename, 'w')

    def _log(self, log_str, print_on_screen=False, newline=True):
        if self._log_file is None:
            self._init_logfile()
        log_str = '%s%s' % (log_str, '\n' if newline else "")
        self._log_file.write(log_str)
        if print_on_screen:
            sys.stdout.write(log_str)

    def _log_screen(self, log_str, newline=True):
        self._log(log_str, True, newline)

    @staticmethod
    def _command(func):
        def acommand(self, *args, **kwargs):
            self._log("Running %s." % func.func_name)
            if func(self, *args, **kwargs):
                self._log("%s completed." % func.func_name)
            else:
                self._log("%s failed." % func.func_name)

        return acommand
