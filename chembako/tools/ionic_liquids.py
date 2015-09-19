# coding=utf-8
import numpy as np
import time
import os
import subprocess
from chembako.bases import Config
from chembako.helpers import gromacs


# Much infomation from:
# http://compchemmpi.wikispaces.com/Manual+on+Computational+Physical+Chemistry+of+Ionic+liquids+at+Interfaces

def packmol_impurity(cation, anion, impurity='', output='packmol.pdb', filetype='pdb', number_il=200, number_im=0,
                     box_size=np.array((50, 50, 50), float), seed=None, log_file="packmol.log", parallel=False):
    """
    Make a box using packmol with the specified cation and anion.
    """
    if seed is None:
        seed = int(time.time() * 1000)
    try:
        inp_str = 'tolerance 2.0\n'
        'filetype {filetype}\n'
        'output {output}\n'
        'seed {seed}\n'
        'add_box_sides\n'
        '\n'
        'structure {cation}\n'
        'number {number_il}\n'
        'inside box 0. 0. 0. {size[0]} {size[1]} {size[2]}\n'
        'end structure\n'
        '\n'
        'structure {anion}\n'
        'number {number_il}\n'
        'inside box 0. 0. 0. {size[0]} {size[1]} {size[2]}\n'
        'end structure\n'
        '\n'
        'structure {impurity}\n'
        'number {number_im}\n'
        'inside box 0. 0. 0. {size[0]} {size[1]} {size[2]}\n'
        'end structure\n'.format(
            filetype=filetype,
            output=output,
            seed=seed,
            cation=cation,
            anion=anion,
            impurity=impurity,
            number_il=number_il,
            number_im=number_im,
            size=box_size
        )
    except TypeError or IndexError or KeyError as e:
        raise e
    packmol_bin = os.path.join(Config.PACKMOL_BIN_DIR, 'ppackmol' if parallel else 'packmol')
    with open(log_file, 'w') as fo:
        sp = subprocess.Popen([packmol_bin], stdin=subprocess.PIPE, stdout=fo)
        sp.stdin.write(inp_str)
        sp.stdin.close()
    if gromacs.editconf(output, '%s.gro' % '.'.join(output.split('.')[:-1])):
        os.remove(output)
        print "Running packmol successfully."
        return True
    else:
        print "Error occured."
        return False
