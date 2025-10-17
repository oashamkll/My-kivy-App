#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import platform

class RedApp(App):
    def build(self):
        # Устанавливаем красный фон для всего приложения
        Window.clearcolor = (1, 0, 0, 1)  # Красный цвет (R, G, B, A)
        
        # Создаем основной layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Добавляем заголовок
        title = Label(
            text='Красное Kivy Приложение',
            font_size='24sp',
            color=(1, 1, 1, 1),  # Белый текст
            size_hint_y=None,
            height=50
        )
        
        # Добавляем описание
        description = Label(
            text='Это приложение собрано с помощью GitHub Actions!',
            font_size='16sp',
            color=(1, 1, 1, 1),  # Белый текст
            text_size=(None, None),
            halign='center',
            valign='middle'
        )
        
        # Добавляем информацию о платформе
        platform_info = Label(
            text=f'Платформа: {platform}',
            font_size='14sp',
            color=(1, 1, 1, 1),  # Белый текст
            size_hint_y=None,
            height=30
        )
        
        # Добавляем все элементы в layout
        layout.add_widget(title)
        layout.add_widget(description)
        layout.add_widget(platform_info)
        
        return layout

if __name__ == '__main__':
    RedApp().run()