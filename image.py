import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.geometry("600x400")
        self.root.config(bg="pink")  # Set background color to pink

        # Add first static image (logo1.png) at the top
        try:
            self.logo1_image = Image.open(r"C:\Users\ADMIN\Desktop\cyber intern\logo.png")  # Replace with the path of your logo1 image
            self.logo1_image = self.logo1_image.resize((200, 100), Image.Resampling.LANCZOS)  # Resize to fit
            self.logo1_photo = ImageTk.PhotoImage(self.logo1_image)
            
            self.logo1_label = tk.Label(self.root, image=self.logo1_photo, bg="lightblue")
            self.logo1_label.pack(pady=10)  # Add some padding for the first logo
        except FileNotFoundError:
            print("logo.png not found. Please check the file path.")
            self.logo1_photo = None  # In case the logo image is not available

        # Add second static image (logo2.png) at the top
        try:
            self.logo2_image = Image.open(r"C:\Users\ADMIN\Desktop\cyber intern\logo1.png")  # Replace with your second image
            self.logo2_image = self.logo2_image.resize((200, 100), Image.Resampling.LANCZOS)  # Resize to fit
            self.logo2_photo = ImageTk.PhotoImage(self.logo2_image)
            
            self.logo2_label = tk.Label(self.root, image=self.logo2_photo, bg="lightblue")
            self.logo2_label.pack(pady=10)  # Add some padding for the second logo
        except FileNotFoundError:
            print("secondary_logo.png not found. Please check the file path.")
            self.logo2_photo = None  # In case the second logo image is not available

        # Initialize the image label for dynamic images
        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        self.current_image_index = 0
        self.image_paths = []

        # Button customizations with pink color scheme
        self.load_images_button = tk.Button(self.root, text="Open Folder", command=self.open_folder, bg="dodgerblue", font=("Helvetica", 12), relief="raised", bd=4)
        self.load_images_button.pack()

        self.previous_button = tk.Button(self.root, text="Previous", command=self.show_previous_image, bg="yellow", font=("Helvetica", 12), relief="raised", bd=4)
        self.previous_button.pack(side="left", padx=10)

        self.next_button = tk.Button(self.root, text="Next", command=self.show_next_image, bg="green", font=("Helvetica", 12), relief="raised", bd=4)
        self.next_button.pack(side="right", padx=10)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_app, bg="red", font=("Helvetica", 12), relief="raised", bd=4)
        self.exit_button.pack(side="bottom", pady=10)

    def open_folder(self):
        # Open a folder dialog to select a folder of images
        folder_path = filedialog.askdirectory()
        if folder_path:
            # Get all images in the selected folder
            self.image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path)
                                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            
            # Check if any image files are found
            if self.image_paths:
                self.current_image_index = 0
                self.show_image(self.image_paths[self.current_image_index])
            else:
                print("No image files found in the selected folder.")
    
    def show_image(self, image_path):
        # Load and display the image
        image = Image.open(image_path)
        image = image.resize((600, 400), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        self.image_label.config(image=photo)
        self.image_label.image = photo  # Keep a reference to the photo

    def show_next_image(self):
        if not self.image_paths:
            return
        
        # Show the first image from the folder only after the first click
        if self.current_image_index == 0:
            self.logo1_label.pack_forget()  # Remove logo1 after first image is displayed

        # Update index and cycle images
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        self.show_image(self.image_paths[self.current_image_index])

    def show_previous_image(self):
        if self.image_paths:
            # Update index and cycle images backwards
            self.current_image_index = (self.current_image_index - 1) % len(self.image_paths)
            self.show_image(self.image_paths[self.current_image_index])

    def exit_app(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    viewer = ImageViewer(root)
    root.mainloop()
