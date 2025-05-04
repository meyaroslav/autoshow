import sys
from PyQt6.QtWidgets import QApplication
from src.forms.login import LoginForm

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_form = LoginForm()
    login_form.show()
    sys.exit(app.exec())