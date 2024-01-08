# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QStackedWidget,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(778, 469)
        MainWindow.setFocusPolicy(Qt.ClickFocus)
        icon = QIcon()
        iconThemeName = u"zoom-out"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u":/app/icon.ico", QSize(), QIcon.Normal, QIcon.Off)

        MainWindow.setWindowIcon(icon)
        self.stylesheet = QWidget(MainWindow)
        self.stylesheet.setObjectName(u"stylesheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.stylesheet.setFont(font)
        self.stylesheet.setFocusPolicy(Qt.ClickFocus)
        self.stylesheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: r"
                        "gb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#leftbotton_logo .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#leftbotton_logo .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#ti"
                        "tleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extr"
                        "a Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPu"
                        "shButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* ////////////////////"
                        "/////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-to"
                        "p-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QS"
                        "crollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: no"
                        "ne;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
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
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub"
                        "-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
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
"	background-image: url(:/icons/images/icons/cil-check-alt"
                        ".png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
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
"	b"
                        "order-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0p"
                        "x;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	bor"
                        "der-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.stylesheet)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.stylesheet)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(80, 0))
        self.frame.setMaximumSize(QSize(2000, 16777215))
        self.frame.setFocusPolicy(Qt.ClickFocus)
        self.frame.setStyleSheet(u"background-color: rgb(26, 29, 34);\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.home = QPushButton(self.frame)
        self.home.setObjectName(u"home")
        self.home.setMinimumSize(QSize(60, 60))
        self.home.setMaximumSize(QSize(60, 60))
        self.home.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/cil-home.png);\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.verticalLayout_9.addWidget(self.home)

        self.explaine = QLabel(self.frame)
        self.explaine.setObjectName(u"explaine")
        self.explaine.setTextFormat(Qt.PlainText)
        self.explaine.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.explaine)

        self.setting = QPushButton(self.frame)
        self.setting.setObjectName(u"setting")
        self.setting.setMinimumSize(QSize(60, 60))
        self.setting.setMaximumSize(QSize(60, 60))
        self.setting.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png)\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.verticalLayout_9.addWidget(self.setting)


        self.horizontalLayout.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(self.stylesheet)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFocusPolicy(Qt.ClickFocus)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(47, 54, 60);\n"
