import os
from datetime import datetime

def ensure_init_files(base_dir=("models", "services", "api", "blueprints"), log_dir="logs/init_creation_logs"):
    """
    Walks through base_dir and ensures each folder containing .py files
    (but no __init__.py) gets an __init__.py file. Logs all changes.
    """

    # Create log directory if it doesn’t exist
    os.makedirs(log_dir, exist_ok=True)

    # Create a timestamped log file
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = os.path.join(log_dir, f"init_creation_log_{timestamp}.txt")

    created = []

    with open(log_path, "w") as log:
        log.write(f"[Init File Creation Log - {timestamp}]\n\n")
        for root, dirs, files in os.walk(base_dir):
            has_py_files = any(f.endswith(".py") for f in files)
            has_init = "__init__.py" in files

            if has_py_files and not has_init:
                init_path = os.path.join(root, "__init__.py")
                with open(init_path, "w") as init_file:
                    init_file.write("# Auto-generated __init__.py\n")
                log.write(f"Created: {init_path}\n")
                created.append(init_path)

        if not created:
            log.write("No missing __init__.py files found.\n")

    print(f"Init creation complete. Log saved to: {log_path}")