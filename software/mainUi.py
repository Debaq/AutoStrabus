# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainBLTMTY.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_AutoStrabus(object):
    def setupUi(self, AutoStrabus):
        if not AutoStrabus.objectName():
            AutoStrabus.setObjectName(u"AutoStrabus")
        AutoStrabus.resize(1011, 793)
        self.centralwidget = QWidget(AutoStrabus)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_7 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_open = QWidget()
        self.tab_open.setObjectName(u"tab_open")
        self.verticalLayout_8 = QVBoxLayout(self.tab_open)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_openList = QFrame(self.tab_open)
        self.frame_openList.setObjectName(u"frame_openList")
        self.layout_openList = QVBoxLayout(self.frame_openList)
        self.layout_openList.setObjectName(u"layout_openList")

        self.verticalLayout_8.addWidget(self.frame_openList)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tab_open, "")
        self.tab_record = QWidget()
        self.tab_record.setObjectName(u"tab_record")
        self.verticalLayout_6 = QVBoxLayout(self.tab_record)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.CameraFrame = QLabel(self.tab_record)
        self.CameraFrame.setObjectName(u"CameraFrame")

        self.horizontalLayout_4.addWidget(self.CameraFrame)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.btn_cal = QPushButton(self.tab_record)
        self.btn_cal.setObjectName(u"btn_cal")

        self.horizontalLayout.addWidget(self.btn_cal)

        self.btn_record = QPushButton(self.tab_record)
        self.btn_record.setObjectName(u"btn_record")

        self.horizontalLayout.addWidget(self.btn_record)

        self.frame_head = QFrame(self.tab_record)
        self.frame_head.setObjectName(u"frame_head")
        self.horizontalLayout_3 = QHBoxLayout(self.frame_head)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.frame_head)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.slider_h = QSlider(self.frame_head)
        self.slider_h.setObjectName(u"slider_h")
        self.slider_h.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_4.addWidget(self.slider_h)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.slider_v = QSlider(self.frame_head)
        self.slider_v.setObjectName(u"slider_v")
        self.slider_v.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_3.addWidget(self.slider_v)


        self.horizontalLayout.addWidget(self.frame_head)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.tab_record)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_7)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.tab_record)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_6 = QLabel(self.tab_record)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)

        self.lbl_blur = QLabel(self.tab_record)
        self.lbl_blur.setObjectName(u"lbl_blur")

        self.gridLayout_2.addWidget(self.lbl_blur, 1, 2, 1, 1)

        self.lbl_threshold = QLabel(self.tab_record)
        self.lbl_threshold.setObjectName(u"lbl_threshold")

        self.gridLayout_2.addWidget(self.lbl_threshold, 2, 2, 1, 1)

        self.label_5 = QLabel(self.tab_record)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.slider_size = QSlider(self.tab_record)
        self.slider_size.setObjectName(u"slider_size")
        self.slider_size.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.slider_size, 3, 1, 1, 1)

        self.slider_threshold = QSlider(self.tab_record)
        self.slider_threshold.setObjectName(u"slider_threshold")
        self.slider_threshold.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.slider_threshold, 2, 1, 1, 1)

        self.lbl_size = QLabel(self.tab_record)
        self.lbl_size.setObjectName(u"lbl_size")

        self.gridLayout_2.addWidget(self.lbl_size, 3, 2, 1, 1)

        self.slider_blur = QSlider(self.tab_record)
        self.slider_blur.setObjectName(u"slider_blur")
        self.slider_blur.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.slider_blur, 1, 1, 1, 1)

        self.slider_focus = QSlider(self.tab_record)
        self.slider_focus.setObjectName(u"slider_focus")
        self.slider_focus.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.slider_focus, 0, 1, 1, 1)

        self.label_17 = QLabel(self.tab_record)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 0, 0, 1, 1)

        self.lbl_focus = QLabel(self.tab_record)
        self.lbl_focus.setObjectName(u"lbl_focus")

        self.gridLayout_2.addWidget(self.lbl_focus, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.tab_record)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.time_alt = QDoubleSpinBox(self.tab_record)
        self.time_alt.setObjectName(u"time_alt")

        self.verticalLayout_3.addWidget(self.time_alt)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.tab_record)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.time_sup = QDoubleSpinBox(self.tab_record)
        self.time_sup.setObjectName(u"time_sup")

        self.verticalLayout.addWidget(self.time_sup)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.btn_act_oclu = QPushButton(self.tab_record)
        self.btn_act_oclu.setObjectName(u"btn_act_oclu")

        self.horizontalLayout_2.addWidget(self.btn_act_oclu)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_record, "")
        self.tab_edit = QWidget()
        self.tab_edit.setObjectName(u"tab_edit")
        self.verticalLayout_10 = QVBoxLayout(self.tab_edit)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.layout_edit = QVBoxLayout()
        self.layout_edit.setObjectName(u"layout_edit")

        self.verticalLayout_10.addLayout(self.layout_edit)

        self.tabWidget.addTab(self.tab_edit, "")
        self.tab_config = QWidget()
        self.tab_config.setObjectName(u"tab_config")
        self.verticalLayout_9 = QVBoxLayout(self.tab_config)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.slider_gamma = QSlider(self.tab_config)
        self.slider_gamma.setObjectName(u"slider_gamma")
        self.slider_gamma.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.slider_gamma, 5, 1, 1, 1)

        self.slide_satur = QSlider(self.tab_config)
        self.slide_satur.setObjectName(u"slide_satur")
        self.slide_satur.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.slide_satur, 3, 1, 1, 1)

        self.chk_autofocus = QCheckBox(self.tab_config)
        self.chk_autofocus.setObjectName(u"chk_autofocus")

        self.gridLayout.addWidget(self.chk_autofocus, 8, 1, 1, 1)

        self.slider_brig = QSlider(self.tab_config)
        self.slider_brig.setObjectName(u"slider_brig")
        self.slider_brig.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.slider_brig, 1, 1, 1, 1)

        self.slider_ligth = QSlider(self.tab_config)
        self.slider_ligth.setObjectName(u"slider_ligth")
        self.slider_ligth.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.slider_ligth, 7, 1, 1, 1)

        self.chk_white_balance_automatic = QCheckBox(self.tab_config)
        self.chk_white_balance_automatic.setObjectName(u"chk_white_balance_automatic")

        self.gridLayout.addWidget(self.chk_white_balance_automatic, 9, 1, 1, 1)

        self.label_12 = QLabel(self.tab_config)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 3, 0, 1, 1)

        self.lbl_contrast = QLabel(self.tab_config)
        self.lbl_contrast.setObjectName(u"lbl_contrast")

        self.gridLayout.addWidget(self.lbl_contrast, 2, 2, 1, 1)

        self.label_16 = QLabel(self.tab_config)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 7, 0, 1, 1)

        self.slider_hue = QSlider(self.tab_config)
        self.slider_hue.setObjectName(u"slider_hue")
        self.slider_hue.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.slider_hue, 4, 1, 1, 1)

        self.label_10 = QLabel(self.tab_config)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)

        self.lbl_ligth = QLabel(self.tab_config)
        self.lbl_ligth.setObjectName(u"lbl_ligth")

        self.gridLayout.addWidget(self.lbl_ligth, 7, 2, 1, 1)

        self.lbl_satur = QLabel(self.tab_config)
        self.lbl_satur.setObjectName(u"lbl_satur")

        self.gridLayout.addWidget(self.lbl_satur, 3, 2, 1, 1)

        self.slider_contrast = QSlider(self.tab_config)
        self.slider_contrast.setObjectName(u"slider_contrast")
        self.slider_contrast.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.slider_contrast, 2, 1, 1, 1)

        self.label_8 = QLabel(self.tab_config)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 0, 1, 1, 1)

        self.label_14 = QLabel(self.tab_config)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 5, 0, 1, 1)

        self.lbl_brig = QLabel(self.tab_config)
        self.lbl_brig.setObjectName(u"lbl_brig")

        self.gridLayout.addWidget(self.lbl_brig, 1, 2, 1, 1)

        self.label_13 = QLabel(self.tab_config)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 4, 0, 1, 1)

        self.label_15 = QLabel(self.tab_config)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 6, 0, 1, 1)

        self.label_11 = QLabel(self.tab_config)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)

        self.lbl_hue = QLabel(self.tab_config)
        self.lbl_hue.setObjectName(u"lbl_hue")

        self.gridLayout.addWidget(self.lbl_hue, 4, 2, 1, 1)

        self.slider_balanceW = QSlider(self.tab_config)
        self.slider_balanceW.setObjectName(u"slider_balanceW")
        self.slider_balanceW.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.slider_balanceW, 6, 1, 1, 1)

        self.lbl_gamma = QLabel(self.tab_config)
        self.lbl_gamma.setObjectName(u"lbl_gamma")

        self.gridLayout.addWidget(self.lbl_gamma, 5, 2, 1, 1)

        self.lbl_balanceW = QLabel(self.tab_config)
        self.lbl_balanceW.setObjectName(u"lbl_balanceW")

        self.gridLayout.addWidget(self.lbl_balanceW, 6, 2, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout)


        self.horizontalLayout_6.addLayout(self.verticalLayout_7)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.tabWidget.addTab(self.tab_config, "")

        self.horizontalLayout_7.addWidget(self.tabWidget)

        AutoStrabus.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AutoStrabus)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1011, 30))
        AutoStrabus.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AutoStrabus)
        self.statusbar.setObjectName(u"statusbar")
        AutoStrabus.setStatusBar(self.statusbar)

        self.retranslateUi(AutoStrabus)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(AutoStrabus)
    # setupUi

    def retranslateUi(self, AutoStrabus):
        AutoStrabus.setWindowTitle(QCoreApplication.translate("AutoStrabus", u"AutoStrabus", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_open), QCoreApplication.translate("AutoStrabus", u"Abrir", None))
        self.CameraFrame.setText(QCoreApplication.translate("AutoStrabus", u"Te&xtLabel", None))
        self.btn_cal.setText(QCoreApplication.translate("AutoStrabus", u"Calibrar", None))
        self.btn_record.setText(QCoreApplication.translate("AutoStrabus", u"Comenzar a Grabar", None))
        self.label_3.setText(QCoreApplication.translate("AutoStrabus", u"Posici\u00f3n cabeza", None))
        self.label_7.setText(QCoreApplication.translate("AutoStrabus", u"Config. Procesamiento", None))
        self.label_4.setText(QCoreApplication.translate("AutoStrabus", u"desenfoque", None))
        self.label_6.setText(QCoreApplication.translate("AutoStrabus", u"minima \u00e1rea", None))
        self.lbl_blur.setText(QCoreApplication.translate("AutoStrabus", u"0", None))
        self.lbl_threshold.setText(QCoreApplication.translate("AutoStrabus", u"0", None))
        self.label_5.setText(QCoreApplication.translate("AutoStrabus", u"umbral", None))
        self.lbl_size.setText(QCoreApplication.translate("AutoStrabus", u"0", None))
        self.label_17.setText(QCoreApplication.translate("AutoStrabus", u"enfoque", None))
        self.lbl_focus.setText(QCoreApplication.translate("AutoStrabus", u"0", None))
        self.label.setText(QCoreApplication.translate("AutoStrabus", u"T", None))
        self.label_2.setText(QCoreApplication.translate("AutoStrabus", u"O", None))
        self.btn_act_oclu.setText(QCoreApplication.translate("AutoStrabus", u"Activar Oclusores", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_record), QCoreApplication.translate("AutoStrabus", u"Medir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_edit), QCoreApplication.translate("AutoStrabus", u"Editar", None))
        self.chk_autofocus.setText(QCoreApplication.translate("AutoStrabus", u"AutoFoco", None))
        self.chk_white_balance_automatic.setText(QCoreApplication.translate("AutoStrabus", u"Auto Balance de Blancos", None))
        self.label_12.setText(QCoreApplication.translate("AutoStrabus", u"Saturaci\u00f3n", None))
        self.lbl_contrast.setText(QCoreApplication.translate("AutoStrabus", u"0", None))
        self.label_16.setText(QCoreApplication.translate("AutoStrabus", u"Compensaci\u00f3nde luz", None))
        self.label_10.setText(QCoreApplication.translate("AutoStrabus", u"Brillo", None))
        self.lbl_ligth.setText(QCoreApplication.translate("AutoStrabus", u"0", None))
        self.lbl_satur.setText(QCoreApplication.translate("AutoStrabus", u"0", None))
        self.label_8.setText(QCoreApplication.translate("AutoStrabus", u"Config. C\u00e1mara", None))
        self.label_14.setText(QCoreApplication.translate("AutoStrabus", u"Gama", None))
        self.lbl_brig.setText(QCoreApplication.translate("AutoStrabus", u"0", None))
        self.label_13.setText(QCoreApplication.translate("AutoStrabus", u"Hue", None))
        self.label_15.setText(QCoreApplication.translate("AutoStrabus", u"Balance de blancos", None))
        self.label_11.setText(QCoreApplication.translate("AutoStrabus", u"Contraste", None))
        self.lbl_hue.setText(QCoreApplication.translate("AutoStrabus", u"0", None))
        self.lbl_gamma.setText(QCoreApplication.translate("AutoStrabus", u"0", None))
        self.lbl_balanceW.setText(QCoreApplication.translate("AutoStrabus", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_config), QCoreApplication.translate("AutoStrabus", u"Configuraci\u00f3n", None))
    # retranslateUi

