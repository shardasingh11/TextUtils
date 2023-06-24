from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    print(type(djtext))
    # check the checkbox is on
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')

    
    # checkbox is on
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'",<>./?@$#%^*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        param = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        djtext=analyzed
    
    if(fullcaps == "on"):
        analyzed =""
        for char in djtext:
            analyzed=analyzed + char.upper()
        param = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed

    if(newlineremover == "on"):
        analyzed =""
        for char in djtext:
            if char !="\n" and char!="\r":
             analyzed=analyzed + char
        param = {'purpose': 'Remove NewLine', 'analyzed_text': analyzed}
        djtext=analyzed

    if(spaceremover == "on"):
        analyzed =""
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed + char
        param = {'purpose': ' Extra Space Removed', 'analyzed_text': analyzed}
    
    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and spaceremover!="on"):
        return HttpResponse("Please select any opetrations and try again !")


    return render(request, 'analyze.html', param)#type ignore
         
    
    