# encoding: utf-8
# module PyQt4.QtScriptTools
# from C:\Python27\lib\site-packages\PyQt4\QtScriptTools.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


# no functions
# classes

class QScriptEngineDebugger(__PyQt4_QtCore.QObject):
    """ QScriptEngineDebugger(QObject parent=None) """
    def action(self, QScriptEngineDebugger_DebuggerAction): # real signature unknown; restored from __doc__
        """ QScriptEngineDebugger.action(QScriptEngineDebugger.DebuggerAction) -> QAction """
        pass

    def attachTo(self, QScriptEngine): # real signature unknown; restored from __doc__
        """ QScriptEngineDebugger.attachTo(QScriptEngine) """
        pass

    def autoShowStandardWindow(self): # real signature unknown; restored from __doc__
        """ QScriptEngineDebugger.autoShowStandardWindow() -> bool """
        return False

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createStandardMenu(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        """ QScriptEngineDebugger.createStandardMenu(QWidget parent=None) -> QMenu """
        pass

    def createStandardToolBar(self, QWidget_parent=None): # real signature unknown; restored from __doc__
        """ QScriptEngineDebugger.createStandardToolBar(QWidget parent=None) -> QToolBar """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def detach(self): # real signature unknown; restored from __doc__
        """ QScriptEngineDebugger.detach() """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def evaluationResumed(self, *args, **kwargs): # real signature unknown
        """ QScriptEngineDebugger.evaluationResumed [signal] """
        pass

    def evaluationSuspended(self, *args, **kwargs): # real signature unknown
        """ QScriptEngineDebugger.evaluationSuspended [signal] """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoShowStandardWindow(self, bool): # real signature unknown; restored from __doc__
        """ QScriptEngineDebugger.setAutoShowStandardWindow(bool) """
        pass

    def standardWindow(self): # real signature unknown; restored from __doc__
        """ QScriptEngineDebugger.standardWindow() -> QMainWindow """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ QScriptEngineDebugger.state() -> QScriptEngineDebugger.DebuggerState """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def widget(self, QScriptEngineDebugger_DebuggerWidget): # real signature unknown; restored from __doc__
        """ QScriptEngineDebugger.widget(QScriptEngineDebugger.DebuggerWidget) -> QWidget """
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass

    BreakpointsWidget = 6
    ClearConsoleAction = 10
    ClearDebugOutputAction = 8
    ClearErrorLogAction = 9
    CodeFinderWidget = 5
    CodeWidget = 4
    ConsoleWidget = 0
    ContinueAction = 1
    DebugOutputWidget = 7
    ErrorLogWidget = 8
    FindInScriptAction = 11
    FindNextInScriptAction = 12
    FindPreviousInScriptAction = 13
    GoToLineAction = 14
    InterruptAction = 0
    LocalsWidget = 3
    RunningState = 0
    RunToCursorAction = 5
    RunToNewScriptAction = 6
    ScriptsWidget = 2
    StackWidget = 1
    StepIntoAction = 2
    StepOutAction = 4
    StepOverAction = 3
    SuspendedState = 1
    ToggleBreakpointAction = 7


