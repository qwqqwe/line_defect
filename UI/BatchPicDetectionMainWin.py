# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BatchPicDetectionMainWin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QScrollArea, QWidget, QGridLayout, QHeaderView, QDesktopWidget


class Ui_BatchpicDetectionMainWindow(object):
    def setupUi(self, PicDetectionMainWindow):
        PicDetectionMainWindow.setObjectName("PicDetectionMainWindow")
        PicDetectionMainWindow.resize(1012, 728)
        font = QtGui.QFont()
        font.setPointSize(9)
        PicDetectionMainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(PicDetectionMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 10, 921, 631))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.origin_scrollArea = QtWidgets.QScrollArea(self.layoutWidget)
        self.origin_scrollArea.setWidgetResizable(True)
        self.origin_scrollArea.setObjectName("origin_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 442, 269))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout1 = QGridLayout(self.scrollAreaWidgetContents)
        self.origin_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.origin_scrollArea)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.scroll_area_images = QScrollArea(self)
        self.scroll_area_images.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget(self)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 442, 269))
        self.scrollAreaWidgetContents.setObjectName('scrollAreaWidgetContends')
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.scroll_area_images.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scroll_area_images)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 6)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 6)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.model = QStandardItemModel(0, 2);
        self.model.setHorizontalHeaderLabels(['图片编号', '缺陷类型'])
        self.resutView = QtWidgets.QTableView(self.layoutWidget)
        self.resutView.setModel(self.model)
        self.resutView.setObjectName("resutView")
        self.resutView.horizontalHeader().setStretchLastSection(True)
        self.resutView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalLayout_3.addWidget(self.resutView)
        PicDetectionMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PicDetectionMainWindow)
        self.statusbar.setObjectName("statusbar")
        PicDetectionMainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(PicDetectionMainWindow)
        self.toolBar.setObjectName("toolBar")
        PicDetectionMainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtWidgets.QMenuBar(PicDetectionMainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1012, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuRun = QtWidgets.QMenu(self.menuBar)
        self.menuRun.setObjectName("menuRun")
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setObjectName("menuSettings")
        self.menumode = QtWidgets.QMenu(self.menuBar)
        self.menumode.setObjectName("menumode")
        PicDetectionMainWindow.setMenuBar(self.menuBar)
        self.actionDetection = QtWidgets.QAction(PicDetectionMainWindow)
        self.actionDetection.setObjectName("actionDetection")
        self.actionTrain = QtWidgets.QAction(PicDetectionMainWindow)
        self.actionTrain.setObjectName("actionTrain")
        self.actionMark = QtWidgets.QAction(PicDetectionMainWindow)
        self.actionMark.setObjectName("actionMark")
        self.actionOpen = QtWidgets.QAction(PicDetectionMainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionStop = QtWidgets.QAction(PicDetectionMainWindow)
        self.actionStop.setObjectName("actionStop")
        self.actionpicture_detection = QtWidgets.QAction(PicDetectionMainWindow)
        self.actionpicture_detection.setObjectName("actionpicture_detection")
        self.actionreal_time_detection = QtWidgets.QAction(PicDetectionMainWindow)
        self.actionreal_time_detection.setObjectName("actionreal_time_detection")
        self.actionrun = QtWidgets.QAction(PicDetectionMainWindow)
        self.actionrun.setObjectName("actionrun")
        self.actionbatch_detection = QtWidgets.QAction(PicDetectionMainWindow)
        self.actionbatch_detection.setObjectName("actionbatch_detection")
        self.actionmagentic_core = QtWidgets.QAction(PicDetectionMainWindow)
        self.actionmagentic_core.setObjectName("actionmagentic_core")
        self.actionpocket_mouth = QtWidgets.QAction(PicDetectionMainWindow)
        self.actionpocket_mouth.setObjectName("actionpocket_mouth")
        self.actionpocket_mouth_2 = QtWidgets.QAction(PicDetectionMainWindow)
        self.actionpocket_mouth_2.setObjectName("actionpocket_mouth_2")
        self.actionimport = QtWidgets.QAction(PicDetectionMainWindow)
        self.actionimport.setObjectName("actionimport")
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDetection)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTrain)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionMark)
        self.toolBar.addSeparator()
        self.menuRun.addSeparator()
        self.menuRun.addAction(self.actionOpen)
        self.menuRun.addSeparator()
        self.menuRun.addAction(self.actionrun)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionpicture_detection)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionreal_time_detection)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionbatch_detection)
        self.menumode.addAction(self.actionmagentic_core)
        self.menumode.addSeparator()
        self.menumode.addAction(self.actionpocket_mouth_2)
        self.menumode.addSeparator()
        self.menumode.addAction(self.actionimport)
        self.menuBar.addAction(self.menuRun.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menumode.menuAction())

        self.retranslateUi(PicDetectionMainWindow)
        QtCore.QMetaObject.connectSlotsByName(PicDetectionMainWindow)
        self.center()
    def retranslateUi(self, PicDetectionMainWindow):
        _translate = QtCore.QCoreApplication.translate
        PicDetectionMainWindow.setWindowTitle(_translate("PicDetectionMainWindow", "缺陷检测系统"))
        self.label_3.setText(_translate("PicDetectionMainWindow", "原图"))
        self.label_2.setText(_translate("PicDetectionMainWindow", "检测图"))
        self.toolBar.setWindowTitle(_translate("PicDetectionMainWindow", "toolBar"))
        self.menuRun.setTitle(_translate("PicDetectionMainWindow", "File"))
        self.menuSettings.setTitle(_translate("PicDetectionMainWindow", "Settings"))
        self.menumode.setTitle(_translate("PicDetectionMainWindow", "Mode"))
        self.actionDetection.setText(_translate("PicDetectionMainWindow", "检测模式"))
        self.actionDetection.setToolTip(_translate("PicDetectionMainWindow", "检测模式"))
        self.actionDetection.setShortcut(_translate("PicDetectionMainWindow", "Ctrl+D"))
        self.actionTrain.setText(_translate("PicDetectionMainWindow", "训练模式"))
        self.actionTrain.setToolTip(_translate("PicDetectionMainWindow", "训练模式"))
        self.actionTrain.setShortcut(_translate("PicDetectionMainWindow", "Ctrl+T"))
        self.actionMark.setText(_translate("PicDetectionMainWindow", "标注模式"))
        self.actionMark.setToolTip(_translate("PicDetectionMainWindow", "标注图片"))
        self.actionMark.setShortcut(_translate("PicDetectionMainWindow", "Ctrl+M"))
        self.actionOpen.setText(_translate("PicDetectionMainWindow", "open"))
        self.actionStop.setText(_translate("PicDetectionMainWindow", "Stop"))
        self.actionpicture_detection.setText(_translate("PicDetectionMainWindow", "picture detection"))
        self.actionreal_time_detection.setText(_translate("PicDetectionMainWindow", "real-time detection"))
        self.actionrun.setText(_translate("PicDetectionMainWindow", "run"))
        self.actionbatch_detection.setText(_translate("PicDetectionMainWindow", "batch detection"))
        self.actionmagentic_core.setText(_translate("PicDetectionMainWindow", "magentic_core"))
        self.actionpocket_mouth.setText(_translate("PicDetectionMainWindow", "pocket mouth"))
        self.actionpocket_mouth_2.setText(_translate("PicDetectionMainWindow", "pocket mouth"))
        self.actionimport.setText(_translate("PicDetectionMainWindow", "import"))
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)