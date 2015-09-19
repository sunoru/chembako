# coding=utf-8
import pybel
import sys
from chembako.bases import ChemIOError, CommandSet


class IOHelper(CommandSet):
    logfile = sys.stdin

    def _load_molecule(self, filename, filetype, opt):
        self.log("Loading %s" % filename, newline=False)
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
        self.log("Done.")
        return tmol

    def load_molecule(self, filename, filetype=None, opt=None):
        mol = self._load_molecule(filename, filetype, opt).next()
        return mol

    def load_molecules(self, filename, filetype=None, opt=None):
        mols = self._load_molecule(filename, filetype, opt)
        return mols
