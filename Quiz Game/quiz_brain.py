class QuizBrain:

    def __init__(self, question_bank):
        self.question_no = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_question(self):
        if (self.question_no != len(self.question_list)):
            return True
        return False

    def next_question(self):
        question = self.question_list[self.question_no]
        self.question_no += 1
        user_ans = input(f"Q.{self.question_no}: {question.text} (True / False) : ")
        self.check_score(user_ans, question.answer)

    def check_score(self, user_ans, correct_ans):
        if (user_ans.lower() == correct_ans.lower()):
            print("You got it Right.")
            self.score += 1

        else:
            print("That's Wrong.")
        
        print(f"The Correct answer was {correct_ans}")
        print(f"Your Current Score is {self.score}/{self.question_no}")
        print()
        