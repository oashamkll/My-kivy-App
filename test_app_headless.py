#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Headless тест для проверки работы Kivy приложения
"""

import sys
import os

def test_imports():
    """Тестируем импорты"""
    try:
        # Устанавливаем headless режим для Kivy
        os.environ['KIVY_WINDOW'] = 'sdl2'
        os.environ['KIVY_GL_BACKEND'] = 'gl'
        
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
        # Устанавливаем headless режим
        os.environ['KIVY_WINDOW'] = 'sdl2'
        os.environ['KIVY_GL_BACKEND'] = 'gl'
        
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

def test_github_workflows():
    """Проверяем наличие GitHub workflows"""
    workflows = [
        '.github/workflows/build-apk.yml',
        '.github/workflows/build-apk-simple.yml',
        '.github/workflows/build-apk-docker.yml'
    ]
    
    found = 0
    for workflow in workflows:
        if os.path.exists(workflow):
            found += 1
            print(f"✓ {workflow} найден")
        else:
            print(f"✗ {workflow} не найден")
    
    return found == len(workflows)

def main():
    """Запускаем все тесты"""
    print("Запуск headless тестов для Kivy приложения...")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_app_creation,
        test_buildozer_config,
        test_requirements,
        test_github_workflows
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 60)
    print(f"Результат: {passed}/{total} тестов пройдено")
    
    if passed == total:
        print("✓ Все тесты пройдены успешно!")
        print("\nПриложение готово для сборки APK через GitHub Actions!")
        return 0
    else:
        print("✗ Некоторые тесты не пройдены")
        return 1

if __name__ == '__main__':
    sys.exit(main())