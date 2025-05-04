from PyQt6.QtWidgets import QWidget, QMessageBox
from src.design.login import Ui_LoginForm
from src.logic.login import auth
from src.forms.admin import AdminForm

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)
        self.ui.login_button.clicked.connect(self.check_auth)

    def check_auth(self):
        login = self.ui.login_line_edit.text()
        password = self.ui.password_line_edit.text()
        success, role = auth(login, password)

        if success:
            QMessageBox.information(self, "Успешная авторизация", f"Добро пожаловать, {login}!")
            self.open_form(role)
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль.")

    def open_form(self, role):
        if role == "admin":
            self.form = AdminForm()
        else:
            QMessageBox.warning(self, "Ошибка", f"Неизвестная роль.")

        self.form.show()
        self.close()