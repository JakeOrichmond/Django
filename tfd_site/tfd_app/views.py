from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Type, Strain

# Create your views here.
# change all the classes to def like HomeView is below...


def Home(request):
    author = "Jake"
    return HttpResponse(render(request, 'tfd_app/home.html', {'author': author }))


def Index(request):
    return HttpResponse(render(request, 'tfd_app/index.html'))


def Detail(request):
    return HttpResponse(render(request,'tfd_app/detail.html'))


def Results(request):
    return HttpResponse(render(request, 'tfd_app/results.html'))



#def index(request):
#    latest_type_list = Type.objects.order_by('-pub_date')[:5]
#    context = {'latest_type_list': latest_type_list}
#    return render(request,'tfd_app/index.html', context)


#def detail(request,type_id):
#    type = get_object_or_404(Type, pk=type_id)
#    return render(request, 'tfd_app/detail.html', {'type' : type})


#def results(request, type_id):
#    type = get_object_or_404(Type, pk=type_id)
#    return render(request, 'tfd_app/results.html',{'type':type})


# def vote(request, type_id):
#     return HttpResponse("You're voting on strain %s." % type_id)
#     t = get_object_or_404(Type, pk=type.id)
#     try:
#         selected_strain = t.strain_set.get(pk=request.POST['strain'])
#     except (KeyError, Strain.DoesNotExist):
#         # Redisplay the type voting form
#         return render(request, 'tfd_app/detail.html',{ 'Type': t,
#             'error_message': "You didn't select a Strain.",
#         })
#     else:
#         selected_strain.votes +=1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#        return HttpResponseRedirect(reverse('tfd/app:results', args=t.id,))
