# from django.http import HttpResponse
import operator

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext)
    wordCount = fulltext.split()
    a_dict = {}
    for element in wordCount:
        if element in a_dict:
            a_dict[element] += 1
        else:
            a_dict[element] = 1
    sortedWord = sorted(a_dict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordCount),
                                          'sortedWord': sortedWord})


def about(request):
    return render(request, 'about.html')