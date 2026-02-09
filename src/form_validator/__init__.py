"""Валидация полей формы регистрации.

Учебный проект для лабораторной работы №3
«Совместная работа над кодом: отслеживание задач и рецензирование».
"""

from .validators import validate_email, validate_username

__all__ = ["validate_email", "validate_username"]
__version__ = "0.1.0"
