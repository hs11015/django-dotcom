from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import AnswerDoubleForm
from ..models import QuestionDouble, AnswerDouble

@login_required(login_url='common:login')#로그아웃 상태에서 @login_required 어노테이션이 적용된 함수가 호출되면 자동으로 로그인 화면으로 이동
def answer_create(request, question_id):
    """
    doubleboard 답변등록
    """
    question = get_object_or_404(QuestionDouble, pk=question_id)
    if request.method == "POST":
        form = AnswerDoubleForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author_double = request.user  # 추가한 속성 author 적용, reqeust.user는 현재 로그인한 계정의 User모델 객체
            answer.create_date_double = timezone.now()
            answer.question_double = question
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('doubleboard:detail', question_id=question.id), answer.id))#redirect함수는 페이지 이동을 위해 장고가 제공하는 함수, #QuestionDouble과 AnswerDouble 모델은 서로 ForeignKey 로 연결되어 있기때문에  question.answer_set은 질문의 답변을 의미
    else:
        form = AnswerDoubleForm()
    context = {'question': question, 'form': form}
    return render(request, 'doubleboard/question_detail.html', context)

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """
    doubleboard 답변수정
    """
    answer = get_object_or_404(AnswerDouble, pk=answer_id)
    if request.user != answer.author_double:
        messages.error(request, '수정권한이 없습니다')
        return redirect('doubleboard:detail', question_id=answer.question_double.id)

    if request.method == "POST":
        form = AnswerDoubleForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author_double = request.user
            answer.modify_date_double = timezone.now()
            answer.save()
            return redirect('{}#answer_{}'.format(
                resolve_url('doubleboard:detail', question_id=answer.question_double.id), answer.id)) #doubleboard:detail url에 #answer_7와같은 앵커태그를 추가하기 위해 format, resolve_url사용. resolve_url은 실제 호출되는 url 문자열을 리턴해주는 장고함수.
    else:
        form = AnswerDoubleForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'doubleboard/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    """
    doubleboard 답변삭제
    """
    answer = get_object_or_404(AnswerDouble, pk=answer_id)
    if request.user != answer.author_double:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('doubleboard:detail', question_id=answer.question_double.id)
