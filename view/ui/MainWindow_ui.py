# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

from view.widgets.CustomDial import CustomDial
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(995, 736)
        icon = QIcon()
        icon.addFile(u":/icons/favicon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget#widget_frame\n"
"{\n"
"	background-color: black;\n"
"}\n"
"\n"
"QWidget#widget_header\n"
"{\n"
"	background: transparent;\n"
"	border-bottom: 3px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.225275 rgba(196, 0, 0, 173), stop:0.505495 rgba(255, 0, 0, 255), stop:0.78022 rgba(196, 0, 0, 173), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"\n"
"QWidget#widget_footer\n"
"{\n"
"	background: transparent;\n"
"	border-top: 3px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.225275 rgba(196, 0, 0, 173), stop:0.505495 rgba(255, 0, 0, 255), stop:0.78022 rgba(196, 0, 0, 173), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"\n"
"QWidget#widget_content\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.496, y2:1, stop:0 rgba(17, 17, 17, 255), stop:1 rgba(82, 82, 82, 255));\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{\n"
"		color: white;\n"
"}\n"
"\n"
"QLabel#label_no_audio\n"
"{\n"
"	colo"
                        "r: #a70000;\n"
"}\n"
"\n"
"QWidget#widget_content QFrame[frameShape=\"5\"]\n"
" {\n"
"    background-color: transparent;\n"
"	border-left: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.225275 rgba(255, 0, 0, 180), stop:0.5 rgba(255, 0, 0, 255), stop:0.774725 rgba(255, 0, 0, 145), stop:1 rgba(255, 0, 0, 0));\n"
"}\n"
"\n"
"QWidget#widget_footer QFrame[frameShape=\"5\"]\n"
"{\n"
"    background-color: transparent;\n"
"	border-left: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.225275 rgba(255, 255, 255, 180), stop:0.5 rgba(255, 255, 255, 255), stop:0.774725 rgba(255, 255, 255, 145), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	border: none;\n"
"	color: white;\n"
"	height: 32px;\n"
"	width: 32px;\n"
"}\n"
"\n"
"QTableView#table_radio_list\n"
"{\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 8px;\n"
"    font-weight: 600;\n"
"}\n"
""
                        "\n"
"QTableView#table_radio_list::item\n"
"{\n"
"    border-right: 1px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.225275 rgba(196, 0, 0, 173), stop:0.505495 rgba(255, 0, 0, 255), stop:0.78022 rgba(196, 0, 0, 173), stop:1 rgba(255, 255, 255, 0));\n"
"    border-left: 1px solid qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:0.225275 rgba(196, 0, 0, 173), stop:0.505495 rgba(255, 0, 0, 255), stop:0.78022 rgba(196, 0, 0, 173), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"\n"
"QTableView#table_radio_list::item:selected\n"
"{\n"
"	color: red;\n"
"}\n"
"\n"
"QTableView#table_radio_list::item:hover:selected\n"
"{\n"
"	color: red;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background: transparent;\n"
"    height: 4px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(98, 98, 98);\n"
"    border-radius: 2px;\n"
"    min-width: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    backg"
                        "round: rgb(68, 68, 68);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: transparent;\n"
"}")
        self.widget_frame = QWidget(MainWindow)
        self.widget_frame.setObjectName(u"widget_frame")
        self.gridLayout = QGridLayout(self.widget_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_volume = QWidget(self.widget_frame)
        self.widget_volume.setObjectName(u"widget_volume")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_volume.sizePolicy().hasHeightForWidth())
        self.widget_volume.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.widget_volume)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_volume = QLabel(self.widget_volume)
        self.label_volume.setObjectName(u"label_volume")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_volume.setFont(font)
        self.label_volume.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_volume)

        self.dial_volume = CustomDial(self.widget_volume)
        self.dial_volume.setObjectName(u"dial_volume")
        self.dial_volume.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.dial_volume.setMinimum(0)
        self.dial_volume.setMaximum(100)
        self.dial_volume.setValue(50)
        self.dial_volume.setInvertedAppearance(False)
        self.dial_volume.setWrapping(False)
        self.dial_volume.setNotchTarget(3.700000000000000)
        self.dial_volume.setNotchesVisible(False)

        self.verticalLayout.addWidget(self.dial_volume)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)


        self.gridLayout.addWidget(self.widget_volume, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.widget_tune = QWidget(self.widget_frame)
        self.widget_tune.setObjectName(u"widget_tune")
        sizePolicy.setHeightForWidth(self.widget_tune.sizePolicy().hasHeightForWidth())
        self.widget_tune.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widget_tune)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.label_tune = QLabel(self.widget_tune)
        self.label_tune.setObjectName(u"label_tune")
        self.label_tune.setFont(font)
        self.label_tune.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_tune)

        self.dial_tune = CustomDial(self.widget_tune)
        self.dial_tune.setObjectName(u"dial_tune")
        self.dial_tune.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.dial_tune.setStyleSheet(u"")
        self.dial_tune.setMinimum(0)
        self.dial_tune.setMaximum(100)
        self.dial_tune.setSliderPosition(0)
        self.dial_tune.setOrientation(Qt.Orientation.Horizontal)
        self.dial_tune.setInvertedAppearance(False)
        self.dial_tune.setWrapping(True)
        self.dial_tune.setNotchTarget(3.700000000000000)
        self.dial_tune.setNotchesVisible(False)

        self.verticalLayout_2.addWidget(self.dial_tune)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)


        self.gridLayout.addWidget(self.widget_tune, 1, 2, 1, 1)

        self.widget_content = QWidget(self.widget_frame)
        self.widget_content.setObjectName(u"widget_content")
        self.verticalLayout_3 = QVBoxLayout(self.widget_content)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_header = QWidget(self.widget_content)
        self.widget_header.setObjectName(u"widget_header")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_header.sizePolicy().hasHeightForWidth())
        self.widget_header.setSizePolicy(sizePolicy1)
        self.widget_header.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_no_audio = QWidget(self.widget_header)
        self.widget_no_audio.setObjectName(u"widget_no_audio")
        sizePolicy.setHeightForWidth(self.widget_no_audio.sizePolicy().hasHeightForWidth())
        self.widget_no_audio.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget_no_audio)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_no_audio_icon = QLabel(self.widget_no_audio)
        self.label_no_audio_icon.setObjectName(u"label_no_audio_icon")
        self.label_no_audio_icon.setMinimumSize(QSize(32, 32))
        self.label_no_audio_icon.setMaximumSize(QSize(32, 32))
        self.label_no_audio_icon.setPixmap(QPixmap(u":/icons/noAudioOutput.png"))
        self.label_no_audio_icon.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_no_audio_icon)

        self.label_no_audio = QLabel(self.widget_no_audio)
        self.label_no_audio.setObjectName(u"label_no_audio")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_no_audio.sizePolicy().hasHeightForWidth())
        self.label_no_audio.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setBold(True)
        self.label_no_audio.setFont(font1)
        self.label_no_audio.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_no_audio)


        self.horizontalLayout_2.addWidget(self.widget_no_audio)

        self.label_current_time = QLabel(self.widget_header)
        self.label_current_time.setObjectName(u"label_current_time")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.label_current_time.setFont(font2)
        self.label_current_time.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_current_time)

        self.dummy_compensator_widget = QWidget(self.widget_header)
        self.dummy_compensator_widget.setObjectName(u"dummy_compensator_widget")

        self.horizontalLayout_2.addWidget(self.dummy_compensator_widget)

        self.horizontalLayout_2.setStretch(0, 33)
        self.horizontalLayout_2.setStretch(1, 33)

        self.verticalLayout_3.addWidget(self.widget_header)

        self.widget_radio_list = QWidget(self.widget_content)
        self.widget_radio_list.setObjectName(u"widget_radio_list")
        sizePolicy1.setHeightForWidth(self.widget_radio_list.sizePolicy().hasHeightForWidth())
        self.widget_radio_list.setSizePolicy(sizePolicy1)
        self.widget_radio_list.setMinimumSize(QSize(0, 40))
        self.widget_radio_list.setMaximumSize(QSize(16777215, 40))
        self.verticalLayout_4 = QVBoxLayout(self.widget_radio_list)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.table_radio_list = QTableView(self.widget_radio_list)
        self.table_radio_list.setObjectName(u"table_radio_list")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.table_radio_list.sizePolicy().hasHeightForWidth())
        self.table_radio_list.setSizePolicy(sizePolicy3)
        self.table_radio_list.setMinimumSize(QSize(0, 40))
        self.table_radio_list.setMaximumSize(QSize(16777215, 40))
        self.table_radio_list.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.table_radio_list.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_radio_list.setEditTriggers(QAbstractItemView.EditTrigger.CurrentChanged)
        self.table_radio_list.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table_radio_list.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.table_radio_list.setShowGrid(False)
        self.table_radio_list.setCornerButtonEnabled(False)
        self.table_radio_list.horizontalHeader().setVisible(False)
        self.table_radio_list.verticalHeader().setVisible(False)

        self.verticalLayout_4.addWidget(self.table_radio_list)


        self.verticalLayout_3.addWidget(self.widget_radio_list)

        self.widget_display = QWidget(self.widget_content)
        self.widget_display.setObjectName(u"widget_display")
        self.verticalLayout_7 = QVBoxLayout(self.widget_display)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_radio_visor = QWidget(self.widget_display)
        self.widget_radio_visor.setObjectName(u"widget_radio_visor")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_radio_visor)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_left_menu = QWidget(self.widget_radio_visor)
        self.widget_left_menu.setObjectName(u"widget_left_menu")
        self.verticalLayout_5 = QVBoxLayout(self.widget_left_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.button_am = QPushButton(self.widget_left_menu)
        self.button_am.setObjectName(u"button_am")
        self.button_am.setFont(font)
        self.button_am.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_am.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.button_am.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	color: red\n"
"}")
        self.button_am.setFlat(True)

        self.verticalLayout_5.addWidget(self.button_am)

        self.button_fm = QPushButton(self.widget_left_menu)
        self.button_fm.setObjectName(u"button_fm")
        self.button_fm.setFont(font)
        self.button_fm.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_fm.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.button_fm.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	color: red\n"
