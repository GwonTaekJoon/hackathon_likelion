from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog_10, Blog_20 , Blog_30, Blog_40, Blog_50, Wish,Comment, Joboffer, Buy,Post, Sell, Comment10, Comment20, Comment30, Comment40, Comment50, Free, apply
from .forms import NewBlog_10, NewBlog_20, NewBlog_30, NewBlog_40, NewBlog_50, SearchForm, NewBuy, Comment10Form, Comment20Form, Comment30Form, Comment40Form, Comment50Form, NewSell, NewFree, NewApply, CommentForm
from .forms import NewWish, CommentForm, NewJoboffer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse 




def developing(request):
    return render(request, 'locally/developing.html')

def home(request):
    return render(request, 'locally/home.html')

def choice(request):
    return render(request, 'locally/choice.html')


def site(request):
    buys= Buy.objects.all()
    frees = Free.objects.all()
    wish_list=Wish.objects.all()
    sells = Sell.objects.all()
    applys = apply.objects.all()
    return render(request, 'locally/site.html',{'wish_list': wish_list, 'buys' : buys , 'frees' : frees , 'sells': sells, 'applys': applys })

def schedule(request):
    return render(request, 'locally/schedule.html')

def schedule_1(request):
    return render(request, 'locally/schedule_1.html')
def schedule_2(request):
    return render(request, 'locally/schedule_2.html')
def schedule_3(request):
    return render(request, 'locally/schedule_3.html')
def schedule_4(request):
    return render(request, 'locally/schedule_4.html')

def wish(request):
    wishs = Wish.objects.all()
    # wish_list=Wish.objects.all()
    paginator = Paginator(wishs, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'locally/wish.html', {'wishs':wishs,'posts':posts})

def joboffer(request):
    joboffers = Joboffer.objects.all()
    # joboffer_list=Joboffer.objects.all()
    paginator = Paginator(joboffers,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'locally/joboffer.html', {'joboffers':joboffers,'posts':posts})

def wishwrite(request):
    return render(request, 'locally/wishwrite.html')

def wishclick(request, wish_id):
    wish_wishclick = get_object_or_404(Wish, pk=wish_id)
    return render(request, 'locally/wishclick.html', {'wish': wish_wishclick})

def wishcreate(request):
    wish = Wish()
    wish.title = request.GET['title']
    wish.body = request.GET['body']
    wish.wish_user = request.user
    wish.pub_date = timezone.datetime.now()
    wish.save()
    return redirect('/locally/wish/' + str(wish.id))


def joboffercreate(request):
    joboffer = Joboffer()
    joboffer.title = request.GET['title']
    joboffer.body = request.GET['body']
    joboffer.objective = request.GET['objective']
    joboffer.gender = request.GET['gender']
    joboffer.name  = request.GET['name']
    joboffer.age  = request.GET['age']
    joboffer.career = request.GET['career']
    joboffer.Phonenumber = request.GET['Phonenumber']
    joboffer.pub_date = timezone.datetime.now()
    joboffer.joboffer_user = request.user
    joboffer.save() 
    return redirect('joboffer')







def wishupdate(request, pk):
    wish = get_object_or_404(Wish, pk = pk)
    form = NewWish(request.POST, instance=wish)
    if form.is_valid():
        wish.save()
        return redirect('wish')
    return render(request,'locally/newform.html',{'form':form})

def wishdelete(request, pk):
    wish = get_object_or_404(Wish, pk = pk)
    wish.delete()
    return redirect('wish')

def comment_write(request, pk):
    wish = get_object_or_404(Wish, pk=pk)
    if request.method == "POST":
        # print(1)
        # form = CommentForm(request.POST)
        # print(request.POST)
        # print(form)
        # # if form.is_valid():
        #     print(2)
        comment = Comment()
        # comment = form.save(commit=False)
        comment.wish = wish
        comment.comment_contents = request.POST['comment_contents']
        comment.save()
        return redirect('/locally/wish/' + str(wish.id))
    else:
        form = CommentForm()
    return redirect('/locally/wish/' + str(wish.id))


def jobofferwrite(request):
    return render(request, 'locally/jobofferwrite.html')

