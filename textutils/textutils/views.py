# created by me

from django.http import HttpResponse
from django.shortcuts import render

# code for practise
# def index(request):
#     return HttpResponse("Code with Vickrant")
#     # with open("1.txt", "r+") as f:
#     #     content = f.read()
#     #     return HttpResponse(content)
#
# def about(request):
#     return HttpResponse("About Vickrant Phandd")
#
# def link(request):
#     return HttpResponse("<a href='https://www.facebook.com/' > FACEBOOK </a>")

def index(request):
    params= {'name': 'Vickrant', 'place': 'Pune'}
    return render(request, 'index.html', params)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

#def removepunc(request):
    #return  HttpResponse("remove the puncs \n <a href='http://127.0.0.1:8000/'>HOME</a>")
    #return HttpResponse("<button><a href='http://127.0.0.1:8000/'>Home</a></button>")


# def removepunc(request):
#     # get the text
#     djtext= request.GET.get('text', 'default')
#     print(djtext)
#     #Analyze the text
#     return HttpResponse("remove punc")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # Check which checkbox is on
    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if (fullcaps == "on"):
        analyzed = djtext.upper()
        params = {'purpose': 'Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == "on"):
        analyzed = " "
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == "  "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("No Options Selected! Please select any option and try again...")

    return render(request, 'analyze.html', params)


# practise-1
# def ex1(request):
#     s='''<h2> Navigation Bar <br> </h2>
#     <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" target="_blank" > Django Code With Harry Bhai </a><br>
#     <a href="https://www.facebook.com/" target="_blank"> Facebook </a> <br>
#     <a href="https://www.flipkart.com/" target="_blank"> Flipkart </a> <br>
#     <a href="https://www.hindustantimes.com/" target="_blank"> News </a> <br>
#     <a href="https://www.google.com/" target="_blank"> Google </a> <br>'''
#     return HttpResponse(s)

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("capitalize first")
#
# def spaceremove(request):
#     return HttpResponse("space remover")
#
# def charcount(request):
#     return HttpResponse("charcount ")