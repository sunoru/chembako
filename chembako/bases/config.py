# coding=utf-8
import os


class Config(object):
    GMX_DIR = "/usr/local/gromacs"
    PACKMOL_BIN_DIR = "/usr/bin"
    LOG_DIR = "."

    @classmethod
    def get_log_file(cls, log_filename, mode='a'):
        return open(os.path.join(cls.LOG_DIR, log_filename), mode)
