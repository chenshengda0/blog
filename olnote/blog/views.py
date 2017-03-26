#coding:utf-8
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.views.decorators.cache import cache_page
from blog.models import *
from django.views.generic import View
from blog.forms import RegisterForm,LoginForm
from markdown import markdown 

# Create your views here.
#@cache_page(60)
def ip_str(ip_str):
	client_ip = ip_str.split('.')
	str0=''
	for i in client_ip:
		str0+=i+'-'
	str0=str0.strip('-')
	return str0

def index(request,**kwargs):
	#return HttpResponse(data['content'])
	return render_to_response(kwargs['template'],kwargs['data'])

def tag(request,**kwargs):
	return render_to_response(kwargs['template'],kwargs['data'])

def list_hr(request,**kwargs):
	return render_to_response(kwargs['template'],kwargs['data'])

def contents(request,**kwargs):
	#return HttpResponse(kwargs['data']['content'])
	#return HttpResponse(kwargs['data']['comment'])
	return render_to_response(kwargs['template'],kwargs['data'])

def register(request,template):
	#return HttpResponse(kwargs['data']['username'])
	if request.is_ajax():
		if request.method=='POST':
		#ajax判断用户名是否已存在 
			if 'username' in request.POST and 'password0' in request.POST and 'password1' in request.POST and 'nickname' in request.POST:
				
				username=request.POST['username']
				password0=request.POST['password0']
				password1=request.POST['password1']
				nickname=request.POST['nickname']
				register_data=RegisterForm({'username':username,'password0':password0,'password1':password1,'nickname':nickname})

				if register_data.is_valid():

					username=register_data.cleaned_data['username']
					password=register_data.cleaned_data['password1']
					nickname=register_data.cleaned_data['nickname']
					import datetime
					import random
					pub_date=datetime.datetime.now()

					img_ids=Img.objects.values('id')
					img_id=random.sample(img_ids,1)[0]['id']
					
					ip_addr=ip_str(request.META['REMOTE_ADDR'])

					data=list(Ouser.objects.get_or_create(username=username,password=password,nickname=nickname,pub_date=pub_date,img_id=img_id,ip_addr=ip_addr))[1]
					return JsonResponse({'data':data})
				else:
					return JsonResponse({'data':False})

			if 'username' in request.POST:
				username=request.POST['username']
				form=RegisterForm({'username':username})
				if form.is_valid():
					username=form.cleaned_data['username']
					#return HttpResponse(data)
					data=Ouser.objects.filter(username=username)
					if data:
						return JsonResponse({'data':True})
					else:
						return JsonResponse({'data':False})#返回json数据给ajax请求
				else:
					return JsonResponse(form.errors)#返回值是一个以字段名为键错误信息为值列表的数据
			#ajax判断昵称是否已存在
			if 'nickname' in request.POST:
				nickname=request.POST['nickname']
				form=RegisterForm({'nickname':nickname})
				if form.is_valid():
					nickname=form.cleaned_data['nickname']
					#return HttpResponse(data)
					data=Ouser.objects.filter(nickname=nickname)
					if data:
						return JsonResponse({'data':True})
					else:
						return JsonResponse({'data':False})#返回json数据给ajax请求
				else:
					return JsonResponse(form.errors)#返回值是一个以字段名为键错误信息为值列表的数据
			#判断用户密码
			if 'password0' in request.POST and 'password1' in request.POST:
				password0=request.POST['password0']
				password1=request.POST['password1']
				form=RegisterForm({'password0':password0,'password1':password1})
				if form.is_valid():
					password0=form.cleaned_data['password0']
					password1=form.cleaned_data['password1']
					return JsonResponse({'data':False})#返回json数据给ajax请求

				else:
					return JsonResponse(form.errors)#返回值是一个以字段名为键错误信息为值列表的数据
		#存数据到数据库Author.objects.get_or_create(name="WeizhongTu", email="tuweizhong@163.com")
			#if username and password1 and nickname:
				#return HttpResponse(username)
					#添加当前时间字段
	else:
		return render_to_response(template)

def login(request,template):
	if request.is_ajax():
		if request.method=="POST":
			if 'username' in request.POST and 'password' in request.POST:
				username=request.POST['username']
				password=request.POST['password']

				form=LoginForm({'username':username,'password':password})
				if form.is_valid():
					#return JsonResponse({'data':True})
					username=form.cleaned_data['username']
					password=form.cleaned_data['password']
					#return JsonResponse({'data':True})
					data=list(Ouser.objects.filter(username=username,password=password).values('id','username','nickname','img'))
					if data:
						#存储session
						data[0]['img']=Img.objects.filter(id=9).values('name')[0]['name']
						request.session[ip_str(request.META['REMOTE_ADDR'])]=data[0]
						#data[0]['username']
						return JsonResponse({'data':data[0]})
					else:
						return JsonResponse({'data':False})

			elif 'del' in request.POST:
				del request.session[ip_str(request.META['REMOTE_ADDR'])]
				return JsonResponse({'data':True})
	else:
		return render_to_response(template)

