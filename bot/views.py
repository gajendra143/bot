from django.shortcuts import render
import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
# from chatterbot import Statement
from chatterbot.ext.django_chatterbot import settings
from chatterbot.ext.django_chatterbot.models import Statement
from django.views.decorators.csrf import csrf_exempt
from chatterbot.trainers import ChatterBotCorpusTrainer
from django.db.transaction import connections
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from chatt.forms import UserLoginForm


# from chatterbot import ChatBot
# #from chatterbot.trainers import ListTrainer
# from chatterbot.trainers import ChatterBotCorpusTrainer
#
# bot = ChatBot('Pinaki',
#               storage_adapter='chatterbot.storage.SQLStorageAdapter',
#               database_uri='sqlite:///database.sqlite3'
#               )

# trainer = ChatterBotCorpusTrainer(bot)
# trainer.train(
#
#     './DataRepositories/Greet.json'
# )

@login_required(login_url = '/login')
def cht(request):
    return render(request, "samp.html")

# @login_required(login_url = '/login')
# @method_decorator(login_required, name='login')
class ChatterBotAppView(TemplateView):
    template_name = 'index.html'


class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)

    # chatterbot.storage.drop()

    # trainer = ChatterBotCorpusTrainer(chatterbot)
    # trainer.train(
    #
    #     './bot/my_export.json'
    #


    # )

    # chatterbot = ChatBot('My Online Bot',
    # 'django_app_name':'django_chatterbot',
    #
    # 'storage_adapter': 'chatterbot.storage.SQLStorageAdapter',
    # 'database_uri': 'sqlite:///online_bot_database.sqlite3',
    #
    # 'logic_adapters': ['chatterbot.logic.BestMatch'])
    # @csrf_exempt
    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """



        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        # response = self.chatterbot.get_response(input_data)
        response = self.chatterbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })
# Create your views here.


# @login_required(login_url = '/login')
# def data_from_chatbot(request):
#     data_list = Statement.objects.all()
#     return render(request, "data_db.html", {'datas': data_list})




def createpost(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            post = Statement()
            post.text = request.POST.get('title')
            post.in_response_to = request.POST.get('content')
            post.save()

            return render(request, 'try.html')

    else:
        return render(request, 'try.html')

