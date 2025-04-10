import os
import shutil

GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

folders = {
    "c/c99": ".c",
    "c/c++": ".cpp",
    "java/java": ".java",
    "java/javascript": ".js",
    "python": ".py",
}

for folder in folders.keys():
    os.makedirs(folder, exist_ok=True)
    print(f"{BLUE}📁 Pasta verificada/criada: {folder}{RESET}")

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
            print(f"{YELLOW}✏️ Renomeado: {folder_path} → {new_path}{RESET}")

        for folder, extension in folders.items():
        if ext == extension:
            shutil.move(filename, os.path.join(folder, filename))
            print(f"{GREEN}✅ Movido: {filename} → {folder}/{RESET}")
            break
