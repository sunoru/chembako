# coding=utf-8
from chembako.bases import ToolBox
from chembako.helpers.gromacs_helper import Gromacs
from chembako.helpers.packmol_helper import Packmol


class Helpers(ToolBox):
    gromacs = ToolBox._lazy_tool(Gromacs)
    packmol = ToolBox._lazy_tool(Packmol)
