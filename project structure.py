import os

# Define structure directly in current folder
structure = {
    "backend": {
        "routes": {},
        "utils": {},
        "static": {},
        "app.py": "",
        "models.py": "",
    },
    "frontend": {
        "src": {
            "components": {},
            "pages": {},
            "App.jsx": "",
        },
        "public": {},
    },
    "requirements.txt": "",
    "package.json": "",
}

def create_structure(base_path, tree):
    for name, content in tree.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, "w") as f:
                f.write(content)

# Run from current directory
create_structure(".", structure)
print("✅ Structure created inside KpolitX-cinema-ticketing-system-React-Flask-")