# coding=utf-8
import numpy as np
import os
from chembako.helpers import gromacs, packmol


# Much infomation from:
# http://compchemmpi.wikispaces.com/Manual+on+Computational+Physical+Chemistry+of+Ionic+liquids+at+Interfaces

def packmol_impurity(cation, anion, impurity='', output='packmol.pdb', filetype='pdb', number_il=200, number_im=0,
                     box_size=np.array((50, 50, 50), float), seed=191917, log_file="packmol.log"):
    """
    Make a box using packmol with the specified cation and anion.
    """
    try:
        inp_str = 'tolerance 2.0\n' \
                  'filetype {filetype}\n' \
                  'output {output}\n' \
                  'seed {seed}\n' \
                  'add_box_sides\n' \
                  '\n' \
                  'structure {cation}\n' \
                  '    number {number_il}\n' \
                  '    inside box 0. 0. 0. {size[0]} {size[1]} {size[2]}\n' \
                  'end structure\n' \
                  '\n' \
                  'structure {anion}\n' \
                  '    number {number_il}\n' \
                  '    inside box 0. 0. 0. {size[0]} {size[1]} {size[2]}\n' \
                  'end structure\n' \
                  '\n' \
                  'structure {impurity}\n' \
                  '    number {number_im}\n' \
                  '    inside box 0. 0. 0. {size[0]} {size[1]} {size[2]}\n' \
                  'end structure\n'.format(filetype=filetype, output=output, seed=seed, cation=cation, anion=anion,
                                           impurity=impurity, number_il=number_il, number_im=number_im, size=box_size)
    except TypeError or IndexError or KeyError as e:
        raise e
    print "Packmol input:"
    print inp_str
    packmol.run(inp_str)
    if gromacs.editconf(output, '%s.gro' % '.'.join(output.split('.')[:-1])):
        os.remove(output)
        print "Packmol successfully."
        return True
    else:
        print "Error occured."
        return False
