# coding=utf-8
import numpy as np
import os
from chembako.helpers import helpers
from chembako.bases import CommandSet


# Much infomation from:
# http://compchemmpi.wikispaces.com/Manual+on+Computational+Physical+Chemistry+of+Ionic+liquids+at+Interfaces
class IonicLiquid(CommandSet):
    _log_filename = 'ionic_liquid.log'

    def packmol_impurity(self, cation, anion, impurity=None, output='packmol.pdb', filetype='pdb', number_il=200,
                         number_im=0,
                         box_size=np.array((50, 50, 50), float), seed=191917):
        """
        Make a box using packmol with the specified cation and anion.
        """
        try:
            inp_str = 'tolerance 2.0\n' \
                      'filetype {filetype}\n' \
                      'output {output}\n' \
                      'seed {seed}\n' \
                      'add_box_sides 1.0\n' \
                      'structure {cation}\n' \
                      '    number {number_il}\n' \
                      '    inside box 0. 0. 0. {size[0]} {size[1]} {size[2]}\n' \
                      'end structure\n' \
                      'structure {anion}\n' \
                      '    number {number_il}\n' \
                      '    inside box 0. 0. 0. {size[0]} {size[1]} {size[2]}\n' \
                      'end structure\n'.format(filetype=filetype, output=output, seed=seed, cation=cation, anion=anion,
                                               number_il=number_il, size=box_size)
            if impurity is not None:
                inp_str += 'structure {impurity}\n' \
                           '    number {number_im}\n' \
                           '    inside box 0. 0. 0. {size[0]} {size[1]} {size[2]}\n' \
                           'end structure\n'.format(impurity=impurity, number_im=number_im, size=box_size)
        except TypeError or IndexError or KeyError as e:
            raise e
        self._log_screen("Packmol impurity input:")
        self._log_screen(inp_str)
        helpers.packmol.run(inp_str)
        if helpers.gromacs.editconf(output, '%s.gro' % '.'.join(output.split('.')[:-1])):
            os.remove(output)
            self._log_screen("Packmol impurity successfully.")
            return True
        else:
            self._log_screen("Error occured.")
            return False
