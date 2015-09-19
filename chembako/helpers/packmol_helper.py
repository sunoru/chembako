# coding=utf-8
import os
import subprocess
import sys
from chembako.bases import Config, CommandSet


class Packmol(CommandSet):
    _log_filename = "packmol.log"

    def __init__(self, parallel=False):
        super(Packmol, self).__init__()
        self.parallel = parallel

    @property
    def _packmol_bin(self):
        return os.path.join(Config.PACKMOL_BIN_DIR, 'ppackmol' if self.parallel else 'packmol')

    def run(self, inp_str):
        sp = subprocess.Popen([self._packmol_bin], stdin=subprocess.PIPE, stdout=sys.stdout, stderr=self._log_file)
        self._log("Running packmol with pid: %s." % sp.pid)
        sp.stdin.write(inp_str)
        sp.stdin.close()
        sp.wait()
        self._log("Packmol completed.")

    def run_with_file(self, inp_file):
        if isinstance(inp_file, str):
            inp_file = open(inp_file)
        sp = subprocess.Popen([self._packmol_bin], stdin=inp_file, stdout=self._log_file)
        self._log("Running packmol with pid: %s." % sp.pid)
        sp.wait()
        inp_file.close()
        self._log("Packmol completed.")
