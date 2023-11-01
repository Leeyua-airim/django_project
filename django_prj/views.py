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

def burger_search(request):
    print("request.GET : ", request.GET) # requst.GET 으로 전달된 데이터 출력
    keyword = request.GET.get("keyword") # 검색한 데이터 변수화
    print("keyword : ", keyword)

    if keyword is not None:
        burgers = Burger.objects.filter(name__contains=keyword)

    else:
        burgers = Burger.objects.none()

    # keyword 변수의 값과 동일한 오브젝트 필터
    # burgers = Burger.objects.filter(name__contains=keyword)
    print("burgers : ", burgers)

    context = {
        "burgers" : burgers,
    }

    return render(request=request,
                  template_name="burger_search.html",
                  context=context)