[app]
# (str) Название вашего приложения
title = Myapp

# (str) Версия вашего приложения
version = 0.1

# (str) Имя пакета в формате домена
package.name = com.pasha.myapp

# (str) Идентификатор пакета в формате домена
package.domain = com.pasha

# (str) Имя автора
author = Pasha

# (str) Электронная почта автора
author.email = your.email@example.com

# (list) Требования для сборки (например, kivy)
requirements = python3,kivy

# (str) Ориентация экрана
orientation = portrait

# (str) Путь к главному файлу Python
source.dir = .

# (str) Путь к иконке приложения (по умолчанию: data/icon.png)
icon.filename = %(source.dir)s/icon.png

# (int) Минимальный API Android (например, 21 для Android 5.0)
android.minapi = 21

# (int) Целевой API Android (например, 33 для Android 13)
android.targetsdk = 33

# (str) Версия NDK Android
android.ndk = 23b

[buildozer]
# (list) Требования для сборки (только для Buildozer)
requirements =

[android]
# (bool) Указывает, нужно ли использовать Kivy service
services = False

# (int) Версия SDK Android
sdk = 33

# (bool) Использовать или нет `python-for-android` master
# (иначе используется стабильная ветка)
# p4a.use_master = 1
