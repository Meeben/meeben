from Question import Question

question_prompts = [
    "How many men have worked on the moon?\n(a) 5\n(b) 12\n(c) 27\n\n",
    "The fastest running terrestial animal is?\n(a) Cheetah\n(b) Lion\n(c) Rabbit\n\n",
    "In what country do the greatest number of tornadoes occur?\n(a) Malaysia\n(b) Indonasia\n(c) United States\n\n",
  
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c"),
]

def run_test(question):
    
    score = 0

    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
       
