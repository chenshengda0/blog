window.onload=function(){
	$("#myCarousel").carousel('cycle');
	var width= window.screen.availWidth;
	var content = document.getElementById('content');
	var list = document.getElementById('list');
	if(width<=768){
		    	//console.log(deltax,width*0.1)
		    	//显示内容页，隐藏标签页
		    	list.className="col-md-3 col-xs-10 col-xs-offset-1"
		    	content.style.display="block";
		    	list.style.display="none";
		   		console.log(content)
		    }
	    document.addEventListener('touchstart',function(event){
                //获取触屏滑动时的所有事件（touchstart获取所有的事件）
                document.querySelector('body').addEventListener("touchmove", function(ev){
                    ev.preventDefault();
                })
            startx = event.touches[0].pageX;//获取手势起点坐标（开始坐标保存在event.touches[]里面）
            });

        document.addEventListener('touchend',function(event){
            endx = event.changedTouches[0].pageX;//获取手势终点坐标（终点坐标保存在event.changeTouches[]里面）
            deltax = endx - startx;
            if(Math.abs(deltax) >= 0.5*width){
		    	//console.log(deltax,width*0.1)
		    	//显示内容页，隐藏标签页
		    	if(content.style.display=="none" && list.style.display=="block"){
		    		content.style.display="block";
		    		list.style.display="none";
		    	}else if (content.style.display=="block" && list.style.display=="none") {
		    		content.style.display="none";
		    		list.style.display="block";
		    	}
		    }
        });
//友情链接样式
	var links=$("#link").find("a");
	var linknum = links.length;
	for(var i=0;i<linknum;i++){
		if (i%3==1) {
			links[i].style.fontSize = '17px';
		}else if (i%3==2) {
			links[i].style.fontSize = '20px';
		}else{
			links[i].style.fontSize = '15px';
		}
	} 
}
function userregister(obj){
	layer.open({
		  type: 2,
		  skin: 'layui-layer-lan', //样式类名
		  title: '用户注册',
		  closeBtn: 1, //不显示关闭按钮
		  anim: 5,
		  area:['400px','380px'],
		  shadeClose: true, //开启遮罩关闭
		  content: '/register'
		});
}

/*function userforget(obj){
	layer.open({
		  type: 2,
		  skin: 'layui-layer-lan', //样式类名
		  title: '忘记密码',
		  closeBtn: 1, //不显示关闭按钮
		  anim: 5,
		  area:['400px','280px'],
		  shadeClose: true, //开启遮罩关闭
		  content: '/forget'
		});
}*/

function userlogin(obj){
		layer.open({
		  type: 2,
		  skin: 'layui-layer-lan', //样式类名
		  title: '用户登录',
		  closeBtn: 1, //不显示关闭按钮
		  anim: 5,
		  area:['400px','280px'],
		  shadeClose: true, //开启遮罩关闭
		  content: '/login',
		});
}

function userforgrt(obj){
	//删除session
	$.ajax({ type	: 'POST', 
			url	: '/login/', 
			data : {'del':"session"}, 
			enctype : "multipart/form-data",//发送ajax请求必须要请求头 
			success: function(data){ 
				if(data.data){
					window.location.href="/";
					
				}
			}
		})
}

function comment(obj,tag='comment',cid=''){
	//判断用户是否已登陆
	var ipaddr=$("#ip").val()
	//console.log(ipaddr)
	$.ajax({ type	: 'POST', 
			url	: '/comment/', 
			data : {'ipaddr':ipaddr}, 
			enctype : "multipart/form-data",//发送ajax请求必须要请求头 
			success: function(data){ 
				console.log(data)
					if(data.data){
						if (tag=="comment"){
							layer.open({
							  type: 2,
							  skin: 'layui-layer-lan', //样式类名
							  title: '评论',
							  closeBtn: 1, //不显示关闭按钮
							  anim: 5,
							  area:['500px','300px'],
							  shadeClose: true, //开启遮罩关闭
							  content: '/discuss/',
							});
						}else if (tag=="mailto") {
							layer.open({
							  type: 2,
							  skin: 'layui-layer-lan', //样式类名
							  title: '评论',
							  closeBtn: 1, //不显示关闭按钮
							  anim: 5,
							  area:['500px','400px'],
							  shadeClose: true, //开启遮罩关闭
							  content: '/discuss/mailto/'+cid+'/',
							});
						}else{
							layer.open({
							  type: 2,
							  skin: 'layui-layer-lan', //样式类名
							  title: '评论',
							  closeBtn: 1, //不显示关闭按钮
							  anim: 5,
							  area:['500px','400px'],
							  shadeClose: true, //开启遮罩关闭
							  content: '/discuss/href/'+cid+'/',
							});
						}
							
					}else{
					layer.msg('系统检测到您未登录，无法评论！',{
						icon: 2,
						time:2000,
					});
				}
			}})
	/*layer.open({
		  type: 2,
		  skin: 'layui-layer-lan', //样式类名
		  title: '评论',
		  closeBtn: 1, //不显示关闭按钮
		  anim: 5,
		  area:['400px','240px'],
		  shadeClose: true, //开启遮罩关闭
		  content: '/comment/',
		});*/
}

