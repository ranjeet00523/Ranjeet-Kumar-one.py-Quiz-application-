TEST_MODE = True

question_bank = [
    {
        "question": "Keyword to define a function?",
        "options": {
            "A": "func",
            "B": "def",
            "C": "function",
            "D": "lambda"
        },
        "answer": "B"
    },
    {
        "question": "len('Hi')?",
        "options": {
            "A": "1",
            "B": "2",
            "C": "3",
            "D": "4"
        },
        "answer": "B"
    },
    {
        "question": "Mutable type?",
        "options": {
            "A": "tuple",
            "B": "str",
            "C": "list",
            "D": "int"
        },
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments?",
        "options": {
            "A": "//",
            "B": "#",
            "C": "/*",
            "D": "--"
        },
        "answer": "B"
    },
    {
        "question": "Which function displays output?",
        "options": {
            "A": "input()",
            "B": "show()",
            "C": "print()",
            "D": "display()"
        },
        "answer": "C"
    },
    {
        "question": "Which data type stores True or False?",
        "options": {
            "A": "int",
            "B": "str",
            "C": "bool",
            "D": "float"
        },
        "answer": "C"
    },
    {
        "question": "Which loop iterates over a sequence?",
        "options": {
            "A": "for",
            "B": "switch",
            "C": "case",
            "D": "define"
        },
        "answer": "A"
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": {
            "A": "^",
            "B": "**",
            "C": "%",
            "D": "//"
        },
        "answer": "B"
    },
    {
        "question": "Which method adds an item to a list?",
        "options": {
            "A": "insert()",
            "B": "push()",
            "C": "append()",
            "D": "add()"
        },
        "answer": "C"
    },
    {
        "question": "Which keyword handles exceptions?",
        "options": {
            "A": "catch",
            "B": "error",
            "C": "except",
            "D": "final"
        },
        "answer": "C"
    }
]

if TEST_MODE:
    questions = question_bank[:10]
else:
    questions = random.sample(question_bank, 10)

score = 0
total = 10
correct_answers = []

print("QUIZ APPLICATION")

for number in range(total):

    question = questions[number]

    print("\nQ", number + 1, ".", question["question"])

    for option, value in question["options"].items():
        print(option, ".", value)

    while True:
        answer = input("Enter answer (A, B, C, D): ").strip().upper()

        if answer in ["A", "B", "C", "D"]:
            break

        print("Invalid option. Enter A, B, C, D.")
        print("(Q", number + 1, "is asked again)")

    correct_answers.append(question["answer"])

    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong. Correct answer:", question["answer"])

percentage = (score / total) * 100

print("QUIZ RESULT")
print("Score:", score, "/", total)
print("Percentage: {:.2f}%".format(percentage))

if percentage >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
    print("Correct answers:", ", ".join(correct_answers))
