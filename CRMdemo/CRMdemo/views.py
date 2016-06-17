from django.shortcuts import render
from django.shortcuts import render_to_response

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext


#def handler404(request):
#    response = render_to_response('404.html', {},
#                                  context_instance=RequestContext(request))
#    response.status_code = 404
#    return response
    

# Create your views here.
def sae_index(request):
    if request.user.is_authenticated():
        return render(request, 'starter.html')
    else:
        return HttpResponseRedirect('/login')
