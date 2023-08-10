import json
from questions import Question

def load_questions(filename):
    """Чтение данных из JSON файла
       Args:
       filename: имя файла (questions.json)
       Returns: декодированный список вопросов в формате list """
    with open(filename, encoding='utf-8') as f:
        data=json.load(f)

    questions=[]
    for i in data:
        text = i["q"]
        health_question = int(i["d"])
        correct_answer = i["a"]
        questions.append(Question(text, health_question, correct_answer))

    return questions

def statistik(questions):
    '''возвращает количество набранных баллов и количество правильных ответов пользователя'''

    total_questions = 0 #количество правильных ответов пользователя
    points_user=0 # количество набранных баллов

    for question in questions:
        if question.is_correct():
            points_user+=question.points
            total_questions += 1

    return f'Вот и всё!\n' \
           f'Отвечено {total_questions} вопроса из {len(questions)}\n' \
           f'Набрано баллов: {points_user}'