# def forget(request,**kwargs):
# 	#return HttpResponse(kwargs['data']['content'])
# 	return render_to_response(kwargs['template'],kwargs['data'])

def forget(request,username,template):
	if request.is_ajax():
		if request.method=="POST":
			if 'username' in request.POST:

				username=request.POST['username']

				ip = ip_str( request.META['REMOTE_ADDR'] )
				form=RegisterForm({'username':username})
				
				if form.is_valid():

					username = form.cleaned_data['username']
					
					data=list(Ouser.objects.filter(username=username,ip_addr=ip).values('ip_addr','username'))
					if data:
						#跳转
						return JsonResponse({'data':data})
					else:
						return JsonResponse({'data':False})
	else:
		data={}
		myview=MyView()
		data['title']=myview.nav()
		data['tag']=myview.tags()
		data['article_new']=myview.recent(x=0,y=1)
		data['article_two']=myview.recent(x=1,y=2)
		data['link']=myview.links()
		data['main']=[{'href':"/",'name':'Home'},{'href':'#','name':u'忘记密码'}]
		dat=list(Ouser.objects.filter(username=username).values('ip_addr','username','nickname','img'))
		dat[0]['img']=list(Img.objects.filter(id=dat[0]['img']).values('name'))[0]['name']
		data['user']=dat[0]
		if 'password0' in request.POST and 'password1' in request.POST:
			password0=request.POST['password0']
			password1=request.POST['password1']
			ip = ip_str( request.META['REMOTE_ADDR'] )
			form= RegisterForm({'password0':password0,'password1':password1})
			dat=list(Ouser.objects.filter(username=username,ip_addr=ip).values('ip_addr','username','id'))
			if dat:
				if  form.is_valid():
					password0=form.cleaned_data['password0']
					password1=form.cleaned_data['password1']
					if password0 == password1:
						#将数据写入数据库
						if Ouser.objects.filter(id=dat[0]['id']).update(password=password0):
							return HttpResponseRedirect("/")
					else:
						data['error']=u"两次输入的密码不一致"
				else:
					data['error']=form.errors.values()[0][0]
			else:
				data['error']=u'用户名匹配不成功修改失败'
		#return HttpResponse(data['user'])
		return render_to_response(template,data)

def comment(request):
	#return render_to_response("user/comment.html")
	if request.is_ajax():
		if request.method=="POST":
			if 'ipaddr' in request.POST and request.POST['ipaddr']:
				ipaddr=request.POST['ipaddr']
				#return JsonResponse({'data':True})#防止恶意修改ip值
				#return JsonResponse({'data':True})
				if ipaddr in request.session and ipaddr == ip_str(request.META['REMOTE_ADDR']):
					#已登录用户
					return JsonResponse({'data':True})#防止恶意修改ip值
			else:#未登陆
				return JsonResponse({'data':False})


def discuss(request):
	s=request.META['HTTP_REFERER']
	if request.is_ajax():
		if request.method=="POST":
			if 'content' in request.POST and 'model' in request.POST and 'aid' in request.POST and 'uid' in request.POST:
				content=request.POST['content']
				model=request.POST['model']
				aid=request.POST['aid']
				uid=request.POST['uid']
				#return JsonResponse({'model':model,'aid':aid})
				import datetime
				pub_date=datetime.datetime.now()
				if model == "study":
					commenta=aid
					data=Comment.objects.get_or_create(username_id=uid,content=content,pub_date=pub_date,commenta=commenta)
				elif model == "chat":
					commentn=aid
					data=Comment.objects.get_or_create(username_id=uid,content=content,pub_date=pub_date,commentn=commentn)
				elif model == "music":
					commentm=aid
					data=Comment.objects.get_or_create(username_id=uid,content=content,pub_date=pub_date,commentm=commentm)
				elif model == "video":
					commentv=aid
					data=Comment.objects.get_or_create(username_id=uid,content=content,pub_date=pub_date,commentv=commentv)
				elif model == "game":
					commentg=aid
					data=Comment.objects.get_or_create(username_id=uid,content=content,pub_date=pub_date,commentg=commentg)
				else:
					commento=aid
					data=Comment.objects.get_or_create(username_id=uid,content=content,pub_date=pub_date,commento=commento)
				#存数据库并显示
				#return JsonResponse({'data':True})
				if data:
					return JsonResponse({'data':True})
				else:
					return JsonResponse({'data':False})	
	else:
		url=request.META['HTTP_REFERER']
		import re
		reg=re.compile(r"\/(\w+)\/\w+\/conts(\d+)\/")#编译
		dat=reg.findall(url)#正则对象去查找字符串
		username=request.session[ip_str(request.META['REMOTE_ADDR'])]['id']
		return render_to_response('user/comment.html',{'purl':url,'model':dat[0][0],'aid':dat[0][1],'uid':username,'url':url})

