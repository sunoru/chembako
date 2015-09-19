# coding=utf-8
import numpy as np
import time
import os


# Much infomation from:
# http://compchemmpi.wikispaces.com/Manual+on+Computational+Physical+Chemistry+of+Ionic+liquids+at+Interfaces

def packmol_impurity(cation, anion, impurity='', filetype='pdb', number_il=200, number_im=0,
                     box_size=np.array((50, 50, 50), float), seed=None, packmol_bindir='/usr/bin'):
    """
    Make a box using packmol with the specified cation and anion.

    :param cation: The cation filename.
    :param anion: The anion filename.
    :param impurity: The impurity filename.
    """
    if seed is None:
        seed = int(time.time() * 1000)
    try:
        inp_str = 'tolerance 2.0\n'
        'filetype {filetype}\n'
        'output packmol . pdb\n'
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
    packmol_bin = os.path.join(packmol_bindir, 'packmol')
    os.system(packmol_bin)
