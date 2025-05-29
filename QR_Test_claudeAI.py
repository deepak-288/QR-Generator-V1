# # # # import qrcode
# # # # import cv2
# # # # import numpy as np
# # # # import urllib.parse
# # # # import os
# # # # import sys
# # # # from PIL import Image
# # # #
# # # #
# # # # class QRCodeHandler:
# # # #     """A comprehensive QR code generator and scanner class."""
# # # #
# # # #     def __init__(self):
# # # #         """Initialize the QR code handler."""
# # # #         self.qr_detector = cv2.QRCodeDetector()
# # # #
# # # #     def validate_url(self, url):
# # # #         """
# # # #         Validate if the provided URL is properly formatted.
# # # #
# # # #         Args:
# # # #             url (str): The URL to validate
# # # #
# # # #         Returns:
# # # #             bool: True if URL is valid, False otherwise
# # # #         """
# # # #         try:
# # # #             result = urllib.parse.urlparse(url)
# # # #             return all([result.scheme, result.netloc])
# # # #         except Exception:
# # # #             return False
# # # #
# # # #     def generate_qr_code(self, url, filename='qrcode.png', size=10, border=4):
# # # #         """
# # # #         Generate a QR code for the given URL and save it as an image.
# # # #
# # # #         Args:
# # # #             url (str): The URL to encode in the QR code
# # # #             filename (str): The filename to save the QR code image
# # # #             size (int): The size of each box in the QR code
# # # #             border (int): The border size around the QR code
# # # #
# # # #         Returns:
# # # #             bool: True if successful, False otherwise
# # # #         """
# # # #         try:
# # # #             # Validate the URL first
# # # #             if not self.validate_url(url):
# # # #                 print(f"Error: Invalid URL format - {url}")
# # # #                 return False
# # # #
# # # #             # Create QR code instance with custom settings
# # # #             qr = qrcode.QRCode(
# # # #                 version=1,  # Controls the size of the QR code
# # # #                 error_correction=qrcode.constants.ERROR_CORRECT_L,
# # # #                 box_size=size,
# # # #                 border=border,
# # # #             )
# # # #
# # # #             # Add data to the QR code
# # # #             qr.add_data(url)
# # # #             qr.make(fit=True)
# # # #
# # # #             # Create an image from the QR code
# # # #             qr_image = qr.make_image(fill_color="black", back_color="white")
# # # #
# # # #             # Save the QR code image
# # # #             qr_image.save(filename)
# # # #             print(f"QR code generated successfully and saved as '{filename}'")
# # # #             print(f"QR code contains URL: {url}")
# # # #
# # # #             return True
# # # #
# # # #         except Exception as e:
# # # #             print(f"Error generating QR code: {str(e)}")
# # # #             return False
# # # #
# # # #     def scan_qr_code_from_camera(self):
# # # #         """
# # # #         Scan QR codes from camera feed in real-time.
# # # #
# # # #         Returns:
# # # #             None
# # # #         """
# # # #         try:
# # # #             # Initialize the camera
# # # #             cap = cv2.VideoCapture(0)
# # # #
# # # #             # Check if camera opened successfully
# # # #             if not cap.isOpened():
# # # #                 print("Error: Could not open camera")
# # # #                 print("Please check if:")
# # # #                 print("1. Camera is connected properly")
# # # #                 print("2. Camera is not being used by another application")
# # # #                 print("3. Camera drivers are installed correctly")
# # # #                 return
# # # #
# # # #             print("QR Code Scanner started...")
# # # #             print("Position a QR code in front of the camera")
# # # #             print("Press 'q' to quit the scanner")
# # # #
# # # #             while True:
# # # #                 # Capture frame from camera
# # # #                 ret, frame = cap.read()
# # # #
# # # #                 if not ret:
# # # #                     print("Error: Failed to grab frame from camera")
# # # #                     break
# # # #
# # # #                 # Detect and decode QR code
# # # #                 data, bbox, _ = self.qr_detector.detectAndDecode(frame)
# # # #
# # # #                 # If QR code is detected
# # # #                 if data:
# # # #                     print(f"\nQR Code detected!")
# # # #                     print(f"Data: {data}")
# # # #
# # # #                     # Draw bounding box around detected QR code
# # # #                     if bbox is not None:
# # # #                         bbox = bbox.astype(int)
# # # #                         # Draw the bounding box
# # # #                         cv2.polylines(frame, [bbox], True, (0, 255, 0), 2)
# # # #
# # # #                         # Add text showing the decoded data
# # # #                         cv2.putText(frame, f"Data: {data[:50]}...",
# # # #                                     (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
# # # #                                     0.7, (0, 255, 0), 2)
# # # #
# # # #                 # Display the frame
# # # #                 cv2.imshow('QR Code Scanner (Press q to quit)', frame)
# # # #
# # # #                 # Break the loop if 'q' key is pressed
# # # #                 if cv2.waitKey(1) & 0xFF == ord('q'):
# # # #                     break
# # # #
# # # #             # Release the camera and close windows
# # # #             cap.release()
# # # #             cv2.destroyAllWindows()
# # # #             print("QR Code Scanner stopped.")
# # # #
# # # #         except Exception as e:
# # # #             print(f"Error during QR code scanning: {str(e)}")
# # # #             # Ensure cleanup even if error occurs
# # # #             try:
# # # #                 cap.release()
# # # #                 cv2.destroyAllWindows()
# # # #             except:
# # # #                 pass
# # # #
# # # #     def scan_qr_code_from_image(self, image_path):
# # # #         """
# # # #         Scan QR code from a static image file.
# # # #
# # # #         Args:
# # # #             image_path (str): Path to the image file containing QR code
# # # #
# # # #         Returns:
# # # #             str: Decoded data from QR code, or None if not found
# # # #         """
# # # #         try:
# # # #             # Check if image file exists
# # # #             if not os.path.exists(image_path):
# # # #                 print(f"Error: Image file '{image_path}' not found")
# # # #                 return None
# # # #
# # # #             # Read the image
# # # #             image = cv2.imread(image_path)
# # # #
# # # #             if image is None:
# # # #                 print(f"Error: Could not read image from '{image_path}'")
# # # #                 return None
# # # #
# # # #             # Detect and decode QR code
# # # #             data, bbox, _ = self.qr_detector.detectAndDecode(image)
# # # #
# # # #             if data:
# # # #                 print(f"QR Code found in image!")
# # # #                 print(f"Decoded data: {data}")
# # # #                 return data
# # # #             else:
# # # #                 print("No QR code found in the image")
# # # #                 return None
# # # #
# # # #         except Exception as e:
# # # #             print(f"Error scanning QR code from image: {str(e)}")
# # # #             return None
# # # #
# # # #
# # # # def main():
# # # #     """Main function to demonstrate QR code generation and scanning."""
# # # #
# # # #     # Create QR code handler instance
# # # #     qr_handler = QRCodeHandler()
# # # #
# # # #     print("=== QR Code Generator and Scanner ===\n")
# # # #
# # # #     while True:
# # # #         print("\nChoose an option:")
# # # #         print("1. Generate QR code from URL")
# # # #         print("2. Scan QR code from camera")
# # # #         print("3. Scan QR code from image file")
# # # #         print("4. Exit")
# # # #
# # # #         try:
# # # #             choice = input("\nEnter your choice (1-4): ").strip()
# # # #
# # # #             if choice == '1':
# # # #                 # Generate QR code
# # # #                 url = input("Enter the URL to encode: ").strip()
# # # #                 if url:
# # # #                     filename = input("Enter filename (press Enter for 'qrcode.png'): ").strip()
# # # #                     if not filename:
# # # #                         filename = 'qrcode.png'
# # # #
# # # #                     success = qr_handler.generate_qr_code(url, filename)
# # # #                     if success:
# # # #                         # Ask if user wants to display the generated QR code
# # # #                         show = input("Display the generated QR code? (y/n): ").strip().lower()
# # # #                         if show == 'y':
# # # #                             try:
# # # #                                 img = Image.open(filename)
# # # #                                 img.show()
# # # #                             except Exception as e:
# # # #                                 print(f"Could not display image: {e}")
# # # #                 else:
# # # #                     print("URL cannot be empty!")
# # # #
# # # #             elif choice == '2':
# # # #                 # Scan from camera
# # # #                 print("\nStarting camera scanner...")
# # # #                 qr_handler.scan_qr_code_from_camera()
# # # #
# # # #             elif choice == '3':
# # # #                 # Scan from image file
# # # #                 image_path = input("Enter the path to the image file: ").strip()
# # # #                 if image_path:
# # # #                     qr_handler.scan_qr_code_from_image(image_path)
# # # #                 else:
# # # #                     print("Image path cannot be empty!")
# # # #
# # # #             elif choice == '4':
# # # #                 print("Goodbye!")
# # # #                 break
# # # #
# # # #             else:
# # # #                 print("Invalid choice! Please enter 1, 2, 3, or 4.")
# # # #
# # # #         except KeyboardInterrupt:
# # # #             print("\n\nProgram interrupted by user. Goodbye!")
# # # #             break
# # # #         except Exception as e:
# # # #             print(f"An unexpected error occurred: {str(e)}")
# # # #
# # # #
# # # # if __name__ == "__main__":
# # # #     # Check if required libraries are available
# # # #     required_modules = {
# # # #         'qrcode': 'qrcode',
# # # #         'cv2': 'opencv-python',
# # # #         'PIL': 'Pillow'
# # # #     }
# # # #
# # # #     missing_modules = []
# # # #     for module, pip_name in required_modules.items():
# # # #         try:
# # # #             __import__(module)
# # # #         except ImportError:
# # # #             missing_modules.append(pip_name)
# # # #
# # # #     if missing_modules:
# # # #         print("Missing required modules. Please install them using:")
# # # #         for module in missing_modules:
# # # #             print(f"pip install {module}")
# # # #         sys.exit(1)
# # # #
# # # #     # Run the main program
# # # #     main()
# # # import qrcode
# # # import cv2
# # # import numpy as np
# # # import urllib.parse
# # # import os
# # # import sys
# # # from PIL import Image
# # #
# # #
# # # class QRCodeHandler:
# # #     """A comprehensive QR code generator and scanner class."""
# # #
# # #     def __init__(self):
# # #         """Initialize the QR code handler."""
# # #         self.qr_detector = cv2.QRCodeDetector()
# # #
# # #     def validate_url(self, url):
# # #         """
# # #         Validate if the provided URL is properly formatted.
# # #
# # #         Args:
# # #             url (str): The URL to validate
# # #
# # #         Returns:
# # #             bool: True if URL is valid, False otherwise
# # #         """
# # #         try:
# # #             result = urllib.parse.urlparse(url)
# # #             return all([result.scheme, result.netloc])
# # #         except Exception:
# # #             return False
# # #
# # #     def generate_qr_code(self, url, filename='qrcode.png', size=10, border=4, save_path=None):
# # #         """
# # #         Generate a QR code for the given URL and save it as an image.
# # #
# # #         Args:
# # #             url (str): The URL to encode in the QR code
# # #             filename (str): The filename to save the QR code image
# # #             size (int): The size of each box in the QR code
# # #             border (int): The border size around the QR code
# # #             save_path (str): Optional directory path to save the file
# # #
# # #         Returns:
# # #             bool: True if successful, False otherwise
# # #         """
# # #         try:
# # #             # Validate the URL first
# # #             if not self.validate_url(url):
# # #                 print(f"Error: Invalid URL format - {url}")
# # #                 return False
# # #
# # #             # Create QR code instance with custom settings
# # #             qr = qrcode.QRCode(
# # #                 version=1,  # Controls the size of the QR code
# # #                 error_correction=qrcode.constants.ERROR_CORRECT_L,
# # #                 box_size=size,
# # #                 border=border,
# # #             )
# # #
# # #             # Add data to the QR code
# # #             qr.add_data(url)
# # #             qr.make(fit=True)
# # #
# # #             # Create an image from the QR code
# # #             qr_image = qr.make_image(fill_color="black", back_color="white")
# # #
# # #             # Determine the full file path
# # #             if save_path:
# # #                 # Create directory if it doesn't exist
# # #                 os.makedirs(save_path, exist_ok=True)
# # #                 full_path = os.path.join(save_path, filename)
# # #             else:
# # #                 full_path = filename
# # #
# # #             # Save the QR code image
# # #             qr_image.save(full_path)
# # #
# # #             # Get absolute path for user feedback
# # #             absolute_path = os.path.abspath(full_path)
# # #
# # #             print(f"QR code generated successfully!")
# # #             print(f"Saved as: {absolute_path}")
# # #             print(f"QR code contains URL: {url}")
# # #             print(f"File size: {os.path.getsize(full_path)} bytes")
# # #
# # #             return True
# # #
# # #         except Exception as e:
# # #             print(f"Error generating QR code: {str(e)}")
# # #             return False
# # #
# # #     def scan_qr_code_from_camera(self):
# # #         """
# # #         Scan QR codes from camera feed in real-time.
# # #
# # #         Returns:
# # #             None
# # #         """
# # #         try:
# # #             # Initialize the camera
# # #             cap = cv2.VideoCapture(0)
# # #
# # #             # Check if camera opened successfully
# # #             if not cap.isOpened():
# # #                 print("Error: Could not open camera")
# # #                 print("Please check if:")
# # #                 print("1. Camera is connected properly")
# # #                 print("2. Camera is not being used by another application")
# # #                 print("3. Camera drivers are installed correctly")
# # #                 return
# # #
# # #             print("QR Code Scanner started...")
# # #             print("Position a QR code in front of the camera")
# # #             print("Press 'q' to quit the scanner")
# # #
# # #             while True:
# # #                 # Capture frame from camera
# # #                 ret, frame = cap.read()
# # #
# # #                 if not ret:
# # #                     print("Error: Failed to grab frame from camera")
# # #                     break
# # #
# # #                 # Detect and decode QR code
# # #                 data, bbox, _ = self.qr_detector.detectAndDecode(frame)
# # #
# # #                 # If QR code is detected
# # #                 if data:
# # #                     print(f"\nQR Code detected!")
# # #                     print(f"Data: {data}")
# # #
# # #                     # Draw bounding box around detected QR code
# # #                     if bbox is not None:
# # #                         bbox = bbox.astype(int)
# # #                         # Draw the bounding box
# # #                         cv2.polylines(frame, [bbox], True, (0, 255, 0), 2)
# # #
# # #                         # Add text showing the decoded data
# # #                         cv2.putText(frame, f"Data: {data[:50]}...",
# # #                                     (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
# # #                                     0.7, (0, 255, 0), 2)
# # #
# # #                 # Display the frame
# # #                 cv2.imshow('QR Code Scanner (Press q to quit)', frame)
# # #
# # #                 # Break the loop if 'q' key is pressed
# # #                 if cv2.waitKey(1) & 0xFF == ord('q'):
# # #                     break
# # #
# # #             # Release the camera and close windows
# # #             cap.release()
# # #             cv2.destroyAllWindows()
# # #             print("QR Code Scanner stopped.")
# # #
# # #         except Exception as e:
# # #             print(f"Error during QR code scanning: {str(e)}")
# # #             # Ensure cleanup even if error occurs
# # #             try:
# # #                 cap.release()
# # #                 cv2.destroyAllWindows()
# # #             except:
# # #                 pass
# # #
# # #     def scan_qr_code_from_image(self, image_path):
# # #         """
# # #         Scan QR code from a static image file.
# # #
# # #         Args:
# # #             image_path (str): Path to the image file containing QR code
# # #
# # #         Returns:
# # #             str: Decoded data from QR code, or None if not found
# # #         """
# # #         try:
# # #             # Check if image file exists
# # #             if not os.path.exists(image_path):
# # #                 print(f"Error: Image file '{image_path}' not found")
# # #                 return None
# # #
# # #     def save_qr_in_multiple_formats(self, url, base_filename='qrcode', save_path=None, formats=['png', 'jpg', 'pdf']):
# # #         """
# # #         Generate and save QR code in multiple formats.
# # #
# # #         Args:
# # #             url (str): The URL to encode
# # #             base_filename (str): Base filename without extension
# # #             save_path (str): Directory to save files
# # #             formats (list): List of formats to save ('png', 'jpg', 'pdf', 'svg')
# # #
# # #         Returns:
# # #             list: List of successfully saved file paths
# # #         """
# # #         saved_files = []
# # #
# # #         try:
# # #             # Create QR code
# # #             qr = qrcode.QRCode(
# # #                 version=1,
# # #                 error_correction=qrcode.constants.ERROR_CORRECT_L,
# # #                 box_size=10,
# # #                 border=4,
# # #             )
# # #             qr.add_data(url)
# # #             qr.make(fit=True)
# # #
# # #             for fmt in formats:
# # #                 try:
# # #                     filename = f"{base_filename}.{fmt.lower()}"
# # #
# # #                     if save_path:
# # #                         os.makedirs(save_path, exist_ok=True)
# # #                         full_path = os.path.join(save_path, filename)
# # #                     else:
# # #                         full_path = filename
# # #
# # #                     if fmt.lower() in ['png', 'jpg', 'jpeg']:
# # #                         # Standard image formats
# # #                         qr_image = qr.make_image(fill_color="black", back_color="white")
# # #                         if fmt.lower() in ['jpg', 'jpeg']:
# # #                             # Convert to RGB for JPEG (remove transparency)
# # #                             qr_image = qr_image.convert('RGB')
# # #                         qr_image.save(full_path)
# # #
# # #                     elif fmt.lower() == 'pdf':
# # #                         # Save as PDF
# # #                         qr_image = qr.make_image(fill_color="black", back_color="white")
# # #                         qr_image.save(full_path, "PDF", resolution=100.0)
# # #
# # #                     elif fmt.lower() == 'svg':
# # #                         # SVG format (requires qrcode[pil])
# # #                         import qrcode.image.svg
# # #                         factory = qrcode.image.svg.SvgPathImage
# # #                         svg_qr = qrcode.QRCode(image_factory=factory)
# # #                         svg_qr.add_data(url)
# # #                         svg_qr.make(fit=True)
# # #                         svg_img = svg_qr.make_image()
# # #                         with open(full_path, 'wb') as f:
# # #                             svg_img.save(f)
# # #
# # #                     saved_files.append(os.path.abspath(full_path))
# # #                     print(f"Saved: {os.path.abspath(full_path)}")
# # #
# # #                 except Exception as e:
# # #                     print(f"Failed to save as {fmt}: {str(e)}")
# # #
# # #             return saved_files
# # #
# # #         except Exception as e:
# # #             print(f"Error generating QR code: {str(e)}")
# # #             return saved_files
# # #
# # #             # Read the image
# # #             image = cv2.imread(image_path)
# # #
# # #             if image is None:
# # #                 print(f"Error: Could not read image from '{image_path}'")
# # #                 return None
# # #
# # #             # Detect and decode QR code
# # #             data, bbox, _ = self.qr_detector.detectAndDecode(image)
# # #
# # #             if data:
# # #                 print(f"QR Code found in image!")
# # #                 print(f"Decoded data: {data}")
# # #                 return data
# # #             else:
# # #                 print("No QR code found in the image")
# # #                 return None
# # #
# # #         except Exception as e:
# # #             print(f"Error scanning QR code from image: {str(e)}")
# # #             return None
# # #
# # #
# # # def main():
# # #     """Main function to demonstrate QR code generation and scanning."""
# # #
# # #     # Create QR code handler instance
# # #     qr_handler = QRCodeHandler()
# # #
# # #     print("=== QR Code Generator and Scanner ===\n")
# # #
# # #     while True:
# # #         print("\nChoose an option:")
# # #         print("1. Generate QR code from URL")
# # #         print("2. Generate QR code in multiple formats")
# # #         print("3. Scan QR code from camera")
# # #         print("4. Scan QR code from image file")
# # #         print("5. Exit")
# # #
# # #         try:
# # #             choice = input("\nEnter your choice (1-5): ").strip()
# # #
# # #             if choice == '1':
# # #                 # Generate QR code
# # #                 url = input("Enter the URL to encode: ").strip()
# # #                 if url:
# # #                     filename = input("Enter filename (press Enter for 'qrcode.png'): ").strip()
# # #                     if not filename:
# # #                         filename = 'qrcode.png'
# # #
# # #                     # Ask for custom save location
# # #                     save_path = input("Enter save directory (press Enter for current directory): ").strip()
# # #                     if not save_path:
# # #                         save_path = None
# # #
# # #                     success = qr_handler.generate_qr_code(url, filename, save_path=save_path)
# # #                     if success:
# # #                         # Ask if user wants to display the generated QR code
# # #                         show = input("Display the generated QR code? (y/n): ").strip().lower()
# # #                         if show == 'y':
# # #                             try:
# # #                                 if save_path:
# # #                                     full_path = os.path.join(save_path, filename)
# # #                                 else:
# # #                                     full_path = filename
# # #                                 img = Image.open(full_path)
# # #                                 img.show()
# # #                             except Exception as e:
# # #                                 print(f"Could not display image: {e}")
# # #                 else:
# # #                     print("URL cannot be empty!")
# # #
# # #             elif choice == '2':
# # #                 # Generate QR code in multiple formats
# # #                 url = input("Enter the URL to encode: ").strip()
# # #                 if url:
# # #                     base_filename = input("Enter base filename (press Enter for 'qrcode'): ").strip()
# # #                     if not base_filename:
# # #                         base_filename = 'qrcode'
# # #
# # #                     save_path = input("Enter save directory (press Enter for current directory): ").strip()
# # #                     if not save_path:
# # #                         save_path = None
# # #
# # #                     print("Available formats: png, jpg, pdf, svg")
# # #                     formats_input = input("Enter formats separated by commas (press Enter for 'png,jpg,pdf'): ").strip()
# # #                     if not formats_input:
# # #                         formats = ['png', 'jpg', 'pdf']
# # #                     else:
# # #                         formats = [f.strip().lower() for f in formats_input.split(',')]
# # #
# # #                     saved_files = qr_handler.save_qr_in_multiple_formats(url, base_filename, save_path, formats)
# # #                     if saved_files:
# # #                         print(f"\nSuccessfully saved {len(saved_files)} files:")
# # #                         for file_path in saved_files:
# # #                             print(f"  - {file_path}")
# # #                 else:
# # #                     print("URL cannot be empty!")
# # #
# # #             elif choice == '3':
# # #                 # Scan from camera
# # #                 print("\nStarting camera scanner...")
# # #                 qr_handler.scan_qr_code_from_camera()
# # #
# # #             elif choice == '4':
# # #                 # Scan from image file
# # #                 image_path = input("Enter the path to the image file: ").strip()
# # #                 if image_path:
# # #                     qr_handler.scan_qr_code_from_image(image_path)
# # #                 else:
# # #                     print("Image path cannot be empty!")
# # #
# # #             elif choice == '5':
# # #                 print("Goodbye!")
# # #                 break
# # #
# # #             else:
# # #                 print("Invalid choice! Please enter 1, 2, 3, 4, or 5.")
# # #
# # #         except KeyboardInterrupt:
# # #             print("\n\nProgram interrupted by user. Goodbye!")
# # #             break
# # #         except Exception as e:
# # #             print(f"An unexpected error occurred: {str(e)}")
# # #
# # #
# # # if __name__ == "__main__":
# # #     # Check if required libraries are available
# # #     required_modules = {
# # #         'qrcode': 'qrcode',
# # #         'cv2': 'opencv-python',
# # #         'PIL': 'Pillow'
# # #     }
# # #
# # #     missing_modules = []
# # #     for module, pip_name in required_modules.items():
# # #         try:
# # #             __import__(module)
# # #         except ImportError:
# # #             missing_modules.append(pip_name)
# # #
# # #     if missing_modules:
# # #         print("Missing required modules. Please install them using:")
# # #         for module in missing_modules:
# # #             print(f"pip install {module}")
# # #         sys.exit(1)
# # #
# # #     # Run the main program
# # #     main()
# # import qrcode
# # import cv2
# # import numpy as np
# # import urllib.parse
# # import os
# # import sys
# # from PIL import Image
# #
# #
# # class QRCodeHandler:
# #     """A comprehensive QR code generator and scanner class."""
# #
# #     def __init__(self):
# #         """Initialize the QR code handler."""
# #         self.qr_detector = cv2.QRCodeDetector()
# #
# #     def validate_url(self, url):
# #         """
# #         Validate if the provided URL is properly formatted.
# #
# #         Args:
# #             url (str): The URL to validate
# #
# #         Returns:
# #             bool: True if URL is valid, False otherwise
# #         """
# #         try:
# #             result = urllib.parse.urlparse(url)
# #             return all([result.scheme, result.netloc])
# #         except Exception:
# #             return False
# #
# #     def generate_qr_code(self, url, filename='qrcode.png', size=10, border=4, save_path=None):
# #         """
# #         Generate a QR code for the given URL and save it as an image.
# #
# #         Args:
# #             url (str): The URL to encode in the QR code
# #             filename (str): The filename to save the QR code image
# #             size (int): The size of each box in the QR code
# #             border (int): The border size around the QR code
# #             save_path (str): Optional directory path to save the file
# #
# #         Returns:
# #             bool: True if successful, False otherwise
# #         """
# #         try:
# #             # Validate the URL first
# #             if not self.validate_url(url):
# #                 print(f"Error: Invalid URL format - {url}")
# #                 return False
# #
# #             # Create QR code instance with custom settings
# #             qr = qrcode.QRCode(
# #                 version=1,  # Controls the size of the QR code
# #                 error_correction=qrcode.constants.ERROR_CORRECT_L,
# #                 box_size=size,
# #                 border=border,
# #             )
# #
# #             # Add data to the QR code
# #             qr.add_data(url)
# #             qr.make(fit=True)
# #
# #             # Create an image from the QR code
# #             qr_image = qr.make_image(fill_color="black", back_color="white")
# #
# #             # Determine the full file path
# #             if save_path:
# #                 # Create directory if it doesn't exist
# #                 os.makedirs(save_path, exist_ok=True)
# #                 full_path = os.path.join(save_path, filename)
# #             else:
# #                 full_path = filename
# #
# #             # Save the QR code image
# #             qr_image.save(full_path)
# #
# #             # Get absolute path for user feedback
# #             absolute_path = os.path.abspath(full_path)
# #
# #             print(f"QR code generated successfully!")
# #             print(f"Saved as: {absolute_path}")
# #             print(f"QR code contains URL: {url}")
# #             print(f"File size: {os.path.getsize(full_path)} bytes")
# #
# #             return True
# #
# #         except Exception as e:
# #             print(f"Error generating QR code: {str(e)}")
# #             return False
# #
# #     def scan_qr_code_from_camera(self):
# #         """
# #         Scan QR codes from camera feed in real-time.
# #
# #         Returns:
# #             None
# #         """
# #         try:
# #             # Initialize the camera
# #             cap = cv2.VideoCapture(0)
# #
# #             # Check if camera opened successfully
# #             if not cap.isOpened():
# #                 print("Error: Could not open camera")
# #                 print("Please check if:")
# #                 print("1. Camera is connected properly")
# #                 print("2. Camera is not being used by another application")
# #                 print("3. Camera drivers are installed correctly")
# #                 return
# #
# #             print("QR Code Scanner started...")
# #             print("Position a QR code in front of the camera")
# #             print("Press 'q' to quit the scanner")
# #
# #             while True:
# #                 # Capture frame from camera
# #                 ret, frame = cap.read()
# #
# #                 if not ret:
# #                     print("Error: Failed to grab frame from camera")
# #                     break
# #
# #                 # Detect and decode QR code
# #                 data, bbox, _ = self.qr_detector.detectAndDecode(frame)
# #
# #                 # If QR code is detected
# #                 if data:
# #                     print(f"\nQR Code detected!")
# #                     print(f"Data: {data}")
# #
# #                     # Draw bounding box around detected QR code
# #                     if bbox is not None:
# #                         bbox = bbox.astype(int)
# #                         # Draw the bounding box
# #                         cv2.polylines(frame, [bbox], True, (0, 255, 0), 2)
# #
# #                         # Add text showing the decoded data
# #                         cv2.putText(frame, f"Data: {data[:50]}...",
# #                                     (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
# #                                     0.7, (0, 255, 0), 2)
# #
# #                 # Display the frame
# #                 cv2.imshow('QR Code Scanner (Press q to quit)', frame)
# #
# #                 # Break the loop if 'q' key is pressed
# #                 if cv2.waitKey(1) & 0xFF == ord('q'):
# #                     break
# #
# #             # Release the camera and close windows
# #             cap.release()
# #             cv2.destroyAllWindows()
# #             print("QR Code Scanner stopped.")
# #
# #         except Exception as e:
# #             print(f"Error during QR code scanning: {str(e)}")
# #             # Ensure cleanup even if error occurs
# #             try:
# #                 cap.release()
# #                 cv2.destroyAllWindows()
# #             except:
# #                 pass
# #
# #     def scan_qr_code_from_image(self, image_path):
# #         """
# #         Scan QR code from a static image file.
# #
# #         Args:
# #             image_path (str): Path to the image file containing QR code
# #
# #         Returns:
# #             str: Decoded data from QR code, or None if not found
# #         """
# #         try:
# #             # Check if image file exists
# #             if not os.path.exists(image_path):
# #                 print(f"Error: Image file '{image_path}' not found")
# #                 return None
# #
# #             # Read the image
# #             image = cv2.imread(image_path)
# #
# #             if image is None:
# #                 print(f"Error: Could not read image from '{image_path}'")
# #                 return None
# #
# #             # Detect and decode QR code
# #             data, bbox, _ = self.qr_detector.detectAndDecode(image)
# #
# #             if data:
# #                 print(f"QR Code found in image!")
# #                 print(f"Decoded data: {data}")
# #                 return data
# #             else:
# #                 print("No QR code found in the image")
# #                 return None
# #
# #         except Exception as e:
# #             print(f"Error scanning QR code from image: {str(e)}")
# #             return None
# #
# #     def save_qr_in_multiple_formats(self, url, base_filename='qrcode', save_path=None, formats=['png', 'jpg', 'pdf']):
# #         """
# #         Generate and save QR code in multiple formats.
# #
# #         Args:
# #             url (str): The URL to encode
# #             base_filename (str): Base filename without extension
# #             save_path (str): Directory to save files
# #             formats (list): List of formats to save ('png', 'jpg', 'pdf', 'svg')
# #
# #         Returns:
# #             list: List of successfully saved file paths
# #         """
# #         saved_files = []
# #
# #         try:
# #             # Create QR code
# #             qr = qrcode.QRCode(
# #                 version=1,
# #                 error_correction=qrcode.constants.ERROR_CORRECT_L,
# #                 box_size=10,
# #                 border=4,
# #             )
# #             qr.add_data(url)
# #             qr.make(fit=True)
# #
# #             for fmt in formats:
# #                 try:
# #                     filename = f"{base_filename}.{fmt.lower()}"
# #
# #                     if save_path:
# #                         os.makedirs(save_path, exist_ok=True)
# #                         full_path = os.path.join(save_path, filename)
# #                     else:
# #                         full_path = filename
# #
# #                     if fmt.lower() in ['png', 'jpg', 'jpeg']:
# #                         # Standard image formats
# #                         qr_image = qr.make_image(fill_color="black", back_color="white")
# #                         if fmt.lower() in ['jpg', 'jpeg']:
# #                             # Convert to RGB for JPEG (remove transparency)
# #                             qr_image = qr_image.convert('RGB')
# #                         qr_image.save(full_path)
# #
# #                     elif fmt.lower() == 'pdf':
# #                         # Save as PDF
# #                         qr_image = qr.make_image(fill_color="black", back_color="white")
# #                         qr_image.save(full_path, "PDF", resolution=100.0)
# #
# #                     elif fmt.lower() == 'svg':
# #                         # SVG format (requires qrcode[pil])
# #                         try:
# #                             import qrcode.image.svg
# #                             factory = qrcode.image.svg.SvgPathImage
# #                             svg_qr = qrcode.QRCode(image_factory=factory)
# #                             svg_qr.add_data(url)
# #                             svg_qr.make(fit=True)
# #                             svg_img = svg_qr.make_image()
# #                             with open(full_path, 'wb') as f:
# #                                 svg_img.save(f)
# #                         except ImportError:
# #                             print(f"SVG support not available. Install with: pip install qrcode[pil]")
# #                             continue
# #
# #                     saved_files.append(os.path.abspath(full_path))
# #                     print(f"Saved: {os.path.abspath(full_path)}")
# #
# #                 except Exception as e:
# #                     print(f"Failed to save as {fmt}: {str(e)}")
# #
# #             return saved_files
# #
# #         except Exception as e:
# #             print(f"Error generating QR code: {str(e)}")
# #             return saved_files
# #
# #
# # def main():
# #     """Main function to demonstrate QR code generation and scanning."""
# #
# #     # Create QR code handler instance
# #     qr_handler = QRCodeHandler()
# #
# #     print("=== QR Code Generator and Scanner ===\n")
# #
# #     while True:
# #         print("\nChoose an option:")
# #         print("1. Generate QR code from URL")
# #         print("2. Generate QR code in multiple formats")
# #         print("3. Scan QR code from camera")
# #         print("4. Scan QR code from image file")
# #         print("5. Exit")
# #
# #         try:
# #             choice = input("\nEnter your choice (1-5): ").strip()
# #
# #             if choice == '1':
# #                 # Generate QR code
# #                 url = input("Enter the URL to encode: ").strip()
# #                 if url:
# #                     filename = input("Enter filename (press Enter for 'qrcode.png'): ").strip()
# #                     if not filename:
# #                         filename = 'qrcode.png'
# #
# #                     # Ask for custom save location
# #                     save_path = input("Enter save directory (press Enter for current directory): ").strip()
# #                     if not save_path:
# #                         save_path = None
# #
# #                     success = qr_handler.generate_qr_code(url, filename, save_path=save_path)
# #                     if success:
# #                         # Ask if user wants to display the generated QR code
# #                         show = input("Display the generated QR code? (y/n): ").strip().lower()
# #                         if show == 'y':
# #                             try:
# #                                 if save_path:
# #                                     full_path = os.path.join(save_path, filename)
# #                                 else:
# #                                     full_path = filename
# #                                 img = Image.open(full_path)
# #                                 img.show()
# #                             except Exception as e:
# #                                 print(f"Could not display image: {e}")
# #                 else:
# #                     print("URL cannot be empty!")
# #
# #             elif choice == '2':
# #                 # Generate QR code in multiple formats
# #                 url = input("Enter the URL to encode: ").strip()
# #                 if url:
# #                     base_filename = input("Enter base filename (press Enter for 'qrcode'): ").strip()
# #                     if not base_filename:
# #                         base_filename = 'qrcode'
# #
# #                     save_path = input("Enter save directory (press Enter for current directory): ").strip()
# #                     if not save_path:
# #                         save_path = None
# #
# #                     print("Available formats: png, jpg, pdf, svg")
# #                     formats_input = input("Enter formats separated by commas (press Enter for 'png,jpg,pdf'): ").strip()
# #                     if not formats_input:
# #                         formats = ['png', 'jpg', 'pdf']
# #                     else:
# #                         formats = [f.strip().lower() for f in formats_input.split(',')]
# #
# #                     saved_files = qr_handler.save_qr_in_multiple_formats(url, base_filename, save_path, formats)
# #                     if saved_files:
# #                         print(f"\nSuccessfully saved {len(saved_files)} files:")
# #                         for file_path in saved_files:
# #                             print(f"  - {file_path}")
# #                 else:
# #                     print("URL cannot be empty!")
# #
# #             elif choice == '3':
# #                 # Scan from camera
# #                 print("\nStarting camera scanner...")
# #                 qr_handler.scan_qr_code_from_camera()
# #
# #             elif choice == '4':
# #                 # Scan from image file
# #                 image_path = input("Enter the path to the image file: ").strip()
# #                 if image_path:
# #                     qr_handler.scan_qr_code_from_image(image_path)
# #                 else:
# #                     print("Image path cannot be empty!")
# #
# #             elif choice == '5':
# #                 print("Goodbye!")
# #                 break
# #
# #             else:
# #                 print("Invalid choice! Please enter 1, 2, 3, 4, or 5.")
# #
# #         except KeyboardInterrupt:
# #             print("\n\nProgram interrupted by user. Goodbye!")
# #             break
# #         except Exception as e:
# #             print(f"An unexpected error occurred: {str(e)}")
# #
# #
# # if __name__ == "__main__":
# #     # Check if required libraries are available
# #     required_modules = {
# #         'qrcode': 'qrcode',
# #         'cv2': 'opencv-python',
# #         'PIL': 'Pillow'
# #     }
# #
# #     missing_modules = []
# #     for module, pip_name in required_modules.items():
# #         try:
# #             __import__(module)
# #         except ImportError:
# #             missing_modules.append(pip_name)
# #
# #     if missing_modules:
# #         print("Missing required modules. Please install them using:")
# #         for module in missing_modules:
# #             print(f"pip install {module}")
# #         sys.exit(1)
# #
# #     # Run the main program
# #     main()
# import qrcode
# import cv2
# import numpy as np
# import urllib.parse
# import os
# import sys
# from PIL import Image
#
#
# class QRCodeHandler:
#     """A comprehensive QR code generator and scanner class."""
#
#     def __init__(self):
#         """Initialize the QR code handler."""
#         self.qr_detector = cv2.QRCodeDetector()
#
#     def validate_url(self, url):
#         """
#         Validate if the provided URL is properly formatted.
#
#         Args:
#             url (str): The URL to validate
#
#         Returns:
#             bool: True if URL is valid, False otherwise
#         """
#         try:
#             result = urllib.parse.urlparse(url)
#             return all([result.scheme, result.netloc])
#         except Exception:
#             return False
#
#     def generate_qr_code(self, url, filename='qrcode.png', size=10, border=4, save_path=None):
#         """
#         Generate a QR code for the given URL and save it as an image.
#
#         Args:
#             url (str): The URL to encode in the QR code
#             filename (str): The filename to save the QR code image
#             size (int): The size of each box in the QR code
#             border (int): The border size around the QR code
#             save_path (str): Optional directory path to save the file
#
#         Returns:
#             bool: True if successful, False otherwise
#         """
#         try:
#             # Validate the URL first
#             if not self.validate_url(url):
#                 print(f"Error: Invalid URL format - {url}")
#                 return False
#
#             # Ensure filename has proper extension
#             if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
#                 filename = filename + '.png'
#                 print(f"Added .png extension. Filename: {filename}")
#
#             # Create QR code instance with custom settings
#             qr = qrcode.QRCode(
#                 version=1,  # Controls the size of the QR code
#                 error_correction=qrcode.constants.ERROR_CORRECT_L,
#                 box_size=size,
#                 border=border,
#             )
#
#             # Add data to the QR code
#             qr.add_data(url)
#             qr.make(fit=True)
#
#             # Create an image from the QR code
#             qr_image = qr.make_image(fill_color="black", back_color="white")
#
#             # Determine the full file path
#             if save_path:
#                 # Create directory if it doesn't exist
#                 os.makedirs(save_path, exist_ok=True)
#                 full_path = os.path.join(save_path, filename)
#             else:
#                 full_path = filename
#
#             # Handle different image formats
#             file_ext = os.path.splitext(filename)[1].lower()
#
#             if file_ext in ['.jpg', '.jpeg']:
#                 # Convert to RGB for JPEG format (removes transparency)
#                 qr_image = qr_image.convert('RGB')
#                 qr_image.save(full_path, 'JPEG', quality=95)
#                 print(f"Saved as JPEG format")
#             else:
#                 # Default to PNG format
#                 qr_image.save(full_path, 'PNG')
#                 print(f"Saved as PNG format")
#
#             # Get absolute path for user feedback
#             absolute_path = os.path.abspath(full_path)
#
#             print(f"QR code generated successfully!")
#             print(f"Saved as: {absolute_path}")
#             print(f"QR code contains URL: {url}")
#             print(f"File size: {os.path.getsize(full_path)} bytes")
#
#             return True
#
#         except Exception as e:
#             print(f"Error generating QR code: {str(e)}")
#             return False
#
#     def scan_qr_code_from_camera(self):
#         """
#         Scan QR codes from camera feed in real-time.
#
#         Returns:
#             None
#         """
#         try:
#             # Initialize the camera
#             cap = cv2.VideoCapture(0)
#
#             # Check if camera opened successfully
#             if not cap.isOpened():
#                 print("Error: Could not open camera")
#                 print("Please check if:")
#                 print("1. Camera is connected properly")
#                 print("2. Camera is not being used by another application")
#                 print("3. Camera drivers are installed correctly")
#                 return
#
#             print("QR Code Scanner started...")
#             print("Position a QR code in front of the camera")
#             print("Press 'q' to quit the scanner")
#
#             while True:
#                 # Capture frame from camera
#                 ret, frame = cap.read()
#
#                 if not ret:
#                     print("Error: Failed to grab frame from camera")
#                     break
#
#                 # Detect and decode QR code
#                 data, bbox, _ = self.qr_detector.detectAndDecode(frame)
#
#                 # If QR code is detected
#                 if data:
#                     print(f"\nQR Code detected!")
#                     print(f"Data: {data}")
#
#                     # Draw bounding box around detected QR code
#                     if bbox is not None:
#                         bbox = bbox.astype(int)
#                         # Draw the bounding box
#                         cv2.polylines(frame, [bbox], True, (0, 255, 0), 2)
#
#                         # Add text showing the decoded data
#                         cv2.putText(frame, f"Data: {data[:50]}...",
#                                     (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
#                                     0.7, (0, 255, 0), 2)
#
#                 # Display the frame
#                 cv2.imshow('QR Code Scanner (Press q to quit)', frame)
#
#                 # Break the loop if 'q' key is pressed
#                 if cv2.waitKey(1) & 0xFF == ord('q'):
#                     break
#
#             # Release the camera and close windows
#             cap.release()
#             cv2.destroyAllWindows()
#             print("QR Code Scanner stopped.")
#
#         except Exception as e:
#             print(f"Error during QR code scanning: {str(e)}")
#             # Ensure cleanup even if error occurs
#             try:
#                 cap.release()
#                 cv2.destroyAllWindows()
#             except:
#                 pass
#
#     def scan_qr_code_from_image(self, image_path):
#         """
#         Scan QR code from a static image file.
#
#         Args:
#             image_path (str): Path to the image file containing QR code
#
#         Returns:
#             str: Decoded data from QR code, or None if not found
#         """
#         try:
#             # Check if image file exists
#             if not os.path.exists(image_path):
#                 print(f"Error: Image file '{image_path}' not found")
#                 return None
#
#             # Read the image
#             image = cv2.imread(image_path)
#
#             if image is None:
#                 print(f"Error: Could not read image from '{image_path}'")
#                 return None
#
#             # Detect and decode QR code
#             data, bbox, _ = self.qr_detector.detectAndDecode(image)
#
#             if data:
#                 print(f"QR Code found in image!")
#                 print(f"Decoded data: {data}")
#                 return data
#             else:
#                 print("No QR code found in the image")
#                 return None
#
#         except Exception as e:
#             print(f"Error scanning QR code from image: {str(e)}")
#             return None
#
#     def save_qr_in_multiple_formats(self, url, base_filename='qrcode', save_path=None, formats=['png', 'jpg', 'pdf']):
#         """
#         Generate and save QR code in multiple formats.
#
#         Args:
#             url (str): The URL to encode
#             base_filename (str): Base filename without extension
#             save_path (str): Directory to save files
#             formats (list): List of formats to save ('png', 'jpg', 'pdf', 'svg')
#
#         Returns:
#             list: List of successfully saved file paths
#         """
#         saved_files = []
#
#         try:
#             # Create QR code
#             qr = qrcode.QRCode(
#                 version=1,
#                 error_correction=qrcode.constants.ERROR_CORRECT_L,
#                 box_size=10,
#                 border=4,
#             )
#             qr.add_data(url)
#             qr.make(fit=True)
#
#             for fmt in formats:
#                 try:
#                     filename = f"{base_filename}.{fmt.lower()}"
#
#                     if save_path:
#                         os.makedirs(save_path, exist_ok=True)
#                         full_path = os.path.join(save_path, filename)
#                     else:
#                         full_path = filename
#
#                     if fmt.lower() in ['png', 'jpg', 'jpeg']:
#                         # Standard image formats
#                         qr_image = qr.make_image(fill_color="black", back_color="white")
#                         if fmt.lower() in ['jpg', 'jpeg']:
#                             # Convert to RGB for JPEG (remove transparency)
#                             qr_image = qr_image.convert('RGB')
#                         qr_image.save(full_path)
#
#                     elif fmt.lower() == 'pdf':
#                         # Save as PDF
#                         qr_image = qr.make_image(fill_color="black", back_color="white")
#                         qr_image.save(full_path, "PDF", resolution=100.0)
#
#                     elif fmt.lower() == 'svg':
#                         # SVG format (requires qrcode[pil])
#                         try:
#                             import qrcode.image.svg
#                             factory = qrcode.image.svg.SvgPathImage
#                             svg_qr = qrcode.QRCode(image_factory=factory)
#                             svg_qr.add_data(url)
#                             svg_qr.make(fit=True)
#                             svg_img = svg_qr.make_image()
#                             with open(full_path, 'wb') as f:
#                                 svg_img.save(f)
#                         except ImportError:
#                             print(f"SVG support not available. Install with: pip install qrcode[pil]")
#                             continue
#
#                     saved_files.append(os.path.abspath(full_path))
#                     print(f"Saved: {os.path.abspath(full_path)}")
#
#                 except Exception as e:
#                     print(f"Failed to save as {fmt}: {str(e)}")
#
#             return saved_files
#
#
# def quick_generate_qr(url, filename=None, format_type='png'):
#     """
#     Quick function to generate a QR code in PNG or JPEG format.
#
#     Args:
#         url (str): URL to encode
#         filename (str): Optional filename. If None, generates based on URL
#         format_type (str): 'png' or 'jpeg'/'jpg'
#
#     Returns:
#         str: Path to saved file, or None if failed
#     """
#     handler = QRCodeHandler()
#
#     # Generate filename if not provided
#     if not filename:
#         # Clean URL for filename
#         clean_url = url.replace('https://', '').replace('http://', '').replace('/', '_').replace(':', '')
#         filename = f"qr_{clean_url[:20]}.{format_type.lower()}"
#
#     # Ensure proper extension
#     if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
#         filename = f"{filename}.{format_type.lower()}"
#
#     success = handler.generate_qr_code(url, filename)
#     return os.path.abspath(filename) if success else None
#
#     except Exception as e:
#     print(f"Error generating QR code: {str(e)}")
#     return saved_files
#
#
# def main():
#     """Main function to demonstrate QR code generation and scanning."""
#
#     # Create QR code handler instance
#     qr_handler = QRCodeHandler()
#
#     print("=== QR Code Generator and Scanner ===\n")
#
#     while True:
#         print("\nChoose an option:")
#         print("1. Generate QR code (PNG/JPEG)")
#         print("2. Generate QR code in multiple formats")
#         print("3. Quick generate (PNG format)")
#         print("4. Scan QR code from camera")
#         print("5. Scan QR code from image file")
#         print("6. Exit")
#
#         try:
#             choice = input("\nEnter your choice (1-6): ").strip()
#
#             if choice == '1':
#                 # Generate QR code
#                 url = input("Enter the URL to encode: ").strip()
#                 if url:
#                     print("Supported formats: PNG (.png) and JPEG (.jpg, .jpeg)")
#                     filename = input("Enter filename with extension (press Enter for 'qrcode.png'): ").strip()
#                     if not filename:
#                         filename = 'qrcode.png'
#
#                     # Ask for custom save location
#                     save_path = input("Enter save directory (press Enter for current directory): ").strip()
#                     if not save_path:
#                         save_path = None
#
#                     success = qr_handler.generate_qr_code(url, filename, save_path=save_path)
#                     if success:
#                         # Ask if user wants to display the generated QR code
#                         show = input("Display the generated QR code? (y/n): ").strip().lower()
#                         if show == 'y':
#                             try:
#                                 if save_path:
#                                     full_path = os.path.join(save_path, filename)
#                                 else:
#                                     full_path = filename
#                                 img = Image.open(full_path)
#                                 img.show()
#                             except Exception as e:
#                                 print(f"Could not display image: {e}")
#                 else:
#                     print("URL cannot be empty!")
#
#             elif choice == '2':
#                 # Generate QR code in multiple formats
#                 url = input("Enter the URL to encode: ").strip()
#                 if url:
#                     base_filename = input("Enter base filename (press Enter for 'qrcode'): ").strip()
#                     if not base_filename:
#                         base_filename = 'qrcode'
#
#                     save_path = input("Enter save directory (press Enter for current directory): ").strip()
#                     if not save_path:
#                         save_path = None
#
#                     print("Available formats: png, jpg (recommended formats)")
#                     formats_input = input("Enter formats separated by commas (press Enter for 'png,jpg'): ").strip()
#                     if not formats_input:
#                         formats = ['png', 'jpg']
#                     else:
#                         formats = [f.strip().lower() for f in formats_input.split(',')]
#
#                     saved_files = qr_handler.save_qr_in_multiple_formats(url, base_filename, save_path, formats)
#                     if saved_files:
#                         print(f"\nSuccessfully saved {len(saved_files)} files:")
#                         for file_path in saved_files:
#                             print(f"  - {file_path}")
#                 else:
#                     print("URL cannot be empty!")
#
#             elif choice == '3':
#                 # Quick generate
#                 url = input("Enter the URL to encode: ").strip()
#                 if url:
#                     print("Generating QR code in PNG format...")
#                     saved_path = quick_generate_qr(url)
#                     if saved_path:
#                         print(f"Quick QR code saved: {saved_path}")
#                         show = input("Display the QR code? (y/n): ").strip().lower()
#                         if show == 'y':
#                             try:
#                                 img = Image.open(saved_path)
#                                 img.show()
#                             except Exception as e:
#                                 print(f"Could not display image: {e}")
#                 else:
#                     print("URL cannot be empty!")
#
#             elif choice == '4':
#                 # Scan from camera
#                 print("\nStarting camera scanner...")
#                 qr_handler.scan_qr_code_from_camera()
#
#             elif choice == '4':
#                 # Scan from image file
#                 image_path = input("Enter the path to the image file: ").strip()
#                 if image_path:
#                     qr_handler.scan_qr_code_from_image(image_path)
#                 else:
#                     print("Image path cannot be empty!")
#
#             elif choice == '5':
#                 print("Goodbye!")
#                 break
#
#             else:
#                 print("Invalid choice! Please enter 1, 2, 3, 4, or 5.")
#
#         except KeyboardInterrupt:
#             print("\n\nProgram interrupted by user. Goodbye!")
#             break
#         except Exception as e:
#             print(f"An unexpected error occurred: {str(e)}")
#
#
# if __name__ == "__main__":
#     # Check if required libraries are available
#     required_modules = {
#         'qrcode': 'qrcode',
#         'cv2': 'opencv-python',
#         'PIL': 'Pillow'
#     }
#
#     missing_modules = []
#     for module, pip_name in required_modules.items():
#         try:
#             __import__(module)
#         except ImportError:
#             missing_modules.append(pip_name)
#
#     if missing_modules:
#         print("Missing required modules. Please install them using:")
#         for module in missing_modules:
#             print(f"pip install {module}")
#         sys.exit(1)
#
#     # Run the main program
#     main()

