from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Review, Person
from django.template import loader
import re, string

def index(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:5]
    template = loader.get_template('reviews/index.html')
    context = {
        'latest_review_list': latest_review_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    s = review.text_before
# удаление всех лишних символов
    i = 0
    while i < len(s) - 2:
        if (s[i] == s[i+1]) and s[i] in string.punctuation:
            s = s[:i] + s[i+1:]
            continue
        i += 1
 # форматирование пробелов
    re.sub(r'\s+', ' ', s)
    if s[0] == " ": s = s[1:]
    if s[-1] == " ": s = s[:-1]
    i = 1
    while i < len(s) - 1:
        if s[i] in string.punctuation:
            if s[i - 1] == " ":
                s = s[:i - 1] + s[i:]
                i -= 1
                continue
            if (s[i + 1] != " ") and not (s[i + 1] in string.punctuation):
                s = s[:i + 1] + " " + s[i + 1:]
                i += 2
                continue
        i += 1
    if s[-1] == " ": s = s[:-1]
# форматирование лишних знаков препинания и поиск 6 ЗАГЛАВНЫХ букв
    i, needToLowerCase = 0, False
    while i < len(s) - 1:
        if i < len(s) - 6:
            letters = "".join(i for i in s[i:i + 6] if not (i in string.punctuation) and (i != " "))
            if (letters.upper() == letters) and (len(letters) == 6):
                needToLowerCase = True
        if (s[i] == s[i + 1]) and s[i] in string.punctuation:
            s = s[:i] + s[i + 1:]
            continue
        i += 1
# форматирование регистров букв, в случае, если встретились 6 ЗАГЛАВНЫХ
    if needToLowerCase:
        l = list(s.lower())
        i = 0
        l[0] = l[0].upper()
        while i < len(l) - 2:
            if l[i] in [".", "!", "?"]:
                l[i + 2] = l[i + 2].upper()
            i += 1
        s = ''.join(l)
    review.text_after = s
    review.save()
    return render(request, 'reviews/detail.html', {'review': review})