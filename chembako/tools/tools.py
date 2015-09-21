# coding=utf-8
from chembako.bases import ToolBox
from chembako.tools.ionic_liquids import IonicLiquid


class Tools(ToolBox):
    ionic_liquid = ToolBox._lazy_tool(IonicLiquid)
