# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QActionGroup(__PyQt4_QtCore.QObject):
    """ QActionGroup(QObject) """
    def actions(self): # real signature unknown; restored from __doc__
        """ QActionGroup.actions() -> list-of-QAction """
        pass

    def addAction(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QActionGroup.addAction(QAction) -> QAction
        QActionGroup.addAction(QString) -> QAction
        QActionGroup.addAction(QIcon, QString) -> QAction
        """
        return QAction

    def checkedAction(self): # real signature unknown; restored from __doc__
        """ QActionGroup.checkedAction() -> QAction """
        return QAction

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def hovered(self, *args, **kwargs): # real signature unknown
        """ QActionGroup.hovered[QAction] [signal] """
        pass

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ QActionGroup.isEnabled() -> bool """
        return False

    def isExclusive(self): # real signature unknown; restored from __doc__
        """ QActionGroup.isExclusive() -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ QActionGroup.isVisible() -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeAction(self, QAction): # real signature unknown; restored from __doc__
        """ QActionGroup.removeAction(QAction) """
        pass

    def selected(self, *args, **kwargs): # real signature unknown
        """ QActionGroup.selected[QAction] [signal] """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDisabled(self, bool): # real signature unknown; restored from __doc__
        """ QActionGroup.setDisabled(bool) """
        pass

    def setEnabled(self, bool): # real signature unknown; restored from __doc__
        """ QActionGroup.setEnabled(bool) """
        pass

    def setExclusive(self, bool): # real signature unknown; restored from __doc__
        """ QActionGroup.setExclusive(bool) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ QActionGroup.setVisible(bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def triggered(self, *args, **kwargs): # real signature unknown
        """ QActionGroup.triggered[QAction] [signal] """
        pass

    def __init__(self, QObject): # real signature unknown; restored from __doc__
        pass