"}")
        self.button_fm.setFlat(True)

        self.verticalLayout_5.addWidget(self.button_fm)

        self.button_dab = QPushButton(self.widget_left_menu)
        self.button_dab.setObjectName(u"button_dab")
        self.button_dab.setFont(font)
        self.button_dab.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_dab.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.button_dab.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	color: red\n"
"}")
        self.button_dab.setFlat(True)

        self.verticalLayout_5.addWidget(self.button_dab)


        self.horizontalLayout_5.addWidget(self.widget_left_menu)

        self.line_11 = QFrame(self.widget_radio_visor)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_11)

        self.widget_3 = QWidget(self.widget_radio_visor)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, 12, -1)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_7 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_radio_icon = QLabel(self.widget_2)
        self.label_radio_icon.setObjectName(u"label_radio_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_radio_icon.sizePolicy().hasHeightForWidth())
        self.label_radio_icon.setSizePolicy(sizePolicy4)
        self.label_radio_icon.setMinimumSize(QSize(128, 128))
        self.label_radio_icon.setMaximumSize(QSize(128, 128))
        self.label_radio_icon.setPixmap(QPixmap(u":/thumbnails/noiconfm.png"))
        self.label_radio_icon.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_radio_icon)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_8 = QVBoxLayout(self.widget_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_radio_freq = QLabel(self.widget_4)
        self.label_radio_freq.setObjectName(u"label_radio_freq")
        font3 = QFont()
        font3.setPointSize(12)
        self.label_radio_freq.setFont(font3)
        self.label_radio_freq.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_radio_freq)

        self.label_radio_name = QLabel(self.widget_4)
        self.label_radio_name.setObjectName(u"label_radio_name")
        font4 = QFont()
        font4.setPointSize(26)
        font4.setBold(False)
        self.label_radio_name.setFont(font4)
        self.label_radio_name.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_radio_name)

        self.label_radio_url = QLabel(self.widget_4)
        self.label_radio_url.setObjectName(u"label_radio_url")
        self.label_radio_url.setFont(font3)
        self.label_radio_url.setTextFormat(Qt.TextFormat.PlainText)
        self.label_radio_url.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_radio_url.setOpenExternalLinks(True)
        self.label_radio_url.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.verticalLayout_8.addWidget(self.label_radio_url)

        self.label_radio_description = QLabel(self.widget_4)
        self.label_radio_description.setObjectName(u"label_radio_description")
        self.label_radio_description.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_radio_description)


        self.horizontalLayout_7.addWidget(self.widget_4)


        self.gridLayout_2.addWidget(self.widget_2, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_8, 2, 1, 1, 1)


        self.horizontalLayout_5.addWidget(self.widget_3)

        self.line_12 = QFrame(self.widget_radio_visor)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.VLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_12)

        self.widget_right_menu = QWidget(self.widget_radio_visor)
        self.widget_right_menu.setObjectName(u"widget_right_menu")
        self.verticalLayout_6 = QVBoxLayout(self.widget_right_menu)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_16 = QPushButton(self.widget_right_menu)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setFont(font)
        self.pushButton_16.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_16.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pushButton_16.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	color: red\n"
