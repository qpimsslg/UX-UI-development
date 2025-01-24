from textual.app import App, ComposeResult
from textual.widgets import Input, Button, Label, RadioButton, RadioSet, Checkbox
from textual.screen import Screen


class LoginScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Label("Login to access the survey", id="login_label")
        yield Input(placeholder="Username", id="username")
        yield Input(placeholder="Password", password=True, id="password")
        yield Button("Login", id="login_button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        username = self.query_one("#username", Input).value
        password = self.query_one("#password", Input).value

        valid_users = {
            "ruzanna": "helpme",
            "student": "development",
            "1": ""
        }

        if username in valid_users and valid_users[username] == password:
            self.app.push_survey_screen(username)
        else:
            self.query_one("#login_label", Label).update("Invalid login or password!")


class SurveyScreen(Screen):
    def __init__(self, username):
        super().__init__()
        self.username = username

    def compose(self) -> ComposeResult:
        if self.username == "ruzanna":
            yield Label("Вы вошли как Ruzanna")
            yield Button("Пройти тест", id="take_survey_button")
            yield Button("Посмотреть все результаты", id="view_results_button")

        else:
            yield Label("Welcome to the Survey", id="survey_label")

            # Вопрос 1
            yield Label("1. Нравится ли вам дедлайн в 1 день относительно заданий?")
            yield RadioSet(
                RadioButton("нет", id="no"),
                RadioButton("не очень", id="not_really"),
                RadioButton("совсем нет", id="not_at_all"),
                id="deadline_question"
            )

            # Вопрос 2
            yield Label("2. Какие предметы в этом семестре вам нравятся больше всего (можно выбрать несколько вариантов)?")
            yield Checkbox("биология", id="biology")
            yield Checkbox("химия", id="chemistry")
            yield Checkbox("теория вероятностей", id="probability")
            yield Checkbox("web", id="web")
            yield Checkbox("ничего из вышеперечисленного", id="none")

            # Вопрос 3
            yield Label("3. Как вы оцениваете общее качество обучения? (шкала от 1 до 10)")
            yield Input(id="education_quality", placeholder="Введите число от 1 до 10")

            # Серьезные вопросы
            yield Label("А теперь серьезные вопросы")

            # Вопрос 5
            yield Label("5. Какая ты феечка Винкс?")
            yield RadioSet(
                RadioButton("а) Блум", id="bloom"),
                RadioButton("б) Стелла", id="stella"),
                RadioButton("в) Флора", id="flora"),
                RadioButton("в) Техна", id="tecna"),
                RadioButton("г) Лейла", id="layla"),
                RadioButton("д) Муза", id="musa"),
                id="winx_question"
            )

            # Вопрос 6
            yield Label("6. Какая вы шутка про Чака Норриса?")
            yield RadioSet(
                RadioButton("а) Когда Чак Норрис смотрит в бездну, бездна смотрит в другую сторону", id="abyss"),
                RadioButton("б) Однажды динозавры косо посмотрели на Чака Норриса. Ты знаешь, что с ними случилось", id="dinosaurs"),
                RadioButton("в) Слезы Чака Норриса лечат рак. Жаль, что он никогда не плакал", id="tears"),
                RadioButton("г) Таксист подвозивший Чака Норриса намазал спасибо на хлеб!", id="taxi"),
                RadioButton("д) Чак Норрис засунул 2 пальца в розетку и ток ударило Чаком", id="electricity"),
                id="chuck_joke_question"
            )

            # Вопрос 7
            yield Label("7. К вам подбегает очумевший учёный и кричит: «Я всажу свой квантовый гармонизатор в вашу фотонно-резонаторную камеру!» Что вы ответите?")
            yield RadioSet(
                RadioButton("а) Но, доктор, это же вызовет параболическую дестабилизацию сингулярности расщепления!", id="science"),
                RadioButton("б) Чё? И туда тебя, козел!", id="eloquence"),
                RadioButton("в) Без разговоров оглушить ученого, огрев его по голове ближайшим тяжелым предметом. Откуда вы знаете: вдруг он собирался взорвать убежище?"
                            , id="bladed_weapon"),
                RadioButton("г) Промолчать и быстренько удалиться, пока ученый не продолжил свою тираду", id="stealth"),
                id="shelter_question"
            )

            yield Button("Submit", id="submit_button")


    def on_button_pressed(self, event: Button.Pressed) -> None:
        if self.username == "ruzanna":
            if event.button.id == "take_survey_button":
                self.app.push_screen("survey_questions", self.username)
            elif event.button.id == "view_results_button":
                self.app.push_screen(ResultScreen({}, self.username), "results")
        else:
            answers = {}

            # Вопрос 1
            deadline_question = self.query_one("#deadline_question", RadioSet)._selected
            answers['deadline_question'] = deadline_question

            # Вопрос 2 (множественный выбор)
            subjects = []
            for subj_id in ['biology', 'chemistry', 'probability', 'web', 'none']:
                if self.query_one(f"#{subj_id}", Checkbox).value:
                    subjects.append(subj_id)
            answers['subjects'] = subjects

            # Вопрос 3
            education_quality = self.query_one("#education_quality", Input).value
            answers['education_quality'] = education_quality

            # Вопрос 5
            winx_question = self.query_one("#winx_question", RadioSet)._selected
            answers['winx_question'] = winx_question

            # Вопрос 6
            chuck_joke_question = self.query_one("#chuck_joke_question", RadioSet)._selected
            answers['chuck_joke_question'] = chuck_joke_question

            # Вопрос 7
            shelter_question = self.query_one("#shelter_question", RadioSet)._selected
            answers['shelter_question'] = shelter_question

            print("Survey answers:", answers)

            self.app.push_screen(ResultScreen(answers, self.username))
        self.app.push_screen(ResultScreen(answers, self.username), "results")


class ResultScreen(Screen):
    def __init__(self, answers, username):
        super().__init__()
        self.answers = answers
        self.username = username

    def compose(self) -> ComposeResult:
        if self.username == "ruzanna":
            yield Label("Все ответы на опрос:", id="result_label")
            # Здесь выведем все результаты, например, из базы данных или другого источника
        else:
            yield Label("Спасибо за внимание! Надеюсь вам понравился опрос :)", id="thank_you_label")

        yield Button("Назад", id="back_button")


    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back_button":
            self.app.pop_screen()

class SurveyApp(App):
    def on_mount(self) -> None:
        self.install_screen(LoginScreen(), "login")
        self.push_screen("login")

    def push_survey_screen(self, username: str):
        survey_screen = SurveyScreen(username)
        self.install_screen(survey_screen,"survey")
        self.push_screen("survey")


if __name__ == "__main__":
    app = SurveyApp()
    app.run()