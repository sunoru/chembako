# coding=utf-8
import os
from chembako.bases import Config


def editconf(input_file, output_file, other_args=None):
    if other_args is None:
        other_args = ""
    return os.system("{gmx} editconf -f {input_file} -o {output_file} {other_args}".format(
        gmx=Config.GMX_BIN, input_file=input_file, output_file=output_file, other_args=other_args
    )) == 0
