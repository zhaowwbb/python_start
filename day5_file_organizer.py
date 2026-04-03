import os
import shutil
def organize_files_by_extension(directory):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    for filename in os.listdir(directory):
        print(f"Processing '{filename}'...")
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1][1:]  
            if ext and ext == 'py':
                ext_dir = os.path.join(directory, ext)
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)
                shutil.copy(file_path, os.path.join(ext_dir, filename))
                print(f"Copied '{filename}' to '{ext_dir}'")
            elif ext and ext == 'txt':
                txt_dir = os.path.join(directory, ext)
                if not os.path.exists(txt_dir):
                    os.makedirs(txt_dir)
                shutil.copy(file_path, os.path.join(txt_dir, filename))
                print(f"Copied '{filename}' to '{txt_dir}'")
            else:
                print(f"'{filename}' has no extension. Skipping.")  

if __name__ == "__main__":
    
    # dir_to_organize = input("Enter the directory to organize: ")
    dir_to_organize = os.getcwd()
    organize_files_by_extension(dir_to_organize)    