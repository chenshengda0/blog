#coding:utf-8
from __future__ import unicode_literals

from django.db import models,connection
class TitleManager(models.Manager):
	def title_id(self):
		cursor = connection.cursor()
		cursor.execute("""
			SELECT blog_title.id,blog_title.name,blog_title.tag_index
			FROM blog_title
		""")
		d = [k[0:] for k in cursor.fetchall()]
		return d

# class ListManager(models.Manager):
# 	def list(self):
# 		cursor = connection.cursor()
# 		cursor.execute("""
# 			SELECT blog_list.id,blog_list.tag_index
# 			FROM blog_list
# 		""")
# 		d = [k[0:] for k in cursor.fetchall()]
# 		return d

# Create your models here.
class Title(models.Model):
	name = models.CharField(max_length=30,verbose_name=u"栏目")
	pub_date = models.DateTimeField(verbose_name=u'添加时间')
	tag_index = models.CharField(default="",max_length=20,verbose_name="标记")
	objects = TitleManager()
	def __unicode__(self):
		return self.name
	class Meta:
		unique_together = (("name",),)


class List(models.Model):
	name = models.CharField(max_length=40,verbose_name=u"列表")
	pid = models.ForeignKey(Title,verbose_name=u"上级栏目")
	tag_index = models.CharField(default="",max_length=20,verbose_name="标记")
	#objects = ListManager()
	def __unicode__(self):
		return self.name
	class Meta:
		unique_together = (("name",),)

class Tag(models.Model):
	name = models.CharField(max_length=5,verbose_name=u"标签")
	#pid = models.ManyToManyField(Title,verbose_name=u"所属栏目")
	pub_date = models.DateTimeField(verbose_name=u'添加时间')
	def __unicode__(self):
		return self.name
	class Meta:
		unique_together = (("name",),)

class State(models.Model):
	name = models.CharField(max_length=10,verbose_name=u"状态")
	def __unicode__(self):
		return self.name
	class Meta:
		unique_together = (("name",),)

class Article(models.Model):
	title = models.CharField(max_length=50,verbose_name=u"标题")#
	tag_state = models.CharField(max_length=50,verbose_name=u"标记",default="text")#
	content = models.TextField(verbose_name=u"内容")#
	intro = models.CharField(max_length=100,verbose_name=u"概要",blank=True)
	tag = models.ManyToManyField(Tag,verbose_name=u"标签")#
	state = models.ForeignKey(State,verbose_name=u"状态")#
	column = models.ForeignKey(List,verbose_name=u"栏目")#
	pub_date = models.DateTimeField(verbose_name=u'添加时间')#
	def __unicode__(self):
		return self.title
	class Meta:
		unique_together = (("title",),)

class New(models.Model):
	title = models.CharField(max_length=50,verbose_name=u"标题")#
	tag_state = models.CharField(max_length=50,verbose_name=u"标记",default="text")#
	content = models.TextField(verbose_name=u"内容")#
	intro = models.CharField(max_length=100,verbose_name=u"概要",blank=True)
	tag = models.ManyToManyField(Tag,verbose_name=u"标签")#
	state = models.ForeignKey(State,verbose_name=u"状态")#
	column = models.ForeignKey(List,verbose_name=u"栏目")#
	pub_date = models.DateTimeField(verbose_name=u'添加时间')#
	def __unicode__(self):
		return self.title
	class Meta:
		unique_together = (("title",),)

class Game(models.Model):
	title = models.CharField(max_length=50,verbose_name=u"标题")#
	tag_state = models.CharField(max_length=50,verbose_name=u"标记",default="text")#
	content = models.TextField(verbose_name=u"内容",blank=True)#
	intro = models.CharField(max_length=100,verbose_name=u"概要",blank=True)
	tag = models.ManyToManyField(Tag,verbose_name=u"标签")#
	state = models.ForeignKey(State,verbose_name=u"状态")#
	column = models.ForeignKey(List,verbose_name=u"栏目")#
	pub_date = models.DateTimeField(verbose_name=u'添加时间')#
	def __unicode__(self):
		return self.title
	class Meta:
		unique_together = (("title",),)


class Other(models.Model):
	title = models.CharField(max_length=50,verbose_name=u"标题")#
	tag_state = models.CharField(max_length=50,verbose_name=u"标记",default="text")#
	content = models.TextField(verbose_name=u"内容")#
	intro = models.CharField(max_length=100,verbose_name=u"概要",blank=True)
	tag = models.ManyToManyField(Tag,verbose_name=u"标签")#
	state = models.ForeignKey(State,verbose_name=u"状态")#
	column = models.ForeignKey(List,verbose_name=u"栏目")#
	pub_date = models.DateTimeField(verbose_name=u'添加时间')#
	def __unicode__(self):
		return self.title
	class Meta:
		unique_together = (("title",),)
   
class Music(models.Model):
	title = models.CharField(max_length=50,verbose_name=u"歌曲名")
	name = models.CharField(max_length=50,default="",verbose_name=u"歌手")
	content=models.TextField(default="",verbose_name=u"歌词",blank=True)
	tag_state = models.CharField(max_length=50,verbose_name=u"标记",default="music")#
	link=models.CharField(max_length=50,verbose_name=u"链接",default="/static/music/")
	tag = models.ManyToManyField(Tag,verbose_name=u"标签")
	state = models.ForeignKey(State,verbose_name=u"状态")
	column = models.ForeignKey(List,verbose_name=u"栏目")
	pub_date = models.DateTimeField(verbose_name=u'添加时间')
  	def __unicode__(self):
		return self.title
	class Meta:
		unique_together = (("title",),)

