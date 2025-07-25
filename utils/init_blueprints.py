import importlib
import os

ROUTES_DIR = "routes"

def register_all_blueprints(app):
    for filename in os.listdir(ROUTES_DIR):
        if filename.endswith("_routes.py"):
            module_name = filename[:-3]  # strip ".py"
            module_path = f"{ROUTES_DIR}.{module_name}".replace('/', '.')
            
            mod = importlib.import_module(module_path)
            
            for attr in dir(mod):
                obj = getattr(mod, attr)
                if hasattr(obj, "name") and hasattr(obj, "route"):
                    try:
                        app.register_blueprint(obj)
                        print(f"✔ Registered blueprint: {obj.name}")
                    except Exception as e:
                        print(f"✖ Failed to register blueprint in {module_name}: {e}")
