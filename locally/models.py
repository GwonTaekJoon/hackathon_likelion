from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

class Wish(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') 
    body = models.TextField()
    wish_user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    wish = models.ForeignKey(Wish, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_contents = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)

class Joboffer(models.Model):
    joboffer_user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') 
    body = models.TextField()
    name = models.CharField(max_length=200)
    objective = models.CharField(max_length=200)
    gender  = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    career  = models.CharField(max_length=200)
    Phonenumber = models.TextField()
    

    
class Blog_10(models.Model):

    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    hits = models.IntegerField(null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def update_counter(self):
        self.post_hit = self.post_hit + 1
        self.save()
        
class Blog_20(models.Model):

    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    hits = models.IntegerField(null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
    def summary20(self):
        return self.body[:20]
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    
      
class Blog_30(models.Model):

    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    hits = models.IntegerField(null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
    def summary30(self):
        return self.body[:20]
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
  
        
class Blog_40(models.Model):

    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    hits = models.IntegerField(null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
    def summary40(self):
        return self.body[:20]
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
   
        
       
class Blog_50(models.Model):

    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    hits = models.IntegerField(null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
    def summary50(self):
        return self.body[:20]
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
   
    
class Comment10(models.Model):
    c10 = models.ForeignKey(Blog_10, on_delete = models.CASCADE, null = True, related_name='comments10')
    comment_contents = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
        
class Comment20(models.Model):
    c20 = models.ForeignKey(Blog_20, on_delete=models.CASCADE, null=True, related_name='comments20')
    comment_contents = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
    
class Comment30(models.Model):
    c30 = models.ForeignKey(Blog_30, on_delete=models.CASCADE, null=True, related_name='comments30')
    comment_contents = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
    
class Comment40(models.Model):
    c40 = models.ForeignKey(Blog_40, on_delete=models.CASCADE, null=True, related_name='comments40')
    comment_contents = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
    
class Comment50(models.Model):
    c50 = models.ForeignKey(Blog_50, on_delete=models.CASCADE, null=True, related_name='comments50')
    comment_contents = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
    
class apply(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') 
    body = models.TextField(null=True,default='')
    pay=models.TextField(null=True,default='')
    day=models.TextField(null=True,default='')
    time=models.TextField(null=True,default='')
    locate=models.TextField(null=True,default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
        
class Photo(models.Model):
    upload_user = models.IntegerField(null=True,default='')
        
class Search(models.Model):
    search_title = models.CharField(max_length=20) 

    
class Buy(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') 
    body = models.TextField()
    photo = models.ImageField(upload_to='images/%y/%m/%d/%H%M%S' , blank=True ) 
    upload_user = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    

    
class Comment_buy(models.Model):
    buy = models.ForeignKey(Buy, on_delete=models.CASCADE, null=True, related_name='comment_buys')
    comment_contents = models.CharField(max_length=20)
    create_date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=500)
    author = models.CharField(null=True,default='',max_length=100)
    
class Sell(models.Model): 
    title = models.CharField(max_length=50) 
    photo = models.ImageField(upload_to='images/%y/%m/%d/%H%M%S' , blank=True) 
    # upload_user = models.ForeignKey(User , on_delete=models.CASCADE, null=True)
    body = models.TextField()
    pub_date = models.DateTimeField('date published') 
    # post= models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    
    

class Free(models.Model): 
    title = models.CharField(max_length=50) 
    body = models.TextField()
    pub_date = models.DateTimeField('date published') 
    photo = models.ImageField(upload_to='images/%y/%m/%d/%H%M%S' , blank=True)
    upload_user = models.ForeignKey(User , on_delete=models.CASCADE, null=True)
    
class Post(models.Model):
    title=models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')
    body = models.TextField()
    user = models.ManyToManyField(User, blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
    def title_summary(self):
        if len(self.title) > 30:
            return self.title[:30] + '...'
        else:
            return self.title
        

    