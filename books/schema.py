import graphene
from graphene_django import DjangoObjectType
from .models import Books


class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        fields= ("id", "title", "excerpt")

class Query(graphene.ObjectType):
    all_books = graphene.List(BooksType)

    def resolve_all_books(root, info):
        # return Books.objects.all()
        return Books.objects.filter(title="django")


schema = graphene.Schema(query=Query)    


'''
from django.db.models import Sum

ItemPrice.objects.aggregate(Sum('price'))
# returns {'price__sum': 1000} for example

aggregation ->
https://docs.djangoproject.com/en/4.2/topics/db/aggregation/
https://stackoverflow.com/questions/7981837/aggregate-vs-annotate-in-django#:~:text=Aggregate%20calculates%20values%20for%20the,each%20item%20in%20the%20queryset.

'''