"}")
        self.pushButton_16.setFlat(True)

        self.verticalLayout_6.addWidget(self.pushButton_16)


        self.horizontalLayout_5.addWidget(self.widget_right_menu)


        self.verticalLayout_7.addWidget(self.widget_radio_visor)

        self.widget_main_menu = QWidget(self.widget_display)
        self.widget_main_menu.setObjectName(u"widget_main_menu")
        sizePolicy1.setHeightForWidth(self.widget_main_menu.sizePolicy().hasHeightForWidth())
        self.widget_main_menu.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_main_menu)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.button_explore = QPushButton(self.widget_main_menu)
        self.button_explore.setObjectName(u"button_explore")
        self.button_explore.setFont(font)
        self.button_explore.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_explore.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.button_explore.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	color: red\n"
"}")
        self.button_explore.setFlat(True)

        self.horizontalLayout_4.addWidget(self.button_explore)

        self.line_7 = QFrame(self.widget_main_menu)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_7)

        self.button_previous = QPushButton(self.widget_main_menu)
        self.button_previous.setObjectName(u"button_previous")
        self.button_previous.setFont(font)
        self.button_previous.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_previous.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.button_previous.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	color: red\n"
"}")
        self.button_previous.setFlat(True)

        self.horizontalLayout_4.addWidget(self.button_previous)

        self.line_8 = QFrame(self.widget_main_menu)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_8)

        self.button_syntonize = QPushButton(self.widget_main_menu)
        self.button_syntonize.setObjectName(u"button_syntonize")
        self.button_syntonize.setFont(font)
        self.button_syntonize.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_syntonize.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.button_syntonize.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	color: red\n"
