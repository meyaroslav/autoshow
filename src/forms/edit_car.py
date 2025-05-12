from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import pyqtSignal

from src.design.edit_car import Ui_EditCarForm
from src.logic.admin import get_all_filters
from src.logic.admin import update_car

class EditCarForm(QWidget):
    car_updated = pyqtSignal()

    def __init__(self, car_data):
        super().__init__()
        self.ui = Ui_EditCarForm()
        self.ui.setupUi(self)

        self.load_combo_box()
        self.load_car_data(car_data)
        self.ui.save_button.clicked.connect(self.save_car)

    def load_combo_box(self):
        filters = get_all_filters()

        self.fill_combo_box(self.ui.brand_combo_box, filters["brands"])
        self.fill_combo_box(self.ui.model_combo_box, filters["models"])
        self.fill_combo_box(self.ui.color_combo_box, filters["colors"])
        self.fill_combo_box(self.ui.transmission_combo_box, filters["transmissions"])

    def fill_combo_box(self, combo_box, values):
        combo_box.clear()
        combo_box.addItem("")
        combo_box.addItems(values)

    def load_car_data(self, car_data):
        vin, brand, model, color, transmission, year, mileage, price, status = car_data

        self.ui.vin_line_edit.setText(vin)
        self.ui.brand_combo_box.setCurrentText(brand)
        self.ui.model_combo_box.setCurrentText(model)
        self.ui.color_combo_box.setCurrentText(color)
        self.ui.transmission_combo_box.setCurrentText(transmission)
        self.ui.year_line_edit.setText(str(year))
        self.ui.mileage_line_edit.setText(str(mileage))
        self.ui.price_line_edit.setText(str(price))

    def save_car(self):
        vin = self.ui.vin_line_edit.text()
        brand = self.ui.brand_combo_box.currentText()
        model = self.ui.model_combo_box.currentText()
        color = self.ui.color_combo_box.currentText()
        transmission = self.ui.transmission_combo_box.currentText()
        year = self.ui.year_line_edit.text()
        mileage = self.ui.mileage_line_edit.text()
        price = self.ui.price_line_edit.text()

        if not all([vin, brand, model, color, transmission, year, mileage, price]):
            QMessageBox.warning(self, "Ошибка", "Заполните все поля")
            return

        try:
            year = int(year)
            mileage = int(mileage)
            price = float(price)
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Год, пробег и цена должны быть числами")
            return

        try:
            update_car(vin, brand, model, color, transmission, year, mileage, price)
            QMessageBox.information(self, "Успех", "Автомобиль успешно обновлён")
            self.car_updated.emit()
            self.close()
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", str(e))