class Question:
    def __init__ (self, text, health_question, correct_answer):
        self.text = text
        self.health_question = health_question
        self.correct_answer = correct_answer

        self.question_asked = False
        self.user_answer = None
        self.points = self.health_question * 10

    def get_points(self):
        return self.points
    def is_correct(self):
        return self.correct_answer == self.user_answer

    def build_question(self):
        return f'Вопрос: {self.text}\n' \
               f'Сложность: {self.health_question}/5'

    def build_feedback(self):
        if self.is_correct():
             return f'Ответ верный, получено {self.points} баллов'
        return f'Ответ неверный, верный ответ - {self.correct_answer}'






