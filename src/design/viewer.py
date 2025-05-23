# Form implementation generated from reading ui file 'viewer.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ViewerForm(object):
    def setupUi(self, ViewerForm):
        ViewerForm.setObjectName("ViewerForm")
        ViewerForm.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=ViewerForm)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.cars_tab = QtWidgets.QWidget()
        self.cars_tab.setObjectName("cars_tab")
        self.tableView = QtWidgets.QTableView(parent=self.cars_tab)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 761, 371))
        self.tableView.setObjectName("tableView")
        self.groupBox = QtWidgets.QGroupBox(parent=self.cars_tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 390, 761, 161))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 261, 126))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.brand_combo_box = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.brand_combo_box.setObjectName("brand_combo_box")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.brand_combo_box)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.model_combo_box = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.model_combo_box.setObjectName("model_combo_box")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.model_combo_box)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.color_combo_box = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.color_combo_box.setObjectName("color_combo_box")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.color_combo_box)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.transmission_combo_box = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.transmission_combo_box.setObjectName("transmission_combo_box")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.transmission_combo_box)
        self.label_7 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.status_combo_box = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.status_combo_box.setObjectName("status_combo_box")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.status_combo_box)
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(320, 40, 311, 86))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.from_mileage_line_edit = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.from_mileage_line_edit.setObjectName("from_mileage_line_edit")
        self.gridLayout_2.addWidget(self.from_mileage_line_edit, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 2, 1, 1)
        self.to_mileage_line_edit = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.to_mileage_line_edit.setObjectName("to_mileage_line_edit")
        self.gridLayout_2.addWidget(self.to_mileage_line_edit, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 2)
        self.label_19 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 3, 0, 1, 1)
        self.from_year_line_edit = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.from_year_line_edit.setObjectName("from_year_line_edit")
        self.gridLayout_2.addWidget(self.from_year_line_edit, 3, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 3, 2, 1, 1)
        self.to_year_line_edit = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.to_year_line_edit.setObjectName("to_year_line_edit")
        self.gridLayout_2.addWidget(self.to_year_line_edit, 3, 3, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(parent=self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(660, 60, 77, 54))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.search_button = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.search_button.setObjectName("search_button")
        self.verticalLayout.addWidget(self.search_button)
        self.cancel_button = QtWidgets.QPushButton(parent=self.layoutWidget2)
        self.cancel_button.setObjectName("cancel_button")
        self.verticalLayout.addWidget(self.cancel_button)
        self.tabWidget.addTab(self.cars_tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        ViewerForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(ViewerForm)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ViewerForm)

    def retranslateUi(self, ViewerForm):
        _translate = QtCore.QCoreApplication.translate
        ViewerForm.setWindowTitle(_translate("ViewerForm", "Автосалон: панель зрителя"))
        self.groupBox.setTitle(_translate("ViewerForm", "Поиск:"))
        self.label.setText(_translate("ViewerForm", "Марка:"))
        self.label_2.setText(_translate("ViewerForm", "Модель:"))
        self.label_3.setText(_translate("ViewerForm", "Цвет:"))
        self.label_4.setText(_translate("ViewerForm", "Тип трансмиссии:"))
        self.label_7.setText(_translate("ViewerForm", "Статус:"))
        self.label_6.setText(_translate("ViewerForm", "Пробег:"))
        self.label_8.setText(_translate("ViewerForm", "от"))
        self.label_9.setText(_translate("ViewerForm", "до"))
        self.label_5.setText(_translate("ViewerForm", "Год выпуска:"))
        self.label_19.setText(_translate("ViewerForm", "от"))
        self.label_20.setText(_translate("ViewerForm", "до"))
        self.search_button.setText(_translate("ViewerForm", "Поиск"))
        self.cancel_button.setText(_translate("ViewerForm", "Отмена"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cars_tab), _translate("ViewerForm", "Автомобили"))
