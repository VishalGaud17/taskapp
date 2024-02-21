from django.shortcuts import render,HttpResponse,redirect
from ToDoapp.models import TaskList
from django.db.models import Q

# Create your views here.

def home_page(request):
    print('Value : ',request.user.is_authenticated)
    if request.user.is_authenticated:
        t=TaskList.objects.filter(Q(is_activate=1) & Q(user_id=request.user.id) )
        print(t) 
        print(request.user.username)
        context={}
        context['data']=t
        return render(request,'ToDoapp/dashboard.html',context)
    else:
        return redirect('/authapp/login')

def delete_task(request,rid):
    obj=TaskList.objects.filter(id=rid)
    obj.update(is_activate=0)
    return redirect('/home')


def edit_task(request,rid):
    # print('ID :',rid)
    # return HttpResponse('data fetched')
    # return redirect('/home')
    if request.method=="POST":
        ut=request.POST['title']
        ud=request.POST['det']
        udt=request.POST['duedt']
        t=TaskList.objects.filter(id=rid)
        t.update(title=ut,detail=ud,due_dt=udt)
        return redirect('/home')
    else:
        context={}
        context['data']=TaskList.objects.get(id=rid)
        return render(request,'ToDoapp/editform.html',context)


def add_task(request):
    print("Method Type :",request.method)
    if request.method=="POST":
        t=request.POST['title']
        d=request.POST['det']
        dt=request.POST['duedt']
        data=TaskList.objects.create(title=t,detail=d,due_dt=dt,user_id=request.user)
        data.save()
        return redirect('/home')
    else:
        print("In else section")
        return render(request,'ToDoapp/addtask.html')
    

def mark_completed(request,rid):
    t=TaskList.objects.filter(id=rid)
    t.update(is_completed=1)
    return redirect('/home')


# def dtl(request):
#     context={}
#     context['a']=20
#     context['User']='Vishal'
#     context['b']=50
#     context['l']=[10,20,30,40,50,60,70,80,90,100]
#     return render(request,'dashboard.html',context)





