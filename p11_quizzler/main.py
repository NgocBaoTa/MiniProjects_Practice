from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from view import QuizInterface

question_blank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_blank.append(new_question)


quiz = QuizBrain(question_blank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_question():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

