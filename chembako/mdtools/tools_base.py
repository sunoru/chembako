# coding=utf-8
from chembako.bases import ToolBox
from chembako.mdtools.ionic_liquids import IonicLiquid


class MDTools(ToolBox):
    ionic_liquid = ToolBox._lazy_tool(IonicLiquid)
