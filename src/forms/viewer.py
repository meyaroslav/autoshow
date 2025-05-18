from PyQt6.QtWidgets import QMainWindow

from src.design.viewer import Ui_ViewerForm

class ViewerForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ViewerForm()
        self.ui.setupUi(self)