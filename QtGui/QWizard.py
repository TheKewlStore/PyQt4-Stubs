# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


from QDialog import QDialog

class QWizard(QDialog):
    """ QWizard(QWidget parent=None, Qt.WindowFlags flags=0) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def addPage(self, QWizardPage): # real signature unknown; restored from __doc__
        """ QWizard.addPage(QWizardPage) -> int """
        return 0

    def back(self): # real signature unknown; restored from __doc__
        """ QWizard.back() """
        pass

    def button(self, QWizard_WizardButton): # real signature unknown; restored from __doc__
        """ QWizard.button(QWizard.WizardButton) -> QAbstractButton """
        return QAbstractButton

    def buttonText(self, QWizard_WizardButton): # real signature unknown; restored from __doc__
        """ QWizard.buttonText(QWizard.WizardButton) -> QString """
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cleanupPage(self, p_int): # real signature unknown; restored from __doc__
        """ QWizard.cleanupPage(int) """
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentId(self): # real signature unknown; restored from __doc__
        """ QWizard.currentId() -> int """
        return 0

    def currentIdChanged(self, *args, **kwargs): # real signature unknown
        """ QWizard.currentIdChanged[int] [signal] """
        pass

    def currentPage(self): # real signature unknown; restored from __doc__
        """ QWizard.currentPage() -> QWizardPage """
        return QWizardPage

    def customButtonClicked(self, *args, **kwargs): # real signature unknown
        """ QWizard.customButtonClicked[int] [signal] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ QWizard.done(int) """
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enabledChange(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ QWizard.event(QEvent) -> bool """
        return False

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def field(self, QString): # real signature unknown; restored from __doc__
        """ QWizard.field(QString) -> QVariant """
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def fontChange(self, *args, **kwargs): # real signature unknown
        pass

    def hasVisitedPage(self, p_int): # real signature unknown; restored from __doc__
        """ QWizard.hasVisitedPage(int) -> bool """
        return False

    def helpRequested(self, *args, **kwargs): # real signature unknown
        """ QWizard.helpRequested [signal] """
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initializePage(self, p_int): # real signature unknown; restored from __doc__
        """ QWizard.initializePage(int) """
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def languageChange(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ QWizard.next() """
        pass

    def nextId(self): # real signature unknown; restored from __doc__
        """ QWizard.nextId() -> int """
        return 0

    def options(self): # real signature unknown; restored from __doc__
        """ QWizard.options() -> QWizard.WizardOptions """
        pass

    def page(self, p_int): # real signature unknown; restored from __doc__
        """ QWizard.page(int) -> QWizardPage """
        return QWizardPage

    def pageAdded(self, *args, **kwargs): # real signature unknown
        """ QWizard.pageAdded[int] [signal] """
        pass

    def pageIds(self): # real signature unknown; restored from __doc__
        """ QWizard.pageIds() -> list-of-int """
        pass

    def pageRemoved(self, *args, **kwargs): # real signature unknown
        """ QWizard.pageRemoved[int] [signal] """
        pass

    def paintEvent(self, QPaintEvent): # real signature unknown; restored from __doc__
        """ QWizard.paintEvent(QPaintEvent) """
        pass

    def paletteChange(self, *args, **kwargs): # real signature unknown
        pass

    def pixmap(self, QWizard_WizardPixmap): # real signature unknown; restored from __doc__
        """ QWizard.pixmap(QWizard.WizardPixmap) -> QPixmap """
        return QPixmap

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removePage(self, p_int): # real signature unknown; restored from __doc__
        """ QWizard.removePage(int) """
        pass

    def resetInputContext(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, QResizeEvent): # real signature unknown; restored from __doc__
        """ QWizard.resizeEvent(QResizeEvent) """
        pass

    def restart(self): # real signature unknown; restored from __doc__
        """ QWizard.restart() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setButton(self, QWizard_WizardButton, QAbstractButton): # real signature unknown; restored from __doc__
        """ QWizard.setButton(QWizard.WizardButton, QAbstractButton) """
        pass

    def setButtonLayout(self, list_of_QWizard_WizardButton): # real signature unknown; restored from __doc__
        """ QWizard.setButtonLayout(list-of-QWizard.WizardButton) """
        pass

    def setButtonText(self, QWizard_WizardButton, QString): # real signature unknown; restored from __doc__
        """ QWizard.setButtonText(QWizard.WizardButton, QString) """
        pass

    def setDefaultProperty(self, p_str, p_str_1, p_str_2): # real signature unknown; restored from __doc__
        """ QWizard.setDefaultProperty(str, str, str) """
        pass

    def setField(self, QString, QVariant): # real signature unknown; restored from __doc__
        """ QWizard.setField(QString, QVariant) """
        pass

    def setOption(self, QWizard_WizardOption, bool_on=True): # real signature unknown; restored from __doc__
        """ QWizard.setOption(QWizard.WizardOption, bool on=True) """
        pass

    def setOptions(self, QWizard_WizardOptions): # real signature unknown; restored from __doc__
        """ QWizard.setOptions(QWizard.WizardOptions) """
        pass

    def setPage(self, p_int, QWizardPage): # real signature unknown; restored from __doc__
        """ QWizard.setPage(int, QWizardPage) """
        pass

    def setPixmap(self, QWizard_WizardPixmap, QPixmap): # real signature unknown; restored from __doc__
        """ QWizard.setPixmap(QWizard.WizardPixmap, QPixmap) """
        pass

    def setSideWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ QWizard.setSideWidget(QWidget) """
        pass

    def setStartId(self, p_int): # real signature unknown; restored from __doc__
        """ QWizard.setStartId(int) """
        pass

    def setSubTitleFormat(self, Qt_TextFormat): # real signature unknown; restored from __doc__
        """ QWizard.setSubTitleFormat(Qt.TextFormat) """
        pass

    def setTitleFormat(self, Qt_TextFormat): # real signature unknown; restored from __doc__
        """ QWizard.setTitleFormat(Qt.TextFormat) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ QWizard.setVisible(bool) """
        pass

    def setWizardStyle(self, QWizard_WizardStyle): # real signature unknown; restored from __doc__
        """ QWizard.setWizardStyle(QWizard.WizardStyle) """
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sideWidget(self): # real signature unknown; restored from __doc__
        """ QWizard.sideWidget() -> QWidget """
        return QWidget

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ QWizard.sizeHint() -> QSize """
        pass

    def startId(self): # real signature unknown; restored from __doc__
        """ QWizard.startId() -> int """
        return 0

    def subTitleFormat(self): # real signature unknown; restored from __doc__
        """ QWizard.subTitleFormat() -> Qt.TextFormat """
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def testOption(self, QWizard_WizardOption): # real signature unknown; restored from __doc__
        """ QWizard.testOption(QWizard.WizardOption) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def titleFormat(self): # real signature unknown; restored from __doc__
        """ QWizard.titleFormat() -> Qt.TextFormat """
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def validateCurrentPage(self): # real signature unknown; restored from __doc__
        """ QWizard.validateCurrentPage() -> bool """
        return False

    def visitedPages(self): # real signature unknown; restored from __doc__
        """ QWizard.visitedPages() -> list-of-int """
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def windowActivationChange(self, *args, **kwargs): # real signature unknown
        pass

    def winEvent(self, MSG): # real signature unknown; restored from __doc__
        """ QWizard.winEvent(MSG) -> (bool, int) """
        pass

    def wizardStyle(self): # real signature unknown; restored from __doc__
        """ QWizard.wizardStyle() -> QWizard.WizardStyle """
        pass

    def __init__(self, QWidget_parent=None, Qt_WindowFlags_flags=0): # real signature unknown; restored from __doc__
        pass

    AeroStyle = 3
    BackButton = 0
    BackgroundPixmap = 3
    BannerPixmap = 2
    CancelButton = 4
    CancelButtonOnLeft = 1024
    ClassicStyle = 0
    CommitButton = 2
    CustomButton1 = 6
    CustomButton2 = 7
    CustomButton3 = 8
    DisabledBackButtonOnLastPage = 64
    ExtendedWatermarkPixmap = 4
    FinishButton = 3
    HaveCustomButton1 = 8192
    HaveCustomButton2 = 16384
    HaveCustomButton3 = 32768
    HaveFinishButtonOnEarlyPages = 256
    HaveHelpButton = 2048
    HaveNextButtonOnLastPage = 128
    HelpButton = 5
    HelpButtonOnRight = 4096
    IgnoreSubTitles = 2
    IndependentPages = 1
    LogoPixmap = 1
    MacStyle = 2
    ModernStyle = 1
    NextButton = 1
    NoBackButtonOnLastPage = 32
    NoBackButtonOnStartPage = 16
    NoCancelButton = 512
    NoDefaultButton = 8
    Stretch = 9
    WatermarkPixmap = 0


