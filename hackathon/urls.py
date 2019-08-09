from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import locally.views
from django.conf.urls.static import static 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('developing', locally.views.developing, name="developing"),
    path('', locally.views.home, name="home"),
    path('choice/', locally.views.choice, name="choice"),
    path('site/', locally.views.site, name="site"),
    path('10/', locally.views.read_10, name="ten"),
    path('20/', locally.views.read_20, name="twenty"),
    path('30/', locally.views.read_30, name="thirty"), 
    path('40/', locally.views.read_40, name="forty"), 
    path('50/', locally.views.read_50, name="fifty"),  
    path('schedule/', locally.views.schedule, name="schedule"),
    path('schedule_1/', locally.views.schedule_1, name="schedule_1"),
    path('schedule_2/', locally.views.schedule_2, name="schedule_2"),
    path('schedule_3/', locally.views.schedule_3, name="schedule_3"),
    path('schedule_4/', locally.views.schedule_4, name="schedule_4"),
    
    path('wish/', locally.views.wish, name="wish"),
    path('locally/wish/<int:wish_id>/', locally.views.wishclick, name="wishclick"),
    path('locally/wishwrite/', locally.views.wishwrite, name="wishwrite"),      
    path('locally/wishcreate/', locally.views.wishcreate, name="wishcreate"),
    path('wishupdate/<int:pk>', locally.views.wishupdate, name="wishupdate"),
    path('wishdelete/<int:pk>', locally.views.wishdelete, name="wishdelete"),   
    path('comment_write/<int:pk>', locally.views.comment_write, name="comment_write"),
    path('10/comment_write/<int:pk>', locally.views.comment_10, name="comment_10"),
    path('20/comment_write/<int:pk>', locally.views.comment_20, name="comment_20"),
    path('30/comment_write/<int:pk>', locally.views.comment_30, name="comment_30"),
    path('40/comment_write/<int:pk>', locally.views.comment_40, name="comment_40"),
    path('50/comment_write/<int:pk>', locally.views.comment_50, name="comment_50"),
    
    path('joboffer/', locally.views.joboffer, name="joboffer"),
    path('joboffer/<int:joboffer_id>/', locally.views.jobofferclick, name="jobofferclick"),
    path('jobofferwrite/', locally.views.jobofferwrite, name='jobofferwrite'),      
    path('joboffercreate/', locally.views.joboffercreate, name='joboffercreate'),
    path('jobofferupdate/<int:pk>', locally.views.jobofferupdate, name="jobofferupdate"),
    path('jobofferdelete/<int:pk>', locally.views.jobofferdelete, name="jobofferdelete"),   
    
    
    
    
    path('market/', locally.views.market, name="market"),
    path('job/', locally.views.job, name="job"),
    path('guide/', locally.views.guide, name="guide"),
    path('write10/', locally.views.create_10, name="write_10"),
    path('write20/', locally.views.create_20, name="write_20"),
    path('write30/', locally.views.create_30, name="write_30"),
    path('write40/', locally.views.create_40, name="write_40"),
    path('write50/', locally.views.create_50, name="write_50"),
    path('accounts/', include('accounts.urls')),
    path('schedulebokji/', locally.views.schedulebokji, name="schedulebokji"),
    
    path('update10/<int:pk>', locally.views.update_10, name="update_10"),
    path('update20/<int:pk>', locally.views.update_20, name="update_20"),
    path('update30/<int:pk>', locally.views.update_30, name="update_30"),
    path('update40/<int:pk>', locally.views.update_40, name="update_40"),
    path('update50/<int:pk>', locally.views.update_50, name="update_50"),
    
    
    path('delete10/<int:pk>', locally.views.delete_10, name="delete_10"),
    path('delete20/<int:pk>', locally.views.delete_20, name="delete_20"),
    path('delete30/<int:pk>', locally.views.delete_30, name="delete_30"),
    path('delete40/<int:pk>', locally.views.delete_40, name="delete_40"),
    path('delete50/<int:pk>', locally.views.delete_50, name="delete_50"),
    
    path('market/buy', locally.views.marketbuy, name="marketbuy"),
    path('market/buy/write', locally.views.marketbuywrite, name="marketbuywrite"),
    path('market/buy/detail/<int:buy_id>', locally.views.marketbuydetail,name="marketbuydetail"), #int:pk말고 buy_id가 맞는거같다
    path('market/buy/detail/comment/<int:pk>', locally.views.add_commentbuy, name="add_commentbuy"),
    path('market/buy/detail/update/<int:pk>', locally.views.update_buy, name="marketbuyupdate"),
    path('market/buy/detail/delete/<int:pk>', locally.views.delete_buy, name="marketbuydelete"),
    
    path('market/sell', locally.views.sell, name="marketsell"),
    path('market/sell/write', locally.views.marketsellwrite, name="marketsellwrite"),
    # path('market/sell/update', locally.views.marketsellupdate, name="marketsellupdate"), 어디에쓰이는 함수인것인가
    path('market/sell/detail/<int:sell_id>', locally.views.marketselldetail, name="marketselldetail"),
    path('market/sell/detail/update/<int:pk>', locally.views.update_sell, name="marketsellupdate"),
    path('market/sell/detail/delete/<int:pk>', locally.views.delete_sell, name="marketselldelete"),
    
    
    path('market/free', locally.views.marketfree, name="marketfree"),
    path('market/free/write', locally.views.marketfreewrite, name="marketfreewrite"),
    path('market/free/detail/<int:free_id>', locally.views.marketfreedetail,name="marketfreedetail"),
    path('market/free/detail/update/<int:pk>', locally.views.update_free, name="marketfreeupdate"),
    path('market/free/detail/delete/<int:pk>', locally.views.delete_free, name="marketfreedelete"),
    
    path('job/apply', locally.views.jobapply, name="jobapply"),
    path('job/apply/write', locally.views.jobapplywrite, name="jobapplywrite"),
    path('job/apply/detail/<int:pk>', locally.views.jobapplydetail, name="jobapplydetail"),
    path('job/apply/detail/update/<int:pk>', locally.views.update_apply, name="update_apply"),
    path('job/apply/detail/delete/<int:pk>', locally.views.delete_apply, name="delete_apply"),
    path('job/apply60', locally.views.apply60, name="apply60"),
    path('job/apply40', locally.views.apply40, name="apply40"),
    path('job/apply20', locally.views.apply20, name="apply20"),
    path('job/apply/female', locally.views.apply_female, name="apply_female"),
    path('job/apply/male', locally.views.apply_male, name="apply_male"),
    path('job/offer', locally.views.offer, name="offer"),
    path('sell_image_upload', locally.views. sell_image_view, name = 'sell_image_upload'), 
    path('success', locally.views.success, name = 'success'), 
    path('10/<int:blog_id>', locally.views.detail_10, name='detail10'),
    path('20/<int:blog_id>', locally.views.detail_20, name='detail20'),
    path('30/<int:blog_id>', locally.views.detail_30, name='detail30'),
    path('40/<int:blog_id>', locally.views.detail_40, name='detail40'),
    path('50/<int:blog_id>', locally.views.detail_50, name='detail50'),
    path('search_10', locally.views.search_10, name='search_10'),
    path('search_20', locally.views.search_20, name='search_20'),
    path('search_30', locally.views.search_30, name='search_30'),
    path('search_40', locally.views.search_40, name='search_40'),
    path('search_50', locally.views.search_50, name='search_50'),
    path('result', locally.views.result, name="result"),
    path('search_site', locally.views.search_site, name="search_site"),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

        
# from django.conf.urls.static import static
# from django.contrib.staticfiles.views import serve
# from django.views.decorators.cache import cache_control

# # YOUR urlpatterns here... 

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, view=cache_control(no_cache=True, must_revalidate=True)(serve))