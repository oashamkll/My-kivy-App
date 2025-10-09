from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
import random


class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cell_size = dp(20)
        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.direction = 'RIGHT'
        self.next_direction = 'RIGHT'
        self.food = self.generate_food()
        self.score = 0
        self.high_score = 0
        self.game_over = False
        self.paused = False
        self.game_event = None
        self.game_speed = 0.15
        
    def start_game(self):
        self.snake = [(5, 5), (4, 5), (3, 5)]
        self.direction = 'RIGHT'
        self.next_direction = 'RIGHT'
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False
        self.paused = False
        self.game_speed = 0.15
        if self.game_event:
            self.game_event.cancel()
        self.game_event = Clock.schedule_interval(self.update, self.game_speed)
        
    def get_grid_size(self):
        grid_w = int(self.width / self.cell_size)
        grid_h = int(self.height / self.cell_size)
        return max(10, grid_w), max(10, grid_h)
        
    def generate_food(self):
        grid_w, grid_h = self.get_grid_size()
        max_attempts = grid_w * grid_h * 2
        
        for _ in range(max_attempts):
            food = (random.randint(0, grid_w - 1), random.randint(0, grid_h - 1))
            if food not in self.snake:
                return food
        
        # Если не нашли свободную клетку, ищем любую
        for x in range(grid_w):
            for y in range(grid_h):
                if (x, y) not in self.snake:
                    return (x, y)
        
        # Если вообще нет свободных клеток - возвращаем первую
        return (0, 0)
                
    def change_direction(self, new_direction):
        opposite = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if new_direction != opposite.get(self.direction):
            self.next_direction = new_direction
            
    def toggle_pause(self):
        self.paused = not self.paused
        
    def update(self, dt):
        if self.game_over or self.paused:
            return
            
        self.direction = self.next_direction
        head_x, head_y = self.snake[0]
        
        if self.direction == 'UP':
            new_head = (head_x, head_y + 1)
        elif self.direction == 'DOWN':
            new_head = (head_x, head_y - 1)
        elif self.direction == 'LEFT':
            new_head = (head_x - 1, head_y)
        elif self.direction == 'RIGHT':
            new_head = (head_x + 1, head_y)
            
        grid_w, grid_h = self.get_grid_size()
        
        # Проверка столкновений
        if (new_head[0] < 0 or new_head[0] >= grid_w or 
            new_head[1] < 0 or new_head[1] >= grid_h or 
            new_head in self.snake):
            self.game_over = True
            app = App.get_running_app()
            if self.score > app.high_score:
                app.high_score = self.score
            if self.game_event:
                self.game_event.cancel()
            return
            
        self.snake.insert(0, new_head)
        
        # Проверка на еду
        if new_head == self.food:
            self.score += 10
            self.food = self.generate_food()
            
            # Увеличиваем скорость каждые 50 очков
            if self.score // 50 > (self.score - 10) // 50:
                self.game_speed = max(0.05, self.game_speed * 0.9)
                if self.game_event:
                    self.game_event.cancel()
                self.game_event = Clock.schedule_interval(self.update, self.game_speed)
        else:
            self.snake.pop()
            
        self.draw_game()
        
    def draw_game(self):
        self.canvas.clear()
        with self.canvas:
            # Фон
            Color(0.1, 0.1, 0.15, 1)
            Rectangle(pos=self.pos, size=self.size)
            
            # Еда с пульсацией
            pulse = (1 + 0.2 * abs((Clock.get_boottime() * 2) % 2 - 1))
            food_size = (self.cell_size - 2) * pulse
            offset = (self.cell_size - food_size) / 2
            
            Color(1, 0, 0, 1)
            food_x = self.x + self.food[0] * self.cell_size + offset
            food_y = self.y + self.food[1] * self.cell_size + offset
            Rectangle(pos=(food_x, food_y), size=(food_size, food_size))
            
            # Змейка
            for i, (x, y) in enumerate(self.snake):
                if i == 0:
                    Color(0, 0.9, 0, 1)  # Голова ярче
                else:
                    Color(0, 0.7, 0, 1)  # Тело
                rect_x = self.x + x * self.cell_size + 1
                rect_y = self.y + y * self.cell_size + 1
                Rectangle(pos=(rect_x, rect_y), 
                         size=(self.cell_size - 2, self.cell_size - 2))
            
            # Сетка (полупрозрачная, поверх всего)
            Color(0.15, 0.15, 0.2, 0.3)
            grid_w, grid_h = self.get_grid_size()
            for i in range(grid_w + 1):
                x = self.x + i * self.cell_size
                Rectangle(pos=(x, self.y), size=(1, self.height))
            for i in range(grid_h + 1):
                y = self.y + i * self.cell_size
                Rectangle(pos=(self.x, y), size=(self.width, 1))


