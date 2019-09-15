print("Running...")

from . import app

if __name__ == "__main__":
    app_cfg = {
        "debug": True,
        "host": "192.168.8.193",
        "port": "5000",    
    }
    app.run(**app_cfg)

