# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QButtonGroup(__PyQt4_QtCore.QObject):
    """ QButtonGroup(QObject parent=None) """
    def addButton(self, QAbstractButton, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QButtonGroup.addButton(QAbstractButton)
        QButtonGroup.addButton(QAbstractButton, int)
        """
        pass

    def button(self, p_int): # real signature unknown; restored from __doc__
        """ QButtonGroup.button(int) -> QAbstractButton """
        return QAbstractButton

    def buttonClicked(self, *args, **kwargs): # real signature unknown
        """
        QButtonGroup.buttonClicked[QAbstractButton] [signal]
        QButtonGroup.buttonClicked[int] [signal]
        """
        pass

    def buttonPressed(self, *args, **kwargs): # real signature unknown
        """
        QButtonGroup.buttonPressed[QAbstractButton] [signal]
        QButtonGroup.buttonPressed[int] [signal]
        """
        pass

    def buttonReleased(self, *args, **kwargs): # real signature unknown
        """
        QButtonGroup.buttonReleased[QAbstractButton] [signal]
        QButtonGroup.buttonReleased[int] [signal]
        """
        pass

    def buttons(self): # real signature unknown; restored from __doc__
        """ QButtonGroup.buttons() -> list-of-QAbstractButton """
        pass

    def checkedButton(self): # real signature unknown; restored from __doc__
        """ QButtonGroup.checkedButton() -> QAbstractButton """
        return QAbstractButton

    def checkedId(self): # real signature unknown; restored from __doc__
        """ QButtonGroup.checkedId() -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def exclusive(self): # real signature unknown; restored from __doc__
        """ QButtonGroup.exclusive() -> bool """
        return False

    def id(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ QButtonGroup.id(QAbstractButton) -> int """
        return 0

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeButton(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ QButtonGroup.removeButton(QAbstractButton) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setExclusive(self, bool): # real signature unknown; restored from __doc__
        """ QButtonGroup.setExclusive(bool) """
        pass

    def setId(self, QAbstractButton, p_int): # real signature unknown; restored from __doc__
        """ QButtonGroup.setId(QAbstractButton, int) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


