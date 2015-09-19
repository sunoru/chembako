# coding=utf-8
import pybel
from chembako.bases import ChemIOError


def _load_molecule(filename, filetype, opt):
    if filetype is None:
        try:
            filetype = filename.split('.')[1]
        except IndexError:
            raise ChemIOError('unable to recognize the file type.')
    try:
        tmol = pybel.readfile(filetype, filename, opt)
    except ValueError as e:
        raise ChemIOError(e.message)
    except IOError as e:
        raise ChemIOError(e.message)
    return tmol


def load_molecule(filename, filetype=None, opt=None):
    mol = _load_molecule(filename, filetype, opt).next()
    return mol


def load_molecules(filename, filetype=None, opt=None):
    mols = _load_molecule(filename, filetype, opt)
    return mols
