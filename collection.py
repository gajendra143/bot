from chatterbot import ChatBot

default = "Huh? I don't get it..."
chatbot = ChatBot('chatboy',trainer="chatterbot.trainers.ListTrainer",
    logic_adapters=[{
        'import_path': 'chatterbot.logic.BestMatch',
        "response_selection_method": "chatterbot.response_selection.get_random_response"
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.50,
            'default_response': default
        }
        ]
    )

chatbot.train(["Hello","Hey",])
def chat(input):
    response = chatbot.get_response(input)
    print(response)

    #########################################################################


def addbook(request):
    if request.POST:
        book_form = BookForm(request.POST)
    author_form = AuthorForm(request.POST)
        if (book_form.is_valid() and author_form.is_valid()):
        log.debug("test....")
            book=book_form.save()
            author=author_form.save()
        author.book=book
        author.save()

        return redirect('/index/')
    else:
    book_form=BookForm()
        author_form=AuthorForm()
        return render_to_response('addbook.html',{'form':book_form,'form':author_form},context_instance=RequestContext(request))


        #####################################################################



<html>
<head>
<title>Create a Post </title>
</head>

<body>
<h1>Create a Post </h1>
<form action="" method="POST">
{% csrf_token %}
Title: <input type="text" name="title"/><br/>
Content: <br/>
<textarea cols="35" rows="8" name="content">
</textarea><br/>
<input type="submit" value="Post"/>
</form>
</body>

</html>
#########################################################################


from django.shortcuts import render
from .models import Post


def createpost(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            post = Post()
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.save()

            return render(request, 'posts/create.html')

    else:
        return render(request, 'posts/create.html')


    ###################################################################

    from django import forms

    class NameForm(forms.Form):
        your_name = forms.CharField(label='Your name', max_length=100)

        < label
        for ="your_name" > Your name: < / label >
        < input id = "your_name" type = "text" name = "your_name" maxlength = "100" required >

        from django.http import HttpResponseRedirect
        from django.shortcuts import render

        from .forms import NameForm

        def get_name(request):
            # if this is a POST request we need to process the form data
            if request.method == 'POST':
                # create a form instance and populate it with data from the request:
                form = NameForm(request.POST)
                # check whether it's valid:
                if form.is_valid():
                    # process the data in form.cleaned_data as required
                    # ...
                    # redirect to a new URL:
                    return HttpResponseRedirect('/thanks/')

            # if a GET (or any other method) we'll create a blank form
            else:
                form = NameForm()

            return render(request, 'name.html', {'form': form})


        ###################################################################




