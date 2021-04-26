import logging

from django.shortcuts       import render, get_object_or_404
from django.core.paginator  import Paginator
from django.db.models       import Q, Count

from ..models               import Question


logger = logging.getLogger(__name__)

def index(request):
    """
    pybo 목록 출력
    """

    logger.info("INFO 레벨로 출력")
    page = request.GET.get('page', '1')     # 페이지
    kw   = request.GET.get('kw', '')        # 검색어
    so   = request.GET.get('so', 'recent')  # 정렬기준

    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-created_at')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-created_at')
    else:
        question_list = Question.objects.order_by('-created_at')

    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(author__username__icontains=kw) |
            Q(answer__author__username__icontains=kw)
        ).distinct()

    paginator     = Paginator(question_list, 10)
    page_obj      = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """

    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}

    return render(request, 'pybo/question_detail.html', context)