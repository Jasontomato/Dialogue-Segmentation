import os
import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QFileDialog, QMessageBox, QLineEdit, QHBoxLayout
from PySide6.QtGui import QTextCursor
from converter import convert_to_csv

class DialogueSegmentationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialogue Segmentation")
        self.setGeometry(100, 100, 600, 500)
        
        # Set up the main layout
        layout = QVBoxLayout(self)
        
        # Select file button
        self.select_button = QPushButton("Select a .txt File")
        self.select_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_button)
        
        # Create a horizontal layout for the file name input and convert button
        file_name_layout = QHBoxLayout()
        
        # File name input field
        self.file_name_input = QLineEdit()
        self.file_name_input.setPlaceholderText("Enter output file name")
        file_name_layout.addWidget(self.file_name_input)
        
        # Convert button
        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert_file)
        file_name_layout.addWidget(self.convert_button)
        
        # Add the horizontal layout to the main layout
        layout.addLayout(file_name_layout)
        
        # Status label
        self.status_label = QLabel("No file selected")
        layout.addWidget(self.status_label)
        
        # Text area for displaying file content
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        layout.addWidget(self.text_area)
        
        # Variable to store selected file path
        self.selected_file_path = None

    def select_file(self):
        file_dialog = QFileDialog(self)
        self.selected_file_path, _ = file_dialog.getOpenFileName(
            self, "Select a Text File", "", "Text Files (*.txt);;All Files (*.*)"
        )
        
        if self.selected_file_path:
            try:
                with open(self.selected_file_path, 'r', encoding="utf-8") as file:
                    file_content = file.read()
                    self.text_area.clear()
                    self.text_area.insertPlainText(file_content)
                    self.text_area.moveCursor(QTextCursor.Start)
                self.status_label.setText(f"Selected File: {self.selected_file_path}")
            except UnicodeDecodeError:
                self.status_label.setText("Error: Unable to read the file due to encoding issues.")
                QMessageBox.critical(self, "Error", "Unable to read the file due to encoding issues.")

    def convert_file(self):
        if self.selected_file_path:
            # Get the user-defined file name or use a default name if none is provided
            user_file_name = self.file_name_input.text().strip()
            if not user_file_name:
                user_file_name = "output.csv"  # Default file name if input is empty
            else:
                # Ensure the file name ends with ".csv"
                if not user_file_name.endswith(".csv"):
                    user_file_name += ".csv"
            
            # Construct the full path in the Downloads directory
            downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
            output_file_path = os.path.join(downloads_dir, user_file_name)
            
            try:
                convert_to_csv(self.selected_file_path, output_file_path)
                self.status_label.setText(f"Conversion Complete! Saved to: {output_file_path}")
            except Exception as e:
                self.status_label.setText("Conversion failed.")
                QMessageBox.critical(self, "Conversion Error", str(e))
