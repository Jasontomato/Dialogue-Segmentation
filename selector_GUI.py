import tkinter as tk
from tkinter import filedialog, Text
from tkinter.scrolledtext import ScrolledText

# Import the custom function from my_functions.py
from DealwithDialogue import convert_to_csv

# Variable to store the selected file path
selected_file_path = None

def select_file():
    global selected_file_path
    selected_file_path = filedialog.askopenfilename(
        title="Select a Text File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    
    if selected_file_path:
        try:
            with open(selected_file_path, 'r', encoding="utf-8") as file:
                file_content = file.read()
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, file_content)
            status_label.config(text=f"Selected File: {selected_file_path}")
        except UnicodeDecodeError:
            status_label.config(text="Error: Unable to read the file due to encoding issues.")

def convert_file():
    if selected_file_path:
        convert_to_csv(selected_file_path, "output.csv")
        status_label.config(text="Custom Conversion Complete!")

def main():
    global text_area, status_label
    # Create the main window
    root = tk.Tk()
    root.title("Dialogue segmentation")
    root.geometry("500x400")

    # Frame to hold the select and convert buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    # Select button
    select_button = tk.Button(button_frame, text="Select a .txt File", command=select_file)
    select_button.grid(row=0, column=0, padx=5)

    # Convert button
    convert_button = tk.Button(button_frame, text="Convert", command=convert_file)
    convert_button.grid(row=0, column=1, padx=5)

    # Status label to display the selected file path
    status_label = tk.Label(root, text="No file selected", fg="blue")
    status_label.pack()

    # Text area to display the contents of the selected file
    text_area = ScrolledText(root, wrap=tk.WORD, width=60, height=15)
    text_area.pack(pady=10)

    # Run the GUI event loop
    root.mainloop()

# Only run the main function if this script is executed directly
if __name__ == "__main__":
    main()
