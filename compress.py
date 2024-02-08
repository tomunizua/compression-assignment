import os
import shutil
import tarfile
import zipfile
from datetime import datetime

def compress_folder(folder_path, compress_type):
    folder_name = os.path.basename(folder_path)
    current_date = datetime.now().strftime("%Y_%m_%d")
    compressed_filename = f"{folder_name}_{current_date}.{compress_type}"

    try:
        if compress_type == "zip":
            with zipfile.ZipFile(compressed_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, _, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, os.path.relpath(file_path, folder_path))
        elif compress_type == "tar":
            with tarfile.open(compressed_filename, 'w') as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))
        elif compress_type == "tgz":
            with tarfile.open(compressed_filename, 'w:gz') as tar:
                tar.add(folder_path, arcname=os.path.basename(folder_path))
        else:
            print("Unsupported compression type.")
            return False

        print(f"Compression successful. Compressed file saved as '{compressed_filename}'.")
        return True
    except Exception as e:
        print(f"Compression failed: {str(e)}")
        return False

def main():
    folder_path = input("Enter the path of the folder to compress: ")
    if not os.path.exists(folder_path):
        print("Error: Folder not found.")
        return

    print("Available compressed file types:")
    print("1. zip")
    print("2. tar")
    print("3. tgz")

    compress_type = input("Select the desired compressed file type (zip/tar/tgz): ").lower()

    if compress_type not in ["zip", "tar", "tgz"]:
        print("Invalid compressed file type selected.")
        return

    compress_folder(folder_path, compress_type)

if __name__ == "__main__":
    main()
