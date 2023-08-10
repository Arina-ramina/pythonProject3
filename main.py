from additional_methods import load_questions, statistik
import random

if __name__ == '__main__':
    filename = 'questions.json'
    questions = load_questions(filename)
    random.shuffle(questions)

    for question in questions:
        print(question.build_question())
        user_answer=input()
        question.user_answer=user_answer
        print (question.build_feedback())
        print ('')

    print (statistik(questions))





