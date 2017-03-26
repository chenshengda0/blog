#coding:utf-8
from django.contrib import admin
from blog.models import *
# Register your models here.
class TitleAdmin(admin.ModelAdmin):
	list_display = ('id','name','tag_index')
	list_filter = ('pub_date',) #过滤
	fields = ('name','pub_date','tag_index') #显示编辑界面能编辑的项
	ordering = ('id',)


class ListAdmin(admin.ModelAdmin):
	list_display = ('id','pid','name','tag_index')
	list_filter = ('pid',) #过滤
	search_fields = ('name',) 
	ordering = ('id',) 
	fields = ('name','pid','tag_index') #显示编辑界面能编辑的项
	raw_id_fields = ('pid',)  #将外键列表显示为搜索框

class TagAdmin(admin.ModelAdmin):
	list_display = ('id','name','pub_date')
	list_filter = ('pub_date',) #过滤
	search_fields = ('name',) 
	ordering = ('id',) 
	fields = ('name','pub_date') #显示编辑界面能编辑的项
	#filter_horizontal = ('pid',)



# a_img = models.ForeignKey(Article,default='',verbose_name=u"文章图片")
# 	n_img = models.ForeignKey(Article,default='',verbose_name=u"新闻图片")
# 	m_img = models.ForeignKey(Article,default='',verbose_name=u"音乐图片")
# 	o_img = models.ForeignKey(Article,default='',verbose_name=u"其它图片")
# 	g_img = models.ForeignKey(Article,default='',verbose_name=u"游戏图片")


# class ImgAdmin(admin.ModelAdmin):
# 	list_display = ('id','name','alt',)
# 	list_filter = ('tag',) #过滤
# 	search_fields = ('tag',) 
# 	ordering = ('id',) 
# 	fields = ('name','tag') #显示编辑界面能编辑的项
# 	raw_id_fields = ('tag',)  #将外键列表显示为搜索框
# 	#filter_horizontal = ('tag',)

class StateAdmin(admin.ModelAdmin):
	list_display = ('id','name')
	#list_filter = ('pid',) #过滤
	search_fields = ('name',) 
	ordering = ('id',) 
	fields = ('name',) #显示编辑界面能编辑的项
	#raw_id_fields = ('pid',)  #将外键列表显示为搜索框
	#filter_horizontal = ('tag',)

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('id','column','title','state','tag_state')
	list_filter = ('state',) #过滤
	search_fields = ('title',) 
	ordering = ('id',) 
	fields = ('title','column','tag_state','state','intro','content','tag','pub_date') #显示编辑界面能编辑的项
	raw_id_fields = ('state','column')  #将外键列表显示为搜索框
	filter_horizontal = ('tag',)

class GameAdmin(admin.ModelAdmin):
	list_display = ('id','column','title','state','tag_state')
	list_filter = ('state',) #过滤
	search_fields = ('title',) 
	ordering = ('id',) 
	fields = ('title','column','tag_state','state','intro','content','tag','pub_date') #显示编辑界面能编辑的项
	raw_id_fields = ('state','column')  #将外键列表显示为搜索框
	filter_horizontal = ('tag',)

class OtherAdmin(admin.ModelAdmin):
	list_display = ('id','column','title','state','tag_state')
	list_filter = ('state',) #过滤
	search_fields = ('title',) 
	ordering = ('id',) 
	fields = ('title','column','tag_state','state','intro','content','tag','pub_date') #显示编辑界面能编辑的项
	raw_id_fields = ('state','column')  #将外键列表显示为搜索框
	filter_horizontal = ('tag',)

class NewAdmin(admin.ModelAdmin):
	list_display = ('id','column','title','state','tag_state')
	list_filter = ('state',) #过滤
	search_fields = ('title',) 
	ordering = ('id',) 
	fields = ('title','column','tag_state','state','intro','content','tag','pub_date') #显示编辑界面能编辑的项
	raw_id_fields = ('state','column')  #将外键列表显示为搜索框
	filter_horizontal = ('tag',)

class MusicAdmin(admin.ModelAdmin):
	list_display = ('id','column','title','state','tag_state','link')
	list_filter = ('state',) #过滤
	search_fields = ('title',) 
	ordering = ('id',) 
	fields = ('title','tag_state','link','name','content','column','state','tag','pub_date') #显示编辑界面能编辑的项
	raw_id_fields = ('state','column')  #将外键列表显示为搜索框
	filter_horizontal = ('tag',)

