import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import qrcode
import cv2
import numpy as np
import urllib.parse
import os
import threading
from PIL import Image, ImageTk
import io


class QRCodeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator & Scanner")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')

        # Variables
        self.qr_image = None
        self.camera_running = False
        self.cap = None

        # Create the main interface
        self.create_widgets()

    def create_widgets(self):
        """Create all GUI widgets."""

        # Main title
        title_label = tk.Label(
            self.root,
            text="QR Code Generator & Scanner",
            font=('Arial', 18, 'bold'),
            bg='#f0f0f0',
            fg='#333333'
        )
        title_label.pack(pady=10)

        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=5)

        # Create tabs
        self.create_generator_tab()
        self.create_scanner_tab()
        self.create_camera_tab()

    def create_generator_tab(self):
        """Create the QR code generator tab."""

        # Generator frame
        gen_frame = ttk.Frame(self.notebook)
        self.notebook.add(gen_frame, text="Generate QR Code")

        # URL input section
        url_frame = tk.Frame(gen_frame, bg='white', relief='groove', bd=2)
        url_frame.pack(fill='x', padx=10, pady=10)

        tk.Label(
            url_frame,
            text="Enter URL to encode:",
            font=('Arial', 12, 'bold'),
            bg='white'
        ).pack(anchor='w', padx=10, pady=(10, 5))

        self.url_entry = tk.Entry(
            url_frame,
            font=('Arial', 11),
            width=60,
            relief='solid',
            bd=1
        )
        self.url_entry.pack(fill='x', padx=10, pady=(0, 10))

        # Settings section
        settings_frame = tk.Frame(gen_frame, bg='white', relief='groove', bd=2)
        settings_frame.pack(fill='x', padx=10, pady=5)

        tk.Label(
            settings_frame,
            text="Settings:",
            font=('Arial', 12, 'bold'),
            bg='white'
        ).pack(anchor='w', padx=10, pady=(10, 5))

        # Format selection
        format_frame = tk.Frame(settings_frame, bg='white')
        format_frame.pack(fill='x', padx=10, pady=5)

        tk.Label(format_frame, text="Format:", bg='white', font=('Arial', 10)).pack(side='left')
        self.format_var = tk.StringVar(value="PNG")
        format_combo = ttk.Combobox(
            format_frame,
            textvariable=self.format_var,
            values=["PNG", "JPEG"],
            state="readonly",
            width=10
        )
        format_combo.pack(side='left', padx=(5, 0))

        # Size selection
        size_frame = tk.Frame(settings_frame, bg='white')
        size_frame.pack(fill='x', padx=10, pady=5)

        tk.Label(size_frame, text="Size:", bg='white', font=('Arial', 10)).pack(side='left')
        self.size_var = tk.StringVar(value="Medium")
        size_combo = ttk.Combobox(
            size_frame,
            textvariable=self.size_var,
            values=["Small", "Medium", "Large"],
            state="readonly",
            width=10
        )
        size_combo.pack(side='left', padx=(5, 0))

        # Filename input
        filename_frame = tk.Frame(settings_frame, bg='white')
        filename_frame.pack(fill='x', padx=10, pady=5)

        tk.Label(filename_frame, text="Filename:", bg='white', font=('Arial', 10)).pack(side='left')
        self.filename_entry = tk.Entry(filename_frame, font=('Arial', 10), width=25)
        self.filename_entry.pack(side='left', padx=(5, 0))
        self.filename_entry.insert(0, "qrcode")

        # Save location
        location_frame = tk.Frame(settings_frame, bg='white')
        location_frame.pack(fill='x', padx=10, pady=(5, 10))

        tk.Label(location_frame, text="Save to:", bg='white', font=('Arial', 10)).pack(side='left')
        self.save_path_var = tk.StringVar(value="Current Directory")
        self.save_path_label = tk.Label(
            location_frame,
            textvariable=self.save_path_var,
            bg='white',
            font=('Arial', 9),
            fg='#666666'
        )
        self.save_path_label.pack(side='left', padx=(5, 0))

        browse_btn = tk.Button(
            location_frame,
            text="Browse",
            command=self.browse_save_location,
            bg='#4CAF50',
            fg='white',
            font=('Arial', 9),
            relief='flat',
            padx=10
        )
        browse_btn.pack(side='right', padx=(0, 10))

        # Generate button
        generate_btn = tk.Button(
            gen_frame,
            text="Generate QR Code",
            command=self.generate_qr_code,
            bg='#2196F3',
            fg='white',
            font=('Arial', 12, 'bold'),
            relief='flat',
            padx=20,
            pady=10
        )
        generate_btn.pack(pady=10)

        # Preview section
        preview_frame = tk.Frame(gen_frame, bg='white', relief='groove', bd=2)
        preview_frame.pack(fill='both', expand=True, padx=10, pady=(5, 10))

        tk.Label(
            preview_frame,
            text="Preview:",
            font=('Arial', 12, 'bold'),
            bg='white'
        ).pack(anchor='w', padx=10, pady=(10, 5))

        self.preview_label = tk.Label(
            preview_frame,
            text="QR code will appear here",
            bg='white',
            fg='#999999',
            font=('Arial', 10)
        )
        self.preview_label.pack(expand=True, pady=20)

    def create_scanner_tab(self):
        """Create the QR code scanner tab."""

        scanner_frame = ttk.Frame(self.notebook)
        self.notebook.add(scanner_frame, text="Scan from File")

        # Instructions
        instructions = tk.Label(
            scanner_frame,
            text="Select an image file containing a QR code to decode",
            font=('Arial', 12),
            bg='#f0f0f0',
            fg='#666666'
        )
        instructions.pack(pady=20)

        # Upload button
        upload_btn = tk.Button(
            scanner_frame,
            text="Select Image File",
            command=self.select_image_file,
            bg='#FF9800',
            fg='white',
            font=('Arial', 12, 'bold'),
            relief='flat',
            padx=20,
            pady=10
        )
        upload_btn.pack(pady=10)

        # Results section
        results_frame = tk.Frame(scanner_frame, bg='white', relief='groove', bd=2)
        results_frame.pack(fill='both', expand=True, padx=10, pady=10)

        tk.Label(
            results_frame,
            text="Scan Results:",
            font=('Arial', 12, 'bold'),
            bg='white'
        ).pack(anchor='w', padx=10, pady=(10, 5))

        self.scan_results = scrolledtext.ScrolledText(
            results_frame,
            height=8,
            font=('Arial', 10),
            wrap=tk.WORD
        )
        self.scan_results.pack(fill='both', expand=True, padx=10, pady=(0, 10))

        # Image preview for scanned file
        self.scan_preview_label = tk.Label(
            results_frame,
            text="Selected image will appear here",
            bg='white',
            fg='#999999'
        )
        self.scan_preview_label.pack(pady=10)

    def create_camera_tab(self):
        """Create the camera scanner tab."""

        camera_frame = ttk.Frame(self.notebook)
        self.notebook.add(camera_frame, text="Camera Scanner")

        # Instructions
        instructions = tk.Label(
            camera_frame,
            text="Use your camera to scan QR codes in real-time",
            font=('Arial', 12),
            bg='#f0f0f0',
            fg='#666666'
        )
        instructions.pack(pady=10)

        # Camera controls
        controls_frame = tk.Frame(camera_frame, bg='#f0f0f0')
        controls_frame.pack(pady=10)

        self.start_camera_btn = tk.Button(
            controls_frame,
            text="Start Camera",
            command=self.start_camera,
            bg='#4CAF50',
            fg='white',
            font=('Arial', 11, 'bold'),
            relief='flat',
            padx=15,
            pady=8
        )
        self.start_camera_btn.pack(side='left', padx=5)

        self.stop_camera_btn = tk.Button(
            controls_frame,
            text="Stop Camera",
            command=self.stop_camera,
            bg='#f44336',
            fg='white',
            font=('Arial', 11, 'bold'),
            relief='flat',
            padx=15,
            pady=8,
            state='disabled'
        )
        self.stop_camera_btn.pack(side='left', padx=5)

        # Camera feed
        self.camera_label = tk.Label(
            camera_frame,
            text="Camera feed will appear here\nClick 'Start Camera' to begin",
            bg='#333333',
            fg='white',
            font=('Arial', 12),
            width=60,
            height=15
        )
        self.camera_label.pack(pady=10)

        # Detected QR codes display
        detection_frame = tk.Frame(camera_frame, bg='white', relief='groove', bd=2)
        detection_frame.pack(fill='x', padx=10, pady=10)

        tk.Label(
            detection_frame,
            text="Detected QR Codes:",
            font=('Arial', 12, 'bold'),
            bg='white'
        ).pack(anchor='w', padx=10, pady=(10, 5))

        self.detection_results = scrolledtext.ScrolledText(
            detection_frame,
            height=6,
            font=('Arial', 10),
            wrap=tk.WORD
        )
        self.detection_results.pack(fill='x', padx=10, pady=(0, 10))

    def browse_save_location(self):
        """Browse for save location."""
        directory = filedialog.askdirectory()
        if directory:
            self.save_path_var.set(directory)

    def validate_url(self, url):
        """Validate URL format."""
        try:
            result = urllib.parse.urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False

    def get_qr_size(self):
        """Get QR code size based on selection."""
        size_map = {
            "Small": 8,
            "Medium": 10,
            "Large": 15
        }
        return size_map.get(self.size_var.get(), 10)

    def generate_qr_code(self):
        """Generate QR code from URL."""
        url = self.url_entry.get().strip()

        if not url:
            messagebox.showerror("Error", "Please enter a URL!")
            return

        if not self.validate_url(url):
            messagebox.showerror("Error", "Please enter a valid URL (include http:// or https://)")
            return

        try:
            # Create QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=self.get_qr_size(),
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)

            # Create image
            qr_image = qr.make_image(fill_color="black", back_color="white")

            # Save image
            filename = self.filename_entry.get().strip() or "qrcode"
            file_format = self.format_var.get().lower()

            if not filename.endswith(f'.{file_format}'):
                filename = f"{filename}.{file_format}"

            save_path = self.save_path_var.get()
            if save_path == "Current Directory":
                file_path = filename
            else:
                file_path = os.path.join(save_path, filename)

            # Handle format conversion for JPEG
            if file_format == 'jpeg':
                qr_image = qr_image.convert('RGB')
                qr_image.save(file_path, 'JPEG', quality=95)
            else:
                qr_image.save(file_path, 'PNG')

            # Show preview
            self.show_qr_preview(qr_image)

            # Show success message
            messagebox.showinfo("Success", f"QR code saved successfully!\nLocation: {os.path.abspath(file_path)}")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate QR code: {str(e)}")

    def show_qr_preview(self, pil_image):
        """Show QR code preview."""
        # Resize for preview
        display_size = (200, 200)
        preview_image = pil_image.resize(display_size, Image.Resampling.LANCZOS)

        # Convert to PhotoImage
        photo = ImageTk.PhotoImage(preview_image)

        # Update label
        self.preview_label.configure(image=photo, text="")
        self.preview_label.image = photo  # Keep a reference

    def select_image_file(self):
        """Select and scan image file."""
        file_path = filedialog.askopenfilename(
            title="Select QR Code Image",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff"),
                ("All files", "*.*")
            ]
        )

        if file_path:
            self.scan_image_file(file_path)

    def scan_image_file(self, file_path):
        """Scan QR code from image file."""
        try:
            # Read image with OpenCV
            image = cv2.imread(file_path)

            if image is None:
                self.scan_results.delete(1.0, tk.END)
                self.scan_results.insert(tk.END, f"Error: Could not read image file\n{file_path}")
                return

            # Detect QR code
            detector = cv2.QRCodeDetector()
            data, bbox, _ = detector.detectAndDecode(image)

            # Display results
            self.scan_results.delete(1.0, tk.END)
            self.scan_results.insert(tk.END, f"File: {os.path.basename(file_path)}\n")
            self.scan_results.insert(tk.END, f"Path: {file_path}\n\n")

            if data:
                self.scan_results.insert(tk.END, f"✅ QR Code Found!\n")
                self.scan_results.insert(tk.END, f"Content: {data}\n\n")

                # Check if it's a URL
                if self.validate_url(data):
                    self.scan_results.insert(tk.END, f"🔗 This appears to be a URL\n")
            else:
                self.scan_results.insert(tk.END, f"❌ No QR code found in this image\n")

            # Show image preview
            self.show_scan_preview(file_path)

        except Exception as e:
            self.scan_results.delete(1.0, tk.END)
            self.scan_results.insert(tk.END, f"Error scanning image: {str(e)}")

    def show_scan_preview(self, file_path):
        """Show preview of scanned image."""
        try:
            # Open and resize image for preview
            pil_image = Image.open(file_path)

            # Calculate size to fit in preview area
            max_size = (300, 200)
            pil_image.thumbnail(max_size, Image.Resampling.LANCZOS)

            # Convert to PhotoImage
            photo = ImageTk.PhotoImage(pil_image)

            # Update preview
            self.scan_preview_label.configure(image=photo, text="")
            self.scan_preview_label.image = photo  # Keep reference

        except Exception as e:
            self.scan_preview_label.configure(text=f"Preview unavailable: {str(e)}")

    def start_camera(self):
        """Start camera for real-time QR scanning."""
        if self.camera_running:
            return

        try:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                messagebox.showerror("Error", "Could not access camera")
                return

            self.camera_running = True
            self.start_camera_btn.configure(state='disabled')
            self.stop_camera_btn.configure(state='normal')

            # Start camera thread
            self.camera_thread = threading.Thread(target=self.camera_loop)
            self.camera_thread.daemon = True
            self.camera_thread.start()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to start camera: {str(e)}")

    def stop_camera(self):
        """Stop camera scanning."""
        self.camera_running = False

        if self.cap:
            self.cap.release()

        self.start_camera_btn.configure(state='normal')
        self.stop_camera_btn.configure(state='disabled')

        # Clear camera display
        self.camera_label.configure(
            image="",
            text="Camera stopped\nClick 'Start Camera' to resume"
        )

    def camera_loop(self):
        """Main camera loop for QR detection."""
        detector = cv2.QRCodeDetector()

        while self.camera_running:
            try:
                ret, frame = self.cap.read()
                if not ret:
                    break

                # Detect QR codes
                data, bbox, _ = detector.detectAndDecode(frame)

                # Draw bounding box if QR code detected
                if data and bbox is not None:
                    bbox = bbox.astype(int)
                    cv2.polylines(frame, [bbox], True, (0, 255, 0), 2)

                    # Add text
                    cv2.putText(frame, "QR Code Detected!", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                    # Update detection results
                    self.root.after(0, self.update_detection_results, data)

                # Convert frame for Tkinter
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(frame_rgb)

                # Resize for display
                display_size = (400, 300)
                pil_image = pil_image.resize(display_size, Image.Resampling.LANCZOS)

                # Convert to PhotoImage
                photo = ImageTk.PhotoImage(pil_image)

                # Update display
                self.root.after(0, self.update_camera_display, photo)

            except Exception as e:
                print(f"Camera error: {e}")
                break

    def update_camera_display(self, photo):
        """Update camera display in main thread."""
        if self.camera_running:
            self.camera_label.configure(image=photo, text="")
            self.camera_label.image = photo  # Keep reference

    def update_detection_results(self, data):
        """Update detection results in main thread."""
        import time
        current_time = time.strftime("%H:%M:%S")

        self.detection_results.insert(tk.END, f"[{current_time}] QR Code Detected:\n")
        self.detection_results.insert(tk.END, f"{data}\n\n")
        self.detection_results.see(tk.END)

    def on_closing(self):
        """Handle application closing."""
        if self.camera_running:
            self.stop_camera()
        self.root.destroy()


def main():
    """Main function to run the GUI application."""

    # Check for required modules
    required_modules = {
        'qrcode': 'qrcode',
        'cv2': 'opencv-python',
        'PIL': 'Pillow'
    }

    missing_modules = []
    for module, pip_name in required_modules.items():
        try:
            __import__(module)
        except ImportError:
            missing_modules.append(pip_name)

    if missing_modules:
        # Create temporary root for messagebox
        temp_root = tk.Tk()
        temp_root.withdraw()  # Hide main window
        messagebox.showerror(
            "Missing Dependencies",
            f"Please install the following modules:\n\n" +
            "\n".join([f"pip install {module}" for module in missing_modules])
        )
        temp_root.destroy()
        return

    # Create and run GUI
    root = tk.Tk()
    app = QRCodeGUI(root)

    # Handle window closing
    root.protocol("WM_DELETE_WINDOW", app.on_closing)

    # Center window on screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")

    root.mainloop()


if __name__ == "__main__":
    main()