import qrcode
import cv2
import numpy as np
import urllib.parse
import os
import sys
from PIL import Image


class QRCodeHandler:
    """A comprehensive QR code generator and scanner class."""

    def __init__(self):
        """Initialize the QR code handler."""
        self.qr_detector = cv2.QRCodeDetector()

    def validate_url(self, url):
        """
        Validate if the provided URL is properly formatted.

        Args:
            url (str): The URL to validate

        Returns:
            bool: True if URL is valid, False otherwise
        """
        try:
            result = urllib.parse.urlparse(url)
            return all([result.scheme, result.netloc])
        except Exception:
            return False

    def generate_qr_code(self, url, filename='qrcode.png', size=10, border=4, save_path=None):
        """
        Generate a QR code for the given URL and save it as PNG or JPEG.

        Args:
            url (str): The URL to encode in the QR code
            filename (str): The filename to save the QR code image
            size (int): The size of each box in the QR code
            border (int): The border size around the QR code
            save_path (str): Optional directory path to save the file

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Validate the URL first
            if not self.validate_url(url):
                print(f"Error: Invalid URL format - {url}")
                return False

            # Ensure filename has proper extension
            if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                filename = filename + '.png'
                print(f"Added .png extension. Filename: {filename}")

            # Create QR code instance with custom settings
            qr = qrcode.QRCode(
                version=1,  # Controls the size of the QR code
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=size,
                border=border,
            )

            # Add data to the QR code
            qr.add_data(url)
            qr.make(fit=True)

            # Create an image from the QR code
            qr_image = qr.make_image(fill_color="black", back_color="white")

            # Determine the full file path
            if save_path:
                # Create directory if it doesn't exist
                os.makedirs(save_path, exist_ok=True)
                full_path = os.path.join(save_path, filename)
            else:
                full_path = filename

            # Handle different image formats
            file_ext = os.path.splitext(filename)[1].lower()

            if file_ext in ['.jpg', '.jpeg']:
                # Convert to RGB for JPEG format (removes transparency)
                qr_image = qr_image.convert('RGB')
                qr_image.save(full_path, 'JPEG', quality=95)
                print(f"Saved as JPEG format")
            else:
                # Default to PNG format
                qr_image.save(full_path, 'PNG')
                print(f"Saved as PNG format")

            # Get absolute path for user feedback
            absolute_path = os.path.abspath(full_path)

            print(f"QR code generated successfully!")
            print(f"Saved as: {absolute_path}")
            print(f"QR code contains URL: {url}")
            print(f"File size: {os.path.getsize(full_path)} bytes")

            return True

        except Exception as e:
            print(f"Error generating QR code: {str(e)}")
            return False

    def scan_qr_code_from_camera(self):
        """
        Scan QR codes from camera feed in real-time.

        Returns:
            None
        """
        try:
            # Initialize the camera
            cap = cv2.VideoCapture(0)

            # Check if camera opened successfully
            if not cap.isOpened():
                print("Error: Could not open camera")
                print("Please check if:")
                print("1. Camera is connected properly")
                print("2. Camera is not being used by another application")
                print("3. Camera drivers are installed correctly")
                return

            print("QR Code Scanner started...")
            print("Position a QR code in front of the camera")
            print("Press 'q' to quit the scanner")

            while True:
                # Capture frame from camera
                ret, frame = cap.read()

                if not ret:
                    print("Error: Failed to grab frame from camera")
                    break

                # Detect and decode QR code
                data, bbox, _ = self.qr_detector.detectAndDecode(frame)

                # If QR code is detected
                if data:
                    print(f"\nQR Code detected!")
                    print(f"Data: {data}")

                    # Draw bounding box around detected QR code
                    if bbox is not None:
                        bbox = bbox.astype(int)
                        # Draw the bounding box
                        cv2.polylines(frame, [bbox], True, (0, 255, 0), 2)

                        # Add text showing the decoded data
                        cv2.putText(frame, f"Data: {data[:50]}...",
                                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                                    0.7, (0, 255, 0), 2)

                # Display the frame
                cv2.imshow('QR Code Scanner (Press q to quit)', frame)

                # Break the loop if 'q' key is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # Release the camera and close windows
            cap.release()
            cv2.destroyAllWindows()
            print("QR Code Scanner stopped.")

        except Exception as e:
            print(f"Error during QR code scanning: {str(e)}")
            # Ensure cleanup even if error occurs
            try:
                cap.release()
                cv2.destroyAllWindows()
            except:
                pass

    def scan_qr_code_from_image(self, image_path):
        """
        Scan QR code from a static image file.

        Args:
            image_path (str): Path to the image file containing QR code

        Returns:
            str: Decoded data from QR code, or None if not found
        """
        try:
            # Check if image file exists
            if not os.path.exists(image_path):
                print(f"Error: Image file '{image_path}' not found")
                return None

            # Read the image
            image = cv2.imread(image_path)

            if image is None:
                print(f"Error: Could not read image from '{image_path}'")
                return None

            # Detect and decode QR code
            data, bbox, _ = self.qr_detector.detectAndDecode(image)

            if data:
                print(f"QR Code found in image!")
                print(f"Decoded data: {data}")
                return data
            else:
                print("No QR code found in the image")
                return None

        except Exception as e:
            print(f"Error scanning QR code from image: {str(e)}")
            return None

    def save_qr_in_multiple_formats(self, url, base_filename='qrcode', save_path=None, formats=['png', 'jpg']):
        """
        Generate and save QR code in multiple formats (PNG/JPEG only).

        Args:
            url (str): The URL to encode
            base_filename (str): Base filename without extension
            save_path (str): Directory to save files
            formats (list): List of formats to save ('png', 'jpg', 'jpeg')

        Returns:
            list: List of successfully saved file paths
        """
        saved_files = []

        try:
            # Create QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)

            for fmt in formats:
                try:
                    # Only support PNG and JPEG formats
                    if fmt.lower() not in ['png', 'jpg', 'jpeg']:
                        print(f"Skipping unsupported format: {fmt}")
                        continue

                    filename = f"{base_filename}.{fmt.lower()}"

                    if save_path:
                        os.makedirs(save_path, exist_ok=True)
                        full_path = os.path.join(save_path, filename)
                    else:
                        full_path = filename

                    # Generate QR image
                    qr_image = qr.make_image(fill_color="black", back_color="white")

                    if fmt.lower() in ['jpg', 'jpeg']:
                        # Convert to RGB for JPEG (remove transparency)
                        qr_image = qr_image.convert('RGB')
                        qr_image.save(full_path, 'JPEG', quality=95)
                    else:
                        # PNG format
                        qr_image.save(full_path, 'PNG')

                    saved_files.append(os.path.abspath(full_path))
                    print(f"Saved: {os.path.abspath(full_path)}")

                except Exception as e:
                    print(f"Failed to save as {fmt}: {str(e)}")

            return saved_files

        except Exception as e:
            print(f"Error generating QR code: {str(e)}")
            return saved_files


def quick_generate_qr(url, filename=None, format_type='png'):
    """
    Quick function to generate a QR code in PNG or JPEG format.

    Args:
        url (str): URL to encode
        filename (str): Optional filename. If None, generates based on URL
        format_type (str): 'png' or 'jpeg'/'jpg'

    Returns:
        str: Path to saved file, or None if failed
    """
    handler = QRCodeHandler()

    # Generate filename if not provided
    if not filename:
        # Clean URL for filename
        clean_url = url.replace('https://', '').replace('http://', '').replace('/', '_').replace(':', '')
        filename = f"qr_{clean_url[:20]}.{format_type.lower()}"

    # Ensure proper extension
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        filename = f"{filename}.{format_type.lower()}"

    success = handler.generate_qr_code(url, filename)
    return os.path.abspath(filename) if success else None


def main():
    """Main function to demonstrate QR code generation and scanning."""

    # Create QR code handler instance
    qr_handler = QRCodeHandler()

    print("=== QR Code Generator and Scanner ===")
    print("Supports PNG and JPEG formats only\n")

    while True:
        print("\nChoose an option:")
        print("1. Generate QR code (PNG/JPEG)")
        print("2. Generate QR code in multiple formats")
        print("3. Quick generate (PNG format)")
        print("4. Scan QR code from camera")
        print("5. Scan QR code from image file")
        print("6. Exit")

        try:
            choice = input("\nEnter your choice (1-6): ").strip()

            if choice == '1':
                # Generate QR code
                url = input("Enter the URL to encode: ").strip()
                if url:
                    print("Supported formats: PNG (.png) and JPEG (.jpg, .jpeg)")
                    filename = input("Enter filename with extension (press Enter for 'qrcode.png'): ").strip()
                    if not filename:
                        filename = 'qrcode.png'

                    # Ask for custom save location
                    save_path = input("Enter save directory (press Enter for current directory): ").strip()
                    if not save_path:
                        save_path = None

                    success = qr_handler.generate_qr_code(url, filename, save_path=save_path)
                    if success:
                        # Ask if user wants to display the generated QR code
                        show = input("Display the generated QR code? (y/n): ").strip().lower()
                        if show == 'y':
                            try:
                                if save_path:
                                    full_path = os.path.join(save_path, filename)
                                else:
                                    full_path = filename
                                img = Image.open(full_path)
                                img.show()
                            except Exception as e:
                                print(f"Could not display image: {e}")
                else:
                    print("URL cannot be empty!")

            elif choice == '2':
                # Generate QR code in multiple formats
                url = input("Enter the URL to encode: ").strip()
                if url:
                    base_filename = input("Enter base filename (press Enter for 'qrcode'): ").strip()
                    if not base_filename:
                        base_filename = 'qrcode'

                    save_path = input("Enter save directory (press Enter for current directory): ").strip()
                    if not save_path:
                        save_path = None

                    print("Available formats: png, jpg")
                    formats_input = input("Enter formats separated by commas (press Enter for 'png,jpg'): ").strip()
                    if not formats_input:
                        formats = ['png', 'jpg']
                    else:
                        formats = [f.strip().lower() for f in formats_input.split(',')]

                    saved_files = qr_handler.save_qr_in_multiple_formats(url, base_filename, save_path, formats)
                    if saved_files:
                        print(f"\nSuccessfully saved {len(saved_files)} files:")
                        for file_path in saved_files:
                            print(f"  - {file_path}")
                else:
                    print("URL cannot be empty!")

            elif choice == '3':
                # Quick generate
                url = input("Enter the URL to encode: ").strip()
                if url:
                    print("Generating QR code in PNG format...")
                    saved_path = quick_generate_qr(url)
                    if saved_path:
                        print(f"Quick QR code saved: {saved_path}")
                        show = input("Display the QR code? (y/n): ").strip().lower()
                        if show == 'y':
                            try:
                                img = Image.open(saved_path)
                                img.show()
                            except Exception as e:
                                print(f"Could not display image: {e}")
                else:
                    print("URL cannot be empty!")

            elif choice == '4':
                # Scan from camera
                print("\nStarting camera scanner...")
                qr_handler.scan_qr_code_from_camera()

            elif choice == '5':
                # Scan from image file
                image_path = input("Enter the path to the image file: ").strip()
                if image_path:
                    qr_handler.scan_qr_code_from_image(image_path)
                else:
                    print("Image path cannot be empty!")

            elif choice == '6':
                print("Goodbye!")
                break

            else:
                print("Invalid choice! Please enter 1, 2, 3, 4, 5, or 6.")

        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    # Check if required libraries are available
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
        print("Missing required modules. Please install them using:")
        for module in missing_modules:
            print(f"pip install {module}")
        sys.exit(1)

    # Run the main program
    main()