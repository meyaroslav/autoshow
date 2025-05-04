from PyQt6.QtWidgets import QWidget, QMessageBox
from src.design.add_car import Ui_AddCarForm
from src.logic.admin import insert_car, get_brands, get_models, get_colors, get_transmissions

class AddCarForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AddCarForm()
        self.ui.setupUi(self)

        self.load_combo_box()

        self.ui.save_button.clicked.connect(self.save_car)

    def load_combo_box(self):
        self.brand_map = self.fill_combo_box(self.ui.brand_combo_box, get_brands())
        self.model_map = self.fill_combo_box(self.ui.model_combo_box, get_models())
        self.color_map = self.fill_combo_box(self.ui.color_combo_box, get_colors())
        self.transmission_map = self.fill_combo_box(self.ui.transmission_combo_box, get_transmissions())

    def fill_combo_box(self, combo_box, data):
        id_map = {}
        combo_box.clear()
        for id_, name in data:
            combo_box.addItem(name)
            id_map[name] = id_
        return id_map

    def save_car(self):
        vin = self.ui.vin_line_edit.text()
        year = self.ui.year_line_edit.text()
        mileage = self.ui.mileage_line_edit.text()
        price = self.ui.price_line_edit.text()

        brand_id = self.brand_map[self.ui.brand_combo_box.currentText()]
        model_id = self.model_map[self.ui.model_combo_box.currentText()]
        color_id = self.color_map[self.ui.color_combo_box.currentText()]
        transmission_id = self.transmission_map[self.ui.transmission_combo_box.currentText()]

        try:
            insert_car(vin, brand_id, model_id, color_id, transmission_id, year, mileage, price)
            QMessageBox.information(self, "Успех", "Автомобиль успешно добавлен!")
            self.close()
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Не удалось добавить автомобиль:\n{e}")