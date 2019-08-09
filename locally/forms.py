from django import forms
from .models import Blog_10, Blog_20, Blog_30, Blog_40, Blog_50, Wish, Comment, Joboffer, Buy, Sell, Free, apply , Comment_buy
from .models import Search
from .models import Comment10,Comment20,Comment30,Comment40,Comment50
from django.db import models

class NewJoboffer(forms.ModelForm):
    class Meta:
        model = Joboffer
        fields = ['title', 'body', 'objective', 'gender', 'age', 'career', 'Phonenumber', 'name']  
    
class NewBlog_10(forms.ModelForm):
    class Meta:
        model = Blog_10
        fields = ['title', 'body']
class NewBlog_20(forms.ModelForm):
    class Meta:
        model = Blog_20
        fields = ['title', 'body']
class NewBlog_30(forms.ModelForm):
    class Meta:
        model = Blog_30
        fields = ['title', 'body']
class NewBlog_40(forms.ModelForm):
    class Meta:
        model = Blog_40
        fields = ['title', 'body']
        
class NewBlog_50(forms.ModelForm):
    class Meta:
        model = Blog_50
        fields = ['title', 'body']

class NewWish(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ['title','body']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_contents']  

class Comment10Form(forms.ModelForm):
    class Meta:
        model = Comment10
        fields=['comment_contents']
    
class Comment20Form(forms.ModelForm):
    class Meta:
        model = Comment20
        fields=['comment_contents']
    
class Comment30Form(forms.ModelForm):
    class Meta:
        model = Comment30
        fields=['comment_contents']
    
class Comment40Form(forms.ModelForm):
    class Meta:
        model = Comment40
        fields = ['comment_contents']
    
class Comment50Form(forms.ModelForm):
     class Meta:
        model = Comment50
        fields=['comment_contents']

        
        
class SearchForm(forms.ModelForm):
    model = Search
    word = ['search_title']
    
        
        
#class CommentForm(forms.ModelForm):
    #class Meta:
     #  model = Comment
   # fields = ('author','text',)

class NewBuy(forms.ModelForm):
	class Meta:
		model = Buy
		fields = ['title','body']
        #,'photo'
        
class NewSell(forms.ModelForm): 
    class Meta: 
        model = Sell
        fields = ['title',  'body']     
        #,'photo'
        
class NewFree(forms.ModelForm): 
    class Meta: 
        model = Free
        fields = ['title', 'body']
        
class NewApply(forms.ModelForm):
    class Meta:
        model = apply
        fields = ['title','body','pay','day','time','locate']
        
        
class SearchForm(forms.ModelForm):
    word = forms.CharField(label='Search Word')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment_buy
        fields = ('author', 'text')
