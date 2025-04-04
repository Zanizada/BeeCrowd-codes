import os
import shutil

folders = {
    "python": ".py",
    "c": ".c",
    "java": ".java"
}

for folder in folders.keys():
    os.makedirs(folder, exist_ok=True)

for filename in os.listdir():
    if not os.path.isfile(filename):
        continue

    if filename == "organizar.py":
        continue
    
    name, ext = os.path.splitext(filename)
    
    for folder, extension in folders.items():
        folder_path = os.path.join(folder, filename)
        
        if ext == "" and os.path.exists(folder_path):
            new_filename = f"{filename}{extension}"
            new_path = os.path.join(folder, new_filename)
            os.rename(folder_path, new_path)
            print(f"Renomeado: {folder_path} → {new_path}")

    if ext in folders.values():
        target_folder = [key for key, value in folders.items() if value == ext][0]
        shutil.move(filename, os.path.join(target_folder, filename))
        print(f"Movido: {filename} → {target_folder}/")
