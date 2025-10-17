#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Простой тест для проверки работы Kivy приложения
"""

import sys
import os

def test_imports():
    """Тестируем импорты"""
    try:
        from kivy.app import App
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        from kivy.core.window import Window
        from kivy.utils import platform
        print("✓ Все импорты успешны")
        return True
    except ImportError as e:
        print(f"✗ Ошибка импорта: {e}")
        return False

def test_app_creation():
    """Тестируем создание приложения"""
    try:
        from main import RedApp
        app = RedApp()
        print("✓ Приложение создается успешно")
        return True
    except Exception as e:
        print(f"✗ Ошибка создания приложения: {e}")
        return False

def test_buildozer_config():
    """Проверяем наличие buildozer.spec"""
    if os.path.exists('buildozer.spec'):
        print("✓ buildozer.spec найден")
        return True
    else:
        print("✗ buildozer.spec не найден")
        return False

def test_requirements():
    """Проверяем requirements.txt"""
    if os.path.exists('requirements.txt'):
        print("✓ requirements.txt найден")
        return True
    else:
        print("✗ requirements.txt не найден")
        return False

def main():
    """Запускаем все тесты"""
    print("Запуск тестов для Kivy приложения...")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_app_creation,
        test_buildozer_config,
        test_requirements
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"Результат: {passed}/{total} тестов пройдено")
    
    if passed == total:
        print("✓ Все тесты пройдены успешно!")
        return 0
    else:
        print("✗ Некоторые тесты не пройдены")
        return 1

if __name__ == '__main__':
    sys.exit(main())