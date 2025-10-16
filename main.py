from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.card import MDCard
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivymd.uix.toolbar import MDTopAppBar


class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Основной layout с отступами
        main_layout = BoxLayout(
            orientation='vertical',
            padding=dp(20),
            spacing=dp(15)
        )
        
        # Верхняя панель
        toolbar = MDTopAppBar(
            title="Моё Приложение",
            elevation=2,
            md_bg_color=(0.2, 0.6, 1, 1)
        )
        main_layout.add_widget(toolbar)
        
        # Карточка с контентом
        card = MDCard(
            orientation='vertical',
            padding=dp(20),
            spacing=dp(15),
            size_hint=(1, None),
            height=dp(400),
            elevation=3,
            radius=[dp(15)]
        )
        
        # Заголовок
        title = MDLabel(
            text="Добро пожаловать!",
            font_style="H5",
            halign="center",
            theme_text_color="Primary",
            size_hint_y=None,
            height=dp(50)
        )
        card.add_widget(title)
        
        # Описание
        description = MDLabel(
            text="Это простое адаптивное приложение на KivyMD.\nОно работает на любом размере экрана!",
            halign="center",
            theme_text_color="Secondary",
            size_hint_y=None,
            height=dp(60)
        )
        card.add_widget(description)
        
        # Поле ввода
        self.text_field = MDTextField(
            hint_text="Введите ваше имя",
            helper_text="Это обязательное поле",
            helper_text_mode="on_focus",
            icon_right="account",
            size_hint_x=1,
            size_hint_y=None,
            height=dp(50)
        )
        card.add_widget(self.text_field)
        
        # Метка для вывода результата
        self.result_label = MDLabel(
            text="",
            halign="center",
            theme_text_color="Primary",
            font_style="H6",
            size_hint_y=None,
            height=dp(40)
        )
        card.add_widget(self.result_label)
        
        # Кнопка
        button = MDRaisedButton(
            text="НАЖМИ МЕНЯ",
            pos_hint={'center_x': 0.5},
            size_hint=(0.8, None),
            height=dp(50),
            on_release=self.on_button_click
        )
        card.add_widget(button)
        
        # Добавляем карточку в основной layout
        main_layout.add_widget(card)
        
        # Нижняя панель с иконками
        bottom_box = BoxLayout(
            size_hint=(1, None),
            height=dp(60),
            spacing=dp(10),
            padding=[dp(20), 0]
        )
        
        icon1 = MDIconButton(
            icon="home",
            pos_hint={'center_y': 0.5},
            on_release=lambda x: self.show_message("Домой")
        )
        icon2 = MDIconButton(
            icon="star",
            pos_hint={'center_y': 0.5},
            on_release=lambda x: self.show_message("Избранное")
        )
        icon3 = MDIconButton(
            icon="cog",
            pos_hint={'center_y': 0.5},
            on_release=lambda x: self.show_message("Настройки")
        )
        
        bottom_box.add_widget(icon1)
        bottom_box.add_widget(icon2)
        bottom_box.add_widget(icon3)
        
        main_layout.add_widget(bottom_box)
        
        self.add_widget(main_layout)
    
    def on_button_click(self, instance):
        name = self.text_field.text
        if name:
            self.result_label.text = f"Привет, {name}! 👋"
        else:
            self.result_label.text = "Пожалуйста, введите имя"
    
    def show_message(self, message):
        self.result_label.text = f"Нажато: {message}"


class MyApp(MDApp):
    def build(self):
        # Настройка темы
        self.theme_cls.theme_style = "Light"  # Light или Dark
        self.theme_cls.primary_palette = "Blue"
        
        return MainScreen()


if __name__ == '__main__':
    MyApp().run()
