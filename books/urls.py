from django.urls import path
from graphene_django.views import GraphQLView
from . import schema
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # ...
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))), # Given that schema path is defined in GRAPHENE['SCHEMA'] in your settings.py
]