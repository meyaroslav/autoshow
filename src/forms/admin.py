from PyQt6.QtWidgets import QMainWindow, QHeaderView, QMessageBox, QTableWidgetItem, QFileDialog
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6 import QtCore

from src.design.admin import Ui_AdminForm
from src.forms.add_car import AddCarForm
from src.forms.edit_car import EditCarForm
from src.forms.add_client import AddClientForm
from src.forms.edit_client import EditClientForm
from src.forms.add_sale import AddSaleForm
from src.logic.admin import cars_data
from src.logic.admin import clients_data
from src.logic.admin import sales_data
from src.logic.admin import users_data
from src.logic.admin import delete_car_by_vin
from src.logic.admin import get_car_by_vin
from src.logic.admin import get_all_filters
from src.logic.admin import filter_cars
from src.logic.admin import get_client_id
from src.logic.admin import filter_clients_universal
from src.logic.admin import filter_sales
from src.logic.admin import generate_sales_report

class AdminForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AdminForm()
        self.ui.setupUi(self)
        self.load_cars_data()
        self.load_clients_data()
        self.load_sales_data()
        self.load_users_data()
        self.load_combo_box()
        self.load_client_filter_combo_box()

        self.ui.add_button.clicked.connect(self.open_add_car_form)
        self.ui.delete_button.clicked.connect(self.delete_car)
        self.ui.edit_button.clicked.connect(self.open_edit_car_form)
        self.ui.add_button_2.clicked.connect(self.open_add_client_form)
        self.ui.edit_button_2.clicked.connect(self.open_edit_client_form)
        self.ui.delete_button_2.clicked.connect(self.delete_client)
        self.ui.search_button_3.clicked.connect(self.search_clients)
        self.ui.cancel_button_3.clicked.connect(self.clear_client_filters)
        self.ui.add_button_4.clicked.connect(self.open_add_sale_form)
        self.ui.search_button.clicked.connect(self.search_filters)
        self.ui.cancel_button.clicked.connect(self.clear_filters)
        self.ui.search_button_2.clicked.connect(self.search_sales_filters)
        self.ui.cancel_button_2.clicked.connect(self.clear_sales_filters)
        self.ui.report_button.clicked.connect(self.generate_report)

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
            for col_idx, value in enumerate(row_data):
                model.setItem(row_idx, col_idx, QStandardItem(str(value)))

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

    def open_edit_car_form(self):
        model = self.ui.tableView.model()
        selection_model = self.ui.tableView.selectionModel()
        selected_rows = selection_model.selectedRows()

        if not selected_rows:
            QMessageBox.warning(self, "Ошибка", "Выберите автомобиль для редактирования")
            return

        row = selected_rows[0].row()
        vin = model.item(row, 0).text()

        car_data = get_car_by_vin(vin)

        self.form = EditCarForm(car_data)
        self.form.car_updated.connect(self.load_cars_data)
        self.form.show()

    def load_combo_box(self):
        filters = get_all_filters()

        def fill_combo_box(combo_box, values):
            combo_box.clear()
            combo_box.addItem("")
            combo_box.addItems(values)

        fill_combo_box(self.ui.brand_combo_box, filters["brands"])
        fill_combo_box(self.ui.model_combo_box, filters["models"])
        fill_combo_box(self.ui.color_combo_box, filters["colors"])
        fill_combo_box(self.ui.transmission_combo_box, filters["transmissions"])
        fill_combo_box(self.ui.status_combo_box, filters["status"])

    def search_filters(self):
        brand = self.ui.brand_combo_box.currentText()
        model = self.ui.model_combo_box.currentText()
        color = self.ui.color_combo_box.currentText()
        transmission = self.ui.transmission_combo_box.currentText()
        status = self.ui.status_combo_box.currentText()
        mileage_min = self.ui.from_mileage_line_edit.text()
        mileage_max = self.ui.to_mileage_line_edit.text()
        year_min = self.ui.from_year_line_edit.text()
        year_max = self.ui.to_year_line_edit.text()

        filters = {
            "brand": brand if brand else None,
            "model": model if model else None,
            "color": color if color else None,
            "transmission": transmission if transmission else None,
            "status": status if status else None,
            "mileage_min": int(mileage_min) if mileage_min else None,
            "mileage_max": int(mileage_max) if mileage_max else None,
            "year_min": int(year_min) if year_min else None,
            "year_max": int(year_max) if year_max else None,
        }

        cars, col_names = filter_cars(filters)
        model = QStandardItemModel(len(cars), len(col_names))
        model.setHorizontalHeaderLabels(col_names)

        for row_idx, row_data in enumerate(cars):
            for col_idx, value in enumerate(row_data):
                model.setItem(row_idx, col_idx, QStandardItem(str(value)))

        self.ui.tableView.setModel(model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def clear_filters(self):
        self.ui.brand_combo_box.setCurrentIndex(-1)
        self.ui.model_combo_box.setCurrentIndex(-1)
        self.ui.color_combo_box.setCurrentIndex(-1)
        self.ui.transmission_combo_box.setCurrentIndex(-1)
        self.ui.status_combo_box.setCurrentIndex(-1)
        self.ui.from_mileage_line_edit.clear()
        self.ui.to_mileage_line_edit.clear()
        self.ui.from_year_line_edit.clear()
        self.ui.to_year_line_edit.clear()
        self.load_cars_data()

    def open_add_client_form(self):
        self.form = AddClientForm()
        self.form.client_added.connect(self.load_clients_data)
        self.form.show()

    def delete_client(self):
        model = self.ui.tableView_2.model()
        selection_model = self.ui.tableView_2.selectionModel()
        selected_rows = selection_model.selectedRows()

        if not selected_rows:
            QMessageBox.warning(self, "Ошибка", "Выберите клиента для удаления")
            return

        row = selected_rows[0].row()
        full_name = model.item(row, 0).text()

        reply = QMessageBox.question(
            self, "Подтверждение",
            f"Удалить клиента {full_name}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                from src.logic.admin import delete_client_by_full_name
                delete_client_by_full_name(full_name)
                QMessageBox.information(self, "Успех", "Клиент удален")
                self.load_clients_data()
            except Exception as e:
                QMessageBox.warning(self, "Ошибка", str(e))

    def open_edit_client_form(self):
        model = self.ui.tableView_2.model()
        selection_model = self.ui.tableView_2.selectionModel()
        selected_rows = selection_model.selectedRows()

        if not selected_rows:
            QMessageBox.warning(self, "Ошибка", "Выберите клиента для редактирования")
            return

        row = selected_rows[0].row()
        full_name = model.item(row, 0).text()
        phone = model.item(row, 1).text()
        email = model.item(row, 2).text()

        client_id = get_client_id(full_name, phone, email)

        self.form = EditClientForm(client_id, full_name, phone, email)
        self.form.client_updated.connect(self.load_clients_data)
        self.form.show()

    def search_clients(self):
        query = self.ui.client_line_edit.text().strip()

        if not query:
            QMessageBox.warning(self, "Ошибка", "Введите данные для поиска")
            return

        try:
            rows, columns = filter_clients_universal(query)
            model = QStandardItemModel(len(rows), len(columns))
            model.setHorizontalHeaderLabels(columns)

            for row_idx, row_data in enumerate(rows):
                for col_idx, value in enumerate(row_data):
                    model.setItem(row_idx, col_idx, QStandardItem(str(value)))

            self.ui.tableView_2.setModel(model)
            self.ui.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", str(e))

    def clear_client_filters(self):
        self.ui.client_line_edit.clear()
        self.load_clients_data()

    def open_add_sale_form(self):
        self.form = AddSaleForm()
        self.form.sale_added.connect(self.update_tables)
        self.form.show()

    def update_tables(self):
        self.load_cars_data()
        self.load_sales_data()

    def search_sales_filters(self):
        date_from = self.ui.from_date_edit.date().toString('yyyy-MM-dd')
        date_to = self.ui.to_date_edit.date().toString('yyyy-MM-dd')
        price_from = self.ui.from_sum_line_edit.text()
        price_to = self.ui.to_sum_line_edit.text()
        client = self.ui.client_combo_box.currentText()

        filters = {
            "date_from": date_from if date_from else None,
            "date_to": date_to if date_to else None,
            "price_from": float(price_from) if price_from else None,
            "price_to": float(price_to) if price_to else None,
            "client": client if client else None
        }

        try:
            rows, columns = filter_sales(filters)
            model = QStandardItemModel(len(rows), len(columns))
            model.setHorizontalHeaderLabels(columns)

            for row_idx, row_data in enumerate(rows):
                for col_idx, value in enumerate(row_data):
                    model.setItem(row_idx, col_idx, QStandardItem(str(value)))

            self.ui.tableView_3.setModel(model)
            self.ui.tableView_3.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", str(e))

    def load_client_filter_combo_box(self):
        from src.logic.add_sale import get_clients
        clients = get_clients()
        self.ui.client_combo_box.clear()
        self.ui.client_combo_box.addItem("")
        self.ui.client_combo_box.addItems([client[0] for client in clients])

    def clear_sales_filters(self):
        self.ui.from_date_edit.setDate(QtCore.QDate(2000, 1, 1))
        self.ui.to_date_edit.setDate(QtCore.QDate.currentDate())
        self.ui.from_sum_line_edit.clear()
        self.ui.to_sum_line_edit.clear()
        self.ui.client_combo_box.setCurrentIndex(-1)
        self.load_sales_data()

    def generate_report(self):
        filters = self.get_sales_filters()

        try:
            report_path = generate_sales_report(filters)
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", str(e))

    def get_sales_filters(self):
        date_from = self.ui.from_date_edit.date().toString('yyyy-MM-dd')
        date_to = self.ui.to_date_edit.date().toString('yyyy-MM-dd')
        price_from = self.ui.from_sum_line_edit.text()
        price_to = self.ui.to_sum_line_edit.text()
        client = self.ui.client_combo_box.currentText()

        filters = {
            "date_from": date_from if date_from else None,
            "date_to": date_to if date_to else None,
            "price_from": float(price_from) if price_from else None,
            "price_to": float(price_to) if price_to else None,
            "client": client if client else None
        }
        return filters