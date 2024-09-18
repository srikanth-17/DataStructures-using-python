import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette

class HighlightButtonApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Layout
        layout = QVBoxLayout()

        # Create Buttons
        self.button1 = QPushButton('Button 1', self)
        self.button2 = QPushButton('Button 2', self)

        # Add buttons to the layout
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        # Connect buttons to the highlight function
        self.button1.clicked.connect(lambda: self.highlightButton(self.button1))
        self.button2.clicked.connect(lambda: self.highlightButton(self.button2))

        # Set the layout
        self.setLayout(layout)

        # Window settings
        self.setWindowTitle('Highlight Button Example')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def highlightButton(self, button):
        # Reset the styles of both buttons
        self.button1.setStyleSheet("")
        self.button2.setStyleSheet("")

        # Highlight the clicked button
        button.setStyleSheet("background-color: lightblue")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HighlightButtonApp()
    sys.exit(app.exec_())
