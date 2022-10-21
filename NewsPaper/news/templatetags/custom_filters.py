from django import template

register = template.Library()


PROHIBITED_WORDS = ['матч', 'мы']

@register.filter()
def censor(value):
   """
   value: значение, к которому нужно применить фильтр
   """
   result = value
   for word in PROHIBITED_WORDS:
      result =  result.replace(word, "*")


   return result