class Video(models.Model):
	title = models.CharField(max_length=50,verbose_name=u"电影名")
	name = models.CharField(max_length=50,default="",verbose_name=u"演员")
	content=models.TextField(default="",verbose_name=u"文章",blank=True)
	tag_state = models.CharField(max_length=50,verbose_name=u"标记",default="video")#
	link=models.CharField(max_length=50,verbose_name=u"链接",default="/static/video/")
	tag = models.ManyToManyField(Tag,verbose_name=u"标签")
	state = models.ForeignKey(State,verbose_name=u"状态")
	column = models.ForeignKey(List,verbose_name=u"栏目")
	pub_date = models.DateTimeField(verbose_name=u'添加时间')
  	def __unicode__(self):
		return self.title
	class Meta:
		unique_together = (("title",),)

class Link(models.Model):
	name=models.CharField(max_length=50,verbose_name=u"名称")
	href=models.CharField(max_length=50,verbose_name=u"链接到")
	pub_date = models.DateTimeField(verbose_name=u'添加时间')
	class Meta:
		unique_together = (("name","href"),)

# class Img(models.Model):
# 	name = models.CharField(max_length=100,verbose_name=u"图片")
# 	alt = models.CharField(max_length=100,default="img",blank=True,verbose_name=u"描叙")
# 	tag = models.ForeignKey(Tag,default='1')
# 	# a_img = models.ForeignKey(Article,default='',verbose_name=u"文章图片")#
# 	# n_img = models.ForeignKey(New,default='',verbose_name=u"新闻图片")#
# 	# m_img = models.ForeignKey(Music,default='',verbose_name=u"音乐图片")#
# 	# o_img = models.ForeignKey(Other,default='',verbose_name=u"其它图片")#
# 	# g_img = models.ForeignKey(Game,default='',verbose_name=u"游戏图片")#
# 	def __unicode__(self):
# 		return self.name
class A_img(models.Model):
	name = models.CharField(max_length=100,verbose_name=u"图片",default="/static/img/article/")
	alt = models.CharField(max_length=100,default=u"这是一张问文章插图",blank=True,verbose_name=u"描叙")
	img = models.ForeignKey(Article,verbose_name=u"文章图片")
	class Meta:
		unique_together = (("name",),)

class N_img(models.Model):
	name = models.CharField(max_length=100,verbose_name=u"图片",default="/static/img/new/")
	alt = models.CharField(max_length=100,default=u"这是一张问新闻插图",blank=True,verbose_name=u"描叙")
	img = models.ForeignKey(New,verbose_name=u"新闻图片")
	class Meta:
		unique_together = (("name",),)

class G_img(models.Model):
	name = models.CharField(max_length=100,verbose_name=u"图片",default="/static/img/game/")
	alt = models.CharField(max_length=100,default=u"这是一张游戏插图",blank=True,verbose_name=u"描叙")
	img = models.ForeignKey(Game,verbose_name=u"游戏图片")
	class Meta:
		unique_together = (("name",),)

class M_img(models.Model):
	name = models.CharField(max_length=100,verbose_name=u"图片",default="/static/img/music/")
	alt = models.CharField(max_length=100,default=u"这是一张音乐插图",blank=True,verbose_name=u"描叙")
	img = models.ForeignKey(Music,verbose_name=u"音乐图片")
	class Meta:
		unique_together = (("name",),)

class O_img(models.Model):
	name = models.CharField(max_length=100,verbose_name=u"图片",default="/static/img/other/")
	alt = models.CharField(max_length=100,default=u"这是一张图片",blank=True,verbose_name=u"描叙")
	img = models.ForeignKey(Other,verbose_name=u"其他图片")
	class Meta:
		unique_together = (("name",),)

class V_img(models.Model):
	name = models.CharField(max_length=100,verbose_name=u"图片",default="/static/img/video/")
	alt = models.CharField(max_length=100,default=u"这是一张图片",blank=True,verbose_name=u"描叙")
	img = models.ForeignKey(Video,verbose_name=u"电影图片")
	class Meta:
		unique_together = (("name",),)

class Img(models.Model):
	name=models.CharField(max_length=100,verbose_name=u"用户图标",default="/static/img/img/")
	pub_date=models.DateTimeField(verbose_name=u"添加时间")
	class Meta:
		unique_together = (("name",),)

class Ouser(models.Model):
	username=models.CharField(max_length=20,verbose_name=u"用户名")
	password=models.CharField(max_length=40,verbose_name=u"密码")
	nickname=models.CharField(max_length=20,verbose_name=u"昵称")
	pub_date=models.DateTimeField(verbose_name=u"添加时间")
	ip_addr=models.CharField(max_length=30,verbose_name=u"IP",default='')
	img=models.ForeignKey(Img,verbose_name=u"图标")
	def __unicode__(self):
		return self.username
	class Meta:
		unique_together = (("username","nickname"),)

class Comment(models.Model):
	content=models.TextField(verbose_name=u"内容")
	pub_date=models.DateTimeField(verbose_name=u"评论时间")
	username=models.ForeignKey(Ouser,verbose_name=u"评论人")
	commenta=models.CharField(max_length=20,verbose_name=u"评论文章",blank=True)
	commentn=models.CharField(max_length=20,verbose_name=u"评论新闻",blank=True)
	commentm=models.CharField(max_length=20,verbose_name=u"评论音乐",blank=True)
	commentv=models.CharField(max_length=20,verbose_name=u"评论电影",blank=True)
	commentg=models.CharField(max_length=20,verbose_name=u"评论游戏",blank=True)
	commento=models.CharField(max_length=20,verbose_name=u"评论其它",blank=True)
	mailto=models.CharField(max_length=20,verbose_name=u"回复",blank=True)
	href=models.CharField(max_length=20,verbose_name=u"引用",blank=True)

