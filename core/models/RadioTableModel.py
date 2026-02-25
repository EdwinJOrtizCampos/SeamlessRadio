from PySide6.QtCore import (
    QAbstractTableModel,
    Qt,
    QModelIndex
)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget

from core.sources.PlayableRadio import PlayableRadio

class RadioTableModel(QAbstractTableModel):
    def __init__(self, parent: QWidget, items: list[PlayableRadio]):
        super().__init__(parent)
        self._items = items

    def rowCount(self, parent=QModelIndex()):
        return 1

    def columnCount(self, parent=QModelIndex()):
        return len(self._items)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        radio: PlayableRadio = self._items[index.column()]

        if role == Qt.ItemDataRole.DisplayRole:
            return radio.name

        # ? if role == Qt.ItemDataRole.DecorationRole:
        # ?     return QIcon(radio.thumbnail)

        if role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignmentFlag.AlignCenter

        return None

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags

        return (
            Qt.ItemFlag.ItemIsEnabled |
            Qt.ItemFlag.ItemIsSelectable
        )

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        return None
