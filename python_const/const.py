class _const:
    class ConstError(TypeError): pass
    class ConstCaseError(ConstError): pass

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't change the const. '%s'" % name

        if not name.isupper():
            raise self.ConstCaseError, "Const name '%s' is not all uppercase" % name

        self.__dict__[name] = value

import sys
sys.modules[__name__] = _const()
