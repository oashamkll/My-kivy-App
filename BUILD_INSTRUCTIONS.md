# Инструкции по сборке APK

## Быстрый старт

1. **Клонируйте репозиторий** (если еще не сделано)
2. **Сделайте push в main/master ветку** - GitHub Actions автоматически запустит сборку
3. **Скачайте APK** из раздела Artifacts после успешной сборки

## Локальная сборка

### Требования
- Python 3.9+
- Android SDK
- Buildozer

### Установка зависимостей

```bash
# Установка Python зависимостей
pip install -r requirements.txt

# Или установка buildozer отдельно
pip install buildozer
```

### Сборка APK

```bash
# Инициализация buildozer (если еще не сделано)
buildozer init

# Сборка debug APK
buildozer android debug

# Сборка release APK (требует подписи)
buildozer android release
```

## GitHub Actions

### Доступные workflows

1. **build-apk.yml** - Основной workflow с полной настройкой Android SDK
2. **build-apk-simple.yml** - Упрощенная версия
3. **build-apk-docker.yml** - Docker-based сборка

### Триггеры

- Push в main/master ветку
- Pull Request в main/master ветку  
- Ручной запуск через GitHub Actions UI

### Результаты

После успешной сборки:
- APK файл будет доступен в разделе Artifacts
- Логи сборки будут загружены в случае ошибки

## Структура проекта

```
.
├── main.py                    # Основное Kivy приложение
├── buildozer.spec            # Конфигурация buildozer
├── requirements.txt          # Python зависимости
├── test_app_headless.py      # Headless тесты
├── .github/workflows/        # GitHub Actions workflows
│   ├── build-apk.yml         # Основной workflow
│   ├── build-apk-simple.yml  # Упрощенный workflow
│   └── build-apk-docker.yml  # Docker workflow
├── README.md                 # Основная документация
└── BUILD_INSTRUCTIONS.md     # Этот файл
```

## Особенности приложения

- **Красный фон** на весь экран
- **Белый текст** для контраста
- **Адаптивный дизайн** для мобильных устройств
- **Информация о платформе** (Android/Linux/etc.)

## Устранение неполадок

### Ошибки сборки

1. **Проверьте логи** в GitHub Actions
2. **Убедитесь** что все файлы на месте
3. **Проверьте** версии зависимостей

### Локальные проблемы

1. **Установите Android SDK** если его нет
2. **Проверьте переменные окружения** (ANDROID_HOME, etc.)
3. **Убедитесь** что все системные зависимости установлены

### Тестирование

```bash
# Запуск headless тестов
python3 test_app_headless.py

# Запуск приложения (требует графический интерфейс)
python3 main.py
```

## Поддержка

Если возникли проблемы:
1. Проверьте логи GitHub Actions
2. Убедитесь что все файлы на месте
3. Проверьте версии зависимостей
4. Создайте Issue в репозитории

## Лицензия

MIT License - свободно используйте и модифицируйте код.