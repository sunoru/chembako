# coding=utf-8
import os


class Config(object):
    GMX_DIR = "/usr/local/gromacs"
    PACKMOL_BIN_DIR = "/usr/bin"

    @property
    def GMX_BIN_DIR(self):
        return os.path.join(self.GMX_DIR, 'bin')

    @property
    def GMX_BIN(self):
        return os.path.join(self.GMX_BIN_DIR, 'gmx')
