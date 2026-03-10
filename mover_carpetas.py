import os
import shutil

# Define the source and destination folder paths
# source_folder: the folder you want to move
# destination_folder: the location where it will be moved
source_folder = r"D:\carpeta de origen"
destination_folder = r"D:\carpeta de destino"

# Validate that the source folder exists
if not os.path.exists(source_folder):
    print(f"Error: La carpeta de origen no existe: {source_folder}")
else:
    # Create the destination parent directory if it does not exist
    os.makedirs(destination_folder, exist_ok=True)

    # Build the full destination path (keeps the source folder name)
    folder_name = os.path.basename(source_folder)
    dest_path = os.path.join(destination_folder, folder_name)

    # Check that the destination path does not already exist
    if os.path.exists(dest_path):
        print(f"Error: Ya existe una carpeta en el destino: {dest_path}")
    else:
        try:
            shutil.move(source_folder, dest_path)
            print(f"Carpeta movida exitosamente: '{source_folder}' -> '{dest_path}'")
        except (OSError, PermissionError, shutil.Error) as e:
            print(f"Error al mover la carpeta: {e}")
