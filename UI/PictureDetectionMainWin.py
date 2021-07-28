# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PictureDetectionMainWin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget


class Ui_PicDetectionMainWindow(object):
    def setupUi(self, PicDetectionMainWindow):
        PicDetectionMainWindow.setObjectName("PicDetectionMainWindow")
        PicDetectionMainWindow.resize(1012, 728)
        font = QtGui.QFont()
        font.setPointSize(9)
        PicDetectionMainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(PicDetectionMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(510, 0, 20, 651))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 461, 621))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.original_img = QtWidgets.QLabel(self.groupBox)
        self.original_img.setGeometry(QtCore.QRect(10, 50, 441, 431))
        self.original_img.setText("")
        self.original_img.setObjectName("original_img")
        self.verticalLayout.addWidget(self.groupBox)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(540, 10, 461, 621))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 40, 441, 571))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.detection_img = QtWidgets.QLabel(self.layoutWidget2)
        self.detection_img.setText("")
        self.detection_img.setObjectName("detection_img")
        self.verticalLayout_3.addWidget(self.detection_img)
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.detection_result = QtWidgets.QLabel(self.layoutWidget2)
        self.detection_result.setText("")
        self.detection_result.setObjectName("detection_result")
        self.verticalLayout_3.addWidget(self.detection_result)
        self.verticalLayout_3.setStretch(0, 5)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
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
        self.menuMode = QtWidgets.QMenu(self.menuBar)
        self.menuMode.setObjectName("menuMode")
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
        self.actionchange_mode = QtWidgets.QAction(PicDetectionMainWindow)
        self.actionchange_mode.setObjectName("actionchange_mode")
        self.actionmagentic_core = QtWidgets.QAction(PicDetectionMainWindow)
        self.actionmagentic_core.setObjectName("actionmagentic core")
        self.actionpocket_mouth = QtWidgets.QAction(PicDetectionMainWindow)
        self.actionpocket_mouth.setObjectName("actionpocket_mouth")
        self.actionimport = QtWidgets.QAction(PicDetectionMainWindow)
        self.actionimport.setObjectName("actionimport")
        self.actiondefault_mode = QtWidgets.QAction(PicDetectionMainWindow)
        self.actiondefault_mode.setObjectName("actiondefault_mode")
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
        self.menuMode.addAction(self.actionmagentic_core)
        self.menuMode.addSeparator()
        self.menuMode.addAction(self.actionpocket_mouth)
        self.menuMode.addSeparator()
        self.menuMode.addAction(self.actiondefault_mode)
        self.menuMode.addSeparator()
        self.menuMode.addAction(self.actionimport)
        self.menuBar.addAction(self.menuRun.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuMode.menuAction())

        self.retranslateUi(PicDetectionMainWindow)
        QtCore.QMetaObject.connectSlotsByName(PicDetectionMainWindow)
        self.center()
    def retranslateUi(self, PicDetectionMainWindow):
        _translate = QtCore.QCoreApplication.translate
        PicDetectionMainWindow.setWindowTitle(_translate("PicDetectionMainWindow", "缺陷检测系统"))
        self.groupBox.setTitle(_translate("PicDetectionMainWindow", "检测图"))
        self.groupBox_2.setTitle(_translate("PicDetectionMainWindow", "检测结果"))
        self.label.setText(_translate("PicDetectionMainWindow", "缺陷类型"))
        self.toolBar.setWindowTitle(_translate("PicDetectionMainWindow", "toolBar"))
        self.menuRun.setTitle(_translate("PicDetectionMainWindow", "File"))
        self.menuSettings.setTitle(_translate("PicDetectionMainWindow", "Settings"))
        self.menuMode.setTitle(_translate("PicDetectionMainWindow", "Mode"))
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
        self.actionchange_mode.setText(_translate("PicDetectionMainWindow", "change mode"))
        self.actionmagentic_core.setText(_translate("PicDetectionMainWindow", "magentic_core"))
        self.actionpocket_mouth.setText(_translate("PicDetectionMainWindow", "pocket mouth"))
        self.actionimport.setText(_translate("PicDetectionMainWindow", "import"))
        self.actiondefault_mode.setText(_translate("PicDetectionMainWindow", "default mode"))
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)