def discuss_mailto(request,metd,cid):
	if metd == 'mailto':
		if request.is_ajax():
			if request.method == "POST":
				if 'content' in request.POST and 'model' in request.POST and 'aid' in request.POST and 'uid' in request.POST and 'cid' in request.POST:
					content=request.POST['content']
					model=request.POST['model']
					aid=request.POST['aid']
					uid=request.POST['uid']
					cid=request.POST['cid']
					#return JsonResponse({'model':model,'aid':aid})
					import datetime
					pub_date=datetime.datetime.now()
					if model == "study":
						commenta=aid
						data=Comment.objects.get_or_create(username_id=uid,content=content,pub_date=pub_date,commenta=commenta,mailto=cid)
					elif model == "chat":
						commentn=aid
						data=Comment.objects.get_or_create(username_id=uid,content=content,pub_date=pub_date,commentn=commentn,mailto=cid)
					elif model == "music":
						commentm=aid
						data=Comment.objects.get_or_create(username_id=uid,content=content,pub_date=pub_date,commentm=commentm,mailto=cid)
					elif model == "video":
						commentv=aid
						data=Comment.objects.get_or_create(username_id=uid,content=content,pub_date=pub_date,commentv=commentv,mailto=cid)
					elif model == "game":
						commentg=aid
						data=Comment.objects.get_or_create(username_id=uid,content=content,pub_date=pub_date,commentg=commentg,mailto=cid)
					else:
						commento=aid
						data=Comment.objects.get_or_create(username_id=uid,content=content,pub_date=pub_date,commento=commento,mailto=cid)
					#存数据库并显示
					#return JsonResponse({'data':True})
					if data:
						return JsonResponse({'data':True})
					else:
						return JsonResponse({'data':False})	

		else:
			url=request.META['HTTP_REFERER']
			import re
			reg=re.compile(r"\/(\w+)\/\w+\/conts(\d+)\/")#编译
			dat=reg.findall(url)#正则对象去查找字符串
			username=request.session[ip_str(request.META['REMOTE_ADDR'])]['id']
			com=Comment.objects.get(id=cid)
			user=Ouser.objects.get(id=com.username_id)
			purl="/discuss/%s/%s/" %(metd,cid)
			#return HttpResponse(user.nickname)
			return render_to_response('user/comment_mailto.html',{'comment':com,'user':user,'model':dat[0][0],'aid':dat[0][1],'uid':username,'purl':purl,'url':url})
	elif metd == "href":
		if request.is_ajax():
			if request.method == "POST":
				if 'content' in request.POST and 'model' in request.POST and 'aid' in request.POST and 'uid' in request.POST and 'cid' in request.POST:
					content=request.POST['content']
					model=request.POST['model']
					aid=request.POST['aid']
					uid=request.POST['uid']
					cid=request.POST['cid']
					#return JsonResponse({'model':model,'aid':aid})
					import datetime
					pub_date=datetime.datetime.now()
					if model == "study":
						commenta=aid
						data=Comment.objects.get_or_create(username_id=uid,content=content,pub_date=pub_date,commenta=commenta,href=cid)
					elif model == "chat":
						commentn=aid
						data=Comment.objects.get_or_create(username_id=uid,content=content,pub_date=pub_date,commentn=commentn,href=cid)
					elif model == "music":
						commentm=aid
						data=Comment.objects.get_or_create(username_id=uid,content=content,pub_date=pub_date,commentm=commentm,href=cid)
					elif model == "video":
						commentv=aid
						data=Comment.objects.get_or_create(username_id=uid,content=content,pub_date=pub_date,commentv=commentv,href=cid)
					elif model == "game":
						commentg=aid
						data=Comment.objects.get_or_create(username_id=uid,content=content,pub_date=pub_date,commentg=commentg,href=cid)
					else:
						commento=aid
						data=Comment.objects.get_or_create(username_id=uid,content=content,pub_date=pub_date,commento=commento,href=cid)
					#存数据库并显示
					#return JsonResponse({'data':True})
					if data:
						return JsonResponse({'data':True})
					else:
						return JsonResponse({'data':False})	
		url=request.META['HTTP_REFERER']
		import re
		reg=re.compile(r"\/(\w+)\/\w+\/conts(\d+)\/")#编译
		dat=reg.findall(url)#正则对象去查找字符串
		username=request.session[ip_str(request.META['REMOTE_ADDR'])]['id']
		com=Comment.objects.get(id=cid)
		user=Ouser.objects.get(id=com.username_id)
		purl="/discuss/%s/%s/" %(metd,cid)
		return render_to_response('user/comment_href.html',{'comment':com,'user':user,'purl':purl,'model':dat[0][0],'aid':dat[0][1],'uid':username,'url':url})

		
