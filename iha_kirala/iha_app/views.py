from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import iha_info,kira_info
from .forms import giris_form,register_form,add_iha
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.template import loader
deneme=0
def giris(request):
    if request.method == "POST":
        form_giris = giris_form(request.POST)
        register_form_=register_form(request.POST)
        if form_giris.is_valid():
            username = form_giris.cleaned_data['username']
            passs = form_giris.cleaned_data['your_password']
            user=authenticate(username=username,password=passs)
            global deneme
            deneme=user.id

            if user is not None:
                if(user.is_superuser):
                    return redirect("index")
                else:
                    return redirect("user")

            else:
                messages.info(request, 'Hatalı Giriş')
        if register_form_.is_valid():
            username=register_form_.cleaned_data['username']
            name = register_form_.cleaned_data['your_name']
            surname = register_form_.cleaned_data['your_surname']
            email = register_form_.cleaned_data['your_email_reg']
            passs = register_form_.cleaned_data['your_password_reg']
            passs_test = register_form_.cleaned_data['your_rep_password']

            # Kayıtlı kullanıcı ara
            if (passs!=passs_test):
                messages.info(request, 'Password aynı değil.')

            else:
                my_user=User.objects.create_user(username,email,passs)
                my_user.first_name=name
                my_user.last_name=surname
                my_user.save()
            form_giris = giris_form()
            register_form_=register_form()

            return render(request, "iha_app/giris.html", {"form1": form_giris,"form2":register_form_})

    form_giris = giris_form()
    register_form_=register_form()
    return render(request, "iha_app/giris.html", {"form1": form_giris,"form2":register_form_})

def index(request):
    form_giris = add_iha()
    bilgiler=iha_info.objects.values()
    if request.method == "POST":
        form_giris = add_iha(request.POST)

        if form_giris.is_valid():
            marka = form_giris.cleaned_data['iha_marka']
            model = form_giris.cleaned_data['iha_model']
            agr = form_giris.cleaned_data['iha_agr']
            kategori = form_giris.cleaned_data['iha_kat']
            fiyat = form_giris.cleaned_data['iha_fiyat']
            bilgiler=iha_info(iha_marka=marka,iha_model=model,iha_kat=kategori,iha_agr=agr,iha_fiyat=fiyat)
            bilgiler.save()
            return redirect("index")
    return render(request,"iha_app/index.html",{"form3":form_giris,"bilgi":bilgiler})

def delete(request, id):
  member = iha_info.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))
def update(request, id):
    iha_list = iha_info.objects.get(id=id)
    iha_form=add_iha(request.POST or None,instance=iha_list)
    if request.method=="POST":
        form=add_iha(request.POST or None,instance=iha_list)
        if form.is_valid:
            form.save()
            return redirect("index")
    else:
        list_iha=iha_info.objects.all()
        return render(request,"iha_app/update.html",{"bilgiler":list_iha,"form":iha_form})
global kullanici_id

def user_page(request):
    bilgiler=iha_info.objects.all()
    kullanici_id=deneme
    user = User.objects.get(id=kullanici_id)



    return render(request,"iha_app/user.html",{"user":user.username,"bilgi":bilgiler})

global kullanici_id2

def kirala(request,id):
    member = iha_info.objects.get(id=id)
    kullanici_id2=deneme

    user = User.objects.get(id=kullanici_id2)
    kullanıcı=user.first_name +" "+user.last_name + " "+ user.username
    kira_bilgi=kira_info(iha_marka=member.iha_marka,iha_model=member.iha_model,iha_kat=member.iha_kat,iha_agr=member.iha_agr,iha_fiyat=member.iha_fiyat,iha_kullanıcı=kullanıcı)
    kira_bilgi.save()
    return HttpResponseRedirect(reverse('user'),{"user":user.username})
def siparis(request):
    kira_bilgi=kira_info.objects.all()
    return render(request,"iha_app/siparis.html",{"bilgi":kira_bilgi})
