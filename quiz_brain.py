class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        max_number_of_questions = len(self.question_list)
        return self.question_number < max_number_of_questions

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text}. (True/False):  ")
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
        else:
            print("That's wrong.")
        print("Correct answer:", correct_answer)

    def score(self):
        if self.check_answer():
            self.score += 1
        print(f"Your current score is {score}/{self.question_number}.")