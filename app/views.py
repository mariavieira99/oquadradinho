from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto
import csv  
from django.core.files.storage import FileSystemStorage
from django.core.files.images import ImageFile
import PIL
from PIL import Image
# Create your views here.


def home (request):

    '''
    with open('static/produtos.csv', encoding='latin-1') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line = 0
        for row in csv_reader:
            if(line==0):
                line+=1
                continue
            produto = Produto()
            produto.nome = row[0]
            produto.descricao = row[1]
            

            f = open(row[2], "rb")
            produto.img1 = row[2]
            produto.img1.save(f.name, f)

            produto.grupo = row[3]

            if row[4] != "":
                f = open(row[4], "rb")
                produto.img2 = row[4]
                produto.img2.save(f.name, f)
            else:
                produto.img2 = row[4]

            if row[5] != "":
                f = open(row[5], "rb")
                produto.img3 = row[5]
                produto.img3.save(f.name, f)
            else:
                produto.img3 = row[5]

            if row[6] != "":
                f = open(row[6], "rb")
                produto.img4 = row[6]
                produto.img4.save(f.name, f)
            else:
                produto.img4 = row[6]
            
            if row[7]!= "":
                f = open(row[7], "rb")
                produto.img5 = row[7]
                produto.img5.save(f.name, f)
            else:
                produto.img5 = row[7]
            
            if row[8]!= "":
                f = open(row[8], "rb")
                produto.img6 = row[8]
                produto.img6.save(f.name, f)
            else:
                produto.img6 = row[8]

            produto.sugestao = row[9]
            
            produto.save()
    
    '''
    produtos = Produto.objects.all().order_by('?')
    return render(request, 'home.html',{'produtos': produtos})


def produtoInfo (request):
    if request.method == "GET":
        query = request.GET.get('nome')
        produto = Produto.objects.get(nome=query)
        contImages=[]
        if(produto.img1):
            contImages.append(produto.img1)
        if(produto.img2):
            contImages.append(produto.img2)
        if(produto.img3):
            contImages.append(produto.img3)
        if(produto.img4):
            contImages.append(produto.img4)
        if(produto.img5):
            contImages.append(produto.img5)
        if(produto.img6):
            contImages.append(produto.img6)
        print("images: " , contImages)
        return render(request, 'produto_information.html', {'produto': produto, 'images_produto': contImages})


def sobreNos(request):
    if request.method == "GET":
        return render(request, 'sobre_nos.html')