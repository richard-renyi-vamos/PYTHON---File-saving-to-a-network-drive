import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)

def select_destination():
    destination_path = filedialog.askdirectory()
    if destination_path:
        entry_destination_path.delete(0, tk.END)
        entry_destination_path.insert(0, destination_path)

def save_file():
    file_path = entry_file_path.get()
    destination_path = entry_destination_path.get()
    
    if not file_path or not destination_path:
        messagebox.showwarning("Input Error", "Please select both a file and a destination.")
        return
    
    try:
        # Construct the full path to the destination file
        file_name = os.path.basename(file_path)
        destination_file_path = os.path.join(destination_path, file_name)
        
        # Copy the file to the destination
        shutil.copy(file_path, destination_file_path)
        
        messagebox.showinfo("Success", f"File successfully saved to {destination_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save the file: {e}")

# Create the main window
root = tk.Tk()
root.title("Save File to Network Drive")

# Create and place the labels and entries
label_file_path = tk.Label(root, text="Select File:")
label_file_path.grid(row=0, column=0, padx=10, pady=10)

entry_file_path = tk.Entry(root, width=50)
entry_file_path.grid(row=0, column=1, padx=10, pady=10)

button_file_path = tk.Button(root, text="Browse", command=select_file)
button_file_path.grid(row=0, column=2, padx=10, pady=10)

label_destination_path = tk.Label(root, text="Select Destination:")
label_destination_path.grid(row=1, column=0, padx=10, pady=10)

entry_destination_path = tk.Entry(root, width=50)
entry_destination_path.grid(row=1, column=1, padx=10, pady=10)

button_destination_path = tk.Button(root, text="Browse", command=select_destination)
button_destination_path.grid(row=1, column=2, padx=10, pady=10)

button_save_file = tk.Button(root, text="Save File", command=save_file)
button_save_file.grid(row=2, column=1, padx=10, pady=20)

# Start the Tkinter event loop
root.mainloop()
