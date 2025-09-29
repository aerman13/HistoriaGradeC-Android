from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.clearcolor = (0.9, 0.95, 1, 1)

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        title = Label(
            text='[b]ΙΣΤΟΡΙΑ Γ\' ΔΗΜΟΤΙΚΟΥ[/b]',
            markup=True,
            font_size='24sp',
            size_hint_y=None,
            height=80,
            color=(0.1, 0.3, 0.6, 1)
        )
        layout.add_widget(title)
        
        buttons = [
            ("🎯 ΠΑΙΞΕ ΚΟΥΙΖ", "quiz"),
            ("📖 ΔΙΑΔΡΑΣΤΙΚΗ ΙΣΤΟΡΙΑ", "story"), 
            ("📚 ΚΕΦΑΛΑΙΑ", "chapters"),
            ("🏆 ΣΚΟΡ", "scores")
        ]
        
        for text, screen_name in buttons:
            btn = Button(
                text=text,
                size_hint_y=None,
                height=80,
                font_size='18sp',
                background_color=(0.2, 0.6, 0.8, 1)
            )
            btn.bind(on_press=lambda instance, sn=screen_name: self.manager.set_current(sn))
            layout.add_widget(btn)
        
        self.add_widget(layout)

class QuizScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.score = 0
        self.current_question = 0
        
        self.questions = [
            {
                "question": "Ποιος ηταν ο βασιλιας των Τιτανων;",
                "options": ["Ο Διας", "Ο Κρονος", "Ο Ουρανος"],
                "correct": 1
            },
            {
                "question": "Ποιος εδωσε τη φωτια στους ανθρωπους;",
                "options": ["Ο Διας", "Ο Προμηθεας", "Ο Ηφαιστος"],
                "correct": 1
            }
        ]
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        back_btn = Button(
            text='← Πισω',
            size_hint_y=None,
            height=50,
            background_color=(0.8, 0.2, 0.2, 1)
        )
        back_btn.bind(on_press=lambda x: self.manager.set_current('main'))
        layout.add_widget(back_btn)
        
        self.question_label = Label(
            text=self.questions[0]["question"],
            font_size='20sp',
            size_hint_y=None,
            height=100
        )
        layout.add_widget(self.question_label)
        
        self.option_buttons = []
        for i, option in enumerate(self.questions[0]["options"]):
            btn = Button(
                text=option,
                size_hint_y=None,
                height=70,
                font_size='16sp'
            )
            btn.bind(on_press=lambda instance, idx=i: self.check_answer(idx))
            self.option_buttons.append(btn)
            layout.add_widget(btn)
        
        self.score_label = Label(
            text='Σκορ: 0',
            font_size='18sp',
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.score_label)
        
        self.add_widget(layout)
    
    def check_answer(self, selected_idx):
        q = self.questions[self.current_question]
        
        for i, btn in enumerate(self.option_buttons):
            if i == q["correct"]:
                btn.background_color = (0, 0.7, 0, 1)
            elif i == selected_idx:
                btn.background_color = (0.9, 0, 0, 1)
        
        if selected_idx == q["correct"]:
            self.score += 10
        
        self.score_label.text = f'Σκορ: {self.score}'

class HistoriaApp(App):
    def build(self):
        self.title = "Ιστορία Γ' Δημοτικού"
        
        from kivy.uix.screenmanager import ScreenManager
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(QuizScreen(name='quiz'))
        
        sm.set_current = sm.current
        return sm

if __name__ == '__main__':
    HistoriaApp().run()
