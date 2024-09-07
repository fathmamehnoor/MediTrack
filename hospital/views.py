from django.shortcuts import render, redirect
from hospital.models import Speciality, User, Patient, Doctor, Book
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.utils.dateparse import parse_date, parse_time
from django.core.exceptions import ObjectDoesNotExist


def addsp(request):
    if request.method == "GET":
        return render(request,'add_sp.html')
    elif request.method=="POST":
        sp = request.POST['speciality']
        x = Speciality.objects.create(Sp_Name = sp)
        x.save()
        return HttpResponse("<script>alert('Added successfully');</script>")
    

def doctor_reg(request):
    if request.method=="GET":
        data=Speciality.objects.all()
        return render(request,'dreg.html', {'data1':data})
    elif request.method=="POST":
        f=request.POST['fname']
        l=request.POST['lname']
        u=request.POST['uname']
        v=request.POST['password']
        e=request.POST['email']
        a=request.POST['add']
        p=request.POST['pno']
        ag=request.POST['age']
        q=request.POST['qual']
        d=request.POST['sp']
        x=User.objects.create_user(first_name=f,last_name=l,username=u, password=v, email=e, usertype='doctor')
        x.save()
        y=Doctor.objects.create(user_id=x, sp_id_id=d, Address=a, Age=ag, Qualification=q,Phone=p )
        y.save()
        return HttpResponse("<script>alert('Registered successfully');</script>")
    

def patient_reg(request):

    if request.method=="GET":
        data=Speciality.objects.all()
        return render(request,'preg.html', {'data1':data})
    elif request.method=="POST":
        f=request.POST['fname']
        l=request.POST['lname']
        u=request.POST['uname']
        v=request.POST['password']
        e=request.POST['email']
        a=request.POST['add']
        p=request.POST['pno']
        ag=request.POST['age']
        d=request.POST['sp']
        x=User.objects.create_user(first_name=f,last_name=l,username=u, password=v, email=e, usertype='patient',is_active=False)
        x.save()
        y=Patient.objects.create(user_id=x, sp_id_id=d, Address=a,Phone=p , Age=ag)
        y.save()
        return HttpResponse("<script>alert('Registered successfully');</script>")
def pbook(request):
    if request.method == "GET":
        data = Speciality.objects.all()
        return render(request, 'pbook.html', {'data1': data})
    
    elif request.method == "POST":
            d = parse_date(request.POST.get('date'))
            t = parse_time(request.POST.get('time'))
            s = request.POST['sp'] # Ensure this is the ID of Speciality
            
            # Create and save the Book instance
            x = Book.objects.create(date=d, time=t, sp_id_id=s, approved=False)
            x.save()
            
            return HttpResponse("<script>alert('Registered successfully'); window.location.href='/';</script>")
    
def patientview(request):
    data = Patient.objects.all()
    return render(request,'pview.html',{'data1': data})

def adminhome(request):
    return render(request,'adminhome.html')

def home(request):
    return render(request, 'home.html')

def approvest(request,uid):
    pat = Patient.objects.get(id=uid)
    pat.user_id.is_active=True
    pat.user_id.save()
    return redirect(patientview)

def logins(request):
    if request.method=="GET":
        return render(request,"logins.html")
    elif request.method=="POST":
        un=request.POST['uname']
        ps= request.POST['password']
        user=authenticate(request,username=un, password=ps)
        if user is not None and user.usertype=="doctor":
            login(request,user)
            request.session['doct_id']=user.id
            return redirect(doctorhome)
        elif user is not None and user.usertype=="patient" and user.is_active==1:
            login(request,user)
            request.session['pat_id']=user.id
            return redirect(patienthome)
        elif user is not None and user.is_superuser==1:
            return redirect(adminhome)
        else:
            return HttpResponse("not valid")
    return HttpResponse("not ok")


def doctorhome(request):
    return render(request,'doctorhome.html')

def patienthome(request):
    return render(request, 'patienthome.html')

def lgout(request):
    logout(request)
    return redirect(logins)

def doctorview(request):
    data = Doctor.objects.all()
    return render(request,'dview.html',{'data1':data})

def bookview(request):
    data = Book.objects.filter(approved=False)
    return render(request, 'bview.html', {'data1': data})

def approveb(request,bid):
    booking = Book.objects.get(id=bid)
    booking.approved = True
    booking.save()
    return redirect(bookview)

def updateprofile(request):
    pat=request.session.get('pat_id')
    st = Patient.objects.get(user_id_id=pat)
    us = User.objects.get(id=pat)
    return render(request,'updateprofile.html',{'view':st,'data':us})

def doctorupdate(request):
    teach=request.session.get('doct_id')
    tr = Doctor.objects.get(user_id_id=teach)
    us = User.objects.get(id=teach)
    return render(request,'doctorupdate.html',{'view':tr,'data':us})



def update_patient(request,uid):
    if request.method=="POST":
        stud =Patient.objects.get(id=uid)
        sid = stud.user_id_id
        user = User.objects.get(id=sid)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email= request.POST['email']
        user.save()

        stud.Address = request.POST['address']
        stud.Phone = request.POST['phone']
        stud.save()

        return HttpResponse("success")
    

def update_doctor(request, uid):
    if request.method =="POST":
        teach = Doctor.objects.get(id=uid)
        tid = teach.user_id_id
        user = User.objects.get(id = tid)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        teach.Address = request.POST['address']
        teach.Phone = request.POST['phone']
        teach.save()

        return HttpResponse("Updated successfully")