class MenuScreen(FloatLayout):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        
        with self.canvas.before:
            Color(0.05, 0.05, 0.1, 1)
            self.bg = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_bg, size=self.update_bg)
        
        layout = BoxLayout(orientation='vertical', spacing=dp(20), 
                          padding=dp(50), size_hint=(0.8, 0.8),
                          pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        title = Label(text='ЗМЕЙКА', font_size=dp(50), 
                     size_hint=(1, 0.3), bold=True,
                     color=(0, 1, 0, 1))
        
        high_score_label = Label(text=f'Рекорд: 0', font_size=dp(30),
                                size_hint=(1, 0.2),
                                color=(1, 1, 0, 1))
        self.app.high_score_label = high_score_label
        
        start_btn = Button(text='НАЧАТЬ ИГРУ', font_size=dp(25),
                          size_hint=(1, 0.25), bold=True,
                          background_color=(0, 0.7, 0, 1),
                          background_normal='')
        start_btn.bind(on_press=self.start_game)
        
        exit_btn = Button(text='ВЫХОД', font_size=dp(25),
                         size_hint=(1, 0.25), bold=True,
                         background_color=(0.7, 0, 0, 1),
                         background_normal='')
        exit_btn.bind(on_press=self.exit_game)
        
        layout.add_widget(title)
        layout.add_widget(high_score_label)
        layout.add_widget(start_btn)
        layout.add_widget(exit_btn)
        
        self.add_widget(layout)
        
    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size
        
    def start_game(self, instance):
        self.app.show_game_screen()
        
    def exit_game(self, instance):
        App.get_running_app().stop()


class GameScreen(FloatLayout):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        
        # Игровое поле
        self.game = SnakeGame(size_hint=(1, 0.7), 
                             pos_hint={'x': 0, 'top': 1})
        self.add_widget(self.game)
        
        # Верхняя панель
        top_panel = BoxLayout(orientation='horizontal', 
                             size_hint=(1, 0.08),
                             pos_hint={'x': 0, 'top': 1},
                             padding=dp(5), spacing=dp(10))
        
        self.score_label = Label(text='Счёт: 0', font_size=dp(20),
                                bold=True, color=(1, 1, 1, 1))
        
        self.pause_btn = Button(text='ПАУЗА', font_size=dp(18),
                               size_hint=(0.3, 1), bold=True,
                               background_color=(0.3, 0.3, 0.8, 1),
                               background_normal='')
        self.pause_btn.bind(on_press=self.toggle_pause)
        
        menu_btn = Button(text='МЕНЮ', font_size=dp(18),
                         size_hint=(0.3, 1), bold=True,
                         background_color=(0.8, 0.3, 0.3, 1),
                         background_normal='')
        menu_btn.bind(on_press=self.back_to_menu)
        
        top_panel.add_widget(self.score_label)
        top_panel.add_widget(self.pause_btn)
        top_panel.add_widget(menu_btn)
        
        self.add_widget(top_panel)
        
        # Панель управления
        self.control_panel = FloatLayout(size_hint=(1, 0.3),
                                   pos_hint={'x': 0, 'y': 0})
        
        btn_size = (0.2, 0.45)
        
        up_btn = self.create_control_button('[size=60]▲[/size]', 
                                          {'center_x': 0.5, 'top': 0.95}, 
                                          'UP')
        
        down_btn = self.create_control_button('[size=60]▼[/size]', 
                                            {'center_x': 0.5, 'y': 0.05}, 
                                            'DOWN')
        
        left_btn = self.create_control_button('[size=60]◀[/size]', 
                                            {'x': 0.15, 'center_y': 0.5}, 
                                            'LEFT')
        
        right_btn = self.create_control_button('[size=60]▶[/size]', 
                                             {'right': 0.85, 'center_y': 0.5}, 
                                             'RIGHT')
        
        self.control_panel.add_widget(up_btn)
        self.control_panel.add_widget(down_btn)
        self.control_panel.add_widget(left_btn)
        self.control_panel.add_widget(right_btn)
        
        self.add_widget(self.control_panel)
        
        # Game Over overlay
        self.game_over_layout = BoxLayout(orientation='vertical',
                                         spacing=dp(20), padding=dp(50),
                                         size_hint=(0.8, 0.5),
                                         pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        with self.game_over_layout.canvas.before:
            Color(0, 0, 0, 0.8)
            self.game_over_bg = Rectangle(pos=self.game_over_layout.pos,
                                         size=self.game_over_layout.size)
        self.game_over_layout.bind(pos=self.update_game_over_bg,
                                  size=self.update_game_over_bg)
        
        game_over_label = Label(text='ИГРА ОКОНЧЕНА', font_size=dp(35),
                               bold=True, color=(1, 0, 0, 1))
        
        self.final_score_label = Label(text='', font_size=dp(25),
                                      color=(1, 1, 1, 1))
        
        restart_btn = Button(text='ЗАНОВО', font_size=dp(22),
                           size_hint=(1, 0.3), bold=True,
                           background_color=(0, 0.7, 0, 1),
                           background_normal='')
        restart_btn.bind(on_press=self.restart_game)
        
        menu_btn2 = Button(text='МЕНЮ', font_size=dp(22),
                          size_hint=(1, 0.3), bold=True,
                          background_color=(0.7, 0.7, 0, 1),
                          background_normal='')
        menu_btn2.bind(on_press=self.back_to_menu)
        
        self.game_over_layout.add_widget(game_over_label)
        self.game_over_layout.add_widget(self.final_score_label)
        self.game_over_layout.add_widget(restart_btn)
        self.game_over_layout.add_widget(menu_btn2)
        
        self.game_over_layout.opacity = 0
        self.add_widget(self.game_over_layout)
        
        Clock.schedule_interval(self.update_score, 0.1)
    
    def create_control_button(self, text, pos_hint, direction):
        btn = Button(text=text, markup=True, bold=True,
                   size_hint=(0.2, 0.45),
                   pos_hint=pos_hint,
                   background_color=(0, 0.6, 0, 1),
                   background_normal='')
        
        def on_press(instance):
            instance.background_color = (0, 0.8, 0, 1)
            self.game.change_direction(direction)
        
        def on_release(instance):
            instance.background_color = (0, 0.6, 0, 1)
        
        btn.bind(on_press=on_press, on_release=on_release)
        return btn
        
    def update_game_over_bg(self, *args):
        self.game_over_bg.pos = self.game_over_layout.pos
        self.game_over_bg.size = self.game_over_layout.size
        
    def update_score(self, dt):
        self.score_label.text = f'Счёт: {self.game.score}'
        
        if self.game.game_over and self.game_over_layout.opacity == 0:
            self.game_over_layout.opacity = 1
            # Отключаем кнопки управления при Game Over
            self.control_panel.disabled = True
            app = App.get_running_app()
            self.final_score_label.text = f'Ваш счёт: {self.game.score}\nРекорд: {app.high_score}'
        
        # Включаем кнопки при рестарте
        elif not self.game.game_over and self.game_over_layout.opacity == 1:
            self.game_over_layout.opacity = 0
            self.control_panel.disabled = False
            
    def toggle_pause(self, instance):
        self.game.toggle_pause()
        if self.game.paused:
            self.pause_btn.text = 'ПРОДОЛЖИТЬ'
            self.pause_btn.background_color = (0.8, 0.5, 0, 1)
        else:
            self.pause_btn.text = 'ПАУЗА'
            self.pause_btn.background_color = (0.3, 0.3, 0.8, 1)
            
    def restart_game(self, instance):
        self.game_over_layout.opacity = 0
        self.control_panel.disabled = False
        self.game.start_game()
        self.pause_btn.text = 'ПАУЗА'
        self.pause_btn.background_color = (0.3, 0.3, 0.8, 1)
        
    def back_to_menu(self, instance):
        if self.game.game_event:
            self.game.game_event.cancel()
        self.app.show_menu_screen()


class SnakeApp(App):
    def build(self):
        self.root_widget = FloatLayout()
        self.menu_screen = MenuScreen(self)
        self.game_screen = None
        self.high_score_label = None
        self.high_score = 0
        
        self.root_widget.add_widget(self.menu_screen)
        return self.root_widget
        
    def show_game_screen(self):
        if self.game_screen:
            self.root_widget.remove_widget(self.game_screen)
        
        self.game_screen = GameScreen(self)
        self.root_widget.remove_widget(self.menu_screen)
        self.root_widget.add_widget(self.game_screen)
        self.game_screen.game.start_game()
        
    def show_menu_screen(self):
        if self.game_screen:
            self.root_widget.remove_widget(self.game_screen)
        
        # Всегда обновляем текст рекорда при показе меню
        if hasattr(self, 'high_score_label') and self.high_score_label:
            self.high_score_label.text = f'Рекорд: {self.high_score}'
        
        self.root_widget.add_widget(self.menu_screen)


if __name__ == '__main__':
    SnakeApp().run()