# coding=utf-8
import sys
from chembako.bases.errors import CommandError


class CommandSet(object):
    _log_file = None
    _log_filename = None

    def __init__(self, log_file=None):
        if self._log_file is None:
            if isinstance(log_file, file):
                self._log_file = log_file
            elif isinstance(log_file, str):
                self._log_file = open(log_file, 'w')
            elif log_file is None:
                self._log_file = open(self._log_filename, 'w')
            else:
                raise CommandError("cannot recognize the log file type.")

    def __del__(self):
        if not (self._log_file is None or (sys is not None and self._log_file is sys.stdin)):
            self._log_file.close()

    def _log(self, log_str, print_on_screen=False, newline=True):
        log_str = '%s%s' % (log_str, '\n' if newline else "")
        self._log_file.write(log_str)
        if print_on_screen:
            sys.stdout.write(log_str)

    def _log_screen(self, log_str, newline=True):
        self._log(log_str, True, newline)

    @staticmethod
    def _command(func):
        def acommand(self, **kwargs):
            self._log("Running %s." % func.func_name)
            if func(self, **kwargs):
                self._log("%s completed." % func.func_name)
            else:
                self._log("%s failed." % func.func_name)

        return acommand
