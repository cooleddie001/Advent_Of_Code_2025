#get the name of the file without extension
import os
def get_input(file_path):
    base_name = os.path.basename(file_path)
    file_name, _ = os.path.splitext(base_name)
    file_name = file_name.split("-")[0] + ".txt"
    try:
        with open(f"Inputs/{file_name}", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        with open(f"../Inputs/{file_name}", "r", encoding="utf-8") as f:
            return f.read()