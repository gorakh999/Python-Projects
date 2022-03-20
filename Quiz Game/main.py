from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_text = item["question"]
    question_answer = item["correct_answer"]
    obj = Question(question_text, question_answer)
    question_bank.append(obj)


quiz = QuizBrain(question_bank)

while (quiz.still_has_question()):
    quiz.next_question()

print("You have Completed the Quiz.")
print(f"Your Final score is {quiz.score}/{quiz.question_no}")