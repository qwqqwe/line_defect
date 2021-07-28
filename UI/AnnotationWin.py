# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnnotationWin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PaintLabel import PaintLabel

class Ui_Annotation(object):
    def setupUi(self, Annotation):
        Annotation.setObjectName("Annotation")
        Annotation.resize(1012, 728)
        font = QtGui.QFont()
        font.setPointSize(9)
        Annotation.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Annotation)
        self.centralwidget.setObjectName("centralwidget")
        self.img_label =PaintLabel(self.centralwidget)
        self.img_label.setGeometry(QtCore.QRect(10, 140, 656, 480))
        self.img_label.setText("")
        self.img_label.setObjectName("img_label")
        self.info = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.info.setFont(font)
        self.info.setGeometry(QtCore.QRect(700, 70, 301, 241))
        self.info.setObjectName("info")
        self.object_info = QtWidgets.QLabel(self.centralwidget)
        self.object_info.setGeometry(QtCore.QRect(700, 35, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.object_info.setFont(font)
        self.object_info.setObjectName("object_info")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(920, 620, 71, 41))
        self.add_button.setObjectName("add_button")
        self.label_input = QtWidgets.QLineEdit(self.centralwidget)
        self.label_input.setGeometry(QtCore.QRect(700, 620, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_input.setFont(font)
        self.label_input.setObjectName("label_input")
        self.label_list = QtWidgets.QListWidget(self.centralwidget)
        self.label_list.setGeometry(QtCore.QRect(700, 370, 291, 231))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_list.setFont(font)
        self.label_list.setObjectName("label_list")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 30, 641, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.open = QtWidgets.QPushButton(self.widget)
        self.open.setObjectName("open")
        self.horizontalLayout.addWidget(self.open)
        self.openDir = QtWidgets.QPushButton(self.widget)
        self.openDir.setObjectName("openDir")
        self.horizontalLayout.addWidget(self.openDir)
        self.previous = QtWidgets.QPushButton(self.widget)
        self.previous.setObjectName("previous")
        self.horizontalLayout.addWidget(self.previous)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.show_label = QtWidgets.QLabel(self.widget)
        self.show_label.setFont(font)
        self.show_label.setText("")
        self.show_label.setObjectName("show_label")
        self.horizontalLayout.addWidget(self.show_label)
        self.next = QtWidgets.QPushButton(self.widget)
        self.next.setObjectName("next")
        self.horizontalLayout.addWidget(self.next)
        self.save = QtWidgets.QPushButton(self.widget)
        self.save.setObjectName("save")
        self.horizontalLayout.addWidget(self.save)
        Annotation.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Annotation)
        self.statusbar.setObjectName("statusbar")
        Annotation.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(Annotation)
        self.toolBar.setObjectName("toolBar")
        Annotation.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionDetection = QtWidgets.QAction(Annotation)
        self.actionDetection.setObjectName("actionDetection")
        self.actionTrain = QtWidgets.QAction(Annotation)
        self.actionTrain.setObjectName("actionTrain")
        self.actionMark = QtWidgets.QAction(Annotation)
        self.actionMark.setObjectName("actionMark")
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDetection)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTrain)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionMark)
        self.toolBar.addSeparator()

        self.retranslateUi(Annotation)
        QtCore.QMetaObject.connectSlotsByName(Annotation)

    def retranslateUi(self, Annotation):
        _translate = QtCore.QCoreApplication.translate
        Annotation.setWindowTitle(_translate("Annotation", "MainWindow"))
        self.object_info.setText(_translate("Annotation", "Object Infomation"))
        self.add_button.setText(_translate("Annotation", "add"))
        self.label_input.setText(_translate("Annotation", "xxxx"))
        self.open.setText(_translate("Annotation", "Open"))
        self.openDir.setText(_translate("Annotation", "Open Dir"))
        self.previous.setText(_translate("Annotation", "<--Previous"))
        self.next.setText(_translate("Annotation", "Next-->"))
        self.save.setText(_translate("Annotation", "Save"))
        self.toolBar.setWindowTitle(_translate("Annotation", "toolBar"))
        self.actionDetection.setText(_translate("Annotation", "检测模式"))
        self.actionDetection.setToolTip(_translate("Annotation", "检测模式"))
        self.actionDetection.setShortcut(_translate("Annotation", "Ctrl+D"))
        self.actionTrain.setText(_translate("Annotation", "训练模式"))
        self.actionTrain.setToolTip(_translate("Annotation", "训练模式"))
        self.actionTrain.setShortcut(_translate("Annotation", "Ctrl+T"))
        self.actionMark.setText(_translate("Annotation", "标注模式"))
        self.actionMark.setToolTip(_translate("Annotation", "标注图片"))
        self.actionMark.setShortcut(_translate("Annotation", "Ctrl+M"))

