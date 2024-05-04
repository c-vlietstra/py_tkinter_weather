from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
import sys
from components.navigation_bar import NavigationBar

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("pyForecast")
        self.setGeometry(100, 100, 800, 600)  # x, y, width, height

        # Layout setup
        layout = QVBoxLayout(self)

        # Create and add the navigation bar to the layout
        nav_bar = NavigationBar
        layout.addWidget(nav_bar)


        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
