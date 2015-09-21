# coding=utf-8


class ToolBox(object):
    @staticmethod
    def _lazy_tool(klass):
        q = "__%s" % klass.__name__

        def getx(self):
            if q not in self.__dict__:
                self.__dict__[q] = klass()
            return self.__dict__[q]

        return property(getx)
