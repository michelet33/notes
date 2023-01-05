from pydantic import BaseSettings
from dotenv import load_dotenv
import os

# config = dotenv_values()
load_dotenv()


class Settings(BaseSettings):
    url_app: str = os.getenv("URL_APP")
    port_app: int = os.getenv("PORT_APP")
    # url_app: str = config.get("URL_APP")
    # port_app: int = config.get("PORT_APP")
