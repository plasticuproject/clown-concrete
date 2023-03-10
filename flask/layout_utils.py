"""layout_utils.py"""
from typing import Dict


def set_menu(section: str) -> Dict[str, str]:
    """Used to highlight menu option."""
    menuconfig = {}

    if len(section) > 0:
        menuconfig[section] = "active"

    return menuconfig
