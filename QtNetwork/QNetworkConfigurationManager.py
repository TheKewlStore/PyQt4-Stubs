# encoding: utf-8
# module PyQt4.QtNetwork
# from C:\Python27\lib\site-packages\PyQt4\QtNetwork.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QNetworkConfigurationManager(__PyQt4_QtCore.QObject):
    """ QNetworkConfigurationManager(QObject parent=None) """
    def allConfigurations(self, QNetworkConfiguration_StateFlags_flags=0): # real signature unknown; restored from __doc__
        """ QNetworkConfigurationManager.allConfigurations(QNetworkConfiguration.StateFlags flags=0) -> list-of-QNetworkConfiguration """
        pass

    def capabilities(self): # real signature unknown; restored from __doc__
        """ QNetworkConfigurationManager.capabilities() -> QNetworkConfigurationManager.Capabilities """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def configurationAdded(self, *args, **kwargs): # real signature unknown
        """ QNetworkConfigurationManager.configurationAdded[QNetworkConfiguration] [signal] """
        pass

    def configurationChanged(self, *args, **kwargs): # real signature unknown
        """ QNetworkConfigurationManager.configurationChanged[QNetworkConfiguration] [signal] """
        pass

    def configurationFromIdentifier(self, QString): # real signature unknown; restored from __doc__
        """ QNetworkConfigurationManager.configurationFromIdentifier(QString) -> QNetworkConfiguration """
        return QNetworkConfiguration

    def configurationRemoved(self, *args, **kwargs): # real signature unknown
        """ QNetworkConfigurationManager.configurationRemoved[QNetworkConfiguration] [signal] """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultConfiguration(self): # real signature unknown; restored from __doc__
        """ QNetworkConfigurationManager.defaultConfiguration() -> QNetworkConfiguration """
        return QNetworkConfiguration

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isOnline(self): # real signature unknown; restored from __doc__
        """ QNetworkConfigurationManager.isOnline() -> bool """
        return False

    def onlineStateChanged(self, *args, **kwargs): # real signature unknown
        """ QNetworkConfigurationManager.onlineStateChanged[bool] [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateCompleted(self, *args, **kwargs): # real signature unknown
        """ QNetworkConfigurationManager.updateCompleted [signal] """
        pass

    def updateConfigurations(self): # real signature unknown; restored from __doc__
        """ QNetworkConfigurationManager.updateConfigurations() """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    ApplicationLevelRoaming = 8
    CanStartAndStopInterfaces = 1
    DataStatistics = 32
    DirectConnectionRouting = 2
    ForcedRoaming = 16
    NetworkSessionRequired = 64
    SystemSessionSupport = 4