def jobofferclick(request, joboffer_id):
    joboffer_jobofferclick = get_object_or_404(Joboffer, pk=joboffer_id)
    return render(request, 'locally/jobofferclick.html', {'joboffer': joboffer_jobofferclick})









def jobofferupdate(request, pk):
    joboffer = get_object_or_404(Joboffer, pk = pk)
    form = NewJoboffer(request.POST, instance=Joboffer)
    if form.is_valid():
        joboffer.save()
        return redirect('joboffer')
    return render(request,'locally/joboffernewform.html',{'form':form})

def jobofferdelete(request, pk):
    joboffer = get_object_or_404(Joboffer, pk = pk)
    joboffer.delete()
    return redirect('joboffer')




def comment_10(request,pk):
    c10 = get_object_or_404(Blog_10, pk=pk)
    if request.method == 'POST':
        form = Comment10Form(request.POST)
        print(form)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.c10 = c10
            comment.save()
            return redirect('/10/'+ str(c10.id))

    


def comment_20(request,pk):
    c20 = get_object_or_404(Blog_20, pk=pk)
    if request.method == 'POST':
        form = Comment20Form(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.c20 = c20
            comment.save()
            return redirect('/20/'+ str(c20.id))

def comment_30(request,pk):
    c30 = get_object_or_404(Blog_30, pk=pk)
    if request.method == 'POST':
        form = Comment30Form(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.c30 = c30
            comment.save()
            return redirect('/30/'+ str(c30.id))

def comment_40(request,pk):
    c40 = get_object_or_404(Blog_40, pk=pk)
    if request.method == 'POST':
        form = Comment40Form(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.c40 = c40
            comment.save()
            return redirect('/40/'+ str(c40.id))

def comment_50(request,pk):
    c50 = get_object_or_404(Blog_50, pk=pk)
    if request.method == 'POST':
        form = Comment50Form(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.c50 = c50
            comment.save()
            return redirect('/50/'+ str(c50.id))






def market(request):
    buys= Buy.objects.all()
    frees = Free.objects.all()
    sells = Sell.objects.all()
    return render(request, 'locally/market.html',{'buys' : buys , 'frees' : frees , 'sells' : sells })




def marketbuy(request):
    buys=Buy.objects.all()
    return render(request, 'locally/marketbuy.html',{'buys' : buys})
    


def detail_10(request,blog_id):
    details=get_object_or_404(Blog_10,pk=blog_id)
    comments = Comment10.objects.filter(c10 = blog_id).order_by('-create_date')
    return render(request, 'locally/10detail.html',{'details':details, 'comments' : comments  })

def detail_20(request,blog_id):
    details=get_object_or_404(Blog_20,pk=blog_id)
    comments = Comment20.objects.filter(c20 = blog_id).order_by('-create_date')
    return render(request, 'locally/20detail.html',{'details':details , 'comments' : comments  })

def detail_30(request,blog_id):
    details=get_object_or_404(Blog_30,pk=blog_id)
    comments = Comment30.objects.filter(c30 = blog_id).order_by('-create_date')
    return render(request, 'locally/30detail.html',{'details':details,  'comments' : comments })

def detail_40(request,blog_id):
    details=get_object_or_404(Blog_40,pk=blog_id)
    comments = Comment40.objects.filter(c40 = blog_id).order_by('-create_date')
    return render(request, 'locally/40detail.html',{'details':details, 'comments' : comments })

def detail_50(request,blog_id):
    details=get_object_or_404(Blog_50,pk=blog_id)
    comments = Comment50.objects.filter(c50 = blog_id).order_by('-create_date')
    return render(request, 'locally/50detail.html',{'details':details, 'comments' : comments })



def job(request):
    
    joboffer_list=Joboffer.objects.all()
    applys=apply.objects.all()
    return render(request, 'locally/job.html', {'joboffer_list': joboffer_list, 'applys':applys})
  

def guide(request):
    return render(request, 'locally/guide.html')

def write(request):
    return render(request, 'locally/write.html')

def read_10(request):
    blogs = Blog_10.objects.all()
    blog_list=Blog_10.objects.all()
    paginator = Paginator(blog_list,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'locally/10.html', {'blogs':blogs,'posts':posts })

def read_20(request):
    blogs = Blog_20.objects.all()
    blog_list=Blog_20.objects.all()
    paginator = Paginator(blog_list,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'locally/20.html', {'blogs':blogs,'posts':posts })

def read_30(request):
    blogs = Blog_30.objects.all()
    blog_list=Blog_30.objects.all()
    paginator = Paginator(blog_list,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'locally/30.html', {'blogs':blogs,'posts':posts })

def read_40(request):
    blogs = Blog_40.objects.all()
    blog_list=Blog_40.objects.all()
    paginator = Paginator(blog_list,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'locally/40.html', {'blogs':blogs,'posts':posts })

def read_50(request):
    blogs = Blog_50.objects.all()
    blog_list=Blog_50.objects.all()
    paginator = Paginator(blog_list,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'locally/50.html', {'blogs':blogs,'posts':posts })


def create_10(request):
    if request.method == 'POST':
        form = NewBlog_10(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.user = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('ten')
    else:
        form = NewBlog_10()
        return render(request, 'locally/write.html', {'form':form})

def create_20(request):
    if request.method == 'POST':
        form = NewBlog_20(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.user = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('twenty')
    else:
        form = NewBlog_20()
        return render(request, 'locally/write20.html', {'form':form})


def create_30(request):
    if request.method == 'POST':
        form = NewBlog_30(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.user = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('thirty')
    else:
        form = NewBlog_30()
        return render(request, 'locally/write30.html', {'form':form}) 
    
    
    
def create_40(request):
    if request.method == 'POST':
        form = NewBlog_40(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.user = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('forty')
    else:
        form = NewBlog_40()
        return render(request, 'locally/write40.html', {'form':form}) 
    
    
    
def create_50(request):
    if request.method == 'POST':
        form = NewBlog_50(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.user = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('fifty')
    else:
        form = NewBlog_50()
        return render(request, 'locally/write50.html', {'form':form}) 
    
    
    
def schedulebokji(request):
    return render(request, 'locally/schedulebokji.html')

def edit(request, post_id):
    edit_post = Post.objects.get(id=post_id)
    return render(request, 'locally/edit.html', {'post':edit_post})




def new_comment(request, post_id):
    comment = Comment()
    comment.writer = request.POST['writer']
    comment.content = request.POST['content']
    comment.post = get_object_or_404(Post, pk=post_id)
    comment.save()
    return redirect('detail', post_id)




def add_commentbuy(request, pk):
    buy = get_object_or_404(Buy, pk=pk)
    if request.method =="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_buy = form.save(commit=False)
            comment_buy.post = buy
            comment_buy.save()
            return redirect('home')
    else:
        form = CommentForm()
    return redirect('marketbuy')

def update_10(request, pk):
    blog = get_object_or_404(Blog_10, pk = pk)
    form = NewBlog_10(request.POST, instance = blog)
    if form.is_valid():
        form.save()
        return redirect('ten')
    return render(request, 'locally/write.html', {'form':form})

def update_20(request, pk):
    blog = get_object_or_404(Blog_20, pk = pk)
    form = NewBlog_10(request.POST, instance = blog)
    if form.is_valid():
        form.save()
        return redirect('twenty')
    return render(request, 'locally/write20.html', {'form':form})

def update_30(request, pk):
    blog = get_object_or_404(Blog_30, pk = pk)
    form = NewBlog_10(request.POST, instance = blog)
    if form.is_valid():
        form.save()
        return redirect('thirty')
    return render(request, 'locally/write30.html', {'form':form})

def update_40(request, pk):
    blog = get_object_or_404(Blog_40, pk = pk)
    form = NewBlog_10(request.POST, instance = blog)
    if form.is_valid():
        form.save()
        return redirect('forty')
    return render(request, 'locally/write40.html', {'form':form})

def update_50(request, pk):
    blog = get_object_or_404(Blog_50, pk = pk)
    form = NewBlog_10(request.POST, instance = blog)
    if form.is_valid():
        form.save()
        return redirect('fifty')
    return render(request, 'locally/write50.html', {'form':form})

        
    





def delete_10(request, pk):
    delete_post=Blog_10.objects.get(pk=pk)
    delete_post.delete()
    return redirect('ten')

def delete_20(request, pk):
    delete_post=Blog_20.objects.get(pk=pk)
    delete_post.delete()
    return redirect('twenty')

def delete_30(request, pk):
    delete_post=Blog_30.objects.get(pk=pk)
    delete_post.delete()
    return redirect('thirty')

def delete_40(request, pk):
    delete_post=Blog_40.objects.get(pk=pk)
    delete_post.delete()
    return redirect('forty')

def delete_50(request, pk):
    delete_post=Blog_50.objects.get(pk=pk)
    delete_post.delete()
    return redirect('fifty')

    
    
    #def index(request):
    #blogs = Blog.objects
    #blog_list = Blog.objects.all()
    #paginator = Paginator(blog_list, 2)
    #page = request.GET.get('page')
    #posts = paginator.get_page(page)
    #return render(request, 'funccrud/funccrud.html', {'blogs':blogs, 'posts':posts})

    
def search_10(request):
    if request.GET.get('q'):
        que = request.GET.get('q')
        variable_column = request.GET.get('search_filter')
        search_type = 'contains'
        filter = variable_column + '__' + search_type
        posts = Blog_10.objects.filter(**{filter:request.GET.get('q')}).order_by('-pub_date')
    else:
        return redirect('10')
    
    return render(request,'locally/search.html',{'posts':posts, 'que':que})

def search_20(request):
    if request.GET.get('q'):
        que = request.GET.get('q')
        variable_column = request.GET.get('search_filter')
        search_type = 'contains'
        filter = variable_column + '__' + search_type
        posts = Blog_20.objects.filter(**{filter:request.GET.get('q')}).order_by('-pub_date')
    else:
        return redirect('20')
    
    return render(request,'locally/search_20.html',{'posts':posts, 'que':que})
    
def search_30(request):
    if request.GET.get('q'):
        que = request.GET.get('q')
        variable_column = request.GET.get('search_filter')
        search_type = 'contains'
        filter = variable_column + '__' + search_type
        posts = Blog_30.objects.filter(**{filter:request.GET.get('q')}).order_by('-pub_date')
    else:
        return redirect('30')
    
    return render(request,'locally/search_30.html',{'posts':posts, 'que':que})
    
def search_40(request):
    if request.GET.get('q'):
        que = request.GET.get('q')
        variable_column = request.GET.get('search_filter')
        search_type = 'contains'
        filter = variable_column + '__' + search_type
        posts = Blog_40.objects.filter(**{filter:request.GET.get('q')}).order_by('-pub_date')
    else:
        return redirect('40')
    
    return render(request,'locally/search_40.html',{'posts':posts, 'que':que})
    
def search_50(request):
    if request.GET.get('q'):
        que = request.GET.get('q')
        variable_column = request.GET.get('search_filter')
        search_type = 'contains'
        filter = variable_column + '__' + search_type
        posts = Blog_50.objects.filter(**{filter:request.GET.get('q')}).order_by('-pub_date')
    else:
        return redirect('50')
    
    return render(request,'locally/search_50.html',{'posts':posts, 'que':que})
    


def search_site(request):
    if request.GET.get('q'):
        que = request.GET.get('q')
        variable_column = "title"
        search_type = 'contains'
        filter = variable_column + '__' + search_type
        
        posts = Blog_10.objects.filter(**{filter:request.GET.get('q')}).order_by('-pub_date')
        posts2 = Blog_20.objects.filter(**{filter:request.GET.get('q')}).order_by('-pub_date')
        posts3 = Blog_30.objects.filter(**{filter:request.GET.get('q')}).order_by('-pub_date')
        posts4 = Blog_40.objects.filter(**{filter:request.GET.get('q')}).order_by('-pub_date')
        posts5 = Blog_50.objects.filter(**{filter:request.GET.get('q')}).order_by('-pub_date')
        posts6 = Wish.objects.filter(**{filter:request.GET.get('q')}).order_by('-pub_date')
        
        post_count = posts.count()
        post_count += posts2.count()
        post_count += posts3.count()
        post_count += posts4.count()
        post_count += posts5.count()
        post_count += posts6.count()
        
        print("count : ", post_count)
    else:
        return redirect('site')
    
    return render(request,'locally/search_site.html',{'posts':posts,'posts2':posts2,'posts3':posts3,'posts4':posts4,'posts5':posts5,'posts6':posts6, 'que':que , 'post_count' : post_count})
    
def result(request):
    return render(request, 'locally/search.html')
    
def marketsellupdate(request, sell_id):
    sell_update = get_object_or_404(Sell, pk=sell_id)
    return render(request, 'locally/marketsellupdate.html')    
#이게 어디에 쓰이는 함수인지 알 수 없다..

def marketbuywrite(request):
    if request.method =='POST':
        form = NewBuy(request.POST, request.FILES)
        if form.is_valid():
            created_buy = form.save(commit=False)
            created_buy.pub_date=timezone.now()
            # created_buy.user = request.user
            # created_buy.upload_user = request.user
            created_buy.image = request.FILES.get('photo','False')
            created_buy.save()
            return redirect('marketbuy')
    else:
        form = NewBuy()
        return render(request,'locally/marketbuywrite.html',{'form':form})
    
    
    
def marketbuydetail(request, buy_id):
    buy_detail = get_object_or_404(Buy, pk=buy_id)
    return render(request, 'locally/marketbuydetail.html', {'buy': buy_detail})

def  delete_buy(request, pk):
    buy = get_object_or_404(Buy, pk=pk)
    buy.delete()
    return redirect('marketbuy')

def  delete_sell(request, pk):
    sell = get_object_or_404(Sell, pk=pk)
    sell.delete()
    return redirect('marketsell')

def  delete_free(request, pk):
    free = get_object_or_404(Free, pk=pk)
    free.delete()
    return redirect('marketfree')

def update_buy(request, pk):
    buy = get_object_or_404(Buy, pk=pk)
    form = NewBuy(request.POST, instance=buy)
    
    if form.is_valid():
        form.save()
        return redirect('marketbuy')
    
    return render(request, 'locally/marketbuywrite.html', {'form':form})

def update_sell(request,pk):
    sell = get_object_or_404(Sell, pk=pk)
    form = NewSell(request.POST, instance=sell)
    
    if form.is_valid():
        form.save()
        return redirect('marketsell')
    
    return render(request, 'locally/marketsellwrite.html', {'form':form})

def update_free(request,pk):
    free = get_object_or_404(Free, pk=pk)
    form = NewFree(request.POST, instance=free)
    
    if form.is_valid():
        form.save()
        return redirect('marketfree')
    
    return render(request, 'locally/marketfreewrite.html', {'form':form})

def marketfree(request):
    # frees=free.objects.all() 뭐가 오류나는지 모르겠으나 일단 여기 다시체크 {'frees' : frees}밑에 잇었음
    frees=Free.objects.all()
    return render(request, 'locally/marketfree.html', {'frees' : frees})

def marketfreewrite(request):
    if request.method =='POST':
        form = NewFree(request.POST)
        if form.is_valid():
            created_free = form.save(commit=False)
            created_free.pub_date=timezone.now()
            created_free.save()
            return redirect('marketfree')
    else:
        form = NewFree()
        return render(request,'locally/marketfreewrite.html',{'form':form})

def marketfreedetail(request, free_id):
    free_detail = get_object_or_404(Free, pk=free_id)
    return render(request, 'locally/marketfreedetail.html', {'free': free_detail})

def sell(request):
    sells = Sell.objects.all()
    return render(request, 'locally/marketsell.html', {'sells': sells})

def marketsellwrite(request): #sell인데 ㅠ NewFree로 통합해도되나ㅏ...? 다 봤다 ㅋㅋㅋ머하한ㅋ하니ㅋㅋㅋㅋㅇㅇ 나니??나앟아 빠르네;ㅋㅋㅋㅋㅋㅋㅋㅋ
    if request.method =='POST':
        form = NewSell(request.POST)
        if form.is_valid():
            created_sell = form.save(commit=False)
            created_sell.pub_date=timezone.now()
            created_sell.save()
            return redirect('marketsell')
    else:
        form = NewSell()
        return render(request, 'locally/marketsellwrite.html',{'form': form})

def marketselldetail(request,sell_id):
    sell_detail= get_object_or_404(Sell, pk=sell_id)
    # sell.views += 1
    # sell.save()
    # comments_list = Comment.objects.filter(sell = sell_id).order_by('-date')
    # imagepost = Imagepost.objects.filter(sell= sell.id).order_by(upload_date)
    return render(request, 'locally/marketselldetail.html', {'sell':sell_detail})
# , 'comments':comments_list, 'imagepost': imagepost 

def marketsell_post(request):
    if request.method == "POST" and request.POST['title'].strip() != "" and request.POST['content'].strip() !="":
        new_post = Post()
        new_post.title = request.POST['title']
        new_post.body = request.POST['content']
        new_post.writer = request.user.username
        new_post.pub_date = timezone.datetime.now()
        new_post. save()
        
        new_images = Imagepost()
        new_images.upload_date = timezone.datetime.now()
        new_images.upload_user = request.user
        new_images.post = new_post
        new_images.image = request.FILES['marketsell_img']
        new_images.save()
        
        return HttpResponseRedirect('images/%d' %new_post.pk)
    return render(request, 'locally/marketsellwrite.html' , {'status' : 'create'})

def jobapply(request):
    applys=apply.objects.all()
    return render(request, 'locally/jobapply.html',{'applys':applys})

def jobapplywrite(request):
    if request.method == 'POST':
        form = NewApply(request.POST)
        if form.is_valid():
            created_apply = form.save(commit=False)
            created_apply.pub_date=timezone.now()
            created_apply.user = request.user
            created_apply.save()
            
            return redirect('jobapply')
    else:
        form = NewApply()
        return render(request, 'locally/jobapplywrite.html', {'form':form})

def  delete_apply(request, pk):
    apply = get_object_or_404(apply, pk=pk)
    apply.delete()
    return redirect('jobapply')

def update_apply(request, pk):
    current_apply = get_object_or_404(apply, pk=pk)
    form = NewApply(request.POST, instance= current_apply)
    
    if form.is_valid():
        form.save()
        return redirect('jobapply')
    
    return render(request, 'locally/jobapply.html', {'form':form})
    
def jobapplyupdate(request, pk):
    current_apply = get_object_or_404(apply, pk=pk)
    form = NewApply(request.POST or None, instance = current_apply)
    if(request.method=='POST'):
        if form.is_valid():
            form.save()
            return redirect('jobapply')
    else:
        return redirect('locally/jobapplyupdate.html', {'form':form})

def jobapplydetail(request, pk):
    apply_detail=get_object_or_404(apply, pk=pk)
    return render(request, 'locally/jobapplydetail.html', {'apply':apply_detail})

def apply60(request):
    return render(request, 'locally/jobapply-60.html')

def apply40(request):
    return render(request, 'locally/jobapply-40.html')

def apply20(request):
    return render(request, 'locally/jobapply-20.html')

def apply_female(request):
    return render(request, 'locally/jobapply-female.html')

def apply_male(request):
    return render(request, 'locally/jobapply-male.html')

def offer(request):
    return render(request, 'locally/joboffer.html')

def detail(request):
    return render(request,'locally/detail.html') 


def sell_image_view(request): 
  
    if request.method == 'POST': 
        form = PostForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = PostForm() 
    return render(request, 'locally/marketsellwrite.html', {'form' : form}) 
  
  

def success(request): 
    return HttpResponse('successfuly uploaded') 

def PostForm(request):
    return render(request, 'locally/marketsellwirte.html')


class SearchFormView():
    form_class = SearchForm
    template_name='locally/search.html'
    
    def form_valid(self,form):
        word = '%s' %self.request.POST['word']
        post_list = Post.objects.filter(
            Q(title_icontains=word) | Q(content_icontains=word)
        ).distinct()
        context = {}
        context['object_list'] = post_list
        context['search_word'] = search_word
        return context
    