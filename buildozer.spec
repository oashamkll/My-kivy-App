[app]

# Название приложения
title = My App

# Название пакета
package.name = myapp

# Домен пакета
package.domain = com.pashagame

# Исходный код
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf

# Версия приложения
version = 1.0.0

# Зависимости - САМЫЕ СТАБИЛЬНЫЕ ВЕРСИИ
requirements = python3==3.10.10,kivy==2.2.1,kivymd==1.1.1,pillow==9.5.0,certifi

# Ориентация
orientation = portrait

# Иконка (если есть)
#icon.filename = %(source.dir)s/icon.png

# Экран загрузки (если есть)
#presplash.filename = %(source.dir)s/presplash.png

# Разрешения Android
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# СТАБИЛЬНЫЕ версии Android API
android.minapi = 21
android.api = 33
android.ndk = 25b

# Принять SDK лицензии
android.accept_sdk_license = True

# Архитектуры (arm64 для современных устройств, armeabi для старых)
android.archs = arm64-v8a,armeabi-v7a

# Bootstrap
p4a.bootstrap = sdl2

# Ветка python-for-android (СТАБИЛЬНАЯ)
p4a.branch = master

# Директории
#p4a.source_dir = 
#p4a.local_recipes = 

# Логирование
log_level = 2
warn_on_root = 1

[buildozer]

# Директория сборки
# build_dir = ./.buildozer

# Bin директория
# bin_dir = ./bin

# Логи
log_level = 2
warn_on_root = 1
