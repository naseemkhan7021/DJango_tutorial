from django.http import Http404, HttpResponse
from django.shortcuts import render
import redis
r = redis.Redis()

# Create your views here.


def index(request):
    return render(request, 'singlepage/index.html')


# The texts are much longer in reality, but have
# been shortened here to save space
texts = ['Veniam minim culpa culpa elit consequat dolore mollit. Cillum aliqua sit ullamco elit aute incididunt labore cillum tempor.', 'Deserunt mollit non irure Lorem aute consequat ullamco aliquip enim esse consectetur.Reprehenderit anim dolor reprehenderit enim irure deserunt.',
         'Eiusmod amet sit consequat dolore do officia est tempor voluptate id.Proident irure sint aliquip cupidatat aliquip aliqua in dolor.']


def section(request, num):
    if 1 <= num <= 3:
        rSection = r.get(f"section_{num-1}")
        if rSection:
            # print(f"rSection is {rSection}")
            return HttpResponse(rSection)
        else:
            r.set(f"section_{num-1}",texts[num-1],60)
            return HttpResponse(texts[num-1])
    else:
         return HttpResponse('out of range!!')
        #  raise Http404("No such section")
