from django.shortcuts import render,redirect
from .models import Instagram
from .forms import formmodel
import os
from django.contrib import messages

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def selenium(user,pswd):

    driver = webdriver.Firefox()
    
    driver.get('https://www.instagram.com/accounts/login/')
    wait = WebDriverWait(driver, 10)
    username = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/span/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')))
    password = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/span/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')))
    login_btn = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/span/section/main/div/article/div/div[1]/div/form/div[4]')))
    username.send_keys(user)
    password.send_keys(pswd)
    login_btn.click()

def home(request):
    form=formmodel()
    if request.method=="POST":
        form=formmodel(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            try:
                user=request.POST.get("username")
                pswd=request.POST.get("password")
                a=Instagram.objects.filter(username=user).first()
                link=a.image.url
                link=os.getcwd()+os.path.abspath(link)
                string=f"instapy -u {user} -p {pswd} -f {link} -t 'TEXT CAPTION'"
                os.system(string)
                selenium(user,pswd)
            except:
                messages.error(request, 'username or password invalid')
                redirect("home")


   
            
    return render(request,"home.html",{"form":form})