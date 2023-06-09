# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASE_AK.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QTabWidget, QVBoxLayout, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 800)
        MainWindow.setMinimumSize(QSize(1000, 800))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Satoshi Black"])
        font.setPointSize(10)
        font.setBold(True)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/logoak16.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background: transparent; \n"
"/*font-family: \"Satoshi Black\"*/\n"
"}\n"
"\n"
"QToolTip {\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"QLineEdit::Text {\n"
"	width: parent.width\n"
"	height: parent.height\n"
"	font.pointSize: 100\n"
"	minimumPointSize: 10\n"
"	fontSizeMode: Text.Fit\n"
"}\n"
"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QLabel {\n"
"	color: rgb(210, 210, 210);\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: rgb(210, 210, 210);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	color: rgb(210, 210, 210);\n"
"}\n"
"\n"
"QSpinBox {\n"
"	color: rgb(210, 210, 210);\n"
"}\n"
"\n"
"QWidget {\n"
"	background: transparent;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	/*	background-image: url(:/bigSize/icons/bigSize/logoakbig.png);*/\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/bigSize/icons/bigSize/logoakbig.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle_menu.setIcon(icon1)
        self.btn_toggle_menu.setIconSize(QSize(50, 50))

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/24x24/icons/24x24/logoak24.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamilies([u"Satoshi Black"])
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setCursor(QCursor(Qt.ArrowCursor))
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon3)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(189, 0, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(189, 88, 88);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon4)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        self.label_top_info_1.setFont(font)
        self.label_top_info_1.setStyleSheet(u"color: rgb(159, 165, 177);")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        self.label_top_info_2.setFont(font)
        self.label_top_info_2.setStyleSheet(u"color: rgb(159, 165, 177);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        self.label_user_icon.setFont(font2)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setStyleSheet(u"QFrame#frame_content {\n"
"	border-image:url(:/bigSize/icons/bigSize/expeve.png) 0 0 0 0 fill stretch;\n"
"	\n"
"}")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"QWidget#page_home {\n"
"/*	border-image: url(:/bigSize/icons/bigSize/expeve.png) 0 0 0 0 fill stretch;*/\n"
"	border-radius: 15px\n"
"	\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame = QFrame(self.page_home)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(850, 500))
        self.frame_2.setStyleSheet(u"background: rgba(217, 217, 217, 0.5);\n"
"border: 2px solid #EBEBF0;\n"
"border-radius: 29px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_25 = QFrame(self.frame_2)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 95))
        self.frame_25.setMaximumSize(QSize(800, 450))
        self.frame_25.setStyleSheet(u"QFrame {\n"
"	background: #EDF3F8;\n"
"	border: 0px solid ;\n"
"	border-radius: 15px;\n"
"	padding: 4px\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_25)
        self.verticalLayout_14.setSpacing(15)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 10)
        self.verticalSpacer_4 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_4)

        self.frame_22 = QFrame(self.frame_25)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 114))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_22)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_22)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 45))
        font3 = QFont()
        font3.setFamilies([u"Satoshi Black"])
        font3.setPointSize(40)
        font3.setBold(True)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color: #2B704A;")
        self.label_6.setFrameShape(QFrame.NoFrame)
        self.label_6.setFrameShadow(QFrame.Plain)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setMargin(0)

        self.verticalLayout_6.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_22)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(790, 0))
        font4 = QFont()
        font4.setFamilies([u"Satoshi"])
        font4.setPointSize(20)
        font4.setBold(False)
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"color: #2B704A;")
        self.label_7.setLineWidth(1)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setMargin(-4)

        self.verticalLayout_6.addWidget(self.label_7)


        self.verticalLayout_14.addWidget(self.frame_22, 0, Qt.AlignHCenter)

        self.frame_15 = QFrame(self.frame_25)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(212, 210))
        self.frame_15.setMaximumSize(QSize(500, 500))
        self.frame_15.setStyleSheet(u"QFrame {\n"
"	/*background-image: url(:/bigSize/icons/bigSize/AKLOGO.png);*/\n"
"	border-image: url(:/bigSize/icons/bigSize/logodak.png) 0 0 0 0 stretch stretch;\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_15)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(9, -1, -1, -1)

        self.verticalLayout_14.addWidget(self.frame_15, 0, Qt.AlignHCenter)

        self.BtnMenuSimu = QPushButton(self.frame_25)
        self.BtnMenuSimu.setObjectName(u"BtnMenuSimu")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.BtnMenuSimu.sizePolicy().hasHeightForWidth())
        self.BtnMenuSimu.setSizePolicy(sizePolicy5)
        self.BtnMenuSimu.setMinimumSize(QSize(270, 55))
        font5 = QFont()
        font5.setFamilies([u"Satoshi Black"])
        font5.setPointSize(23)
        font5.setBold(True)
        font5.setStrikeOut(False)
        font5.setKerning(True)
        self.BtnMenuSimu.setFont(font5)
        self.BtnMenuSimu.setAutoFillBackground(False)
        self.BtnMenuSimu.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(56, 170, 72);\n"
