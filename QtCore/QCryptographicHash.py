# encoding: utf-8
# module PyQt4.QtCore
# from C:\Python27\lib\site-packages\PyQt4\QtCore.pyd
# by generator 1.145
# no doc

# imports
import sip as __sip


class QCryptographicHash(): # skipped bases: <type 'sip.simplewrapper'>
    """ QCryptographicHash(QCryptographicHash.Algorithm) """
    def addData(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QCryptographicHash.addData(str)
        QCryptographicHash.addData(QByteArray)
        """
        pass

    def hash(self, QByteArray, QCryptographicHash_Algorithm): # real signature unknown; restored from __doc__
        """ QCryptographicHash.hash(QByteArray, QCryptographicHash.Algorithm) -> QByteArray """
        return QByteArray

    def reset(self): # real signature unknown; restored from __doc__
        """ QCryptographicHash.reset() """
        pass

    def result(self): # real signature unknown; restored from __doc__
        """ QCryptographicHash.result() -> QByteArray """
        return QByteArray

    def __init__(self, QCryptographicHash_Algorithm): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Md4 = 0
    Md5 = 1
    Sha1 = 2