"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_5 = QVBoxLayout(self.page_home)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(self.page_home)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.help_erections = QRadioButton(self.frame_3)
        self.help_erections.setObjectName(u"help_erections")
        self.help_erections.setMinimumSize(QSize(160, 0))
        self.help_erections.setMaximumSize(QSize(160, 16777215))
        self.help_erections.setFocusPolicy(Qt.ClickFocus)
        self.help_erections.setLayoutDirection(Qt.LeftToRight)
        self.help_erections.setAutoFillBackground(False)
        self.help_erections.setStyleSheet(u"text-align: center;")
        self.help_erections.setChecked(True)

        self.horizontalLayout_39.addWidget(self.help_erections)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(160, 0))
        self.frame_6.setMaximumSize(QSize(160, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.run = QPushButton(self.frame_6)
        self.run.setObjectName(u"run")
        self.run.setMinimumSize(QSize(160, 0))
        self.run.setMaximumSize(QSize(160, 16777215))
        self.run.setFocusPolicy(Qt.ClickFocus)
        self.run.setStyleSheet(u"background-repeat: no-repeat;\n"
"background-image: url(:/icons/images/icons/cil-media-play.png);\n"
"background-position: center;\n"
"border: none;\n"
"outline: none;\n"
"")

        self.verticalLayout_8.addWidget(self.run)


        self.horizontalLayout_2.addWidget(self.frame_6)

        self.frame_18 = QFrame(self.frame_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.global_key_control = QRadioButton(self.frame_18)
        self.global_key_control.setObjectName(u"global_key_control")
        self.global_key_control.setMinimumSize(QSize(160, 0))
        self.global_key_control.setMaximumSize(QSize(160, 16777215))
        self.global_key_control.setFocusPolicy(Qt.ClickFocus)
        self.global_key_control.setLayoutDirection(Qt.LeftToRight)
        self.global_key_control.setAutoFillBackground(False)
        self.global_key_control.setStyleSheet(u"text-align: center;")

        self.horizontalLayout_40.addWidget(self.global_key_control)


        self.horizontalLayout_2.addWidget(self.frame_18)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.page_home)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.L0ff = QFrame(self.frame_5)
        self.L0ff.setObjectName(u"L0ff")
        self.L0ff.setFrameShape(QFrame.StyledPanel)
        self.L0ff.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.L0ff)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.L0ff)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.L0_speed = QSlider(self.frame_9)
        self.L0_speed.setObjectName(u"L0_speed")
        self.L0_speed.setFocusPolicy(Qt.ClickFocus)
        self.L0_speed.setMinimum(1)
        self.L0_speed.setMaximum(100)
        self.L0_speed.setPageStep(1)
        self.L0_speed.setValue(1)
        self.L0_speed.setSliderPosition(1)
        self.L0_speed.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.L0_speed)

        self.L0_value = QLabel(self.frame_9)
        self.L0_value.setObjectName(u"L0_value")
        self.L0_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.L0_value)

        self.L0_p = QLabel(self.frame_9)
        self.L0_p.setObjectName(u"L0_p")
        self.L0_p.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.L0_p)

        self.L0_position = QSlider(self.frame_9)
        self.L0_position.setObjectName(u"L0_position")
        self.L0_position.setFocusPolicy(Qt.ClickFocus)
        self.L0_position.setMinimum(0)
        self.L0_position.setMaximum(999)
        self.L0_position.setPageStep(1)
        self.L0_position.setValue(500)
        self.L0_position.setSliderPosition(500)
        self.L0_position.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.L0_position)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.L0f = QFrame(self.L0ff)
        self.L0f.setObjectName(u"L0f")
        self.L0f.setFrameShape(QFrame.StyledPanel)
        self.L0f.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.L0f)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.L0_min = QSlider(self.L0f)
        self.L0_min.setObjectName(u"L0_min")
        self.L0_min.setFocusPolicy(Qt.ClickFocus)
        self.L0_min.setMinimum(0)
        self.L0_min.setMaximum(999)
        self.L0_min.setPageStep(1)
        self.L0_min.setValue(1)
        self.L0_min.setSliderPosition(1)
        self.L0_min.setOrientation(Qt.Horizontal)

        self.horizontalLayout_8.addWidget(self.L0_min)

        self.L0 = QRadioButton(self.L0f)
        self.L0.setObjectName(u"L0")
        self.L0.setEnabled(True)
        self.L0.setToolTipDuration(0)
        self.L0.setLayoutDirection(Qt.LeftToRight)
        self.L0.setAutoFillBackground(False)
        self.L0.setChecked(False)
        self.L0.setAutoExclusive(False)

        self.horizontalLayout_8.addWidget(self.L0)

        self.L0_max = QSlider(self.L0f)
        self.L0_max.setObjectName(u"L0_max")
        self.L0_max.setFocusPolicy(Qt.ClickFocus)
        self.L0_max.setMinimum(0)
        self.L0_max.setMaximum(999)
        self.L0_max.setPageStep(1)
        self.L0_max.setValue(999)
        self.L0_max.setSliderPosition(999)
        self.L0_max.setOrientation(Qt.Horizontal)

        self.horizontalLayout_8.addWidget(self.L0_max)

        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 2)

        self.verticalLayout_3.addWidget(self.L0f)


        self.verticalLayout.addWidget(self.L0ff)

        self.R1ff = QFrame(self.frame_5)
        self.R1ff.setObjectName(u"R1ff")
        self.R1ff.setFrameShape(QFrame.StyledPanel)
        self.R1ff.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.R1ff)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.R1ff)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.R1_speed = QSlider(self.frame_7)
        self.R1_speed.setObjectName(u"R1_speed")
        self.R1_speed.setFocusPolicy(Qt.ClickFocus)
        self.R1_speed.setMinimum(1)
        self.R1_speed.setMaximum(100)
        self.R1_speed.setPageStep(1)
        self.R1_speed.setValue(1)
        self.R1_speed.setSliderPosition(1)
        self.R1_speed.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.R1_speed)

        self.R1_value = QLabel(self.frame_7)
        self.R1_value.setObjectName(u"R1_value")
        self.R1_value.setAlignment(Qt.AlignCenter)
        self.R1_value.setIndent(0)

        self.horizontalLayout_5.addWidget(self.R1_value)

        self.R1_p = QLabel(self.frame_7)
        self.R1_p.setObjectName(u"R1_p")
        self.R1_p.setAlignment(Qt.AlignCenter)
        self.R1_p.setIndent(0)

        self.horizontalLayout_5.addWidget(self.R1_p)

        self.R1_position = QSlider(self.frame_7)
        self.R1_position.setObjectName(u"R1_position")
        self.R1_position.setMinimum(0)
        self.R1_position.setMaximum(999)
        self.R1_position.setPageStep(1)
        self.R1_position.setValue(500)
        self.R1_position.setSliderPosition(500)
        self.R1_position.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.R1_position)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.R1f = QFrame(self.R1ff)
        self.R1f.setObjectName(u"R1f")
        self.R1f.setFrameShape(QFrame.StyledPanel)
        self.R1f.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.R1f)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.R1_min = QSlider(self.R1f)
        self.R1_min.setObjectName(u"R1_min")
        self.R1_min.setMinimum(0)
        self.R1_min.setMaximum(999)
        self.R1_min.setSingleStep(1)
        self.R1_min.setPageStep(1)
        self.R1_min.setValue(350)
        self.R1_min.setTracking(True)
        self.R1_min.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.R1_min)

        self.R1 = QRadioButton(self.R1f)
        self.R1.setObjectName(u"R1")
        self.R1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_6.addWidget(self.R1)

        self.R1_max = QSlider(self.R1f)
        self.R1_max.setObjectName(u"R1_max")
        self.R1_max.setMinimum(0)
        self.R1_max.setMaximum(999)
        self.R1_max.setPageStep(1)
        self.R1_max.setValue(650)
        self.R1_max.setSliderPosition(650)
        self.R1_max.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.R1_max)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 2)

        self.verticalLayout_2.addWidget(self.R1f)


        self.verticalLayout.addWidget(self.R1ff)

        self.R2ff = QFrame(self.frame_5)
        self.R2ff.setObjectName(u"R2ff")
        self.R2ff.setFrameShape(QFrame.StyledPanel)
        self.R2ff.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.R2ff)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.R2ff)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.R2_speed = QSlider(self.frame_11)
        self.R2_speed.setObjectName(u"R2_speed")
        self.R2_speed.setMinimum(1)
        self.R2_speed.setMaximum(100)
        self.R2_speed.setPageStep(1)
        self.R2_speed.setValue(1)
        self.R2_speed.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.R2_speed)

        self.R2_value = QLabel(self.frame_11)
        self.R2_value.setObjectName(u"R2_value")
        self.R2_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.R2_value)

        self.R2_p = QLabel(self.frame_11)
        self.R2_p.setObjectName(u"R2_p")
        self.R2_p.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.R2_p)

        self.R2_position = QSlider(self.frame_11)
        self.R2_position.setObjectName(u"R2_position")
        self.R2_position.setMinimum(0)
        self.R2_position.setMaximum(999)
        self.R2_position.setPageStep(1)
        self.R2_position.setValue(500)
        self.R2_position.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.R2_position)


        self.verticalLayout_4.addWidget(self.frame_11)

        self.R2f = QFrame(self.R2ff)
        self.R2f.setObjectName(u"R2f")
        self.R2f.setFrameShape(QFrame.StyledPanel)
        self.R2f.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.R2f)
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.R2_min = QSlider(self.R2f)
        self.R2_min.setObjectName(u"R2_min")
        self.R2_min.setMinimum(0)
        self.R2_min.setMaximum(999)
        self.R2_min.setPageStep(1)
        self.R2_min.setValue(450)
        self.R2_min.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.R2_min)

        self.R2 = QRadioButton(self.R2f)
        self.R2.setObjectName(u"R2")
        self.R2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.R2)

        self.R2_max = QSlider(self.R2f)
        self.R2_max.setObjectName(u"R2_max")
        self.R2_max.setMinimum(0)
        self.R2_max.setMaximum(999)
        self.R2_max.setPageStep(1)
        self.R2_max.setValue(550)
        self.R2_max.setSliderPosition(550)
        self.R2_max.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.R2_max)

        self.horizontalLayout_10.setStretch(0, 2)
        self.horizontalLayout_10.setStretch(1, 1)
        self.horizontalLayout_10.setStretch(2, 2)

        self.verticalLayout_4.addWidget(self.R2f)


        self.verticalLayout.addWidget(self.R2ff)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.page_home)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 100))
        self.frame_4.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 0))
        self.label.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.label)

        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.run_com = QPushButton(self.frame_4)
        self.run_com.setObjectName(u"run_com")
        self.run_com.setMinimumSize(QSize(50, 50))
        self.run_com.setMaximumSize(QSize(50, 50))
        self.run_com.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: rgb(220, 147, 249);\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    border-radius: 25px;\n"
