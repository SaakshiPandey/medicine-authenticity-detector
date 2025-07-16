import os

def shorten_filenames(folder_path, prefix='img'):
    if not os.path.exists(folder_path):
        print(f"Folder does not exist: {folder_path}")
        return

    files = sorted(os.listdir(folder_path))
    for idx, filename in enumerate(files):
        old_path = os.path.join(folder_path, filename)
        if os.path.isfile(old_path):
            ext = os.path.splitext(filename)[1]
            new_name = f"{prefix}_{str(idx).zfill(4)}{ext}"
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {new_name}")

# Rename image files
shorten_filenames("data/counterfeit_med_detection/train/images")
shorten_filenames("data/counterfeit_med_detection/test/images")
shorten_filenames("data/counterfeit_med_detection/valid/images")

# Rename label files
shorten_filenames("data/counterfeit_med_detection/train/labels")
shorten_filenames("data/counterfeit_med_detection/test/labels")
shorten_filenames("data/counterfeit_med_detection/valid/labels")
