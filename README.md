# Form Validator

Учебный проект для лабораторной работы №3 — демонстрация полного цикла
работы над задачей: Issue → ветка → коммиты → Pull Request → Code Review → Merge.

## Возможности

| Поле | Правило |
|------|---------|
| `email` | формат `name@domain.zone`, нормализуется в нижний регистр |
| `username` | 3–20 символов: латиница, цифры, подчёркивание |

## Структура

```
form-validator/
├── src/form_validator/     # исходный код
│   ├── __init__.py
│   └── validators.py
├── tests/                  # тесты
│   └── test_validators.py
└── README.md
```

## Запуск тестов

```bash
python -m unittest discover -s tests -v
```

## Лицензия

MIT