"    background-image: url(:/icons/images/icons/cil-media-play.png);\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(240, 200, 249); /* \u8bbe\u7f6e\u60ac\u505c\u72b6\u6001\u4e0b\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")

        self.horizontalLayout_3.addWidget(self.run_com)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_home)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.verticalLayout_12 = QVBoxLayout(self.page_setting)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea = QScrollArea(self.page_setting)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 621, 2570))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.singkeysetting = QFrame(self.scrollAreaWidgetContents)
        self.singkeysetting.setObjectName(u"singkeysetting")
        self.singkeysetting.setFrameShape(QFrame.StyledPanel)
        self.singkeysetting.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.singkeysetting)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_10 = QFrame(self.singkeysetting)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 80))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_11.addWidget(self.label_4)


        self.verticalLayout_6.addWidget(self.frame_10)

        self.frame_8 = QFrame(self.singkeysetting)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_11.addWidget(self.label_2)

        self.k_l0_p_u = QPushButton(self.frame_8)
        self.k_l0_p_u.setObjectName(u"k_l0_p_u")
        self.k_l0_p_u.setMinimumSize(QSize(100, 30))
        self.k_l0_p_u.setMaximumSize(QSize(100, 30))
        self.k_l0_p_u.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_11.addWidget(self.k_l0_p_u)


        self.verticalLayout_6.addWidget(self.frame_8)

        self.frame_12 = QFrame(self.singkeysetting)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_6 = QLabel(self.frame_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(300, 0))
        self.label_6.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_12.addWidget(self.label_6)

        self.k_l0_p_d = QPushButton(self.frame_12)
        self.k_l0_p_d.setObjectName(u"k_l0_p_d")
        self.k_l0_p_d.setMinimumSize(QSize(100, 30))
        self.k_l0_p_d.setMaximumSize(QSize(100, 30))
        self.k_l0_p_d.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_12.addWidget(self.k_l0_p_d)


        self.verticalLayout_6.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.singkeysetting)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_8 = QLabel(self.frame_13)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_13.addWidget(self.label_8)

        self.k_r1_p_l = QPushButton(self.frame_13)
        self.k_r1_p_l.setObjectName(u"k_r1_p_l")
        self.k_r1_p_l.setMinimumSize(QSize(100, 30))
        self.k_r1_p_l.setMaximumSize(QSize(100, 30))
        self.k_r1_p_l.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_13.addWidget(self.k_r1_p_l)


        self.verticalLayout_6.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.singkeysetting)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_10 = QLabel(self.frame_14)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_14.addWidget(self.label_10)

        self.k_r1_p_r = QPushButton(self.frame_14)
        self.k_r1_p_r.setObjectName(u"k_r1_p_r")
        self.k_r1_p_r.setMinimumSize(QSize(100, 30))
        self.k_r1_p_r.setMaximumSize(QSize(100, 30))
        self.k_r1_p_r.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_14.addWidget(self.k_r1_p_r)


        self.verticalLayout_6.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.singkeysetting)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_12 = QLabel(self.frame_15)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_15.addWidget(self.label_12)

        self.k_r2_p_f = QPushButton(self.frame_15)
        self.k_r2_p_f.setObjectName(u"k_r2_p_f")
        self.k_r2_p_f.setMinimumSize(QSize(100, 30))
        self.k_r2_p_f.setMaximumSize(QSize(100, 30))
        self.k_r2_p_f.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_15.addWidget(self.k_r2_p_f)


        self.verticalLayout_6.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.singkeysetting)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_13 = QLabel(self.frame_16)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_16.addWidget(self.label_13)

        self.k_r2_p_b = QPushButton(self.frame_16)
        self.k_r2_p_b.setObjectName(u"k_r2_p_b")
        self.k_r2_p_b.setMinimumSize(QSize(100, 30))
        self.k_r2_p_b.setMaximumSize(QSize(100, 30))
        self.k_r2_p_b.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_16.addWidget(self.k_r2_p_b)


        self.verticalLayout_6.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.singkeysetting)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_14 = QLabel(self.frame_17)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_17.addWidget(self.label_14)

        self.k_k_c = QPushButton(self.frame_17)
        self.k_k_c.setObjectName(u"k_k_c")
        self.k_k_c.setMinimumSize(QSize(100, 30))
        self.k_k_c.setMaximumSize(QSize(100, 30))
        self.k_k_c.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_17.addWidget(self.k_k_c)


        self.verticalLayout_6.addWidget(self.frame_17)

        self.frame_19 = QFrame(self.singkeysetting)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_16 = QLabel(self.frame_19)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_18.addWidget(self.label_16)

        self.k_k_r = QPushButton(self.frame_19)
        self.k_k_r.setObjectName(u"k_k_r")
        self.k_k_r.setMinimumSize(QSize(100, 30))
        self.k_k_r.setMaximumSize(QSize(100, 30))
        self.k_k_r.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_18.addWidget(self.k_k_r)


        self.verticalLayout_6.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.singkeysetting)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_17 = QLabel(self.frame_20)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_19.addWidget(self.label_17)

        self.k_l0_t = QPushButton(self.frame_20)
        self.k_l0_t.setObjectName(u"k_l0_t")
        self.k_l0_t.setMinimumSize(QSize(100, 30))
        self.k_l0_t.setMaximumSize(QSize(100, 30))
        self.k_l0_t.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_19.addWidget(self.k_l0_t)


        self.verticalLayout_6.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.singkeysetting)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_18 = QLabel(self.frame_21)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_20.addWidget(self.label_18)

        self.k_r1_t = QPushButton(self.frame_21)
        self.k_r1_t.setObjectName(u"k_r1_t")
        self.k_r1_t.setMinimumSize(QSize(100, 30))
        self.k_r1_t.setMaximumSize(QSize(100, 30))
        self.k_r1_t.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_20.addWidget(self.k_r1_t)


        self.verticalLayout_6.addWidget(self.frame_21)

        self.frame_23 = QFrame(self.singkeysetting)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_20 = QLabel(self.frame_23)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_21.addWidget(self.label_20)

        self.k_r2_t = QPushButton(self.frame_23)
        self.k_r2_t.setObjectName(u"k_r2_t")
        self.k_r2_t.setMinimumSize(QSize(100, 30))
        self.k_r2_t.setMaximumSize(QSize(100, 30))
        self.k_r2_t.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_21.addWidget(self.k_r2_t)


        self.verticalLayout_6.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.singkeysetting)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_21 = QLabel(self.frame_24)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_22.addWidget(self.label_21)

        self.k_a_t = QPushButton(self.frame_24)
        self.k_a_t.setObjectName(u"k_a_t")
        self.k_a_t.setMinimumSize(QSize(100, 30))
        self.k_a_t.setMaximumSize(QSize(100, 30))
        self.k_a_t.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_22.addWidget(self.k_a_t)


        self.verticalLayout_6.addWidget(self.frame_24)

        self.frame_39 = QFrame(self.singkeysetting)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_36 = QLabel(self.frame_39)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_38.addWidget(self.label_36)

        self.k_windows_t = QPushButton(self.frame_39)
        self.k_windows_t.setObjectName(u"k_windows_t")
        self.k_windows_t.setMinimumSize(QSize(100, 30))
        self.k_windows_t.setMaximumSize(QSize(100, 30))
        self.k_windows_t.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_38.addWidget(self.k_windows_t)


        self.verticalLayout_6.addWidget(self.frame_39)

        self.frame_26 = QFrame(self.singkeysetting)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_23 = QLabel(self.frame_26)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_23.addWidget(self.label_23)

        self.k_help_erections = QPushButton(self.frame_26)
        self.k_help_erections.setObjectName(u"k_help_erections")
        self.k_help_erections.setMinimumSize(QSize(100, 30))
        self.k_help_erections.setMaximumSize(QSize(100, 30))
        self.k_help_erections.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_23.addWidget(self.k_help_erections)


        self.verticalLayout_6.addWidget(self.frame_26)

        self.frame_53 = QFrame(self.singkeysetting)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_52 = QLabel(self.frame_53)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_55.addWidget(self.label_52)

        self.k_p_r_i = QPushButton(self.frame_53)
        self.k_p_r_i.setObjectName(u"k_p_r_i")
        self.k_p_r_i.setMinimumSize(QSize(100, 30))
        self.k_p_r_i.setMaximumSize(QSize(100, 30))
        self.k_p_r_i.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_55.addWidget(self.k_p_r_i)


        self.verticalLayout_6.addWidget(self.frame_53)

        self.frame_54 = QFrame(self.singkeysetting)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_54 = QLabel(self.frame_54)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_57.addWidget(self.label_54)

        self.k_p_r_d = QPushButton(self.frame_54)
        self.k_p_r_d.setObjectName(u"k_p_r_d")
        self.k_p_r_d.setMinimumSize(QSize(100, 30))
        self.k_p_r_d.setMaximumSize(QSize(100, 30))
        self.k_p_r_d.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_57.addWidget(self.k_p_r_d)


        self.verticalLayout_6.addWidget(self.frame_54)


        self.verticalLayout_13.addWidget(self.singkeysetting)

        self.doublekeysetting = QFrame(self.scrollAreaWidgetContents)
        self.doublekeysetting.setObjectName(u"doublekeysetting")
        self.doublekeysetting.setFrameShape(QFrame.StyledPanel)
        self.doublekeysetting.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.doublekeysetting)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_25 = QFrame(self.doublekeysetting)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 80))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_22 = QLabel(self.frame_25)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_36.addWidget(self.label_22)


        self.verticalLayout_7.addWidget(self.frame_25)

        self.frame_29 = QFrame(self.doublekeysetting)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_26 = QLabel(self.frame_29)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_24.addWidget(self.label_26)

        self.k_l0_s_i = QPushButton(self.frame_29)
        self.k_l0_s_i.setObjectName(u"k_l0_s_i")
        self.k_l0_s_i.setMinimumSize(QSize(100, 30))
        self.k_l0_s_i.setMaximumSize(QSize(100, 30))
        self.k_l0_s_i.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_24.addWidget(self.k_l0_s_i)


        self.verticalLayout_7.addWidget(self.frame_29)

        self.frame_32 = QFrame(self.doublekeysetting)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_29 = QLabel(self.frame_32)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_25.addWidget(self.label_29)

        self.k_l0_s_d = QPushButton(self.frame_32)
        self.k_l0_s_d.setObjectName(u"k_l0_s_d")
        self.k_l0_s_d.setMinimumSize(QSize(100, 30))
        self.k_l0_s_d.setMaximumSize(QSize(100, 30))
        self.k_l0_s_d.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_25.addWidget(self.k_l0_s_d)


        self.verticalLayout_7.addWidget(self.frame_32)

        self.frame_31 = QFrame(self.doublekeysetting)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_28 = QLabel(self.frame_31)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_26.addWidget(self.label_28)

        self.k_r1_s_i = QPushButton(self.frame_31)
        self.k_r1_s_i.setObjectName(u"k_r1_s_i")
        self.k_r1_s_i.setMinimumSize(QSize(100, 30))
        self.k_r1_s_i.setMaximumSize(QSize(100, 30))
        self.k_r1_s_i.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_26.addWidget(self.k_r1_s_i)


        self.verticalLayout_7.addWidget(self.frame_31)

        self.frame_28 = QFrame(self.doublekeysetting)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_25 = QLabel(self.frame_28)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_29.addWidget(self.label_25)

        self.k_r1_s_d = QPushButton(self.frame_28)
        self.k_r1_s_d.setObjectName(u"k_r1_s_d")
        self.k_r1_s_d.setMinimumSize(QSize(100, 30))
        self.k_r1_s_d.setMaximumSize(QSize(100, 30))
        self.k_r1_s_d.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_29.addWidget(self.k_r1_s_d)


        self.verticalLayout_7.addWidget(self.frame_28)

        self.frame_30 = QFrame(self.doublekeysetting)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_27 = QLabel(self.frame_30)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_28.addWidget(self.label_27)

        self.k_r2_s_i = QPushButton(self.frame_30)
        self.k_r2_s_i.setObjectName(u"k_r2_s_i")
        self.k_r2_s_i.setMinimumSize(QSize(100, 30))
        self.k_r2_s_i.setMaximumSize(QSize(100, 30))
        self.k_r2_s_i.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_28.addWidget(self.k_r2_s_i)


        self.verticalLayout_7.addWidget(self.frame_30)

        self.frame_27 = QFrame(self.doublekeysetting)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_24 = QLabel(self.frame_27)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_27.addWidget(self.label_24)

        self.k_r2_s_d = QPushButton(self.frame_27)
        self.k_r2_s_d.setObjectName(u"k_r2_s_d")
        self.k_r2_s_d.setMinimumSize(QSize(100, 30))
        self.k_r2_s_d.setMaximumSize(QSize(100, 30))
        self.k_r2_s_d.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_27.addWidget(self.k_r2_s_d)


        self.verticalLayout_7.addWidget(self.frame_27)

        self.frame_33 = QFrame(self.doublekeysetting)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_37 = QLabel(self.frame_33)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_30.addWidget(self.label_37)

        self.k_l0_p_max = QPushButton(self.frame_33)
        self.k_l0_p_max.setObjectName(u"k_l0_p_max")
        self.k_l0_p_max.setMinimumSize(QSize(100, 30))
        self.k_l0_p_max.setMaximumSize(QSize(100, 30))
        self.k_l0_p_max.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_30.addWidget(self.k_l0_p_max)


        self.verticalLayout_7.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.doublekeysetting)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_40 = QLabel(self.frame_34)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_31.addWidget(self.label_40)

        self.k_l0_p_min = QPushButton(self.frame_34)
        self.k_l0_p_min.setObjectName(u"k_l0_p_min")
        self.k_l0_p_min.setMinimumSize(QSize(100, 30))
        self.k_l0_p_min.setMaximumSize(QSize(100, 30))
        self.k_l0_p_min.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_31.addWidget(self.k_l0_p_min)


        self.verticalLayout_7.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.doublekeysetting)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_41 = QLabel(self.frame_35)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_32.addWidget(self.label_41)

        self.k_r1_p_max = QPushButton(self.frame_35)
        self.k_r1_p_max.setObjectName(u"k_r1_p_max")
        self.k_r1_p_max.setMinimumSize(QSize(100, 30))
        self.k_r1_p_max.setMaximumSize(QSize(100, 30))
        self.k_r1_p_max.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_32.addWidget(self.k_r1_p_max)


        self.verticalLayout_7.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.doublekeysetting)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_42 = QLabel(self.frame_36)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(300, 0))
        self.label_42.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_33.addWidget(self.label_42)

        self.k_r1_p_min = QPushButton(self.frame_36)
        self.k_r1_p_min.setObjectName(u"k_r1_p_min")
        self.k_r1_p_min.setMinimumSize(QSize(100, 30))
        self.k_r1_p_min.setMaximumSize(QSize(100, 30))
        self.k_r1_p_min.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_33.addWidget(self.k_r1_p_min)


        self.verticalLayout_7.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.doublekeysetting)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_43 = QLabel(self.frame_37)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_34.addWidget(self.label_43)

        self.k_r2_p_max = QPushButton(self.frame_37)
        self.k_r2_p_max.setObjectName(u"k_r2_p_max")
        self.k_r2_p_max.setMinimumSize(QSize(100, 30))
        self.k_r2_p_max.setMaximumSize(QSize(100, 30))
        self.k_r2_p_max.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_34.addWidget(self.k_r2_p_max)


        self.verticalLayout_7.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.doublekeysetting)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_44 = QLabel(self.frame_38)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_35.addWidget(self.label_44)

        self.k_r2_p_min = QPushButton(self.frame_38)
        self.k_r2_p_min.setObjectName(u"k_r2_p_min")
        self.k_r2_p_min.setMinimumSize(QSize(100, 30))
        self.k_r2_p_min.setMaximumSize(QSize(100, 30))
        self.k_r2_p_min.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_35.addWidget(self.k_r2_p_min)


        self.verticalLayout_7.addWidget(self.frame_38)


        self.verticalLayout_13.addWidget(self.doublekeysetting)

        self.triplekeysetting = QFrame(self.scrollAreaWidgetContents)
        self.triplekeysetting.setObjectName(u"triplekeysetting")
        self.triplekeysetting.setFrameShape(QFrame.StyledPanel)
        self.triplekeysetting.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.triplekeysetting)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_40 = QFrame(self.triplekeysetting)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(0, 80))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_30 = QLabel(self.frame_40)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_37.addWidget(self.label_30)


        self.verticalLayout_10.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.triplekeysetting)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_31 = QLabel(self.frame_41)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_41.addWidget(self.label_31)

        self.k_l0_max_i = QPushButton(self.frame_41)
        self.k_l0_max_i.setObjectName(u"k_l0_max_i")
        self.k_l0_max_i.setMinimumSize(QSize(130, 30))
        self.k_l0_max_i.setMaximumSize(QSize(130, 30))
        self.k_l0_max_i.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_41.addWidget(self.k_l0_max_i)


        self.verticalLayout_10.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.triplekeysetting)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_32 = QLabel(self.frame_42)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_42.addWidget(self.label_32)

        self.k_l0_max_d = QPushButton(self.frame_42)
        self.k_l0_max_d.setObjectName(u"k_l0_max_d")
        self.k_l0_max_d.setMinimumSize(QSize(130, 30))
        self.k_l0_max_d.setMaximumSize(QSize(130, 30))
        self.k_l0_max_d.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_42.addWidget(self.k_l0_max_d)


        self.verticalLayout_10.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.triplekeysetting)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_33 = QLabel(self.frame_43)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_43.addWidget(self.label_33)

        self.k_r1_max_i = QPushButton(self.frame_43)
        self.k_r1_max_i.setObjectName(u"k_r1_max_i")
        self.k_r1_max_i.setMinimumSize(QSize(130, 30))
        self.k_r1_max_i.setMaximumSize(QSize(130, 30))
        self.k_r1_max_i.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_43.addWidget(self.k_r1_max_i)


        self.verticalLayout_10.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.triplekeysetting)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_34 = QLabel(self.frame_44)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_44.addWidget(self.label_34)

        self.k_r1_max_d = QPushButton(self.frame_44)
        self.k_r1_max_d.setObjectName(u"k_r1_max_d")
        self.k_r1_max_d.setMinimumSize(QSize(130, 30))
        self.k_r1_max_d.setMaximumSize(QSize(130, 30))
        self.k_r1_max_d.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_44.addWidget(self.k_r1_max_d)


        self.verticalLayout_10.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.triplekeysetting)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_35 = QLabel(self.frame_45)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_45.addWidget(self.label_35)

        self.k_r2_max_i = QPushButton(self.frame_45)
        self.k_r2_max_i.setObjectName(u"k_r2_max_i")
        self.k_r2_max_i.setMinimumSize(QSize(130, 30))
        self.k_r2_max_i.setMaximumSize(QSize(130, 30))
        self.k_r2_max_i.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_45.addWidget(self.k_r2_max_i)


        self.verticalLayout_10.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.triplekeysetting)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_38 = QLabel(self.frame_46)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_46.addWidget(self.label_38)

        self.k_r2_max_d = QPushButton(self.frame_46)
        self.k_r2_max_d.setObjectName(u"k_r2_max_d")
        self.k_r2_max_d.setMinimumSize(QSize(130, 30))
        self.k_r2_max_d.setMaximumSize(QSize(130, 30))
        self.k_r2_max_d.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_46.addWidget(self.k_r2_max_d)


        self.verticalLayout_10.addWidget(self.frame_46)

        self.frame_47 = QFrame(self.triplekeysetting)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_39 = QLabel(self.frame_47)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_47.addWidget(self.label_39)

        self.k_l0_min_i = QPushButton(self.frame_47)
        self.k_l0_min_i.setObjectName(u"k_l0_min_i")
        self.k_l0_min_i.setMinimumSize(QSize(130, 30))
        self.k_l0_min_i.setMaximumSize(QSize(130, 30))
        self.k_l0_min_i.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_47.addWidget(self.k_l0_min_i)


        self.verticalLayout_10.addWidget(self.frame_47)

        self.frame_48 = QFrame(self.triplekeysetting)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_45 = QLabel(self.frame_48)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_48.addWidget(self.label_45)

        self.k_l0_min_d = QPushButton(self.frame_48)
        self.k_l0_min_d.setObjectName(u"k_l0_min_d")
        self.k_l0_min_d.setMinimumSize(QSize(130, 30))
        self.k_l0_min_d.setMaximumSize(QSize(130, 30))
        self.k_l0_min_d.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_48.addWidget(self.k_l0_min_d)


        self.verticalLayout_10.addWidget(self.frame_48)

        self.frame_49 = QFrame(self.triplekeysetting)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_46 = QLabel(self.frame_49)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_49.addWidget(self.label_46)

        self.k_r1_min_i = QPushButton(self.frame_49)
        self.k_r1_min_i.setObjectName(u"k_r1_min_i")
        self.k_r1_min_i.setMinimumSize(QSize(130, 30))
        self.k_r1_min_i.setMaximumSize(QSize(130, 30))
        self.k_r1_min_i.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_49.addWidget(self.k_r1_min_i)


        self.verticalLayout_10.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.triplekeysetting)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_47 = QLabel(self.frame_50)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(300, 0))
        self.label_47.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_50.addWidget(self.label_47)

        self.k_r1_min_d = QPushButton(self.frame_50)
        self.k_r1_min_d.setObjectName(u"k_r1_min_d")
        self.k_r1_min_d.setMinimumSize(QSize(130, 30))
        self.k_r1_min_d.setMaximumSize(QSize(130, 30))
        self.k_r1_min_d.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_50.addWidget(self.k_r1_min_d)


        self.verticalLayout_10.addWidget(self.frame_50)

        self.frame_51 = QFrame(self.triplekeysetting)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_48 = QLabel(self.frame_51)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_51.addWidget(self.label_48)

        self.k_r2_min_i = QPushButton(self.frame_51)
        self.k_r2_min_i.setObjectName(u"k_r2_min_i")
        self.k_r2_min_i.setMinimumSize(QSize(130, 30))
        self.k_r2_min_i.setMaximumSize(QSize(130, 30))
        self.k_r2_min_i.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_51.addWidget(self.k_r2_min_i)


        self.verticalLayout_10.addWidget(self.frame_51)

        self.frame_52 = QFrame(self.triplekeysetting)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_49 = QLabel(self.frame_52)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_52.addWidget(self.label_49)

        self.k_r2_min_d = QPushButton(self.frame_52)
        self.k_r2_min_d.setObjectName(u"k_r2_min_d")
        self.k_r2_min_d.setMinimumSize(QSize(130, 30))
        self.k_r2_min_d.setMaximumSize(QSize(130, 30))
        self.k_r2_min_d.setStyleSheet(u"QPushButton {\n"
"	 border: none;\n"
"     background-position: center;\n"
"     background-repeat: no-repeat; \n"
"     background-color: rgb(35, 40, 49);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: none;\n"
"}")

        self.horizontalLayout_52.addWidget(self.k_r2_min_d)


        self.verticalLayout_10.addWidget(self.frame_52)


        self.verticalLayout_13.addWidget(self.triplekeysetting)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_setting)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.stylesheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"easy help", None))
        self.home.setText("")
        self.explaine.setText(QCoreApplication.translate("MainWindow", u"Since \n"
"pywin32\n"
"ctypes\n"
"detects \n"
"the \n"
"global \n"
"mouse \n"
"keyboard, \n"
"don't \n"
"use it \n"
"in PVP", None))
        self.setting.setText("")
        self.help_erections.setText(QCoreApplication.translate("MainWindow", u"help erections", None))
        self.run.setText("")
        self.global_key_control.setText(QCoreApplication.translate("MainWindow", u"turn global key control", None))
        self.L0_value.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>L0_speed</p></body></html>", None))
        self.L0_p.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>L0_position</p></body></html>", None))
        self.L0.setText(QCoreApplication.translate("MainWindow", u"L0", None))
        self.R1_value.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>R1_speed: </p></body></html>", None))
        self.R1_p.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>R1_position</p></body></html>", None))
        self.R1.setText(QCoreApplication.translate("MainWindow", u"R1", None))
        self.R2_value.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>R2_speed: </p></body></html>", None))
        self.R2_p.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>R2_position</p></body></html>", None))
        self.R2.setText(QCoreApplication.translate("MainWindow", u"R2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">COM</span></p></body></html>", None))
        self.run_com.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">single key control:</span><span style=\" font-size:14pt;\">you can use them with single key</span></p><p><span style=\" font-size:8pt;\">(if don't want to setting key pleause push ESC to exit)</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"key control L0 position up", None))
        self.k_l0_p_u.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"key control L0 position down", None))
        self.k_l0_p_d.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"key control R1 position left", None))
        self.k_r1_p_l.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"key control R1 position right", None))
        self.k_r1_p_r.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"key control R2 position front", None))
        self.k_r2_p_f.setText(QCoreApplication.translate("MainWindow", u"Space", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"key control R2 position back", None))
        self.k_r2_p_b.setText(QCoreApplication.translate("MainWindow", u"Lshift", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"key control Key speed combinations", None))
        self.k_k_c.setText(QCoreApplication.translate("MainWindow", u"Lctrl", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"key control Key position restrictions combinations", None))
        self.k_k_r.setText(QCoreApplication.translate("MainWindow", u"Lalt", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"key control L0 turn", None))
        self.k_l0_t.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"key control R1 turn", None))
        self.k_r1_t.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"key control R2 turn", None))
        self.k_r2_t.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"key control All turn", None))
        self.k_a_t.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"key control app windows turn", None))
        self.k_windows_t.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"key control Helping with erections", None))
        self.k_help_erections.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"key control position restrictions increase", None))
        self.k_p_r_i.setText(QCoreApplication.translate("MainWindow", u"UP", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"key control position restrictions decrease", None))
        self.k_p_r_d.setText(QCoreApplication.translate("MainWindow", u"DOWN", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">double key control:</span><span style=\" font-size:14pt;\">you must use them with the key combinations.</span></p><p><span style=\" font-size:8pt;\">(if don't want to setting key pleause push ESC to exit,you cann't change it directly)</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"key control L0 speed increase", None))
        self.k_l0_s_i.setText(QCoreApplication.translate("MainWindow", u"L_ctrl+w", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"key control L0 speed decrease", None))
        self.k_l0_s_d.setText(QCoreApplication.translate("MainWindow", u"L_ctrl+s", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"key control R1 speed increase", None))
        self.k_r1_s_i.setText(QCoreApplication.translate("MainWindow", u"L_ctrl+a", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"key control R1 speed decrease", None))
        self.k_r1_s_d.setText(QCoreApplication.translate("MainWindow", u"L_ctrl+d", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"key control R2 speed increase", None))
        self.k_r2_s_i.setText(QCoreApplication.translate("MainWindow", u"L_ctrl+space", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"key control R2 speed decrease", None))
        self.k_r2_s_d.setText(QCoreApplication.translate("MainWindow", u"L_ctrl+L_shift", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"key control L0 position max", None))
        self.k_l0_p_max.setText(QCoreApplication.translate("MainWindow", u"L_alt+w", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"key control L0 position min", None))
        self.k_l0_p_min.setText(QCoreApplication.translate("MainWindow", u"L_alt+s", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"key control R1 position max", None))
        self.k_r1_p_max.setText(QCoreApplication.translate("MainWindow", u"L_alt+a", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"key control R1 position min", None))
        self.k_r1_p_min.setText(QCoreApplication.translate("MainWindow", u"L_alt+d", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"key control R2 position max", None))
        self.k_r2_p_max.setText(QCoreApplication.translate("MainWindow", u"L_alt+space", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"key control R2 position min", None))
        self.k_r2_p_min.setText(QCoreApplication.translate("MainWindow", u"L_alt+L_shift", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">triple key control:</span><span style=\" font-size:14pt;\">you must use them with the key combinations</span></p><p><span style=\" font-size:8pt;\">(if don't want to setting key pleause push ESC to exit,you cann't change it directly)</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"key control L0 max increase", None))
        self.k_l0_max_i.setText(QCoreApplication.translate("MainWindow", u"Lalt+W+UP", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"key control L0 max decrease", None))
        self.k_l0_max_d.setText(QCoreApplication.translate("MainWindow", u"Lalt+W+DOWN", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"key control R1 max increase", None))
        self.k_r1_max_i.setText(QCoreApplication.translate("MainWindow", u"Lalt+A+UP", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"key control R1 max decrease", None))
        self.k_r1_max_d.setText(QCoreApplication.translate("MainWindow", u"Lalt+A+DOWN", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"key control R2 max increase", None))
        self.k_r2_max_i.setText(QCoreApplication.translate("MainWindow", u"Lalt+Space+UP", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"key control R2 max decrease", None))
        self.k_r2_max_d.setText(QCoreApplication.translate("MainWindow", u"Lalt+Space+DOWN", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"key control L0 min increase", None))
        self.k_l0_min_i.setText(QCoreApplication.translate("MainWindow", u"Lalt+S+UP", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"key control L0 min decrease", None))
        self.k_l0_min_d.setText(QCoreApplication.translate("MainWindow", u"Lalt+S+DOWN", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"key control R1 min increase", None))
        self.k_r1_min_i.setText(QCoreApplication.translate("MainWindow", u"Lalt+D+UP", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"key control R1 min decrease", None))
        self.k_r1_min_d.setText(QCoreApplication.translate("MainWindow", u"Lalt+D+DOWN", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"key control R2 min increase", None))
        self.k_r2_min_i.setText(QCoreApplication.translate("MainWindow", u"Lalt+Lshift+UP", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"key control R2 min decrease", None))
        self.k_r2_min_d.setText(QCoreApplication.translate("MainWindow", u"L_alt+L_shift+DOWN", None))
    # retranslateUi