class VideoAdmin(admin.ModelAdmin):
	list_display = ('id','column','title','state','tag_state','link')
	list_filter = ('state',) #过滤
	search_fields = ('title',) 
	ordering = ('id',) 
	fields = ('title','tag_state','link','name','content','column','state','tag','pub_date') #显示编辑界面能编辑的项
	raw_id_fields = ('state','column')  #将外键列表显示为搜索框
	filter_horizontal = ('tag',)

class A_imgAdmin(admin.ModelAdmin):
	list_display = ('id','name','alt','img')
	list_filter = ('img',) #过滤
	ordering = ('id',) 
	fields = ('name','alt','img') #显示编辑界面能编辑的项
	raw_id_fields = ('img',)  #将外键列表显示为搜索框

class M_imgAdmin(admin.ModelAdmin):
	list_display = ('id','name','alt','img')
	list_filter = ('img',) #过滤
	ordering = ('id',) 
	fields = ('name','alt','img') #显示编辑界面能编辑的项
	raw_id_fields = ('img',)  #将外键列表显示为搜索框

class G_imgAdmin(admin.ModelAdmin):
	list_display = ('id','name','alt','img')
	list_filter = ('img',) #过滤
	ordering = ('id',) 
	fields = ('name','alt','img') #显示编辑界面能编辑的项
	raw_id_fields = ('img',)  #将外键列表显示为搜索框

class O_imgAdmin(admin.ModelAdmin):
	list_display = ('id','name','alt','img')
	list_filter = ('img',) #过滤
	ordering = ('id',) 
	fields = ('name','alt','img') #显示编辑界面能编辑的项
	raw_id_fields = ('img',)  #将外键列表显示为搜索框

class N_imgAdmin(admin.ModelAdmin):
	list_display = ('id','name','alt','img')
	list_filter = ('img',) #过滤
	ordering = ('id',) 
	fields = ('name','alt','img') #显示编辑界面能编辑的项
	raw_id_fields = ('img',)  #将外键列表显示为搜索框

class V_imgAdmin(admin.ModelAdmin):
	list_display = ('id','name','alt','img')
	list_filter = ('img',) #过滤
	ordering = ('id',) 
	fields = ('name','alt','img') #显示编辑界面能编辑的项
	raw_id_fields = ('img',)  #将外键列表显示为搜索框

class LinkAdmin(admin.ModelAdmin):
	list_display = ('id','name','href','pub_date')
	list_filter = ('pub_date',) #过滤
	ordering = ('id',) 
	fields = ('name','href','pub_date') #显示编辑界面能编辑的项

class ImgAdmin(admin.ModelAdmin):
	list_display = ('id','name','pub_date')
	list_filter = ('pub_date',) #过滤
	ordering = ('id',) 
	fields = ('name','pub_date') #显示编辑界面能编辑的项

class CommentAdmin(admin.ModelAdmin):
	list_display = ('id','username','mailto','href','commenta','commentn','commentm','commentv','commentg','commento')
	list_filter = ('commenta','commentn','commentm','commentv','commentg','commentv') #过滤
	search_fields = ('username',) 
	ordering = ('id',) 
	fields = ('username','commenta','commentn','commentm','commentv','commentg','commento','content','mailto','href','pub_date') #显示编辑界面能编辑的项
	raw_id_fields = ('username',)  #将外键列表显示为搜索框
	#filter_horizontal = ('tag',)

class OuserAdmin(admin.ModelAdmin):
	list_display = ('id','username','nickname','img','pub_date','ip_addr')
	list_filter = ('pub_date',) #过滤
	search_fields = ('nickname',) 
	ordering = ('id',) 
	fields = ('username','password','nickname','img','pub_date','ip_addr') #显示编辑界面能编辑的项
	raw_id_fields = ('img',)  #将外键列表显示为搜索框
	#filter_horizontal = ('tag',)

admin.site.register(Title,TitleAdmin)
admin.site.register(List,ListAdmin)
admin.site.register(Tag,TagAdmin)
#admin.site.register(Img,ImgAdmin)
admin.site.register(State,StateAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(New,NewAdmin)
admin.site.register(Music,MusicAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(Link,LinkAdmin)
admin.site.register(Other,OtherAdmin)
admin.site.register(Game,GameAdmin)
admin.site.register(A_img,A_imgAdmin)
admin.site.register(N_img,N_imgAdmin)
admin.site.register(M_img,M_imgAdmin)
admin.site.register(G_img,G_imgAdmin)
admin.site.register(O_img,O_imgAdmin)
admin.site.register(V_img,V_imgAdmin)
admin.site.register(Img,ImgAdmin)
admin.site.register(Ouser,OuserAdmin)
admin.site.register(Comment,CommentAdmin)


