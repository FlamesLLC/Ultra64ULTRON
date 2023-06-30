import tkinter as tk
from tkinter import filedialog

class PSBinFile:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read(self):
        with open(self.file_path, 'rb') as f:
            data = f.read()
        return data
    
    def write(self, data):
        with open(self.file_path, 'wb') as f:
            f.write(data)

def browse_file():
    filepath = filedialog.askopenfilename(initialdir="/", title="Select .bin File")
    
    if filepath.endswith(".bin"):
        
        # Create PSBinFile instance for the selected file
        bin_file = PSBinFile(filepath)
        
        # Read from the .bin file
        content_text.delete('1.0', tk.END)  # Clear current text in Text widget
        content_text.insert(tk.END, bin_file.read())
    
def save_changes():
    filepath = filedialog.asksaveasfilename(defaultextension=".bin", initialfile="modified.bin")
    
    if filepath.endswith(".bin"):
        
         # Create PSBinFile instance for the selected or entered path/file name 
         modified_bin_file = PSBinFile(filepath)
         
         # Write changes to the modified .bin file 
         modified_bin_file.write(content_text.get('1.0', tk.END))
  
# Create main application window using Tkinter
window = tk.Tk()
window.title("SM64 ROM Manager")
window.geometry("500x300")

# Browse button to select .bin file  
browse_button = tk.Button(window,text="Browse",command=browse_file)
browse_button.pack()

# Display area for displaying/editing the content of .bin file  
content_text = tk.Text(window, height=10, width=50)
content_text.pack()

# Save button to save the changes made 
save_button = tk.Button(window,text="Save Changes",command=save_changes)
save_button.pack()

window.mainloop()