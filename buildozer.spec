[app]

title = Snake By Pasha
package.name = snake
package.domain = com.pashagame
source.dir = .
source.main = main.py
version = 1.0.0

requirements = python3,kivy==2.3.0

android.arch = armeabi-v7a
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b

android.permissions = INTERNET
android.features = android.hardware.touchscreen

fullscreen = 0
orientation = portrait

android.build_tools_version = 30.0.3

presplash.filename = %(source.dir)s/presplash.png
icon.filename = %(source.dir)s/icon.png

log_level = 1

[buildozer]
log_level = 1
build_dir = .buildozer
bin_dir = ./bin

[app-source]
source.include_exts = py,png,jpg,kv,atlas,ttf,json
source.exclude_dirs = tests, bin, docs, .buildozer, .git, venv

[android]
android.allow_backup = True
android.entrypoint = org.kivy.android.PythonActivity
