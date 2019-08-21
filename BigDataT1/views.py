import pathlib
import textwrap

from django.http import HttpResponse
from django.shortcuts import render
import os.path
import re
import pandas as pd
import matplotlib
import wordcloud
import matplotlib.pyplot as plt

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
    frec_data = ""
    totalWords_file1 = 0
    totalWords_file2 = 0
    totalWords_file3 = 0
    filename1 = ""
    filename2 = ""
    filename3 = ""
    key_word = ""
    repeat_keyword1 = 0
    repeat_keyword2 = 0
    repeat_keyword3 = 0
    text_string = ""
    clouddata1=""
    clouddata2=""
    clouddata3=""
    repeat_frec1=0
    repeat_frec2=0
    repeat_frec3=0
    
    if request.method == 'POST':
        if request.POST.get('file_1'):
            totalWords_file1 = -1
            filename1 = request.POST.get('file_1')
            selected = request.POST.get('file_1')
            currentdirectory = pathlib.Path('Reuters/' + selected)
            if os.path.exists(currentdirectory):
                document_text = open(currentdirectory, 'r')
                text_string = document_text.read().lower()
                totalWords_file1 = word_count(text_string)
                clouddata1 = frec_datas(text_string).head(5).to_html(index=False,classes="table-striped")
                
            if request.POST.get('file_1') and request.POST.get('keyword_archivo'):
                key_word = request.POST.get('keyword_archivo')
                repeat_keyword1 = frec_datas(text_string)
                repeat_keyword1 = repeat_keyword1[repeat_keyword1.palabras == key_word]['frecuencia']
                if repeat_keyword1.count() == 0:
                    repeat_frec1 =  0
                else:
                    repeat_frec1 =  int(repeat_keyword1)           

        if request.POST.get('file_2'):
            totalWords_file2 = -1
            filename2 = request.POST.get('file_2')
            selected = request.POST.get('file_2')
            currentdirectory = pathlib.Path('Reuters/' + selected)
            if os.path.exists(currentdirectory):
                document_text = open(currentdirectory, 'r')
                text_string = document_text.read().lower()
                totalWords_file2 = word_count(text_string)
                clouddata2 = frec_datas(text_string).head(5).to_html(index=False,classes="table-striped")
                
            if request.POST.get('file_2') and request.POST.get('keyword_archivo'):
                key_word = request.POST.get('keyword_archivo')
                repeat_keyword2 = frec_datas(text_string)
                repeat_keyword2 = repeat_keyword2[repeat_keyword2.palabras == key_word]['frecuencia']
                if repeat_keyword2.count() == 0:
                    repeat_frec2 =  0
                else:
                    repeat_frec2 =  int(repeat_keyword2)
                
        if request.POST.get('file_3'):
            totalWords_file3 = -1
            filename3 = request.POST.get('file_3')
            selected = request.POST.get('file_3')
            currentdirectory = pathlib.Path('Reuters/' + selected)            
            if os.path.exists(currentdirectory):
                document_text = open(currentdirectory, 'r')
                text_string = document_text.read().lower()
                totalWords_file3 = word_count(text_string)
                clouddata3 = frec_datas(text_string).head(5).to_html(index=False,classes="table-striped")
                
            if request.POST.get('file_3') and request.POST.get('keyword_archivo'):
                key_word = request.POST.get('keyword_archivo')
                repeat_keyword3 = frec_datas(text_string)
                repeat_keyword3 = repeat_keyword3[repeat_keyword3.palabras == key_word]['frecuencia']
                if repeat_keyword3.count() == 0:
                    repeat_frec3 =  0
                else:
                    repeat_frec3 =  int(repeat_keyword3)
                
    return render(request, "puntoE.html", {'data': sorted_list, 'totalWords_file1': totalWords_file1, 'totalWords_file2': totalWords_file2, 'totalWords_file3': totalWords_file3, 'filename1': filename1, 'filename2': filename2, 'filename3': filename3,'clouddata1':clouddata1,'clouddata2':clouddata2,'clouddata3':clouddata3,"key_word":key_word,"repeat_keyword1":repeat_frec1,"repeat_keyword2":repeat_frec2,"repeat_keyword3":repeat_frec3})

def frec_datas(text_string):
    text_string = text_string.splitlines()
    selec_lineas = []
    n = 0
    indice = 0
    for linea in text_string:
        n += 1
        if '<body>' in linea:
            indice = 1
        if '</body>' in linea:
            indice = 0
        if indice == 1:
            selec_lineas.append(n)
    separator=' '
    noticia = separator.join(list(text_string[i] for i in selec_lineas)).lower()
    b = "!@#$<>/&.;,"
    for char in b:
        noticia = noticia.replace(char,"")
    tabla = dict(word_count_frec(noticia))
    frecuencia = list(tabla.values())
    palabras = list(tabla.keys())
    tabla = pd.DataFrame({'palabras':palabras, 'frecuencia':frecuencia})
    return tabla.sort_values(by='frecuencia', ascending = False)

def word_count_frec(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

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