"	border-radius: 12px;	\n"
"	background-color: #3F985A;\n"
"	color: #FFFFFF;\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 198, 84);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(37, 138, 26);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}")
        self.BtnMenuSimu.setIconSize(QSize(20, 20))
        self.BtnMenuSimu.setFlat(False)

        self.verticalLayout_14.addWidget(self.BtnMenuSimu, 0, Qt.AlignHCenter)


        self.horizontalLayout_12.addWidget(self.frame_25)


        self.horizontalLayout_9.addWidget(self.frame_2)


        self.verticalLayout_10.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_home)
        self.page_simular = QWidget()
        self.page_simular.setObjectName(u"page_simular")
        self.page_simular.setStyleSheet(u"QWidget#page_simular {\n"
"/*	border-image:url(:/bigSize/icons/bigSize/treeak.png) 0 0 0 0 fill stretch;*/\n"
"	border-radius: 15px\n"
"	\n"
"}")
        self.horizontalLayout_14 = QHBoxLayout(self.page_simular)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.frame_4 = QFrame(self.page_simular)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(450, 16777215))
        self.frame_4.setLayoutDirection(Qt.LeftToRight)
        self.frame_4.setStyleSheet(u"QFrame#frame_4 {\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"/*background-size: cover;\n"
"background-color: rgb(255, 255, 255);*/\n"
"border-radius: 5px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.calendarWidget = QCalendarWidget(self.frame_3)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setMaximumSize(QSize(16777215, 350))
        font6 = QFont()
        font6.setFamilies([u"Satoshi"])
        self.calendarWidget.setFont(font6)
        self.calendarWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.calendarWidget.setStyleSheet(u"QCalendarWidget {\n"
"    background-color: #FFFFFF; /* Establece el color de fondo claro */\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView {\n"
"    background-color: rgb(85, 255, 127); /* Establece el color de fondo claro para las vistas de los d\u00edas */\n"
"}\n"
"\n"
"QCalendarWidget QTableView {\n"
"    background-color: #FFFFFF; /* Establece el color de fondo claro para la tabla */\n"
"}")
        self.calendarWidget.setSelectedDate(QDate(2023, 8, 1))
        self.calendarWidget.setMinimumDate(QDate(2023, 8, 1))
        self.calendarWidget.setMaximumDate(QDate(2023, 8, 31))

        self.verticalLayout_8.addWidget(self.calendarWidget)

        self.BtnSimular = QPushButton(self.frame_3)
        self.BtnSimular.setObjectName(u"BtnSimular")
        sizePolicy5.setHeightForWidth(self.BtnSimular.sizePolicy().hasHeightForWidth())
        self.BtnSimular.setSizePolicy(sizePolicy5)
        self.BtnSimular.setMinimumSize(QSize(270, 55))
        self.BtnSimular.setMaximumSize(QSize(270, 16777215))
        font7 = QFont()
        font7.setFamilies([u"Satoshi Black"])
        font7.setPointSize(20)
        font7.setBold(True)
        font7.setStrikeOut(False)
        font7.setKerning(True)
        self.BtnSimular.setFont(font7)
        self.BtnSimular.setAutoFillBackground(False)
        self.BtnSimular.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(56, 170, 72);\n"
"	border-radius: 12px;	\n"
"	background-color: #3F985A;\n"
"	color: #FFFFFF;\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 198, 84);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(37, 138, 26);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}")
        self.BtnSimular.setIconSize(QSize(20, 20))
        self.BtnSimular.setFlat(False)

        self.verticalLayout_8.addWidget(self.BtnSimular, 0, Qt.AlignHCenter)


        self.verticalLayout_12.addWidget(self.frame_3)


        self.horizontalLayout_14.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.page_simular)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(380, 550))
        self.frame_5.setStyleSheet(u"QFrame#frame_5 {\n"
"background: rgba(217, 217, 217, 0.5);\n"
"border: 2px solid #EBEBF0;\n"
"border-radius: 29px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_37 = QFrame(self.frame_5)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMaximumSize(QSize(350, 515))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_37)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_37)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 75))
        self.frame_6.setStyleSheet(u"QFrame {\n"
"	background: #EDF3F8;\n"
"	border: 0px solid ;\n"
"	border-radius: 15px;\n"
"	padding: 4px\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.dia_label = QLabel(self.frame_6)
        self.dia_label.setObjectName(u"dia_label")
        font8 = QFont()
        font8.setFamilies([u"Satoshi Black"])
        font8.setPointSize(28)
        font8.setBold(True)
        self.dia_label.setFont(font8)
        self.dia_label.setStyleSheet(u"color: #2B704A;")
        self.dia_label.setFrameShape(QFrame.NoFrame)
        self.dia_label.setFrameShadow(QFrame.Plain)
        self.dia_label.setAlignment(Qt.AlignCenter)
        self.dia_label.setMargin(-10)

        self.verticalLayout_20.addWidget(self.dia_label)


        self.verticalLayout_18.addWidget(self.frame_6)

        self.verticalSpacer = QSpacerItem(0, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_18.addItem(self.verticalSpacer)

        self.frame_7 = QFrame(self.frame_37)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 50))
        self.frame_7.setStyleSheet(u"QFrame#frame_7 {\n"
"	background: rgba(221, 255, 227, 0.85);\n"
"	border: 0px solid ;\n"
"	border-radius: 15px;\n"
"	padding: 4px\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_7)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        font9 = QFont()
        font9.setFamilies([u"Satoshi Black"])
        font9.setPointSize(22)
        font9.setBold(True)
        self.label_12.setFont(font9)
        self.label_12.setStyleSheet(u"color: #3F894B;")
        self.label_12.setFrameShape(QFrame.NoFrame)
        self.label_12.setFrameShadow(QFrame.Plain)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setMargin(0)

        self.verticalLayout_22.addWidget(self.label_12)


        self.verticalLayout_18.addWidget(self.frame_7)

        self.frame_12 = QFrame(self.frame_37)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 70))
        self.frame_12.setStyleSheet(u"QFrame#frame_12 {\n"
"	background: rgba(221, 255, 227, 0.85);\n"
"	border: 0px solid ;\n"
"	border-radius: 15px;\n"
"	padding: 4px\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(310, 55))
        self.frame_13.setLayoutDirection(Qt.LeftToRight)
        self.frame_13.setAutoFillBackground(False)
        self.frame_13.setStyleSheet(u"QFrame {\n"
"	background: #3F894B;\n"
"	border: 0px solid ;\n"
"	border-radius: 10px;\n"
"	padding: 4px\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(10, 0, 17, 0)
        self.frame_50 = QFrame(self.frame_13)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(40, 40))
        self.frame_50.setMaximumSize(QSize(40, 40))
        self.frame_50.setStyleSheet(u"QFrame {\n"
"	/*background-image: url(:/bigSize/icons/bigSize/AKLOGO.png);*/\n"
"	border-image: url(:/24x24/icons/24x24/visitante.png) 0 0 0 0 stretch stretch;\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_50)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_25.addWidget(self.frame_50)

        self.visitantes_label = QLabel(self.frame_13)
        self.visitantes_label.setObjectName(u"visitantes_label")
        font10 = QFont()
        font10.setFamilies([u"Satoshi Black"])
        font10.setPointSize(20)
        font10.setBold(True)
        self.visitantes_label.setFont(font10)
        self.visitantes_label.setStyleSheet(u"color: #ffffff;")
        self.visitantes_label.setFrameShape(QFrame.NoFrame)
        self.visitantes_label.setFrameShadow(QFrame.Plain)
        self.visitantes_label.setAlignment(Qt.AlignCenter)
        self.visitantes_label.setMargin(0)

        self.horizontalLayout_25.addWidget(self.visitantes_label, 0, Qt.AlignHCenter)


        self.horizontalLayout_16.addWidget(self.frame_13)


        self.verticalLayout_18.addWidget(self.frame_12)

        self.verticalSpacer_2 = QSpacerItem(0, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_18.addItem(self.verticalSpacer_2)

        self.frame_8 = QFrame(self.frame_37)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 50))
        self.frame_8.setStyleSheet(u"QFrame#frame_8 {\n"
"	background: rgba(205, 229, 249, 0.85);\n"
"	border: 0px solid ;\n"
"	border-radius: 15px;\n"
"	padding: 4px\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_8)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font9)
        self.label_13.setStyleSheet(u"color: rgba(63, 136, 197, 1);")
        self.label_13.setFrameShape(QFrame.NoFrame)
        self.label_13.setFrameShadow(QFrame.Plain)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setMargin(0)

        self.verticalLayout_29.addWidget(self.label_13)


        self.verticalLayout_18.addWidget(self.frame_8)

        self.frame_40 = QFrame(self.frame_37)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMaximumSize(QSize(16777215, 95))
        self.frame_40.setStyleSheet(u"QFrame#frame_40 {\n"
"	background: rgba(205, 229, 249, 0.85);\n"
"	border: 0px solid ;\n"
"	border-radius: 15px;\n"
"	padding: 4px\n"
"}")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_40)
        self.verticalLayout_21.setSpacing(4)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 4, 0, 4)
        self.frame_46 = QFrame(self.frame_40)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(300, 38))
        self.frame_46.setMaximumSize(QSize(300, 16777215))
        self.frame_46.setLayoutDirection(Qt.LeftToRight)
        self.frame_46.setAutoFillBackground(False)
        self.frame_46.setStyleSheet(u"QFrame {\n"
"	background: rgba(63, 136, 197, 1);\n"
"	border: 0px solid ;\n"
"	border-radius: 10px;\n"
"	padding: 4px\n"
"}")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(6, 2, 6, 2)
        self.label_tipo_lluvia = QLabel(self.frame_46)
        self.label_tipo_lluvia.setObjectName(u"label_tipo_lluvia")
        self.label_tipo_lluvia.setMaximumSize(QSize(175, 16777215))
        font11 = QFont()
        font11.setFamilies([u"Satoshi Black"])
        font11.setPointSize(14)
        font11.setBold(True)
        self.label_tipo_lluvia.setFont(font11)
        self.label_tipo_lluvia.setStyleSheet(u"color: #ffffff;")
        self.label_tipo_lluvia.setFrameShape(QFrame.NoFrame)
        self.label_tipo_lluvia.setFrameShadow(QFrame.Plain)
        self.label_tipo_lluvia.setAlignment(Qt.AlignCenter)
        self.label_tipo_lluvia.setMargin(-4)

        self.horizontalLayout_32.addWidget(self.label_tipo_lluvia)

        self.horizontalSpacer = QSpacerItem(176, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer)

        self.lluvia_label = QLabel(self.frame_46)
        self.lluvia_label.setObjectName(u"lluvia_label")
        self.lluvia_label.setFont(font11)
        self.lluvia_label.setStyleSheet(u"color: #FBC400;")
        self.lluvia_label.setFrameShape(QFrame.NoFrame)
        self.lluvia_label.setFrameShadow(QFrame.Plain)
        self.lluvia_label.setAlignment(Qt.AlignCenter)
        self.lluvia_label.setMargin(0)

        self.horizontalLayout_32.addWidget(self.lluvia_label)

        self.lluvia_frame = QFrame(self.frame_46)
        self.lluvia_frame.setObjectName(u"lluvia_frame")
        self.lluvia_frame.setStyleSheet(u"")
        self.lluvia_frame.setFrameShape(QFrame.StyledPanel)
        self.lluvia_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.lluvia_frame)
        self.verticalLayout_32.setSpacing(6)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(9, -1, -1, -1)

        self.horizontalLayout_32.addWidget(self.lluvia_frame)


        self.verticalLayout_21.addWidget(self.frame_46, 0, Qt.AlignHCenter)

        self.frame_48 = QFrame(self.frame_40)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(300, 38))
        self.frame_48.setLayoutDirection(Qt.LeftToRight)
        self.frame_48.setAutoFillBackground(False)
        self.frame_48.setStyleSheet(u"QFrame {\n"
"	background: rgba(63, 136, 197, 1);\n"
"	border: 0px solid ;\n"
"	border-radius: 10px;\n"
"	padding: 4px\n"
"}")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(6, 2, 6, 2)
        self.label_25 = QLabel(self.frame_48)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(100, 16777215))
        self.label_25.setFont(font11)
        self.label_25.setStyleSheet(u"color: #ffffff;")
        self.label_25.setFrameShape(QFrame.NoFrame)
        self.label_25.setFrameShadow(QFrame.Plain)
        self.label_25.setAlignment(Qt.AlignCenter)
        self.label_25.setMargin(0)

        self.horizontalLayout_33.addWidget(self.label_25)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_2)

        self.huracan_label = QLabel(self.frame_48)
        self.huracan_label.setObjectName(u"huracan_label")
        self.huracan_label.setFont(font11)
        self.huracan_label.setStyleSheet(u"color: #FF0000;")
        self.huracan_label.setFrameShape(QFrame.NoFrame)
        self.huracan_label.setFrameShadow(QFrame.Plain)
        self.huracan_label.setAlignment(Qt.AlignCenter)
        self.huracan_label.setMargin(0)

        self.horizontalLayout_33.addWidget(self.huracan_label)

        self.huracan_frame = QFrame(self.frame_48)
        self.huracan_frame.setObjectName(u"huracan_frame")
        self.huracan_frame.setStyleSheet(u"")
        self.huracan_frame.setFrameShape(QFrame.StyledPanel)
        self.huracan_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.huracan_frame)
        self.verticalLayout_37.setSpacing(6)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(9, -1, -1, -1)

        self.horizontalLayout_33.addWidget(self.huracan_frame)


        self.verticalLayout_21.addWidget(self.frame_48, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.frame_40)

        self.verticalSpacer_3 = QSpacerItem(0, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_18.addItem(self.verticalSpacer_3)

        self.frame_11 = QFrame(self.frame_37)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 50))
        self.frame_11.setStyleSheet(u"QFrame#frame_11 {\n"
"	background: rgba(255, 210, 210, 0.85);\n"
"	border: 0px solid ;\n"
"	border-radius: 15px;\n"
"	padding: 4px\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_11)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font9)
        self.label_14.setStyleSheet(u"color: rgba(219, 69, 69, 1);")
        self.label_14.setFrameShape(QFrame.NoFrame)
        self.label_14.setFrameShadow(QFrame.Plain)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_14.setMargin(0)

        self.verticalLayout_30.addWidget(self.label_14)


        self.verticalLayout_18.addWidget(self.frame_11)

        self.frame_42 = QFrame(self.frame_37)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMaximumSize(QSize(16777215, 70))
        self.frame_42.setStyleSheet(u"QFrame#frame_42 {\n"
"	background: rgba(255, 210, 210, 0.85);\n"
"	border: 0px solid ;\n"
"	border-radius: 15px;\n"
"	padding: 4px\n"
"}")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.frame_42)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMaximumSize(QSize(310, 55))
        self.frame_41.setLayoutDirection(Qt.LeftToRight)
        self.frame_41.setAutoFillBackground(False)
        self.frame_41.setStyleSheet(u"QFrame#frame_41 {\n"
"background: rgba(197, 63, 63, 1);\n"
"border: 0px solid ;\n"
"border-radius: 10px;\n"
"padding: 4px;\n"
"}")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(10, 0, 40, 0)
        self.frame_51 = QFrame(self.frame_41)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMaximumSize(QSize(40, 40))
        self.frame_51.setStyleSheet(u"QFrame {\n"
"	/*background-image: url(:/bigSize/icons/bigSize/AKLOGO.png);*/\n"
"	border-image: url(:/24x24/icons/24x24/dinero.png) 0 0 0 0 stretch stretch;\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_51)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_34.addWidget(self.frame_51)

        self.perdidas_label = QLabel(self.frame_41)
        self.perdidas_label.setObjectName(u"perdidas_label")
        self.perdidas_label.setFont(font10)
        self.perdidas_label.setStyleSheet(u"color: #ffffff;")
        self.perdidas_label.setFrameShape(QFrame.NoFrame)
        self.perdidas_label.setFrameShadow(QFrame.Plain)
        self.perdidas_label.setAlignment(Qt.AlignCenter)
        self.perdidas_label.setMargin(0)

        self.horizontalLayout_34.addWidget(self.perdidas_label, 0, Qt.AlignHCenter)


        self.horizontalLayout_31.addWidget(self.frame_41)


        self.verticalLayout_18.addWidget(self.frame_42)


        self.horizontalLayout_20.addWidget(self.frame_37)


        self.horizontalLayout_14.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.page_simular)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.horizontalLayout_11 = QHBoxLayout(self.page_settings)
        self.horizontalLayout_11.setSpacing(3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(6, 6, 6, 6)
        self.frame_43 = QFrame(self.page_settings)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_43)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_43)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_18.setSpacing(3)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_27)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(180, 0))
        self.frame_14.setMaximumSize(QSize(350, 16777215))
        self.frame_14.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_14)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(7, 7, 7, 7)
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_title_bar_top_5 = QLabel(self.frame_14)
        self.label_title_bar_top_5.setObjectName(u"label_title_bar_top_5")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_5.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_5.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_5.setMinimumSize(QSize(0, 80))
        self.label_title_bar_top_5.setMaximumSize(QSize(16777215, 200))
        font12 = QFont()
        font12.setFamilies([u"Satoshi Black"])
        font12.setPointSize(14)
        font12.setBold(True)
        font12.setItalic(False)
        font12.setUnderline(False)
        font12.setStrikeOut(False)
        font12.setKerning(True)
        self.label_title_bar_top_5.setFont(font12)
        self.label_title_bar_top_5.setCursor(QCursor(Qt.ArrowCursor))
        self.label_title_bar_top_5.setStyleSheet(u"QLabel{\n"
"background-color: rgb(27, 29, 35);\n"
"border: 0px solid ;\n"
"border-radius: 8px;\n"
"}")
        self.label_title_bar_top_5.setScaledContents(True)
        self.label_title_bar_top_5.setAlignment(Qt.AlignCenter)
        self.label_title_bar_top_5.setWordWrap(False)

        self.gridLayout_6.addWidget(self.label_title_bar_top_5, 0, 0, 1, 1, Qt.AlignTop)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 280))
        self.frame_16.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_16)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, -1, -1, 9)
        self.label_top_info_16 = QLabel(self.frame_16)
        self.label_top_info_16.setObjectName(u"label_top_info_16")
        self.label_top_info_16.setMinimumSize(QSize(0, 25))
        self.label_top_info_16.setMaximumSize(QSize(16777215, 25))
        font13 = QFont()
        font13.setFamilies([u"Satoshi Black"])
        font13.setPointSize(12)
        font13.setBold(True)
        self.label_top_info_16.setFont(font13)
        self.label_top_info_16.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"}")
        self.label_top_info_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_top_info_16)

        self.label_top_info_17 = QLabel(self.frame_16)
        self.label_top_info_17.setObjectName(u"label_top_info_17")
        self.label_top_info_17.setMinimumSize(QSize(250, 20))
        self.label_top_info_17.setMaximumSize(QSize(16777215, 30))
        font14 = QFont()
        font14.setFamilies([u"Satoshi"])
        font14.setPointSize(12)
        font14.setBold(True)
        self.label_top_info_17.setFont(font14)
        self.label_top_info_17.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_top_info_17)

        self.maxCarrierASK = QSpinBox(self.frame_16)
        self.maxCarrierASK.setObjectName(u"maxCarrierASK")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.maxCarrierASK.sizePolicy().hasHeightForWidth())
        self.maxCarrierASK.setSizePolicy(sizePolicy6)
        self.maxCarrierASK.setMinimumSize(QSize(150, 30))
        font15 = QFont()
        font15.setFamilies([u"Satoshi"])
        font15.setPointSize(10)
        font15.setBold(True)
        self.maxCarrierASK.setFont(font15)
        self.maxCarrierASK.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.maxCarrierASK.setMinimum(1)
        self.maxCarrierASK.setMaximum(10000)
        self.maxCarrierASK.setValue(200)

        self.verticalLayout_23.addWidget(self.maxCarrierASK, 0, Qt.AlignHCenter)

        self.label_top_info_18 = QLabel(self.frame_16)
        self.label_top_info_18.setObjectName(u"label_top_info_18")
        self.label_top_info_18.setMinimumSize(QSize(250, 20))
        self.label_top_info_18.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_18.setFont(font14)
        self.label_top_info_18.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_top_info_18)

        self.minCarrierASK = QSpinBox(self.frame_16)
        self.minCarrierASK.setObjectName(u"minCarrierASK")
        sizePolicy6.setHeightForWidth(self.minCarrierASK.sizePolicy().hasHeightForWidth())
        self.minCarrierASK.setSizePolicy(sizePolicy6)
        self.minCarrierASK.setMinimumSize(QSize(150, 30))
        self.minCarrierASK.setFont(font15)
        self.minCarrierASK.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.minCarrierASK.setMinimum(1)
        self.minCarrierASK.setMaximum(10000)

        self.verticalLayout_23.addWidget(self.minCarrierASK, 0, Qt.AlignHCenter)

        self.line = QFrame(self.frame_16)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_23.addWidget(self.line)

        self.btn_AplicarASK = QPushButton(self.frame_16)
        self.btn_AplicarASK.setObjectName(u"btn_AplicarASK")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_AplicarASK.sizePolicy().hasHeightForWidth())
        self.btn_AplicarASK.setSizePolicy(sizePolicy7)
        self.btn_AplicarASK.setMinimumSize(QSize(150, 30))
        self.btn_AplicarASK.setMaximumSize(QSize(16777215, 40))
        self.btn_AplicarASK.setFont(font11)
        self.btn_AplicarASK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(56, 170, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(63, 152, 90);\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 198, 84);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(37, 138, 26);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/16x16/icons/16x16/cil-check-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_AplicarASK.setIcon(icon5)

        self.verticalLayout_23.addWidget(self.btn_AplicarASK)

        self.frame_10 = QFrame(self.frame_16)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_top_info_31 = QLabel(self.frame_10)
        self.label_top_info_31.setObjectName(u"label_top_info_31")
        self.label_top_info_31.setMinimumSize(QSize(0, 20))
        self.label_top_info_31.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_31.setFont(font14)
        self.label_top_info_31.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_top_info_31)

        self.label_maxASK = QLabel(self.frame_10)
        self.label_maxASK.setObjectName(u"label_maxASK")
        self.label_maxASK.setMinimumSize(QSize(0, 20))
        self.label_maxASK.setMaximumSize(QSize(16777215, 30))
        self.label_maxASK.setFont(font14)
        self.label_maxASK.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_maxASK.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_maxASK, 0, Qt.AlignRight)


        self.verticalLayout_23.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_16)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_top_info_26 = QLabel(self.frame_9)
        self.label_top_info_26.setObjectName(u"label_top_info_26")
        self.label_top_info_26.setMinimumSize(QSize(0, 20))
        self.label_top_info_26.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_26.setFont(font14)
        self.label_top_info_26.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_top_info_26)

        self.label_minASK = QLabel(self.frame_9)
        self.label_minASK.setObjectName(u"label_minASK")
        self.label_minASK.setMinimumSize(QSize(0, 20))
        self.label_minASK.setMaximumSize(QSize(16777215, 30))
        self.label_minASK.setFont(font14)
        self.label_minASK.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_minASK.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_minASK, 0, Qt.AlignRight)


        self.verticalLayout_23.addWidget(self.frame_9)


        self.gridLayout_6.addWidget(self.frame_16, 1, 0, 1, 1, Qt.AlignTop)


        self.verticalLayout_16.addLayout(self.gridLayout_6)


        self.horizontalLayout_18.addWidget(self.frame_14, 0, Qt.AlignTop)

        self.frame_18 = QFrame(self.frame_27)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(180, 0))
        self.frame_18.setMaximumSize(QSize(350, 16777215))
        self.frame_18.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_18)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(7, 7, 7, 7)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(10)
        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy5.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy5)
        self.frame_21.setMaximumSize(QSize(16777215, 280))
        self.frame_21.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_21)
        self.verticalLayout_26.setSpacing(6)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_top_info_22 = QLabel(self.frame_21)
        self.label_top_info_22.setObjectName(u"label_top_info_22")
        self.label_top_info_22.setMinimumSize(QSize(0, 25))
        self.label_top_info_22.setMaximumSize(QSize(16777215, 25))
        self.label_top_info_22.setFont(font13)
        self.label_top_info_22.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"}")
        self.label_top_info_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_top_info_22)

        self.label_top_info_23 = QLabel(self.frame_21)
        self.label_top_info_23.setObjectName(u"label_top_info_23")
        self.label_top_info_23.setMinimumSize(QSize(250, 20))
        self.label_top_info_23.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_23.setFont(font14)
        self.label_top_info_23.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_top_info_23)

        self.maxCarrierFSK1 = QSpinBox(self.frame_21)
        self.maxCarrierFSK1.setObjectName(u"maxCarrierFSK1")
        sizePolicy6.setHeightForWidth(self.maxCarrierFSK1.sizePolicy().hasHeightForWidth())
        self.maxCarrierFSK1.setSizePolicy(sizePolicy6)
        self.maxCarrierFSK1.setMinimumSize(QSize(150, 30))
        self.maxCarrierFSK1.setFont(font15)
        self.maxCarrierFSK1.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.maxCarrierFSK1.setMinimum(1)
        self.maxCarrierFSK1.setMaximum(10000)
        self.maxCarrierFSK1.setValue(200)

        self.verticalLayout_26.addWidget(self.maxCarrierFSK1, 0, Qt.AlignHCenter)

        self.label_top_info_21 = QLabel(self.frame_21)
        self.label_top_info_21.setObjectName(u"label_top_info_21")
        self.label_top_info_21.setMinimumSize(QSize(250, 20))
        self.label_top_info_21.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_21.setFont(font14)
        self.label_top_info_21.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_top_info_21)

        self.minCarrierFSK1 = QSpinBox(self.frame_21)
        self.minCarrierFSK1.setObjectName(u"minCarrierFSK1")
        sizePolicy6.setHeightForWidth(self.minCarrierFSK1.sizePolicy().hasHeightForWidth())
        self.minCarrierFSK1.setSizePolicy(sizePolicy6)
        self.minCarrierFSK1.setMinimumSize(QSize(150, 30))
        self.minCarrierFSK1.setFont(font15)
        self.minCarrierFSK1.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
