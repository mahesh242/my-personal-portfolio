from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import (api_view,
                                       parser_classes,
                                    )
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from articles.models import Article
from django.utils.translation import ugettext_lazy as _

# Create your views here.

"""RestAPI Test Functionality - STARTS"""
@csrf_exempt
@parser_classes([JSONParser])
# @parser_classes([FormParser, JSONParser])
@api_view(['GET'])
def restapi_test(request):
    if request.method == "GET":
        results = []
        try:
            articles = Article.objects.all()
        except:
            articles = None
            
        if articles:
            for elem in articles:
                try:
                    articles_dtl = elem.id
                except:
                    articles_dtl = None
                if articles_dtl:
                    result_data = {}
                    result_data['article_name'] = elem.title if elem.title else None
                    results.append({'article_data':result_data})

        
#         data = request.data #Getting the parameters
# 	
#         decrpyt_password = decrypt_password_from_encrypt(str(data.get('password')))
#         
#         if data.get('username') and data.get('password'):
#             user = authenticate(username=data.get('username'),
#                                 password= decrpyt_password
#                                 )
#         if user is not None:
#             if user.is_active:
#                 results = {'status':1,
#                            'message':user.id,
#                          }
#             else:
#                 message = _('Account is Blocked ! Please contact Admin')
#                 results = {'status':0,
#                            'message':message,
#                          }
#             return Response(results)
#         message = _('Account is Blocked ! Please contact Admin')
#         results = {'status':0,
#             'message':message,
#         }
        return Response(results)
"""RestAPI Test Functionality - ENDS"""
