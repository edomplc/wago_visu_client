# src/wago_visu_client/__init__.py
__version__ = "0.1.0"

from .api import API as WagoPLC  # Re-export your main class (rename if needed)
from .api import APIConnectionError as ConnectionError  # Public exceptions

__all__ = ["WagoPLC", "APIConnectionError"]  # What users see in dir()