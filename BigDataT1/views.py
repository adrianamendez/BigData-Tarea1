import pathlib
import textwrap

from django.http import HttpResponse
from django.shortcuts import render
import os.path
import re

BASE = os.path.dirname(os.path.abspath(__file__))

def index(request):

    sorted_list = get_list()

    return render(request, "index.html", {'data': sorted_list})

def response1(request):

    sorted_list = get_list()
    selected = request.POST.get('selected_file')

    currentDirectory = pathlib.Path('Reuters/'+selected)
    document_text = open(currentDirectory, 'r')
    text_string = document_text.read().lower()
    total = word_count(text_string)

    print(total)
    return render(request, "index.html",  {'data': sorted_list,'p1':total})


def puntoA(request):
    sorted_list = get_list()
    totalWords = 0
    selected = ""

    if request.method == 'POST':
        totalWords = -1
        if request.POST.get('selected_file'):
            selected = request.POST.get('selected_file')
            currentdirectory = pathlib.Path('Reuters/' + selected)
            document_text = open(currentdirectory, 'r')
            text_string = document_text.read().lower()
            totalWords = word_count(text_string)


    return render(request, "puntoA.html", {'data': sorted_list,'totalWords':totalWords, 'filename': selected})


def puntoB(request):

    totalWords = 0
    split_list = get_listSplit()
    selected = ""
    if request.method == 'POST':
        totalWords = -1


        if request.POST.get('textfield_p2'):
            selected = request.POST.get('textfield_p2')
            userinput = request.POST.get('textfield_p2')
            userinput = userinput.lower()
            userfinalinput = get_FileName(userinput)
            currentdirectory = pathlib.Path('Reuters/' + userfinalinput)
        if os.path.exists(currentdirectory):
            document_text = open(currentdirectory, 'r')
            text_string = document_text.read().lower()
            totalWords = word_count(text_string)


    print(totalWords)
    return render(request, "puntoB.html",  {'data': split_list, 'totalWords': totalWords, 'filename': selected})


def puntoC(request):
    sorted_list = get_list()
    totalWords = 0
    selected = ""

    if request.method == 'POST':
        totalWords = -1
        if request.POST.get('selected_file'):
            selected = request.POST.get('selected_file')
            currentdirectory = pathlib.Path('Reuters/' + selected)
            document_text = open(currentdirectory, 'r')
            text_string = document_text.read().lower()
            totalWords = word_count(text_string)

    return render(request, "puntoC.html", {'data': sorted_list, 'totalWords': totalWords, 'filename': selected})


def puntoD(request):
    sorted_list = get_list()

    return render(request, "puntoD.html", {'data': sorted_list})


def puntoE(request):
    sorted_list = get_list()
    totalWords_file1 = 0
    totalWords_file2 = 0
    totalWords_file3 = 0
    filename1 = ""
    filename2 = ""
    filename3 = ""
    key_word = ""

    if request.method == 'POST':

        if request.POST.get('keyword_archivo'):
            key_word = request.POST.get('keyword_archivo')

        if request.POST.get('file_1'):
            totalWords_file1 = -1
            filename1 = request.POST.get('file_1')
            selected = request.POST.get('file_1')
            currentdirectory = pathlib.Path('Reuters/' + selected)
            if os.path.exists(currentdirectory):
                document_text = open(currentdirectory, 'r')
                text_string = document_text.read().lower()
                totalWords_file1 = word_count(text_string)

        if request.POST.get('file_2'):
            totalWords_file2 = -1
            filename2 = request.POST.get('file_2')
            selected = request.POST.get('file_2')
            currentdirectory = pathlib.Path('Reuters/' + selected)
            if os.path.exists(currentdirectory):
                document_text = open(currentdirectory, 'r')
                text_string = document_text.read().lower()
                totalWords_file2 = word_count(text_string)

        if request.POST.get('file_3'):
            totalWords_file3 = -1
            filename3 = request.POST.get('file_3')
            selected = request.POST.get('file_3')
            currentdirectory = pathlib.Path('Reuters/' + selected)
            if os.path.exists(currentdirectory):
                document_text = open(currentdirectory, 'r')
                text_string = document_text.read().lower()
                totalWords_file3 = word_count(text_string)

        print("totalWords_file1 " + str(totalWords_file1))
        print("totalWords_file2 " + str(totalWords_file2))
        print("totalWords_file3 " + str(totalWords_file3))
        print("key_word " + key_word)

    return render(request, "puntoE.html", {'data': sorted_list, 'totalWords_file1': totalWords_file1, 'totalWords_file2': totalWords_file2, 'totalWords_file3': totalWords_file3, 'filename1': filename1, 'filename2': filename2, 'filename3': filename3, "key_word":key_word})


def puntoF(request):
    sorted_list = get_list()

    return render(request, "puntoF.html", {'data': sorted_list})

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return len(counts)



def get_list():
    sorted_list = []
    data = {}
    currentDirectory = pathlib.Path('Reuters')
    counter = 0
    for currentFile in currentDirectory.iterdir():
        data[counter] = currentFile.name
        counter += 1
    sorted_list = sorted(data.values(), key=lambda x: x[0])
    print(sorted_list)

    return sorted_list


def get_listSplit():
    sorted_list = []
    data = {}
    currentDirectory = pathlib.Path('Reuters')
    counter = 0
    for currentFile in currentDirectory.iterdir():
        fileNameSplit = currentFile.name.split(".")
        data[counter] = fileNameSplit[0]
        counter += 1
    sorted_list = sorted(data.values(), key=lambda x: x[0])

    print(sorted_list)

    return sorted_list


def get_FileName(userinput):
    userfinalinput = "notExists"
    sorted_list = get_list()
    for listitem in sorted_list:
        splitname = listitem.split(".")
        if splitname[0] == userinput:
            totalwords = 0
            userfinalinput = listitem
            break

    return userfinalinput
