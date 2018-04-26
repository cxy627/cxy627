from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Question,Choice
from django.template import loader
from django.views import generic
from django.utils import timezone



# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_data')[:5]
#     "polls/index.html"
#     context = {
#         "latest_question_list":latest_question_list
#     }
#     return render(request,"polls/index.html",context)

def vote(request,question_id):
    question =  get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError,Choice.DoesNotExist):
        return render(request,"polls/detail.html",{"question":question,
                "error_message": "You didn't select a choice."})
    else:
        selected_choice.votes +=1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# def detail(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,"polls/detail.html",context={"question":question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        
        return Question.objects.filter(pub_data__lte=timezone.now()).order_by("-pub_data")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name="Polls/detail.html"
    def get_queryset(self):
        return Question.objects.filter(pub_data__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name="polls/results.html"
