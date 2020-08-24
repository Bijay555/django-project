from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(req):
	return HttpResponse('<h1 style="color:red"><center>hello, welcome to django</center></h1>')


def hi(req,val):
	return HttpResponse("hi "+val)

def details(req,name):
	return HttpResponse("<h1 style='color:blue'><center> hi"+ name+ " How are you doing</center></h1>")

def home(req):
	return render(req,'myapp/index.html')	

def home1(req,name):
	return render(req,'myapp/about.html', {'na': name})


def excr(req):
	return render(req,'myapp/cmt.html')

def jsp(req):
	return render(req,'myapp/javascript.html')

def reg(req):
	return render(req, 'myapp/register.html')

def regi(req):
	return render(req, 'myapp/botreg.html')

def rgform(req):
	if req.method == "POST":
		# return HttpResponse("Uploaded Successfully")
		usname = req.POST['uname']
		pswd = req.POST['pwd']
		gen = req.POST['gender']
		language = req.POST['lang']
		message = req.POST['msg']
		# print(usname, pswd, gen, language, message)
		dt = {'username':usname,'password':pswd,'gend':gen,'languag':language,'messag':message}
		return render(req,'myapp/disp.html',{'fr':dt})

	return render(req,'myapp/registerform.html')