# class RegisterView(View):
# 	def get(self,request,**kwargs):
# 		kwargs['template']="user/register.html"
# 		if request.method=="POST":
# 			form=RegisterForm({'username':request.POST['username']})
# 			if form.is_valid():
# 				kwargs['data']['forms']=False
# 				return JsonResponse(kwargs['data']['forms'], safe=False)
# 		else:	
# 			form=RegisterForm()
# 			return register(request,**kwargs)

# class ForgetView(View):
# 	def get(self,request,**kwargs):
# 		kwargs['template']="user/forget.html"
# 		return login(request,**kwargs)

class CommentView(View):
	def get(self,request,**kwargs):
		kwargs['template']="user/comment.html"
		return comment(request,**kwargs)


class MyView(View):
	def get(self,request,**kwargs):
		if kwargs.has_key('lid'):#传过来文章id
			kwargs['lid']=kwargs['lid'].split('s')[1]
			if kwargs['lid']:
				kwargs['template']="content/content.html"
				kwargs['data']=self.common()
				kwargs['data']['article_two']=self.recent(x=1,y=2)
				kwargs['data']['content']=self.cont_data(kwargs['conts'],kwargs['lid'])
				kwargs['data']['tag_list']=self.tag_cont_list(tags=self.cont_data(kwargs['conts'],kwargs['lid']))
				kwargs['data']['main']=self.main_list(kwargs['conts'],kwargs['temp'],kwargs['lid'])
				kwargs['data']['login']=self.login(request)
				kwargs['data']['comment']=self.comment_list(request,kwargs['conts'],kwargs['lid'])

				return contents(request,**kwargs)
			else:#传过来标题列表
				kwargs['template']="list/list_0.html"
				kwargs['data']=self.common()
				kwargs['data']['article_two']=self.recent(x=1,y=2)
				kwargs['data']['content']=self.list_hr_data(kwargs['conts'],kwargs['temp'])
				kwargs['data']['tag_list']=self.tag_cont_list(tags=self.list_hr_data(kwargs['conts'],kwargs['temp']))
				kwargs['data']['main']=self.main_list(kwargs['conts'],kwargs['temp'])
				kwargs['data']['login']=self.login(request)
				return list_hr(request,**kwargs)
		elif kwargs.has_key('tag'):#传过来标签
			kwargs['template']="tag/tag.html"
			kwargs['tag']=int(kwargs['tag'].split('_')[1])#分割字符串为列表转换成整型
			#return HttpResponse(tag)
			kwargs['data']=self.common()
			kwargs['data']['article_two']=self.recent(x=1,y=2)
			kwargs['data']['tags']=self.tag_data(kwargs['tag'])
			kwargs['data']['tag_list']=self.tag_cont_list(tags=self.tag_data(kwargs['tag']))
			kwargs['data']['main']=self.main_list(kwargs['tag'])
			kwargs['data']['login']=self.login(request)
			return tag(request,**kwargs)
		elif not kwargs:#没有传任何东西
			kwargs['template']="index.html"
			kwargs['data']=self.common()
			kwargs['data']['article_two']=self.recent(x=1,y=2)
			kwargs['data']['content']=self.cont()
			kwargs['data']['main']=self.main_list('index')
			kwargs['data']['tag_list']=self.tag_cont_list(tags=self.cont())
			kwargs['data']['login']=self.login(request)
			return index(request,**kwargs)
	
	def login(self,request):
		if ip_str(request.META['REMOTE_ADDR']) in request.session:
			login={}
			login['ip']=ip_str(request.META['REMOTE_ADDR'])
			login['username']=request.session[login['ip']]['username']
			login['nickname']=request.session[login['ip']]['nickname']
			login['id']=request.session[login['ip']]['id']
			return login
		else:
			return False
	
	def comment_list(self,request,conts,lid):
		if conts=="study":
			data=list(Comment.objects.filter(commenta=lid).values('id','pub_date','username','commenta','mailto','href','content').order_by('-pub_date'))
			data=self.comment_list_data(data=data,dbobj=Article.objects)
		elif conts=="chat":
			data=list(Comment.objects.filter(commentn=lid).values('id','pub_date','username','commenta','mailto','href','content').order_by('-pub_date'))
			data=self.comment_list_data(data=data,dbobj=New.objects)
		elif conts=="music":
			data=list(Comment.objects.filter(commentm=lid).values('id','pub_date','username','commenta','mailto','href','content').order_by('-pub_date'))
			data=self.comment_list_data(data=data,dbobj=Music.objects)
		elif conts=="video":
			data=list(Comment.objects.filter(commentv=lid).values('id','pub_date','username','commenta','mailto','href','content').order_by('-pub_date'))
			data=self.comment_list_data(data=data,dbobj=Video.objects)
		elif conts=="game":
			data=list(Comment.objects.filter(commentg=lid).values('id','pub_date','username','commenta','mailto','href','content').order_by('-pub_date'))
			data=self.comment_list_data(data=data,dbobj=Game.objects)
		elif conts=="other":
			data=list(Comment.objects.filter(commento=lid).values('id','pub_date','username','commenta','mailto','href','content').order_by('-pub_date'))
			data=self.comment_list_data(data=data,dbobj=Other.objects)
		return data
			#数据处理
			
	def comment_list_data(self,data,dbobj):
		for i in data:
			i['username'] = list(Ouser.objects.filter(id="%s" %i['username']).values('nickname','img','id'))[0]
			i['username']['img']=list(Img.objects.filter(id=i['username']['img']).values('name'))[0]['name']
			if i['mailto']:
				i['mailto']=list(Comment.objects.filter(id=i['mailto']).values('pub_date','username','content'))[0]
				i['mailto']['username']=Ouser.objects.get(id=i['mailto']['username'])
			if i['href']:
				i['href']=list(Comment.objects.filter(id=i['href']).values('pub_date','username','content'))[0]
				i['href']['username']=Ouser.objects.get(id=i['href']['username'])
		if data:
			return data
		else:
			return u'暂无评论'		
			


	def nav(self):
		'导航栏'
		t=list(Title.objects.values('id','name','tag_index').order_by("id"))
		for i in range(len(t)):
			#id t[i][0]
			t[i]['son']=list(Title.objects.get(id=t[i]['id']).list_set.values('name','id','tag_index').order_by('id'))
			if t[i]['son']:
				for j in range(len(t[i]['son'])):
					t[i]['son'][j]['href']="/%s/%s/conts" % (t[i]['tag_index'],t[i]['son'][j]['tag_index'])
		return t

	def tags(self):
		import random

		tag=[[],[],[],[]]
		tas=[]
		ta=list(Tag.objects.values('id','name'))
		for j in ta:
			j['href']="/tags/t_%s" % j['id']
		#判断当tag对应的模块有内容时才显示
		for i in range(len(ta)):
			tp0=list(Tag.objects.get(id=ta[i]['id']).article_set.all())
			tm1=Tag.objects.get(id=ta[i]['id']).music_set.all()
			tv2=Tag.objects.get(id=ta[i]['id']).video_set.all()
			tn3=Tag.objects.get(id=ta[i]['id']).new_set.all()
			tg4=Tag.objects.get(id=ta[i]['id']).game_set.all()
			to5=Tag.objects.get(id=ta[i]['id']).other_set.all()
			if tp0 or tm1 or tv2 or tn3 or tg4 or to5:
				tas.append(ta[i])
		tags=random.sample(tas,16)
		for index in range(len(tags)):
			if index%4==0:
				tag[0].append(tags[index])
			elif index%4==1:
				tag[1].append(tags[index])
			elif index%4==2:
				tag[2].append(tags[index])
			else:
				tag[3].append(tags[index])
		return tag

	def recent(self,x,y):
		'''最近更新'''
		stats=[]
		stat=list(State.objects.values('id','name'))
		for st in stat:
			if st['name'] != 'draft' and st['name'] != 'index':
				stats.append(st['id'])
		article_new=[]
		arts=[]
		columns=[]
		for s in stats:
			article_new.append(list(Article.objects.filter(state_id = s).values('title','column','id').order_by("-pub_date")[x:y])) 
			article_new.append(list(New.objects.filter(state_id = s).values('title','column','id').order_by("-pub_date")[x:y])) 
			article_new.append(list(Game.objects.filter(state_id = s).values('title','column','id').order_by("-pub_date")[x:y])) 
			article_new.append(list(Other.objects.filter(state_id = s).values('title','column','id').order_by("-pub_date")[x:y])) 
			article_new.append(list(Music.objects.filter(state_id = s).values('title','column','id').order_by("-pub_date")[x:y])) 
			article_new.append(list(Video.objects.filter(state_id = s).values('title','column','id').order_by("-pub_date")[x:y]))
		for art in article_new:
			arts.append(art[0]['column'])
		for i in arts:
			a=list(List.objects.filter(id=i).select_related('pid').values('pid')[:1])[0]['pid']
			b=list(Title.objects.filter(id=a).values('tag_index'))[0]['tag_index']
			c=list(List.objects.filter(id=i).values('tag_index'))[0]['tag_index']
			for art in article_new:
				if art[0]['column']==i:
					art[0]['column']="/%s/%s/conts%s" % (b,c,art[0]['id'])
		return article_new

	def links(self):
		link = Link.objects.values('name','href')
		return link 

	def cont(self):
		"""内容"""
		stats=[]
		stat=list(State.objects.values('id','name'))
		for st in stat:
			if st['name'] == 'index':
				stats.append(st['id'])#stats[0]
		contents=()
		arts=[]
		tag_id=[]
		contents+=tuple(list(Article.objects.filter(state=stats[0]).values('id','title','column','content','pub_date','state').order_by('-pub_date')[:4]))
		contents+=tuple(list(Music.objects.filter(state=stats[0]).values('id','column','title','pub_date','state').order_by('-pub_date')[:4]))
		contents+=tuple(list(Other.objects.filter(state=stats[0]).values('id','column','title','content','pub_date','state').order_by('-pub_date')[:2]))
		contents+=tuple(list(New.objects.filter(state=stats[0]).values('id','column','title','content','pub_date','state').order_by('-pub_date')[:2]))
		contents+=tuple(list(Game.objects.filter(state=stats[0]).values('id','column','title','content','pub_date','state').order_by('-pub_date')[:2]))
		contents+=tuple(list(Video.objects.filter(state=stats[0]).values('id','column','title','pub_date','state').order_by('-pub_date')[:2]))
		
		#链接
		
		for j in range(len(contents)):
			arts.append(contents[j]['column'])
			if j>=0 and j<4:
				contents[j]['tag']=list(Article.objects.get(id=contents[j]['id']).tag.values('id','name'))
				contents[j]['img']=list(Article.objects.get(id=contents[j]['id']).a_img_set.all())
			elif j>=4 and j<8:
				contents[j]['tag']=list(Music.objects.get(id=contents[j]['id']).tag.values('id','name'))
				contents[j]['img']=list(Music.objects.get(id=contents[j]['id']).m_img_set.all())
			elif j>=8 and j<10:
				contents[j]['tag']=list(Other.objects.get(id=contents[j]['id']).tag.values('id','name'))
				contents[j]['img']=list(Other.objects.get(id=contents[j]['id']).o_img_set.all())
			elif j>=10 and j<12:
				contents[j]['tag']=list(New.objects.get(id=contents[j]['id']).tag.values('id','name'))
				contents[j]['img']=list(New.objects.get(id=contents[j]['id']).n_img_set.all())
			elif  j>=12 and j<14:
				contents[j]['tag']=list(Game.objects.get(id=contents[j]['id']).tag.values('id','name'))
				contents[j]['img']=list(Game.objects.get(id=contents[j]['id']).g_img_set.all())
			else:
				contents[j]['tag']=list(Video.objects.get(id=contents[j]['id']).tag.values('id','name'))		
				contents[j]['img']=list(Video.objects.get(id=contents[j]['id']).v_img_set.all())
			for k in contents[j]['tag']:
				k['href']="/tags/t_%s" % k['id']
		for i in arts:
			a=list(List.objects.filter(id=i).select_related('pid').values('pid')[:1])[0]['pid']
			b=list(Title.objects.filter(id=a).values('tag_index'))[0]['tag_index']
			c=list(List.objects.filter(id=i).values('tag_index'))[0]['tag_index']
			for j in range(len(contents)):
				if contents[j]['column']==i:
					contents[j]['column']="/%s/%s/conts%s" % (b,c,contents[j]['id'])
		return contents

	##首页##
	def common(self):
		data={}
		data['title']=self.nav()
		data['tag']=self.tags()
		data['article_new']=self.recent(x=0,y=1)
		data['link']=self.links()
		return data

	def tag_data_null(self,listname,model,img):
		st=[]
		tp=[]
		arts=[]
		stat=list(State.objects.values('id','name'))
		#状态
		for i in range(len(stat)):
			if stat[i]['name'] != 'draft':
				st.append(stat[i]['id'])
		if range(len(listname))==0:
			return False
		else:
			for i in range(len(listname)):
				if listname[i]['state'] in st:
					tp.append(listname[i])
		if tp:
			#处理标签与图片
			for i in range(len(tp)):
				#标签，图片
				tp[i]['tag']=list(model.get(id=tp[i]['id']).tag.values('id','name'))
				for k in tp[i]['tag']:
					k['href']="/tags/t_%s" % k['id']
				if img=='a_img_set':
					tp[i]['img']=list(model.get(id=tp[i]['id']).a_img_set.all())
				elif img=='m_img_set':
					tp[i]['img']=list(model.get(id=tp[i]['id']).m_img_set.all())
				elif img=='n_img_set':
					tp[i]['img']=list(model.get(id=tp[i]['id']).n_img_set.all())
				elif img=='o_img_set':
					tp[i]['img']=list(model.get(id=tp[i]['id']).o_img_set.all())
				elif img=='v_img_set':
					tp[i]['img']=list(model.get(id=tp[i]['id']).v_img_set.all())
				else:
					tp[i]['img']=list(model.get(id=tp[i]['id']).g_img_set.all())
				#链接
				arts.append(tp[i]['column'])
			for j in arts:
				a=list(List.objects.filter(id=j).select_related('pid').values('pid')[:1])[0]['pid']
				b=list(Title.objects.filter(id=a).values('tag_index'))[0]['tag_index']
				c=list(List.objects.filter(id=j).values('tag_index'))[0]['tag_index']
				for k in range(len(tp)):
					if tp[k]['column']==j:
						tp[k]['column']="/%s/%s/conts%s" % (b,c,tp[k]['id'])
			return tp
		else:
			return False
		

	def tag_data(self,tag):

		contents=()
		tp0=list(Tag.objects.get(id=tag).article_set.values('id','title','column','content','pub_date','state'))
		tm1=list(Tag.objects.get(id=tag).music_set.values('id','column','title','pub_date','state'))
		tn2=list(Tag.objects.get(id=tag).new_set.values('id','column','title','pub_date','state'))
		to3=list(Tag.objects.get(id=tag).other_set.values('id','column','title','pub_date','state'))
		tv4=list(Tag.objects.get(id=tag).video_set.values('id','column','title','pub_date','state'))
		tg5=list(Tag.objects.get(id=tag).game_set.values('id','column','title','pub_date','state'))
		tp0=self.tag_data_null(listname=tp0,model=Article.objects,img='a_img_set')
		tm1=self.tag_data_null(listname=tm1,model=Music.objects,img='m_img_set')
		tn2=self.tag_data_null(listname=tn2,model=New.objects,img='n_img_set')
		to3=self.tag_data_null(listname=to3,model=Other.objects,img='o_img_set')
		tv4=self.tag_data_null(listname=tv4,model=Video.objects,img='v_img_set')
		tg5=self.tag_data_null(listname=tg5,model=Game.objects,img='g_img_set')
		if tp0:
			contents+=tuple(tp0)
		if tm1:
			contents+=tuple(tm1)
		if tn2:
			contents+=tuple(tn2)
		if to3:
			contents+=tuple(to3)
		if tv4:
			contents+=tuple(tv4)
		if tg5:
			contents+=tuple(tg5)
		return contents

	def tag_cont_list(self,tags): 
		tag={}
		ta=[]
		for i in range(len(tags)):
			for j in tags[i]['tag']:
				tag["tag%s" % j['id']]=[j['id'],j['name'],"/tags/t_%s" % j['id']]
		#return tag.items()
		if len(tag)>=14:
			import random
			cont_tag=random.sample(tag.items(),14)
			return cont_tag
		else:
			return tag.items()

	def main_list(self,tag,*hrefs):
		if tag=='index':
			ta=[{'href':"/",'name':'Home'},]
		elif len(hrefs)==0:
			t=Tag.objects.get(id=tag)
			ta=[{'href':"/",'name':'Home'},{'href':'#','name':u'标签'},{'href':'#','name':t.name}]
		elif len(hrefs)==1:
			tname=Title.objects.filter(tag_index=tag).values('name')#惰性评估，使用到才会调用否则报错
			lname=List.objects.filter(tag_index=hrefs[0]).values('name')
			#return tname
			ta=[{'href':"/",'name':'Home'},{'href':'#','name':tname[0]['name']},{'href':'#','name':lname[0]['name']}]
		elif len(hrefs)==2:
			ctname=Title.objects.filter(tag_index=tag).values('name')#惰性评估，使用到才会调用否则报错
			clname=List.objects.filter(tag_index=hrefs[0]).values('name')
			if tag=='study':
				ccname=Article.objects.filter(id=hrefs[1]).values('title')
			elif tag=="chat":
				ccname=New.objects.filter(id=hrefs[1]).values('title')
			elif tag=="music":
				ccname=Music.objects.filter(id=hrefs[1]).values('title')
			elif tag=="video":
				ccname=Video.objects.filter(id=hrefs[1]).values('title')
			elif tag=="game":
				ccname=Game.objects.filter(id=hrefs[1]).values('title')
			elif tag=="other":
				ccname=Other.objects.filter(id=hrefs[1]).values('title')
			#return myconname
			ta=[{'href':"/",'name':'Home'},{'href':'#','name':ctname[0]['name']},{'href':'/%s/%s/conts' % (tag,hrefs[0]),'name':clname[0]['name']},{'href':'#','name':"%s" % ccname[0]['title']}]
		return ta	

	def list_hr_data(self,conts,temp):
		lid=List.objects.filter(tag_index=temp).values_list('id')
		content=()
		if conts=='study':
			tdata=list(List.objects.get(id='%s' % lid[0]).article_set.values('id','title','content','state','column','pub_date').order_by('-pub_date'))
			tdata=self.tag_data_null(listname=tdata,model=Article.objects,img='a_img_set')
		elif conts=='chat':
			tdata=list(List.objects.get(id='%s' % lid[0]).new_set.values('id','title','content','state','column','pub_date').order_by('-pub_date'))
			tdata=self.tag_data_null(listname=tdata,model=New.objects,img='n_img_set')
		elif conts=='music':
			tdata=list(List.objects.get(id='%s' % lid[0]).music_set.values('id','title','name','state','column','pub_date').order_by('-pub_date'))
			tdata=self.tag_data_null(listname=tdata,model=Music.objects,img='m_img_set')
		elif conts=='video':
			tdata=list(List.objects.get(id='%s' % lid[0]).video_set.values('id','title','name','state','column','pub_date').order_by('-pub_date'))
			tdata=self.tag_data_null(listname=tdata,model=Video.objects,img='v_img_set')
		elif conts=='game':
			tdata=list(List.objects.get(id='%s' % lid[0]).game_set.values('id','title','content','state','column','pub_date').order_by('-pub_date'))
			tdata=self.tag_data_null(listname=tdata,model=Game.objects,img='g_img_set')
		else:
			tdata=list(List.objects.get(id='%s' % lid[0]).other_set.values('id','title','content','state','column','pub_date').order_by('-pub_date'))
			tdata=self.tag_data_null(listname=tdata,model=Other.objects,img='o_img_set')
		content+=tuple(tdata)
		return content
	
	def cont_data(self,conts,lid):
		if conts=='study':
			tdata=list(Article.objects.filter(id=lid).values('id','title','content','state','column','pub_date','tag_state'))
			tdata[0]['content']=markdown(tdata[0]['content'])
			tdata=self.tag_data_null(listname=tdata,model=Article.objects,img='a_img_set')
		elif conts=='chat':
			tdata=list(New.objects.filter(id=lid).values('id','title','content','state','column','pub_date','tag_state'))
			tdata[0]['content']=markdown(tdata[0]['content'])
			tdata=self.tag_data_null(listname=tdata,model=New.objects,img='n_img_set')
		elif conts=='music':
			tdata=list(Music.objects.filter(id=lid).values('id','title','name','content','link','state','column','pub_date','tag_state'))
			tdata[0]['content']=markdown(tdata[0]['content'])
			tdata=self.tag_data_null(listname=tdata,model=Music.objects,img='m_img_set')
		elif conts=='video':
			tdata=list(Video.objects.filter(id=lid).values('id','title','content','link','name','state','column','pub_date','tag_state'))
			tdata[0]['content']=markdown(tdata[0]['content'])
			tdata=self.tag_data_null(listname=tdata,model=Video.objects,img='v_img_set')
		elif conts=='game':
			tdata=list(Game.objects.filter(id=lid).values('id','title','content','state','column','pub_date','tag_state'))
			tdata[0]['content']=markdown(tdata[0]['content'])
			tdata=self.tag_data_null(listname=tdata,model=Game.objects,img='g_img_set')
		else:
			tdata=list(Other.objects.filter(id=lid).values('id','title','content','state','column','pub_date','tag_state'))
			tdata[0]['content']=markdown(tdata[0]['content'])
			tdata=self.tag_data_null(listname=tdata,model=Other.objects,img='o_img_set')
		return tdata
	