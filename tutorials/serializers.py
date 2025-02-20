from rest_framework import serializers
from tutorials.models import Tutorial

class Meta : 
    model = Tutorial 
    fields = ( 'id',
              'title',
              'description',
              'published')