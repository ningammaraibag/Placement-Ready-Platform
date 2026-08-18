import os
import shutil
import zipfile

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USER_PROFILE = os.environ.get("USERPROFILE", "C:\\Users\\sony raibag")
DESKTOP_DIR = os.path.join(USER_PROFILE, "Desktop")
OUTPUT_DIR = os.path.join(DESKTOP_DIR, "Placement-Ready-Platform")
ZIP_FILE = os.path.join(DESKTOP_DIR, "Placement-Ready-Platform.zip")

print("Copying project to Desktop for easy access & GitHub upload...")

if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)

shutil.copytree(BASE_DIR, OUTPUT_DIR, ignore=shutil.ignore_patterns('*.pyc', '__pycache__', '.git'))


with zipfile.ZipFile(ZIP_FILE, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(BASE_DIR):
        if '__pycache__' in root:
            continue
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, BASE_DIR)
            zipf.write(file_path, arcname)

print(f"✅ Folder copied to: {OUTPUT_DIR}")
print(f"✅ ZIP file created at: {ZIP_FILE}")
