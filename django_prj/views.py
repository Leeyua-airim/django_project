from django.http import HttpResponse
from django.shortcuts import render
from burgers.models import Burger

def main(request):
    # return HttpResponse("안녕하세요! 테스트 입니다.")
    return render(request=request,template_name="main.html")

def burger_list(request):
    # return HttpResponse("pyburger 의 햄버거 목록 입니다.")
    # return render(request=request, template_name="burger_list.html")
    burgers = Burger.objects.all()
    print("전체 햄버거 목록 : ", burgers)

    context = {
        'burgers' : burgers,
    }

    return render(request=request,
                  template_name="burger_list.html",
                  context=context)
