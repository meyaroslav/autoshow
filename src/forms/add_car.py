from PyQt6.QtWidgets import QWidget
from src.design.add_car import Ui_AddCarForm

class AddCarForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AddCarForm()
        self.ui.setupUi(self)