# encoding: utf-8
# module PyQt4.QtCore
# from C:\Python27\lib\site-packages\PyQt4\QtCore.pyd
# by generator 1.145
# no doc

# imports
import sip as __sip


from object import object

class pyqtSignal(object):
    """
    pyqtSignal(*types, name=str) -> signal

    types is normally a sequence of individual types.  Each type is either a
    type object or a string that is the name of a C++ type.  Alternatively
    each type could itself be a sequence of types each describing a different
    overloaded signal.
    name is the optional C++ name of the signal.  If it is not specified then
    the name of the class attribute that is bound to the signal is used.
    """
    def __call__(self, *more): # real signature unknown; restored from __doc__
        """ x.__call__(...) <==> x(...) """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __get__(self, obj, type=None): # real signature unknown; restored from __doc__
        """ descr.__get__(obj[, type]) -> value """
        pass

    def __init__(self, name=None, *types): # real signature unknown; restored from __doc__
        pass

    def connect(self, function):
        pass

    def emit(self, *args):
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass


