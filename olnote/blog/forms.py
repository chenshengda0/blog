#coding:utf-8
from django import forms

class RegisterForm(forms.Form):
	username=forms.CharField(required=False)
	password0=forms.CharField(required=False)
	password1=forms.CharField(required=False)
	nickname=forms.CharField(required=False)
	
	def clean_username(self):
		username=self.cleaned_data['username']
		#num_words = len(message.split())
		if username:
			if len(username) < 6:
				raise forms.ValidationError(u"用户名不能小于6位")
			if len(username) > 15:
				raise forms.ValidationError(u"用户名不能大于15位")
		return username

	def clean_password0(self):
		password0=self.cleaned_data['password0']
		#num_words = len(message.split())
		if password0:
			if len(password0) < 6:
				raise forms.ValidationError(u"密码长度不能小于6位")
			if len(password0) > 15:
				raise forms.ValidationError(u"密码长度不能大于15位")
			password0=self.mymd5(password0)
			return password0

	def clean_password1(self):
		password1=self.cleaned_data['password1']
		#num_words = len(message.split())
		if password1:
			if len(password1) < 6:
				raise forms.ValidationError(u"密码长度不能小于6位")
			if len(password1) > 15:
				raise forms.ValidationError(u"密码长度不能大于15位")
			password1=self.mymd5(password1)
			return password1

	def clean_nickname(self):
		nickname=self.cleaned_data['nickname']
		if nickname:
			#password1=self.mymd5(password1)
			if len(nickname) < 3:
				raise forms.ValidationError(u"昵称不能小于3位")
			if len(nickname) > 8:
				raise forms.ValidationError(u"昵称不能大于8位")
			#password0=self.mymd5(password0)
			return nickname

	def mymd5(self,str):
		import hashlib
		myMd5 = hashlib.md5()
		myMd5.update(str)
		myMd5_Digest = myMd5.hexdigest()
		return myMd5_Digest

class LoginForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField()

	def clean_username(self):
		username=self.cleaned_data['username']
		#num_words = len(message.split())
		if username:
			if len(username) < 6:
				raise forms.ValidationError(u"用户名不能小于6位")
			if len(username) > 15:
				raise forms.ValidationError(u"用户名不能大于15位")
		return username

	def clean_password(self):
		password=self.cleaned_data['password']
		#num_words = len(message.split())
		if password:
			if len(password) < 6:
				raise forms.ValidationError(u"用户名不能小于6位")
			if len(password) > 15:
				raise forms.ValidationError(u"用户名不能大于15位")
			password=self.mymd5(password)
			return password

	def mymd5(self,str):
		import hashlib
		myMd5 = hashlib.md5()
		myMd5.update(str)
		myMd5_Digest = myMd5.hexdigest()
		return myMd5_Digest
