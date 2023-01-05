import os


TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": [
                "backend.src.database.models", "aerich.models"
            ],
            "default_connection": "default"
        }
    }
}
