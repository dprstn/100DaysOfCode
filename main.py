from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import re

QuestionBank = []
Score = 0


def AddUp(question_data):
    if len(question_data) == 0:
        return
    QuestionBank.append(Question(re.compile(r'[^a-zA-Z\s(/)]').sub('', question_data[0]['question']),
                                 question_data[0]['correct_answer']))
    return AddUp(question_data[1:])


AddUp(question_data)
quiz = QuizBrain(QuestionBank)
print(f"{'QUIZ GAME':*^60}")
while quiz._QuestionList:
    if quiz.CheckQuestionAnswer() is True:
        Score += 1
        print('You Got it Right')
    print(f'Score: {Score}/{len(QuestionBank)}')
