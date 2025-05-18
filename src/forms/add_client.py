from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import pyqtSignal

from src.design.add_client import Ui_AddClientForm
from src.logic.add_client import add_client

class AddClientForm(QWidget):
    client_added = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_AddClientForm()
        self.ui.setupUi(self)

        self.ui.save_button.clicked.connect(self.save_client)

    def save_client(self):
        full_name = self.ui.full_name_line_edit.text()
        phone = self.ui.phone_line_edit.text()
        email = self.ui.email_line_edit.text()

        if not all([full_name, phone, email]):
            QMessageBox.warning(self, "Ошибка", "Заполните все поля")
            return

        try:
            add_client(full_name, phone, email)
            QMessageBox.information(self, "Успех", "Клиент добавлен")
            self.client_added.emit()
            self.close()
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", str(e))