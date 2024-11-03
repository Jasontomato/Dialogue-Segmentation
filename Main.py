# main.py
import sys
from PySide6.QtWidgets import QApplication
from ui_components import DialogueSegmentationApp

def main():
    app = QApplication(sys.argv)
    window = DialogueSegmentationApp()
    window.setGeometry(200, 200, 500, 500)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
