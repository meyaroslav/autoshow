from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import pyqtSignal

from src.design.add_sale import Ui_AddSaleForm
from src.logic.add_sale import add_sale, get_car_price, get_clients, get_available_cars

class AddSaleForm(QWidget):
    sale_added = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_AddSaleForm()
        self.ui.setupUi(self)

        self.load_combo_box()
        self.ui.add_button.clicked.connect(self.add_sale)

    def load_combo_box(self):
        clients = get_clients()
        self.ui.cleint_combo_box.clear()
        self.ui.cleint_combo_box.addItem("")  # Пустой элемент
        self.ui.cleint_combo_box.addItems([client[0] for client in clients])

        cars = get_available_cars()
        self.ui.car_combo_box.clear()
        self.ui.car_combo_box.addItem("")  # Пустой элемент
        self.ui.car_combo_box.addItems([car[0] for car in cars])

        self.car_vins = {car[0]: car[1] for car in cars}

        # Устанавливаем текущий индекс на пустой
        self.ui.cleint_combo_box.setCurrentIndex(0)
        self.ui.car_combo_box.setCurrentIndex(0)

    def add_sale(self):
        client_name = self.ui.cleint_combo_box.currentText()
        car_info = self.ui.car_combo_box.currentText()
        sale_date = self.ui.date_edit.date().toString('yyyy-MM-dd')

        if not all([client_name, car_info]):
            QMessageBox.warning(self, "Ошибка", "Заполните все поля")
            return

        car_vin = self.car_vins.get(car_info)

        try:
            price = get_car_price(car_vin)
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", str(e))
            return

        try:
            add_sale(client_name, car_vin, sale_date, price)
            QMessageBox.information(self, "Успех", "Сделка успешно добавлена")
            self.sale_added.emit()
            self.close()
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", str(e))