function comusername(obj){
	var str=$.trim($(obj).val());
	if(/^[a-z,A-Z]{1}\w{5,14}$/.test(str)){
		$.ajax({ type	: 'POST', 
			url	: '/register/', 
			data : {'username':str}, 
			enctype : "multipart/form-data",//发送ajax请求必须要请求头 
			success: function(data){ 
				if(! data.data){
					document.getElementById("username").style.color="green"
					$("#username").html('用户名可用')
				}else{
					document.getElementById("username").style.color="red"
					$("#username").html('用户名已被占用')
				}
			}})
	}else{
		var msg=$("#username").html()
		//console.log(msg)
		document.getElementById("username").style.color="red"
		$("#username").html('用户名不合法')
		obj.focus()
		setTimeout(function(){
			$("#username").html(msg)
		},2000);
	}
	
}

function compassword(obj){
	var str=$.trim($(obj).val());
	if(/^.{6,15}$/.test(str)){
		
		
	}else{
		var msg=$("#password0").html()
		document.getElementById("password0").style.color="red"
		$("#password0").html('密码不合法')
		obj.focus()
		setTimeout(function(){
			$("#password0").html(msg)
		},2000);
	}
}

function forgetpassword(obj){
	var pasword0=$.trim($("#forgetpassa").val())
	var pasword1=$.trim($("#forgetpassb").val())
	if (/^.{6,15}$/.test(password0)  && password0==password1 ){
		//提交表单
	}else{
		$("#passwordb").val()="密码不匹配"
	}
}

function comupassword1(obj){
	var a=$.trim($(obj).val());
	var b=$.trim($('#exampleInputAmount1').val())
	$.ajax({ type	: 'POST', 
			url	: '/register/', 
			data : {'password0':b,'password1':a}, 
			enctype : "multipart/form-data",//发送ajax请求必须要请求头 
			success: function(data){ 
				if(! data.data){
					document.getElementById("password1").style.color="green"
					$("#password1").html('密码匹配成功')
				}else{
					document.getElementById("password1").style.color="red"
					$("#password1").html('两次输入的密码不一致')
				}
			}})
	if(!a==b){
		var msg=$("#password1").html()
		document.getElementById("password1").style.color="red"
		$("password1").html('两次输入的密码不一致')
		obj.focus()
		setTimeout(function(){
			$("#password1").html(msg)
		},2000);
	}
}

function comunickname(obj){
	var str=$.trim($(obj).val());
	if(/^[\u4e00-\u9fa5]{3,8}$/.test(str)){
		//ajax
		$.ajax({ type	: 'POST', 
			url	: '/register/', 
			data : {'nickname':str}, 
			enctype : "multipart/form-data",//发送ajax请求必须要请求头 
			success: function(data){ 
				if(! data.data){
					document.getElementById("nickname").style.color="green"
					$("#nickname").html('昵称可用')
				}else{
					document.getElementById("nickname").style.color="red"
					$("#nickname").html('昵称已经被占用')
				}
			}})
	}else{
		var msg=$("#nickname").html()
		document.getElementById("nickname").style.color="red"
		$("#nickname").html('昵称不合法')
		obj.focus()
		setTimeout(function(){
			$("#nickname").html(msg)
		},2000);
	}
}

function sub(obj){
	var username=document.getElementById("username").innerHTML
	var password=document.getElementById("password1").innerHTML
	var nickname=document.getElementById("nickname").innerHTML

	if(username=="用户名可用" && password=="密码匹配成功" && nickname=="昵称可用"){
		var user=$("#exampleInputAmount0").val()
		var pass0=$("#exampleInputAmount1").val()
		var pass=$("#exampleInputAmount2").val()
		var nick=$("#exampleInputAmount3").val()
		$.ajax({ type	: 'POST', 
			url	: '/register/', 
			data : {'username':user,'password0':pass0,'password1':pass,'nickname':nick}, 
			enctype : "multipart/form-data",//发送ajax请求必须要请求头 
			success: function(data){ 
				console.log(data)
				if(data.data){
					obj.innerHTML="注册成功，请登录！"
					$("#loginmsg")[0].style.display='block';
					$('#timemsg')[0].innerHTML=2;
					setTimeout(function(){
						parent.layer.closeAll()
					}, 2000)
					
				}else{
					obj.innerHTML="发生未知错误，请刷新页面重新填写"
				}
			}
		})
	}
}

