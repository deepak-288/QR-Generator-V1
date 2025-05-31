#
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
# #             # Ensure filename has proper extension
# #             if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
# #                 filename = filename + '.png'
# #                 print(f"Added .png extension. Filename: {filename}")
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
# #             # Handle different image formats
# #             file_ext = os.path.splitext(filename)[1].lower()
# #
# #             if file_ext in ['.jpg', '.jpeg']:
# #                 # Convert to RGB for JPEG format (removes transparency)
# #                 qr_image = qr_image.convert('RGB')
# #                 qr_image.save(full_path, 'JPEG', quality=95)
# #                 print(f"Saved as JPEG format")
# #             else:
# #                 # Default to PNG format
# #                 qr_image.save(full_path, 'PNG')
# #                 print(f"Saved as PNG format")
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
# #
# # def quick_generate_qr(url, filename=None, format_type='png'):
# #     """
# #     Quick function to generate a QR code in PNG or JPEG format.
# #
# #     Args:
# #         url (str): URL to encode
# #         filename (str): Optional filename. If None, generates based on URL
# #         format_type (str): 'png' or 'jpeg'/'jpg'
# #
# #     Returns:
# #         str: Path to saved file, or None if failed
# #     """
# #     handler = QRCodeHandler()
# #
# #     # Generate filename if not provided
# #     if not filename:
# #         # Clean URL for filename
# #         clean_url = url.replace('https://', '').replace('http://', '').replace('/', '_').replace(':', '')
# #         filename = f"qr_{clean_url[:20]}.{format_type.lower()}"
# #
# #     # Ensure proper extension
# #     if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
# #         filename = f"{filename}.{format_type.lower()}"
# #
# #     success = handler.generate_qr_code(url, filename)
# #     return os.path.abspath(filename) if success else None
# #
# #     except Exception as e:
# #     print(f"Error generating QR code: {str(e)}")
# #     return saved_files
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
# #         print("1. Generate QR code (PNG/JPEG)")
# #         print("2. Generate QR code in multiple formats")
# #         print("3. Quick generate (PNG format)")
# #         print("4. Scan QR code from camera")
# #         print("5. Scan QR code from image file")
# #         print("6. Exit")
# #
# #         try:
# #             choice = input("\nEnter your choice (1-6): ").strip()
# #
# #             if choice == '1':
# #                 # Generate QR code
# #                 url = input("Enter the URL to encode: ").strip()
# #                 if url:
# #                     print("Supported formats: PNG (.png) and JPEG (.jpg, .jpeg)")
# #                     filename = input("Enter filename with extension (press Enter for 'qrcode.png'): ").strip()
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
# #                     print("Available formats: png, jpg (recommended formats)")
# #                     formats_input = input("Enter formats separated by commas (press Enter for 'png,jpg'): ").strip()
# #                     if not formats_input:
# #                         formats = ['png', 'jpg']
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
# #                 # Quick generate
# #                 url = input("Enter the URL to encode: ").strip()
# #                 if url:
# #                     print("Generating QR code in PNG format...")
# #                     saved_path = quick_generate_qr(url)
# #                     if saved_path:
# #                         print(f"Quick QR code saved: {saved_path}")
# #                         show = input("Display the QR code? (y/n): ").strip().lower()
# #                         if show == 'y':
# #                             try:
# #                                 img = Image.open(saved_path)
# #                                 img.show()
# #                             except Exception as e:
# #                                 print(f"Could not display image: {e}")
# #                 else:
# #                     print("URL cannot be empty!")
# #
# #             elif choice == '4':
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
#
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
#         Generate a QR code for the given URL and save it as PNG or JPEG.
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
#     def save_qr_in_multiple_formats(self, url, base_filename='qrcode', save_path=None, formats=['png', 'jpg']):
#         """
#         Generate and save QR code in multiple formats (PNG/JPEG only).
#
#         Args:
#             url (str): The URL to encode
#             base_filename (str): Base filename without extension
#             save_path (str): Directory to save files
#             formats (list): List of formats to save ('png', 'jpg', 'jpeg')
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
#                     # Only support PNG and JPEG formats
#                     if fmt.lower() not in ['png', 'jpg', 'jpeg']:
#                         print(f"Skipping unsupported format: {fmt}")
#                         continue
#
#                     filename = f"{base_filename}.{fmt.lower()}"
#
#                     if save_path:
#                         os.makedirs(save_path, exist_ok=True)
#                         full_path = os.path.join(save_path, filename)
#                     else:
#                         full_path = filename
#
#                     # Generate QR image
#                     qr_image = qr.make_image(fill_color="black", back_color="white")
#
#                     if fmt.lower() in ['jpg', 'jpeg']:
#                         # Convert to RGB for JPEG (remove transparency)
#                         qr_image = qr_image.convert('RGB')
#                         qr_image.save(full_path, 'JPEG', quality=95)
#                     else:
#                         # PNG format
#                         qr_image.save(full_path, 'PNG')
#
#                     saved_files.append(os.path.abspath(full_path))
#                     print(f"Saved: {os.path.abspath(full_path)}")
#
#                 except Exception as e:
#                     print(f"Failed to save as {fmt}: {str(e)}")
#
#             return saved_files
#
#         except Exception as e:
#             print(f"Error generating QR code: {str(e)}")
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
#
# def main():
#     """Main function to demonstrate QR code generation and scanning."""
#
#     # Create QR code handler instance
#     qr_handler = QRCodeHandler()
#
#     print("=== QR Code Generator and Scanner ===")
#     print("Supports PNG and JPEG formats only\n")
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
#                     print("Available formats: png, jpg")
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
#             elif choice == '5':
#                 # Scan from image file
#                 image_path = input("Enter the path to the image file: ").strip()
#                 if image_path:
#                     qr_handler.scan_qr_code_from_image(image_path)
#                 else:
#                     print("Image path cannot be empty!")
#
#             elif choice == '6':
#                 print("Goodbye!")
#                 break
#
#             else:
#                 print("Invalid choice! Please enter 1, 2, 3, 4, 5, or 6.")
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
        current_time = tk.Tk().tk.call('clock', 'format', tk.Tk().tk.call('clock', 'seconds'))

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
        root = tk.Tk()
        root.withdraw()  # Hide main window
        messagebox.showerror(
            "Missing Dependencies",
            f"Please install the following modules:\n\n" +
            "\n".join([f"pip install {module}" for module in missing_modules])
        )
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