""
                        "}\n"
"\n"
"QSpinBox::down-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.minCarrierFSK1.setMinimum(1)
        self.minCarrierFSK1.setMaximum(10000)

        self.verticalLayout_26.addWidget(self.minCarrierFSK1, 0, Qt.AlignHCenter)

        self.line_2 = QFrame(self.frame_21)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(16777215, 1))
        self.line_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_26.addWidget(self.line_2)

        self.btn_AplicarFSK1 = QPushButton(self.frame_21)
        self.btn_AplicarFSK1.setObjectName(u"btn_AplicarFSK1")
        sizePolicy7.setHeightForWidth(self.btn_AplicarFSK1.sizePolicy().hasHeightForWidth())
        self.btn_AplicarFSK1.setSizePolicy(sizePolicy7)
        self.btn_AplicarFSK1.setMinimumSize(QSize(150, 30))
        self.btn_AplicarFSK1.setMaximumSize(QSize(16777215, 40))
        self.btn_AplicarFSK1.setFont(font11)
        self.btn_AplicarFSK1.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(56, 170, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(63, 152, 90);\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 198, 84);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(37, 138, 26);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}")
        self.btn_AplicarFSK1.setIcon(icon5)

        self.verticalLayout_26.addWidget(self.btn_AplicarFSK1)

        self.frame_30 = QFrame(self.frame_21)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_top_info_32 = QLabel(self.frame_30)
        self.label_top_info_32.setObjectName(u"label_top_info_32")
        self.label_top_info_32.setMinimumSize(QSize(0, 20))
        self.label_top_info_32.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_32.setFont(font14)
        self.label_top_info_32.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_top_info_32)

        self.label_maxFSK_1 = QLabel(self.frame_30)
        self.label_maxFSK_1.setObjectName(u"label_maxFSK_1")
        self.label_maxFSK_1.setMinimumSize(QSize(0, 20))
        self.label_maxFSK_1.setMaximumSize(QSize(16777215, 30))
        self.label_maxFSK_1.setFont(font14)
        self.label_maxFSK_1.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_maxFSK_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_maxFSK_1, 0, Qt.AlignRight)


        self.verticalLayout_26.addWidget(self.frame_30)

        self.frame_29 = QFrame(self.frame_21)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_top_info_27 = QLabel(self.frame_29)
        self.label_top_info_27.setObjectName(u"label_top_info_27")
        self.label_top_info_27.setMinimumSize(QSize(0, 20))
        self.label_top_info_27.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_27.setFont(font14)
        self.label_top_info_27.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_top_info_27)

        self.label_minFSK_1 = QLabel(self.frame_29)
        self.label_minFSK_1.setObjectName(u"label_minFSK_1")
        self.label_minFSK_1.setMinimumSize(QSize(0, 20))
        self.label_minFSK_1.setMaximumSize(QSize(16777215, 30))
        self.label_minFSK_1.setFont(font14)
        self.label_minFSK_1.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_minFSK_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_minFSK_1, 0, Qt.AlignRight)


        self.verticalLayout_26.addWidget(self.frame_29)


        self.gridLayout_7.addWidget(self.frame_21, 1, 0, 1, 1)

        self.frame_23 = QFrame(self.frame_18)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy5.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy5)
        self.frame_23.setMaximumSize(QSize(16777215, 280))
        self.frame_23.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_23)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_top_info_24 = QLabel(self.frame_23)
        self.label_top_info_24.setObjectName(u"label_top_info_24")
        self.label_top_info_24.setMinimumSize(QSize(0, 25))
        self.label_top_info_24.setMaximumSize(QSize(16777215, 25))
        self.label_top_info_24.setFont(font13)
        self.label_top_info_24.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"}")
        self.label_top_info_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_top_info_24)

        self.label_top_info_25 = QLabel(self.frame_23)
        self.label_top_info_25.setObjectName(u"label_top_info_25")
        self.label_top_info_25.setMinimumSize(QSize(250, 20))
        self.label_top_info_25.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_25.setFont(font14)
        self.label_top_info_25.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_top_info_25)

        self.maxCarrierFSK2 = QSpinBox(self.frame_23)
        self.maxCarrierFSK2.setObjectName(u"maxCarrierFSK2")
        sizePolicy6.setHeightForWidth(self.maxCarrierFSK2.sizePolicy().hasHeightForWidth())
        self.maxCarrierFSK2.setSizePolicy(sizePolicy6)
        self.maxCarrierFSK2.setMinimumSize(QSize(150, 30))
        self.maxCarrierFSK2.setFont(font15)
        self.maxCarrierFSK2.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.maxCarrierFSK2.setMinimum(1)
        self.maxCarrierFSK2.setMaximum(10000)
        self.maxCarrierFSK2.setValue(200)

        self.verticalLayout_27.addWidget(self.maxCarrierFSK2, 0, Qt.AlignHCenter)

        self.label_top_info_28 = QLabel(self.frame_23)
        self.label_top_info_28.setObjectName(u"label_top_info_28")
        self.label_top_info_28.setMinimumSize(QSize(250, 20))
        self.label_top_info_28.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_28.setFont(font14)
        self.label_top_info_28.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_top_info_28)

        self.minCarrierFSK2 = QSpinBox(self.frame_23)
        self.minCarrierFSK2.setObjectName(u"minCarrierFSK2")
        sizePolicy6.setHeightForWidth(self.minCarrierFSK2.sizePolicy().hasHeightForWidth())
        self.minCarrierFSK2.setSizePolicy(sizePolicy6)
        self.minCarrierFSK2.setMinimumSize(QSize(150, 30))
        self.minCarrierFSK2.setFont(font15)
        self.minCarrierFSK2.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.minCarrierFSK2.setMinimum(1)
        self.minCarrierFSK2.setMaximum(10000)

        self.verticalLayout_27.addWidget(self.minCarrierFSK2, 0, Qt.AlignHCenter)

        self.line_3 = QFrame(self.frame_23)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMaximumSize(QSize(16777215, 1))
        self.line_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27.addWidget(self.line_3)

        self.btn_AplicarFSK2 = QPushButton(self.frame_23)
        self.btn_AplicarFSK2.setObjectName(u"btn_AplicarFSK2")
        sizePolicy7.setHeightForWidth(self.btn_AplicarFSK2.sizePolicy().hasHeightForWidth())
        self.btn_AplicarFSK2.setSizePolicy(sizePolicy7)
        self.btn_AplicarFSK2.setMinimumSize(QSize(150, 30))
        self.btn_AplicarFSK2.setMaximumSize(QSize(16777215, 40))
        self.btn_AplicarFSK2.setFont(font11)
        self.btn_AplicarFSK2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(56, 170, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(63, 152, 90);\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 198, 84);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(37, 138, 26);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}")
        self.btn_AplicarFSK2.setIcon(icon5)

        self.verticalLayout_27.addWidget(self.btn_AplicarFSK2)

        self.frame_32 = QFrame(self.frame_23)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_top_info_35 = QLabel(self.frame_32)
        self.label_top_info_35.setObjectName(u"label_top_info_35")
        self.label_top_info_35.setMinimumSize(QSize(0, 20))
        self.label_top_info_35.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_35.setFont(font14)
        self.label_top_info_35.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_top_info_35)

        self.label_maxFSK_2 = QLabel(self.frame_32)
        self.label_maxFSK_2.setObjectName(u"label_maxFSK_2")
        self.label_maxFSK_2.setMinimumSize(QSize(0, 20))
        self.label_maxFSK_2.setMaximumSize(QSize(16777215, 30))
        self.label_maxFSK_2.setFont(font14)
        self.label_maxFSK_2.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_maxFSK_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_maxFSK_2, 0, Qt.AlignRight)


        self.verticalLayout_27.addWidget(self.frame_32)

        self.frame_31 = QFrame(self.frame_23)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_top_info_34 = QLabel(self.frame_31)
        self.label_top_info_34.setObjectName(u"label_top_info_34")
        self.label_top_info_34.setMinimumSize(QSize(0, 20))
        self.label_top_info_34.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_34.setFont(font14)
        self.label_top_info_34.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_top_info_34)

        self.label_minFSK_2 = QLabel(self.frame_31)
        self.label_minFSK_2.setObjectName(u"label_minFSK_2")
        self.label_minFSK_2.setMinimumSize(QSize(0, 20))
        self.label_minFSK_2.setMaximumSize(QSize(16777215, 30))
        self.label_minFSK_2.setFont(font14)
        self.label_minFSK_2.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_minFSK_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_minFSK_2, 0, Qt.AlignRight)


        self.verticalLayout_27.addWidget(self.frame_31)


        self.gridLayout_7.addWidget(self.frame_23, 2, 0, 1, 1)

        self.label_title_bar_top_6 = QLabel(self.frame_18)
        self.label_title_bar_top_6.setObjectName(u"label_title_bar_top_6")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_6.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_6.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_6.setMinimumSize(QSize(0, 80))
        self.label_title_bar_top_6.setMaximumSize(QSize(16777215, 200))
        self.label_title_bar_top_6.setFont(font12)
        self.label_title_bar_top_6.setCursor(QCursor(Qt.ArrowCursor))
        self.label_title_bar_top_6.setStyleSheet(u"QLabel{\n"
"background-color: rgb(27, 29, 35);\n"
"border: 0px solid ;\n"
"border-radius: 8px;\n"
"}")
        self.label_title_bar_top_6.setScaledContents(True)
        self.label_title_bar_top_6.setAlignment(Qt.AlignCenter)
        self.label_title_bar_top_6.setWordWrap(False)

        self.gridLayout_7.addWidget(self.label_title_bar_top_6, 0, 0, 1, 1)


        self.verticalLayout_24.addLayout(self.gridLayout_7)


        self.horizontalLayout_18.addWidget(self.frame_18, 0, Qt.AlignTop)

        self.frame_24 = QFrame(self.frame_27)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(180, 0))
        self.frame_24.setMaximumSize(QSize(350, 16777215))
        self.frame_24.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_24)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(7, 7, 7, 7)
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_title_bar_top_7 = QLabel(self.frame_24)
        self.label_title_bar_top_7.setObjectName(u"label_title_bar_top_7")
        sizePolicy3.setHeightForWidth(self.label_title_bar_top_7.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top_7.setSizePolicy(sizePolicy3)
        self.label_title_bar_top_7.setMinimumSize(QSize(0, 80))
        self.label_title_bar_top_7.setMaximumSize(QSize(16777215, 200))
        self.label_title_bar_top_7.setFont(font12)
        self.label_title_bar_top_7.setCursor(QCursor(Qt.ArrowCursor))
        self.label_title_bar_top_7.setStyleSheet(u"QLabel{\n"
"background-color: rgb(27, 29, 35);\n"
"border: 0px solid ;\n"
"border-radius: 8px;\n"
"}")
        self.label_title_bar_top_7.setScaledContents(True)
        self.label_title_bar_top_7.setAlignment(Qt.AlignCenter)
        self.label_title_bar_top_7.setWordWrap(False)

        self.gridLayout_8.addWidget(self.label_title_bar_top_7, 0, 0, 1, 1)

        self.frame_20 = QFrame(self.frame_24)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 280))
        self.frame_20.setStyleSheet(u"background-color: rgb(23, 32, 77);\n"
"border-radius: 5px;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_20)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_top_info_19 = QLabel(self.frame_20)
        self.label_top_info_19.setObjectName(u"label_top_info_19")
        self.label_top_info_19.setMinimumSize(QSize(0, 25))
        self.label_top_info_19.setMaximumSize(QSize(16777215, 25))
        self.label_top_info_19.setFont(font13)
        self.label_top_info_19.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(33, 46, 112);\n"
"	border: 0px solid ;\n"
"	border-radius: 8px;\n"
"}")
        self.label_top_info_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_top_info_19)

        self.label_top_info_20 = QLabel(self.frame_20)
        self.label_top_info_20.setObjectName(u"label_top_info_20")
        self.label_top_info_20.setMinimumSize(QSize(250, 20))
        self.label_top_info_20.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_20.setFont(font14)
        self.label_top_info_20.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_top_info_20)

        self.maxCarrierPSK = QSpinBox(self.frame_20)
        self.maxCarrierPSK.setObjectName(u"maxCarrierPSK")
        sizePolicy6.setHeightForWidth(self.maxCarrierPSK.sizePolicy().hasHeightForWidth())
        self.maxCarrierPSK.setSizePolicy(sizePolicy6)
        self.maxCarrierPSK.setMinimumSize(QSize(150, 30))
        self.maxCarrierPSK.setFont(font15)
        self.maxCarrierPSK.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.maxCarrierPSK.setMinimum(1)
        self.maxCarrierPSK.setMaximum(10000)
        self.maxCarrierPSK.setValue(200)

        self.verticalLayout_25.addWidget(self.maxCarrierPSK, 0, Qt.AlignHCenter)

        self.label_top_info_29 = QLabel(self.frame_20)
        self.label_top_info_29.setObjectName(u"label_top_info_29")
        self.label_top_info_29.setMinimumSize(QSize(250, 20))
        self.label_top_info_29.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_29.setFont(font14)
        self.label_top_info_29.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_top_info_29)

        self.minCarrierPSK = QSpinBox(self.frame_20)
        self.minCarrierPSK.setObjectName(u"minCarrierPSK")
        sizePolicy6.setHeightForWidth(self.minCarrierPSK.sizePolicy().hasHeightForWidth())
        self.minCarrierPSK.setSizePolicy(sizePolicy6)
        self.minCarrierPSK.setMinimumSize(QSize(150, 30))
        self.minCarrierPSK.setFont(font15)
        self.minCarrierPSK.setStyleSheet(u"QSpinBox{\n"
"	background-color: rgb(5, 7, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(10, 11, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QSpinBox:hover{\n"
"	border: 2px solid rgb(0, 0, 127)\n"
"}\n"
"QSpinBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 29, 35);\n"
"}\n"
"/*\n"
"rgb(27, 29, 35);\n"
"rgb(13, 9, 59)\n"
"*/\n"
"\n"
"QSpinBox::up-button{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-top.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-button:hover{\n"
"	background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QSpinBox::down-bu"
                        "tton{\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.minCarrierPSK.setMinimum(1)
        self.minCarrierPSK.setMaximum(10000)

        self.verticalLayout_25.addWidget(self.minCarrierPSK, 0, Qt.AlignHCenter)

        self.line_4 = QFrame(self.frame_20)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMaximumSize(QSize(16777215, 1))
        self.line_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_25.addWidget(self.line_4)

        self.btn_AplicarPSK = QPushButton(self.frame_20)
        self.btn_AplicarPSK.setObjectName(u"btn_AplicarPSK")
        sizePolicy7.setHeightForWidth(self.btn_AplicarPSK.sizePolicy().hasHeightForWidth())
        self.btn_AplicarPSK.setSizePolicy(sizePolicy7)
        self.btn_AplicarPSK.setMinimumSize(QSize(150, 30))
        self.btn_AplicarPSK.setMaximumSize(QSize(16777215, 40))
        self.btn_AplicarPSK.setFont(font11)
        self.btn_AplicarPSK.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(56, 170, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(63, 152, 90);\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background-color: rgb(60, 198, 84);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(37, 138, 26);\n"
"	border: 2px solid rgb(60, 196, 72);\n"
"}")
        self.btn_AplicarPSK.setIcon(icon5)

        self.verticalLayout_25.addWidget(self.btn_AplicarPSK)

        self.frame_34 = QFrame(self.frame_20)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_top_info_37 = QLabel(self.frame_34)
        self.label_top_info_37.setObjectName(u"label_top_info_37")
        self.label_top_info_37.setMinimumSize(QSize(0, 20))
        self.label_top_info_37.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_37.setFont(font14)
        self.label_top_info_37.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_top_info_37)

        self.label_maxPSK = QLabel(self.frame_34)
        self.label_maxPSK.setObjectName(u"label_maxPSK")
        self.label_maxPSK.setMinimumSize(QSize(0, 20))
        self.label_maxPSK.setMaximumSize(QSize(16777215, 30))
        self.label_maxPSK.setFont(font14)
        self.label_maxPSK.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_maxPSK.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_maxPSK, 0, Qt.AlignRight)


        self.verticalLayout_25.addWidget(self.frame_34)

        self.frame_33 = QFrame(self.frame_20)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_top_info_36 = QLabel(self.frame_33)
        self.label_top_info_36.setObjectName(u"label_top_info_36")
        self.label_top_info_36.setMinimumSize(QSize(0, 20))
        self.label_top_info_36.setMaximumSize(QSize(16777215, 30))
        self.label_top_info_36.setFont(font14)
        self.label_top_info_36.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_top_info_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_top_info_36)

        self.label_minPSK = QLabel(self.frame_33)
        self.label_minPSK.setObjectName(u"label_minPSK")
        self.label_minPSK.setMinimumSize(QSize(0, 20))
        self.label_minPSK.setMaximumSize(QSize(16777215, 30))
        self.label_minPSK.setFont(font14)
        self.label_minPSK.setStyleSheet(u"color: rgb(191, 203, 217)")
        self.label_minPSK.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_minPSK, 0, Qt.AlignRight)


        self.verticalLayout_25.addWidget(self.frame_33)


        self.gridLayout_8.addWidget(self.frame_20, 1, 0, 1, 1)


        self.verticalLayout_28.addLayout(self.gridLayout_8)


        self.horizontalLayout_18.addWidget(self.frame_24, 0, Qt.AlignTop)


        self.verticalLayout_36.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_43)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.Btn_helpSettings = QPushButton(self.frame_28)
        self.Btn_helpSettings.setObjectName(u"Btn_helpSettings")
        sizePolicy3.setHeightForWidth(self.Btn_helpSettings.sizePolicy().hasHeightForWidth())
        self.Btn_helpSettings.setSizePolicy(sizePolicy3)
        self.Btn_helpSettings.setMinimumSize(QSize(100, 30))
        self.Btn_helpSettings.setMaximumSize(QSize(103, 30))
        self.Btn_helpSettings.setFont(font11)
        self.Btn_helpSettings.setStyleSheet(u"QPushButton {\n"
"   color: #FFFFFF;\n"
"   background-color: #3D94F6;\n"
"   border: 1px solid #0059A0;\n"
"   border-radius: 15px;\n"
"}\n"
"\n"
"/* rgb(52, 59, 72)*/\n"
"QPushButton:hover {\n"
"	background: #0078FF;\n"
"	border: 1px solid #0059A0;\n"
"   border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(0, 87, 131);\n"
"	border: 1px solid #0059A0;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/16x16/icons/16x16/cil-help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_helpSettings.setIcon(icon6)

        self.horizontalLayout_21.addWidget(self.Btn_helpSettings)


        self.verticalLayout_36.addWidget(self.frame_28, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.horizontalLayout_11.addWidget(self.frame_43)

        self.stackedWidget.addWidget(self.page_settings)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setStyleSheet(u"color: rgb(159, 165, 177);")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet(u"color: rgb(159, 165, 177);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font)
        self.label_version.setStyleSheet(u"color: rgb(159, 165, 177);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Animal Kingdom", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"C:\\Program Files\\Blender Foundation\\Blender 2.82", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| INICIO", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"AK", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"DISNEY ANIMAL KINGDOM", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Simulador de condiciones clim\u00e1ticas y perdidas econ\u00f3micas</p></body></html>", None))
        self.BtnMenuSimu.setText(QCoreApplication.translate("MainWindow", u"SIMULAR", None))
        self.BtnSimular.setText(QCoreApplication.translate("MainWindow", u"Simular", None))
        self.dia_label.setText(QCoreApplication.translate("MainWindow", u"D\u00eda 06/08/2023", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Aforo Esperado", None))
        self.visitantes_label.setText(QCoreApplication.translate("MainWindow", u"- visitantes", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Probabilidades", None))
        self.label_tipo_lluvia.setText(QCoreApplication.translate("MainWindow", u"Lluvia", None))
        self.lluvia_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Hurac\u00e1n", None))
        self.huracan_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Perdidas Potenciales", None))
        self.perdidas_label.setText(QCoreApplication.translate("MainWindow", u"$ -", None))
        self.label_title_bar_top_5.setText(QCoreApplication.translate("MainWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n de Amplitud\n"
"ASK", None))
        self.label_top_info_16.setText(QCoreApplication.translate("MainWindow", u"Se\u00f1al Portadora", None))
        self.label_top_info_17.setText(QCoreApplication.translate("MainWindow", u"Frecuencia M\u00e1xima (Hz) | 1 a 10.000", None))
#if QT_CONFIG(tooltip)
        self.maxCarrierASK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_top_info_18.setText(QCoreApplication.translate("MainWindow", u"Frecuencia M\u00ednima (Hz) | 1 a 10.000", None))
#if QT_CONFIG(tooltip)
        self.minCarrierASK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_AplicarASK.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.label_top_info_31.setText(QCoreApplication.translate("MainWindow", u"Frec M\u00e1xima Actual:", None))
        self.label_maxASK.setText(QCoreApplication.translate("MainWindow", u"200 Hz", None))
        self.label_top_info_26.setText(QCoreApplication.translate("MainWindow", u"Frec M\u00ednima Actual:", None))
        self.label_minASK.setText(QCoreApplication.translate("MainWindow", u"1 Hz", None))
        self.label_top_info_22.setText(QCoreApplication.translate("MainWindow", u"Se\u00f1al 1", None))
        self.label_top_info_23.setText(QCoreApplication.translate("MainWindow", u"Frecuencia M\u00e1xima (Hz) | 1 a 10.000", None))
#if QT_CONFIG(tooltip)
        self.maxCarrierFSK1.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_top_info_21.setText(QCoreApplication.translate("MainWindow", u"Frecuencia M\u00ednima (Hz) | 1 a 10.000", None))
#if QT_CONFIG(tooltip)
        self.minCarrierFSK1.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_AplicarFSK1.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.label_top_info_32.setText(QCoreApplication.translate("MainWindow", u"Frec M\u00e1xima Actual:", None))
        self.label_maxFSK_1.setText(QCoreApplication.translate("MainWindow", u"200 Hz", None))
        self.label_top_info_27.setText(QCoreApplication.translate("MainWindow", u"Frec M\u00ednima Actual:", None))
        self.label_minFSK_1.setText(QCoreApplication.translate("MainWindow", u"1 Hz", None))
        self.label_top_info_24.setText(QCoreApplication.translate("MainWindow", u"Se\u00f1al 2", None))
        self.label_top_info_25.setText(QCoreApplication.translate("MainWindow", u"Frecuencia M\u00e1xima (Hz) | 1 a 10.000", None))
#if QT_CONFIG(tooltip)
        self.maxCarrierFSK2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_top_info_28.setText(QCoreApplication.translate("MainWindow", u"Frecuencia M\u00ednima (Hz) | 1 a 10.000", None))
#if QT_CONFIG(tooltip)
        self.minCarrierFSK2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_AplicarFSK2.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.label_top_info_35.setText(QCoreApplication.translate("MainWindow", u"Frec M\u00e1xima Actual:", None))
        self.label_maxFSK_2.setText(QCoreApplication.translate("MainWindow", u"200 Hz", None))
        self.label_top_info_34.setText(QCoreApplication.translate("MainWindow", u"Frec M\u00ednima Actual:", None))
        self.label_minFSK_2.setText(QCoreApplication.translate("MainWindow", u"1 Hz", None))
        self.label_title_bar_top_6.setText(QCoreApplication.translate("MainWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n de Frecuencias\n"
"FSK", None))
        self.label_title_bar_top_7.setText(QCoreApplication.translate("MainWindow", u"Modulaci\u00f3n por\n"
"Conmutaci\u00f3n de Fase\n"
"PSK", None))
        self.label_top_info_19.setText(QCoreApplication.translate("MainWindow", u"Se\u00f1al Portadora", None))
        self.label_top_info_20.setText(QCoreApplication.translate("MainWindow", u"Frecuencia M\u00e1xima (Hz) | 1 a 10.000", None))
#if QT_CONFIG(tooltip)
        self.maxCarrierPSK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_top_info_29.setText(QCoreApplication.translate("MainWindow", u"Frecuencia M\u00ednima (Hz) | 1 a 10.000", None))
#if QT_CONFIG(tooltip)
        self.minCarrierPSK.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_AplicarPSK.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.label_top_info_37.setText(QCoreApplication.translate("MainWindow", u"Frec M\u00e1xima Actual:", None))
        self.label_maxPSK.setText(QCoreApplication.translate("MainWindow", u"200 Hz", None))
        self.label_top_info_36.setText(QCoreApplication.translate("MainWindow", u"Frec M\u00ednima Actual:", None))
        self.label_minPSK.setText(QCoreApplication.translate("MainWindow", u"1 Hz", None))
#if QT_CONFIG(tooltip)
        self.Btn_helpSettings.setToolTip(QCoreApplication.translate("MainWindow", u"Consigue ayuda sobre esta p\u00e1gina", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Btn_helpSettings.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.Btn_helpSettings.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.Btn_helpSettings.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Desarrollado por: Lucas Depetris, Santiago Figueroa, Emanuel Haro y Maribel Masucci", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
    # retranslateUi

