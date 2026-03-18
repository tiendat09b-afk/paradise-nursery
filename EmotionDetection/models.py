from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)


class Enrollment(models.Model):
    user = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_text = models.TextField()
    grade = models.IntegerField()

    def is_get_score(self, selected_ids):
        correct_choices = self.choice_set.filter(is_correct=True)
        correct_ids = set(c.id for c in correct_choices)
        return correct_ids == set(selected_ids)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)


class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)
