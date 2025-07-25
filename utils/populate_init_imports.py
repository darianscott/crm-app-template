import os

def populate_init_with_models(folder_path):
    """
    Populates the __init__.py file in the specified folder with import statements for all Python modules in that folder.

    Args:
        folder_path (str): The path to the folder containing the model files.

    This function scans the given folder for all Python files (excluding __init__.py), and writes import statements
    to the __init__.py file to import all contents from each module. This allows for easier access to all models
    when importing from the package.
    """
    model_files = [f for f in os.listdir(folder_path) if f.endswith(".py") and f != "__init__.py"]
    with open(os.path.join(folder_path, "__init__.py"), "w") as init_file:
        for f in model_files:
            model_name = f.replace(".py", "")
            init_file.write(f"from .{model_name} import *\n") 