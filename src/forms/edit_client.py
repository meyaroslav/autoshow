from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtCore import pyqtSignal

from src.design.edit_client import Ui_EditClientForm
from src.logic.edit_client import update_client

class EditClientForm(QWidget):
    client_updated = pyqtSignal()

    def __init__(self, client_id, full_name, phone, email):
        super().__init__()
        self.ui = Ui_EditClientForm()
        self.ui.setupUi(self)

        self.client_id = client_id
        self.ui.full_name_line_edit.setText(full_name)
        self.ui.phone_line_edit.setText(phone)
        self.ui.email_line_edit.setText(email)

        self.ui.save_button.clicked.connect(self.save_client)

    def save_client(self):
        full_name = self.ui.full_name_line_edit.text()
        phone = self.ui.phone_line_edit.text()
        email = self.ui.email_line_edit.text()

        if not all([full_name, phone, email]):
            QMessageBox.warning(self, "Ошибка", "Заполните все поля")
            return

        try:
            update_client(self.client_id, full_name, phone, email)
            QMessageBox.information(self, "Успех", "Клиент обновлен")
            self.client_updated.emit()
            self.close()
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", str(e))
