"""Правила валидации полей формы регистрации."""

import re

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
USERNAME_RE = re.compile(r"^[A-Za-z0-9_]{3,20}$")


class ValidationError(ValueError):
    """Ошибка валидации поля формы."""


def validate_email(value: str) -> str:
    """Проверяет адрес электронной почты.

    :param value: проверяемое значение
    :return: нормализованный адрес (в нижнем регистре)
    :raises ValidationError: если адрес не соответствует формату
    """
    if not isinstance(value, str):
        raise ValidationError("Email должен быть строкой")

    normalized = value.strip().lower()
    if not normalized:
        raise ValidationError("Email не может быть пустым")

    if not EMAIL_RE.match(normalized):
        raise ValidationError(f"Некорректный email: {value!r}")

    return normalized


def validate_username(value: str) -> str:
    """Проверяет имя пользователя (3-20 символов, латиница, цифры, подчёркивание)."""
    if not isinstance(value, str):
        raise ValidationError("Имя пользователя должно быть строкой")

    value = value.strip()
    if not USERNAME_RE.match(value):
        raise ValidationError(
            "Имя пользователя должно содержать от 3 до 20 символов: "
            "латиница, цифры или подчёркивание"
        )

    return value


PHONE_DIGITS_RE = re.compile(r"\D")


def validate_phone(value: str) -> str:
    """Проверяет номер телефона и приводит его к формату +7XXXXXXXXXX.

    :param value: проверяемое значение
    :return: нормализованный номер
    :raises ValidationError: если номер не соответствует формату
    """
    if not isinstance(value, str):
        raise ValidationError("Телефон должен быть строкой")

    digits = PHONE_DIGITS_RE.sub("", value)

    if len(digits) == 11 and digits[0] in "78":
        digits = "7" + digits[1:]
    elif len(digits) == 10:
        digits = "7" + digits
    else:
        raise ValidationError(f"Некорректный номер телефона: {value!r}")

    return "+" + digits
