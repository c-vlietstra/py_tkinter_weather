from PyQt6.QtWidgets import QVBoxLayout, QWidget, QPushButton
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon

class NavigationBar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()

        # Adjust layout spacing and alignment
        layout.setSpacing(10)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # List of icons for the buttons
        icons = ['home', 'search', 'calendar', 'bell', 'gear']

        for icon_name in icons:
            button = QPushButton()
            button.setIcon(QIcon(f'icons/{icon_name}.png'))  # Ensure you have these icons in the specified directory
            button.setIconSize(QSize(40, 40))  # Icon size
            button.setFixedSize(60, 60)  # Button size
            button.setStyleSheet("QPushButton { border: none; }")
            layout.addWidget(button)

        self.setLayout(layout)
        self.setStyleSheet("background-color: black;")  # Set background color of the navigation bar

# Usage in your main application, assuming your project structure allows for this import
# from components.navigation import NavigationBar
