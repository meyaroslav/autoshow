from PyQt6.QtWidgets import QMainWindow, QHeaderView, QMessageBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from src.database.connection import db_connection
from src.design.admin import Ui_AdminForm
from src.logic.admin import cars_data
from src.logic.admin import clients_data
from src.logic.admin import sales_data
from src.logic.admin import users_data
from src.forms.add_car import AddCarForm

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
        self.add_car_form = AddCarForm()
        self.add_car_form.show()

    def refresh_cars_data(self):
        cars, col_names = cars_data()

        model = QStandardItemModel(len(cars), len(col_names))
        model.setHorizontalHeaderLabels(col_names)

        for row_idx, row_data in enumerate(cars):
            for col_idx, value in enumerate(row_data):
                model.setItem(row_idx, col_idx, QStandardItem(str(value)))

        self.ui.tableView.setModel(model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def delete_car(self):
        selected_row = self.ui.tableView.selectedIndexes()

        if not selected_row:
            QMessageBox.warning(self, "Ошибка", "Выберите автомобиль для удаления!")
            return

        selected_vin = self.ui.tableView.model().item(selected_row[0].row(), 0).text()

        try:
            self.remove_car_from_db(selected_vin)
            self.refresh_cars_data()
            QMessageBox.information(self, "Успех", f"Автомобиль с VIN {selected_vin} успешно удалён!")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось удалить автомобиль:\n{e}")

    def remove_car_from_db(self, vin):
        conn = db_connection()
        cur = conn.cursor()

        cur.execute("DELETE FROM cars WHERE vin = %s", (vin,))
        conn.commit()

        cur.close()
        conn.close()