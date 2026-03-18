class Question:
    def __init__(self, text):
        self.text = text


class Choice:
    def __init__(self, question, text):
        self.question = question
        self.text = text


class Submission:
    def __init__(self, user, question, choice):
        self.user = user
        self.question = question
        self.choice = choice
