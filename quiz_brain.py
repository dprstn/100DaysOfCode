


class QuizBrain:
    def __init__(self, QuestionBank):
        self._QuestionList = QuestionBank
        self._QuestionNumber = 0

    def DisplayNextQuiz(self):
        CurrentQuestion = self._QuestionList[0]
        self._QuestionList = self._QuestionList[1:]
        self._QuestionNumber += 1
        return f'Q.{self._QuestionNumber}\t{CurrentQuestion._text}(True/False) :'

    def CheckQuestionAnswer(self) -> bool:
        return self._QuestionList[0]._answer == input(self.DisplayNextQuiz()).title().strip()
