from django.shortcuts import render,redirect
from .forms import *
from django.db.models import Q
from .models import *
import pandas

def login_page(request):
    return render(request,'app/login.html')

def register(request):
    UserForm=User_Form()
    return render(request, 'app/Register.html',{'UserForm':UserForm})

def Add_user(request):
    UserForm=User_Form()
    if request.method=="POST":
        name=request.POST['Name']
        email=request.POST['Email']
        mobile=request.POST['Mobile']
        data=User.objects.filter(Email=email)
        if data:
            msg ="User is Already Exists"
            return render(request, 'app/Register.html',{'UserForm':UserForm,'msg':msg})
        else:

            user=User(Name=name,Email=email,Mobile=mobile)
            user.save()
            msg="User Add succes"
            return render(request, 'app/login.html',{'msg':msg})
    else:
        msg="Request is not 'Post' "
        return render(request, 'app/Register.html',{'UserForm':UserForm,'msg':msg})


def login(request):
    if request.method=='POST':
        email=request.POST['Email']
        mobile=request.POST['Mobile']
        btn=request.POST['btnradio']

        if btn=="user":
            # data=User.objects.filter(Q(Email=email) & Q(Mobile=mobile))
            data=User.objects.get(Email=email)
            id=str(data.id)
            if data:
                n=data.Name
                request.session['Name']=n

                my_task=Task.objects.filter(Detail_id=id)
                # return redirect('dashboard')
                return render(request,'app/dashboard.html',{'my_task':my_task,'name':n})

            else:
                msg="Email is not Match "
                return render(request,'app/login.html',{'msg':msg})
        
        else:
            email=request.POST['Email']
            if email=='admin@gmail.com':
                user_login="Admin"
                return render(request,'app/dashboard.html',{'user_login':user_login})

    else:
        msg="Request is not 'Post' "
        return render(request,'app/login.html',{'msg':msg})

# def dashboard(request):
#     fname=request.session['Name']
#     return render(request,'app/dashboard.html',{'fname':fname})

def add_task(request):
    taskForm=Task_form()
    if request.method=="POST":
        taskForm=Task_form(request.POST)
        if taskForm.is_valid:
            taskForm.save()
            msg='Task Add '
            return render(request,'app/add_task.html',{'taskForm':taskForm,'msg':msg})
    return render(request,'app/add_task.html',{'taskForm':taskForm})

def show(request,pk):
    if pk=="user":
        user_data=User.objects.all()
        return render(request, 'app/show.html',{'user_data':user_data})
    elif pk=="task":
        task_data=Task.objects.all()
        return render(request, 'app/show.html',{'task_data':task_data})

def Excel(request,pk):
    if pk=="user":
        user_data=User.objects.all()
        excel_data=[]

        for i in user_data:
            excel_data.append({
                'ID':i.id ,
                'Name':i.Name ,
                'Email':i.Email ,
                'Mobile':i.Mobile ,
            })

        pandas.DataFrame(excel_data).to_excel('UserData.xlsx')
        msg="Excel file generate successfully"
        return render(request, 'app/show.html',{'user_data':user_data,'msg':msg})
    
    elif pk=="task":
        task_data=Task.objects.all()
        excel_data=[]

        for i in task_data:
            excel_data.append({
                'ID':i.id,
                'Detail':i.Detail ,
                'Task_type':i.Task_type ,
                'Task':i.Task
            })

        pandas.DataFrame(excel_data).to_excel('TaskData.xlsx')
        msg="Excel file generate successfully"
        return render(request, 'app/show.html',{'task_data':task_data,'msg':msg})


