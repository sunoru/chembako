# coding=utf-8
import os
from chembako.bases import Config, CommandSet


class Gromacs(CommandSet):
    _log_filename = "gromacs.log"

    @property
    def _gmx_bin_dir(self):
        return os.path.join(Config.GMX_DIR, 'bin')

    @property
    def _gmx_bin(self):
        return os.path.join(self._gmx_bin_dir, 'gmx')

    @CommandSet._command
    def editconf(self, input_file, output_file, other_args=None):
        if other_args is None:
            other_args = ""
        return os.system("{gmx} editconf -f {input_file} -o {output_file} {other_args}".format(
            gmx=self._gmx_bin, input_file=input_file, output_file=output_file, other_args=other_args
        )) == 0
