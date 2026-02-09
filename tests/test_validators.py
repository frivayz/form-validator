"""Тесты для правил валидации формы регистрации."""

import sys
import unittest
from pathlib import Path

# PATH_SETUP: запуск тестов из корня проекта без установки пакета.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from form_validator import validate_email, validate_username
from form_validator.validators import ValidationError


class TestValidateEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertEqual(validate_email("Student@Example.COM"), "student@example.com")

    def test_email_with_plus_and_dots(self):
        self.assertEqual(validate_email(" a.b+tag@mail.ru "), "a.b+tag@mail.ru")

    def test_empty_email_rejected(self):
        with self.assertRaises(ValidationError):
            validate_email("   ")

    def test_email_without_at_rejected(self):
        with self.assertRaises(ValidationError):
            validate_email("student.example.com")

    def test_email_without_domain_zone_rejected(self):
        with self.assertRaises(ValidationError):
            validate_email("student@example")

    def test_non_string_rejected(self):
        with self.assertRaises(ValidationError):
            validate_email(None)


class TestValidateUsername(unittest.TestCase):
    def test_valid_username(self):
        self.assertEqual(validate_username(" student_01 "), "student_01")

    def test_too_short_rejected(self):
        with self.assertRaises(ValidationError):
            validate_username("ab")

    def test_too_long_rejected(self):
        with self.assertRaises(ValidationError):
            validate_username("a" * 21)

    def test_cyrillic_rejected(self):
        with self.assertRaises(ValidationError):
            validate_username("студент")


if __name__ == "__main__":
    unittest.main()
