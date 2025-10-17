# Красное Kivy Приложение

Простое приложение на Python Kivy с красным фоном, которое автоматически собирается в APK с помощью GitHub Actions.

## Описание

Это приложение демонстрирует:
- Создание простого Kivy приложения с красным фоном
- Настройку buildozer для сборки Android APK
- Автоматическую сборку APK через GitHub Actions

## Структура проекта

```
.
├── main.py                 # Основное приложение Kivy
├── buildozer.spec         # Конфигурация buildozer для сборки APK
├── requirements.txt       # Python зависимости
├── .github/workflows/     # GitHub Actions workflows
│   ├── build-apk.yml      # Основной workflow
│   ├── build-apk-simple.yml # Упрощенный workflow
│   └── build-apk-docker.yml # Docker-based workflow
└── README.md              # Этот файл
```

## Локальная разработка

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Запуск приложения

```bash
python main.py
```

### Локальная сборка APK

1. Установите buildozer:
```bash
pip install buildozer
```

2. Инициализируйте buildozer:
```bash
buildozer init
```

3. Соберите APK:
```bash
buildozer android debug
```

## GitHub Actions

Проект настроен для автоматической сборки APK при каждом push в main/master ветку.

### Доступные workflows:

1. **build-apk.yml** - Основной workflow с полной настройкой Android SDK
2. **build-apk-simple.yml** - Упрощенная версия
3. **build-apk-docker.yml** - Docker-based сборка

### Как использовать:

1. Сделайте push в main/master ветку
2. GitHub Actions автоматически запустит сборку
3. После успешной сборки APK будет доступен в разделе Artifacts

## Требования

- Python 3.9+
- Kivy 2.1.0+
- Buildozer 1.5.0+
- Android SDK (для локальной сборки)

## Особенности приложения

- Красный фон на весь экран
- Белый текст для контраста
- Отображение информации о платформе
- Адаптивный дизайн для мобильных устройств

## Поддержка платформ

- Android (APK)
- Linux (для разработки)
- Windows (для разработки)
- macOS (для разработки)

## Лицензия

MIT License