import os
import shutil

target_folder = r"./"

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
    "Audio": [".mp3", ".wav", ".ogg", ".aac"],
    "Compressed": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".ts", ".html", ".css", ".json", ".java", ".cpp", ".cs"],
    "Executables": [".exe", ".msi", ".bat", ".sh"],
    "Unknown": [],
    "Folders": []
}

category_folders = list(categories.keys())

def organize_folder():
    for item in os.listdir(target_folder):
        item_path = os.path.join(target_folder, item)

        if item.startswith('.'):
            continue

        if item in category_folders:
            continue

        if os.path.isdir(item_path):
            destination = os.path.join(target_folder, "Folders")
            os.makedirs(destination, exist_ok=True)
            shutil.move(item_path, os.path.join(destination, item))
            print(f"Moved folder: {item} → Folders")
            continue

        _, ext = os.path.splitext(item)
        ext = ext.lower()
        destination = None

        for category, extensions in categories.items():
            if ext in extensions:
                destination = os.path.join(target_folder, category)
                break

        if not destination:
            destination = os.path.join(target_folder, "Unknown")

        if os.path.dirname(item_path) == destination:
            continue

        os.makedirs(destination, exist_ok=True)
        shutil.move(item_path, os.path.join(destination, item))
        print(f"Moved file: {item} → {os.path.basename(destination)}")

if __name__ == "__main__":
    organize_folder()
    print("✅ Organization completed.")
    input("Press Enter to exit...")
