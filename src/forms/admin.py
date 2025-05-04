from PyQt6.QtWidgets import QMainWindow, QHeaderView, QMessageBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem

from src.design.admin import Ui_AdminForm
from src.forms.add_car import AddCarForm
from src.logic.admin import cars_data
from src.logic.admin import clients_data
from src.logic.admin import sales_data
from src.logic.admin import users_data
from src.logic.admin import delete_car_by_vin

class AdminForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AdminForm()
        self.ui.setupUi(self)
        self.load_cars_data()
        self.load_clients_data()
        self.load_sales_data()
        self.load_users_data()

        self.ui.add_button.clicked.connect(self.open_add_car_form)
        self.ui.delete_button.clicked.connect(self.delete_car)

    def load_cars_data(self):
        cars, col_names = cars_data()

        model = QStandardItemModel(len(cars), len(col_names))
        model.setHorizontalHeaderLabels(col_names)

        for row_idx, row_data in enumerate(cars):
            for col_idx, value in enumerate(row_data):
                model.setItem(row_idx, col_idx, QStandardItem(str(value)))

        self.ui.tableView.setModel(model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def load_clients_data(self):
        clients, col_names = clients_data()

        model = QStandardItemModel(len(clients), len(col_names))
        model.setHorizontalHeaderLabels(col_names)

        for row_idx, row_data in enumerate(clients):
            for col_idx, value in enumerate(row_data):
                model.setItem(row_idx, col_idx, QStandardItem(str(value)))

        self.ui.tableView_2.setModel(model)
        self.ui.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def load_sales_data(self):
        sales, col_names = sales_data()

        model = QStandardItemModel(len(sales), len(col_names))
        model.setHorizontalHeaderLabels(col_names)

        for row_idx, row_data in enumerate(sales):
            for col_inx, value in enumerate(row_data):
                model.setItem(row_idx, col_inx, QStandardItem(str(value)))

        self.ui.tableView_3.setModel(model)
        self.ui.tableView_3.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def load_users_data(self):
        users, col_names = users_data()

        model = QStandardItemModel(len(users), len(col_names))
        model.setHorizontalHeaderLabels(col_names)

        for row_idx, row_data in enumerate(users):
            for col_inx, value in enumerate(row_data):
                model.setItem(row_idx, col_inx, QStandardItem(str(value)))

        self.ui.tableView_4.setModel(model)
        self.ui.tableView_4.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def open_add_car_form(self):
        self.form = AddCarForm()
        self.form.car_added.connect(self.load_cars_data)
        self.form.show()

    def delete_car(self):
        model = self.ui.tableView.model()
        selection_model = self.ui.tableView.selectionModel()
        selected_rows = selection_model.selectedRows()

        if not selected_rows:
            QMessageBox.warning(self, "Ошибка", "Выберите автомобиль для удаления")
            return

        row = selected_rows[0].row()
        vin = model.item(row, 0).text()

        reply = QMessageBox.question(self, "Подтверждение", f"Удалить автомобиль с VIN {vin}?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            try:
                delete_car_by_vin(vin)
                QMessageBox.information(self, "Успех", "Автомобиль удалён")
                self.load_cars_data()
            except Exception as e:
                QMessageBox.warning(self, "Ошибка", str(e))