"}")
        self.button_syntonize.setFlat(True)

        self.horizontalLayout_4.addWidget(self.button_syntonize)

        self.line_9 = QFrame(self.widget_main_menu)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_9)

        self.button_next = QPushButton(self.widget_main_menu)
        self.button_next.setObjectName(u"button_next")
        self.button_next.setFont(font)
        self.button_next.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_next.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.button_next.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	color: red\n"
"}")
        self.button_next.setFlat(True)

        self.horizontalLayout_4.addWidget(self.button_next)

        self.line_10 = QFrame(self.widget_main_menu)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_10)

        self.button_menu_audio = QPushButton(self.widget_main_menu)
        self.button_menu_audio.setObjectName(u"button_menu_audio")
        self.button_menu_audio.setFont(font)
        self.button_menu_audio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_menu_audio.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.button_menu_audio.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: white\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	color: red\n"
"}")
        self.button_menu_audio.setFlat(True)

        self.horizontalLayout_4.addWidget(self.button_menu_audio)


        self.verticalLayout_7.addWidget(self.widget_main_menu)


        self.verticalLayout_3.addWidget(self.widget_display)

        self.widget_footer = QWidget(self.widget_content)
        self.widget_footer.setObjectName(u"widget_footer")
        sizePolicy1.setHeightForWidth(self.widget_footer.sizePolicy().hasHeightForWidth())
        self.widget_footer.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_footer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_radio = QPushButton(self.widget_footer)
        self.button_radio.setObjectName(u"button_radio")
        self.button_radio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_radio.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.button_radio.setStyleSheet(u"QPushButton\n"
"{\n"
"image: url(:/icons/radioIconUnselected.png);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"image: url(:/icons/radioIconSelected.png);\n"
"}")
        self.button_radio.setIconSize(QSize(0, 0))
        self.button_radio.setFlat(True)

        self.horizontalLayout_3.addWidget(self.button_radio)

        self.line = QFrame(self.widget_footer)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.button_media = QPushButton(self.widget_footer)
        self.button_media.setObjectName(u"button_media")
        self.button_media.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_media.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.button_media.setStyleSheet(u"QPushButton\n"
"{\n"
"image: url(:/icons/mediaIconUnselected.png);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"image: url(:/icons/mediaIconSelected.png);\n"
"}")
        self.button_media.setFlat(True)

        self.horizontalLayout_3.addWidget(self.button_media)

        self.line_2 = QFrame(self.widget_footer)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.button_phone = QPushButton(self.widget_footer)
        self.button_phone.setObjectName(u"button_phone")
        self.button_phone.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_phone.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.button_phone.setStyleSheet(u"QPushButton\n"
"{\n"
"image: url(:/icons/phoneIconUnselected.png);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"image: url(:/icons/phoneIconSelected.png);\n"
"}")
        self.button_phone.setFlat(True)

        self.horizontalLayout_3.addWidget(self.button_phone)

        self.line_3 = QFrame(self.widget_footer)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.button_connect = QPushButton(self.widget_footer)
        self.button_connect.setObjectName(u"button_connect")
        self.button_connect.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_connect.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.button_connect.setStyleSheet(u"QPushButton\n"
"{\n"
"image: url(:/icons/connectIconUnselected.png);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"image: url(:/icons/connectIconSelected.png);\n"
"}")
        self.button_connect.setFlat(True)

        self.horizontalLayout_3.addWidget(self.button_connect)

        self.line_4 = QFrame(self.widget_footer)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_4)

        self.button_footer_audio = QPushButton(self.widget_footer)
        self.button_footer_audio.setObjectName(u"button_footer_audio")
        self.button_footer_audio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_footer_audio.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.button_footer_audio.setStyleSheet(u"QPushButton\n"
"{\n"
"image: url(:/icons/footerAudioIconUnselected.png);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"image: url(:/icons/footerAudioIconSelected.png);\n"
"}")
        self.button_footer_audio.setFlat(True)

        self.horizontalLayout_3.addWidget(self.button_footer_audio)

        self.line_5 = QFrame(self.widget_footer)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_5)

        self.button_settings = QPushButton(self.widget_footer)
        self.button_settings.setObjectName(u"button_settings")
        self.button_settings.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_settings.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.button_settings.setStyleSheet(u"QPushButton\n"
"{\n"
"image: url(:/icons/settingsIconUnselected.png);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"image: url(:/icons/settingsIconSelected.png);\n"
"}")
        self.button_settings.setFlat(True)

        self.horizontalLayout_3.addWidget(self.button_settings)

        self.line_6 = QFrame(self.widget_footer)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_6)

        self.button_trip = QPushButton(self.widget_footer)
        self.button_trip.setObjectName(u"button_trip")
        self.button_trip.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.button_trip.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.button_trip.setStyleSheet(u"QPushButton\n"
"{\n"
"image: url(:/icons/tripIconUnselected.png);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"image: url(:/icons/tripIconSelected.png);\n"
"}")
        self.button_trip.setFlat(True)

        self.horizontalLayout_3.addWidget(self.button_trip)


        self.verticalLayout_3.addWidget(self.widget_footer)


        self.gridLayout.addWidget(self.widget_content, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.widget_frame)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Seamless Radio", None))
        self.label_volume.setText(QCoreApplication.translate("MainWindow", u"\n"
"VOL", None))
        self.label_tune.setText(QCoreApplication.translate("MainWindow", u"SCROLL\n"
"TUNE", None))
        self.label_no_audio_icon.setText("")
        self.label_no_audio.setText(QCoreApplication.translate("MainWindow", u"Audio Inhabilitado", None))
        self.label_current_time.setText(QCoreApplication.translate("MainWindow", u"16:08", None))
        self.button_am.setText(QCoreApplication.translate("MainWindow", u"AM", None))
        self.button_fm.setText(QCoreApplication.translate("MainWindow", u"FM", None))
        self.button_dab.setText(QCoreApplication.translate("MainWindow", u"DAB", None))
        self.label_radio_icon.setText("")
        self.label_radio_freq.setText(QCoreApplication.translate("MainWindow", u"11.20 MHz", None))
        self.label_radio_name.setText(QCoreApplication.translate("MainWindow", u"TEST FM", None))
        self.label_radio_url.setText(QCoreApplication.translate("MainWindow", u"www.example.com", None))
        self.label_radio_description.setText(QCoreApplication.translate("MainWindow", u"Some description", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.button_explore.setText(QCoreApplication.translate("MainWindow", u"Explora", None))
        self.button_previous.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.button_syntonize.setText(QCoreApplication.translate("MainWindow", u" Sintonizar", None))
        self.button_next.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.button_menu_audio.setText(QCoreApplication.translate("MainWindow", u"Audio", None))
        self.button_radio.setText("")
        self.button_media.setText("")
        self.button_phone.setText("")
        self.button_connect.setText("")
        self.button_footer_audio.setText("")
        self.button_settings.setText("")
        self.button_trip.setText("")
    # retranslateUi

