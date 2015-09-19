# coding=utf-8
import sys
from chembako.bases.errors import CommandError


class CommandSet(object):
    log_file = None
    log_filename = None

    def __init__(self, log_file=None):
        if isinstance(log_file, file):
            self.log_file = log_file
        elif isinstance(log_file, str):
            self.log_file = open(log_file, 'w')
        elif log_file is None:
            self.log_file = open(self.log_filename, 'w')
        else:
            raise CommandError("cannot recognize the log file type.")

    def __del__(self):
        if self.log_file is not None and self.log_file is not sys.stdin:
            self.log_file.close()

    def log(self, log_str, newline=True):
        self.log_file.write('%s%s' % (log_str, '\n' if newline else ""))

    @staticmethod
    def command(func):
        def acommand(self, **kwargs):
            self.log("Running %s." % func.func_name)
            if func(self, **kwargs):
                self.log("%s completed." % func.func_name)
            else:
                self.log("%s failed." % func.func_name)

        return acommand