function login(obj){
	var username=$.trim($("#exampleInputAmount0").val());
	var password=$.trim($("#exampleInputAmount1").val());
	if(username.length<6 || username.length>15 || password.length<6 || password.length>15){
		$("#usernamemsg")[0].style.color="red";
		$("#usernamemsg")[0].innerHTML="用户名或密码错误";
		setTimeout(function(){
					$("#usernamemsg")[0].innerHTML="";	
					}, 2000)
	}else{
		$.ajax({ type	: 'POST', 
			url	: '/login/', 
			data : {'username':username,'password':password}, 
			enctype : "multipart/form-data",//发送ajax请求必须要请求头 
			success: function(data){ 
				if(data.data){
					 
					parent.layer.closeAll();
					//parent.location.href="/"
					parent.location.reload ();
					//window.location.reload("/");
					
				}else{
					$("#usernamemsg")[0].style.color="red";
					$("#usernamemsg")[0].innerHTML="用户名或密码错误";
					setTimeout(function(){
						$("#usernamemsg")[0].innerHTML="";	
					}, 2000)
				}
			}
		})
	}
}

function forget(obj){
	var username=$.trim($("#exampleInputAmount0").val())
	if (username.length<6 || username.length>15){
		$("#usernamemsg")[0].style.color="red";
		$("#usernamemsg")[0].innerHTML="请在本页面输入用户名以作为忘记密码的依据";
		setTimeout(function(){
					$("#usernamemsg")[0].innerHTML="";	
					}, 2000)
		return false;
	}else{
		$.ajax({ type	: 'POST', 
			url	: '/forget/'+username+"/", 
			data : {'username':username}, 
			enctype : "multipart/form-data",//发送ajax请求必须要请求头 
			success: function(data){ 
				//console.log(data)
				if(data.data){
					//console.log(data.data[0].username)
					parent.layer.closeAll();
					parent.location.href="/forget/"+data.data[0].username+"/";
				}else{
					$("#usernamemsg")[0].style.color="red";
					$("#usernamemsg")[0].innerHTML="请核对用户名,且忘记密码必须在注册的机器上进行";
					setTimeout(function(){
							$("#usernamemsg")[0].innerHTML="";	
						}, 2000);
				}
			}
		})
	}
}

function discuss(obj){
	var content=$("#demo").val()
	var purl=$("#purl").val()
	var model=$("#model").val()
	var uid=$("#uid").val()
	var aid=$("#aid").val()
	//console.log(purl,model,aid,uid)
	if($.trim(content).length){
		$.ajax({ type	: 'POST', 
			url	: '/discuss/', 
			data : {'content':content,'model':model,'aid':aid,'uid':uid}, 
			enctype : "multipart/form-data",//发送ajax请求必须要请求头 
			success: function(data){ 
				if(data.data){
					parent.layer.closeAll();
					parent.location.href=purl;
				}else{
					$("#errormsg")[0].style.color="red";
					$("#errormsg")[0].innerHTML="出错了,请稍后重试";
					setTimeout(function(){
							$("#errormsg")[0].innerHTML="";	
						}, 2000);
				}
			}})
	}else{
		//console.log(text)
	}
	//console.log(text)
}
//回复 写入数据库
function discuss_mailto(obj){
	var content=$("#demo").val()
	var purl=$("#purl").val()
	var url=$("#url").val()
	var model=$("#model").val()
	var uid=$("#uid").val()
	var aid=$("#aid").val()
	var cid=$("#cid").val()
	console.log(purl,model,aid,uid)
	if($.trim(content).length){
		$.ajax({ type	: 'POST', 
			url	: purl, 
			data : {'content':content,'model':model,'aid':aid,'uid':uid,'cid':cid}, 
			enctype : "multipart/form-data",//发送ajax请求必须要请求头 
			success: function(data){ 
				if(data.data){
					parent.layer.closeAll();
					parent.location.href=url;
				}else{
					$("#errormsg")[0].style.color="red";
					$("#errormsg")[0].innerHTML="出错了,请稍后重试";
					setTimeout(function(){
							$("#errormsg")[0].innerHTML="";	
						}, 2000);
				}
			}})
	}else{
		//console.log(text)
	}
}
//引用 写入数据库
function discuss_href(obj){
	var content=$("#demo").val()
	var url=$("#url").val()
	var purl=$("#purl").val()
	var model=$("#model").val()
	var uid=$("#uid").val()
	var aid=$("#aid").val()
	var cid=$("#cid").val()
	console.log(content)
	if($.trim(content).length && $.trim(content).length<=200){
		$.ajax({ type	: 'POST', 
			url	: purl, 
			data : {'content':content,'model':model,'aid':aid,'uid':uid,'cid':cid}, 
			enctype : "multipart/form-data",//发送ajax请求必须要请求头 
			success: function(data){ 
				if(data.data){
					parent.layer.closeAll();
					parent.location.href=url;
					//parent.location.reload="/";
				}else{
					$("#errormsg")[0].style.color="red";
					$("#errormsg")[0].innerHTML="出错了,请稍后重试";
					setTimeout(function(){
							$("#errormsg")[0].innerHTML="";	
						}, 2000);
				}
			}})
	}else{
		//console.log(text)
	}
}