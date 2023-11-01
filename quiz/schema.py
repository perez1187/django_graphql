import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Quizzes, Category, Question, Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id","name")

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id","title","category")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title","quiz")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question","answer_text")

class Query(graphene.ObjectType):

    # quiz = graphene.String()

    # def resolve_quiz(root,info):
    #     return f"This is first question"

    ############################################3

    # all_quizzes = DjangoListField(QuizzesType) # to jest to samo co graphene.List

    # all_quizzes = graphene.List(QuizzesType)
    # all_questions = graphene.List(QuestionType)

    # tu def resolve

    ############################################

    # ''' chcemy jeden rekord (np User), podajemy model oraz argument jaki przyjmujemy'''
    # all_quizzes = graphene.Field(QuizzesType, id=graphene.Int())

    # def resolve_all_questions(root, info, id):
    #     return Question.objects.get(pk=id)

    #############################################

    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())

    def resolve_all_questions(root, info, id):
        return Question.objects.get(pk=id)
    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)

schema = graphene.Schema(query=Query)