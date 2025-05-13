from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import pyqtSignal

from src.design.add_car import Ui_AddCarForm
from src.logic.add_car import add_car
from src.logic.add_car import get_all_brands
from src.logic.add_car import get_all_models
from src.logic.add_car import get_all_colors
from src.logic.add_car import get_all_transmissions
from src.logic.add_car import get_models_for_brand

class AddCarForm(QWidget):
    car_added = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_AddCarForm()
        self.ui.setupUi(self)

        self.load_combo_box()
        self.ui.save_button.clicked.connect(self.save_car)

        self.clear_form()
        self.ui.brand_combo_box.currentTextChanged.connect(self.update_models)

    def load_combo_box(self):
        brands = get_all_brands()
        self.ui.brand_combo_box.addItems(brands)

        models = get_all_models()
        self.ui.model_combo_box.addItems(models)

        colors = get_all_colors()
        self.ui.color_combo_box.addItems(colors)

        transmissions = get_all_transmissions()
        self.ui.transmission_combo_box.addItems(transmissions)

    def update_models(self):
        brand = self.ui.brand_combo_box.currentText()

        if not brand:
            return

        models = get_models_for_brand(brand)

        self.ui.model_combo_box.clear()
        self.ui.model_combo_box.addItem("")
        self.ui.model_combo_box.addItems(models)

    def clear_form(self):
        self.ui.vin_line_edit.clear()
        self.ui.brand_combo_box.setCurrentIndex(-1)
        self.ui.model_combo_box.clear()
        self.ui.color_combo_box.setCurrentIndex(-1)
        self.ui.transmission_combo_box.setCurrentIndex(-1)
        self.ui.year_line_edit.clear()
        self.ui.mileage_line_edit.clear()
        self.ui.price_line_edit.clear()

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
            add_car(vin, brand, model, color, transmission, year, mileage, price)
            QMessageBox.information(self, "Успех", "Автомобиль успешно добавлен")
            self.car_added.emit()
            self.clear_form()
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", str(e))