# encoding: utf-8
# module PyQt4.QtGui
# from C:\Python27\lib\site-packages\PyQt4\QtGui.pyd
# by generator 1.145
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QAbstractProxyModel(__PyQt4_QtCore.QAbstractItemModel):
    """ QAbstractProxyModel(QObject parent=None) """
    def beginInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def buddy(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.buddy(QModelIndex) -> QModelIndex """
        pass

    def canFetchMore(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.canFetchMore(QModelIndex) -> bool """
        return False

    def changePersistentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, QModelIndex, int_role=None): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.data(QModelIndex, int role=Qt.DisplayRole) -> QVariant """
        pass

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def encodeData(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endMoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def endResetModel(self, *args, **kwargs): # real signature unknown
        pass

    def fetchMore(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.fetchMore(QModelIndex) """
        pass

    def flags(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.flags(QModelIndex) -> Qt.ItemFlags """
        pass

    def hasChildren(self, QModelIndex_parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ QAbstractProxyModel.hasChildren(QModelIndex parent=QModelIndex()) -> bool """
        pass

    def headerData(self, p_int, Qt_Orientation, p_int_1): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.headerData(int, Qt.Orientation, int) -> QVariant """
        pass

    def itemData(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.itemData(QModelIndex) -> dict-of-int-QVariant """
        pass

    def mapFromSource(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.mapFromSource(QModelIndex) -> QModelIndex """
        pass

    def mapSelectionFromSource(self, QItemSelection): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.mapSelectionFromSource(QItemSelection) -> QItemSelection """
        return QItemSelection

    def mapSelectionToSource(self, QItemSelection): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.mapSelectionToSource(QItemSelection) -> QItemSelection """
        return QItemSelection

    def mapToSource(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.mapToSource(QModelIndex) -> QModelIndex """
        pass

    def mimeData(self, list_of_QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.mimeData(list-of-QModelIndex) -> QMimeData """
        pass

    def mimeTypes(self): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.mimeTypes() -> QStringList """
        pass

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def resetInternalData(self, *args, **kwargs): # real signature unknown
        pass

    def revert(self): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.revert() """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, QModelIndex, QVariant, int_role=None): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.setData(QModelIndex, QVariant, int role=Qt.EditRole) -> bool """
        return False

    def setHeaderData(self, p_int, Qt_Orientation, QVariant, int_role=None): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.setHeaderData(int, Qt.Orientation, QVariant, int role=Qt.EditRole) -> bool """
        return False

    def setItemData(self, QModelIndex, dict_of_int_QVariant): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.setItemData(QModelIndex, dict-of-int-QVariant) -> bool """
        return False

    def setRoleNames(self, *args, **kwargs): # real signature unknown
        pass

    def setSourceModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.setSourceModel(QAbstractItemModel) """
        pass

    def sort(self, p_int, Qt_SortOrder_order=None): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.sort(int, Qt.SortOrder order=Qt.AscendingOrder) """
        pass

    def sourceModel(self): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.sourceModel() -> QAbstractItemModel """
        pass

    def span(self, QModelIndex): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.span(QModelIndex) -> QSize """
        pass

    def submit(self): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.submit() -> bool """
        return False

    def supportedDropActions(self): # real signature unknown; restored from __doc__
        """ QAbstractProxyModel.supportedDropActions() -> Qt.DropActions """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QObject_parent=None): # real signature unknown; restored from __doc__
        pass


