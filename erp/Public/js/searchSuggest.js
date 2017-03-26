navList(12);
$(function(){
  $("#keyword").keyup(function (e) {
          var content=this.value.replace(/\s+/g, "");
          //return console.log(content);
          var webaddr="/Admin/Goods/goodsseach";
          var jsondata={'content':content};
          var obj=document.getElementById("dropdownlist");
          if(content.length >= 1)
          ajaxseach(webaddr,jsondata,obj);
          else return false;
     })

  $("#shopkeyword").keyup(function (e) {
    //alert(1);
          var content=this.value.replace(/\s+/g, "");
          //return console.log(content);
          var webaddr="/Admin/Shop/shopseach";
          var jsondata={'content':content};
          var obj=document.getElementById("dropdownlist");
          if(content.length >= 1)
          ajaxseach(webaddr,jsondata,obj);
          else return false;
     })

  $("#userkeyword").keyup(function (e) {
    //alert(1);
          var content=this.value.replace(/\s+/g, "");
          //return console.log(content);
          var webaddr="/Admin/User/userseach";
          var jsondata={'content':content};
          var obj=document.getElementById("dropdownlist");
          if(content.length >= 1)
          ajaxseach(webaddr,jsondata,obj);
          else return false;
     })

  $('#taskgoodskeyword').keyup(function(event) {
    var content = this.value.replace(/\s+/g,'');

    var webaddr="/Admin/Task/searchtask";
    var jsondata={'content':content};
    var obj=document.getElementById('dropdownlist');
    if(content.length >= 1) ajaxseach(webaddr,jsondata,obj);
    else return false;
  });

  $('#oneselfkeyword').keyup(function(event) {
    var content = this.value.replace(/\s+/g,'');
    //return alert(content);
    var webaddr="/Admin/Oneself/searchoneself";
    var jsondata={'content':content};
    var obj=document.getElementById('dropdownlist');
    if(content.length >= 1) ajaxseach(webaddr,jsondata,obj);
    else return false;
  });

  $('#giftkeyword').keyup(function(event) {
    var content = this.value.replace(/\s+/g,'');
    //return alert(content);
    var webaddr="/Admin/Gift/searchgift";
    var jsondata={'content':content};
    var obj=document.getElementById('dropdownlist');
    if(content.length >= 1) ajaxseach(webaddr,jsondata,obj);
    else return false;
  });

})

function ajaxseach(webaddr,jsondata,obj){
  

  $.post(webaddr,jsondata,function(data){
//return console.log(data);
    obj.style.display='block';
    $(obj).empty();
    $(obj).append(data);
  },'text');
}

function selectgiftdata(obj,$id){
  var content = obj.innerHTML;
  $("#giftkeyword").val(content);
  $('#searchgoodsid').val($id);
  document.getElementById('dropdownlist').style.display='none'; 
  //return alert(1);
  $('#seachgiftform').submit();
}

function selectoneselfdata(obj,$id){
  var content = obj.innerHTML;
  $("#oneselfkeyword").val(content);
  $('#searchgoodsid').val($id);
  document.getElementById('dropdownlist').style.display='none';
  $('#seachoneselfform').submit();
}

function selecttaskdata(obj,$id){
  var content = obj.innerHTML;
  $("#taskgoodskeyword").val(content);
  $('#searchgoodsid').val($id);
  document.getElementById('dropdownlist').style.display='none';
  $('#searchtaskform').submit();
}

function selectuserdata(obj,$id){
  var content = obj.innerHTML;
  $("#userkeyword").val(content);
  $('#seachgoodsid').val($id);
  document.getElementById('dropdownlist').style.display='none';
  $('#seachgoodsform').submit();
}

function selectshopdata(obj,$id){
  var content = obj.innerHTML;
  $("#shopkeyword").val(content);
  $('#seachgoodsid').val($id);
  document.getElementById('dropdownlist').style.display='none';
  $('#seachgoodsform').submit();
}

function selectdata(obj,$id){
  var content = obj.innerHTML;
  $("#keyword").val(content);
  $('#seachgoodsid').val($id);
  document.getElementById('dropdownlist').style.display='none';
  $('#seachgoodsform').submit();
}



function handlegift($id){
  $.post("{:U('Gift/giftlist')}",{'autoid':$id},function(data){
    if(data==1) location.href="?";
    else console.log(data);
  },'text');
}
function addgiftcard(){
  var msg =document.getElementById('addcardmsg');
  $.post("{:U('Gift/giftadd')}",$('#giftcardform').serialize(),function(data){
    if(data=='') location.href='/Admin/Gift/giftlist';
    else msg.innerHTML=data;
  },'text');
}

$(function(){
  $('#selectnumber').change(function(event) {
    var num=this.value;
    $.post("{:U('Oneself/batch')}",{'num':num},function(data){
      location.href='/Admin/Oneself/accept';
    },'text');
  });
  /*var number=$('#selectnumber').val();
  return console.log(number);*/
});

function oneselfnumber(id){
  $.post("{:U('Oneself/tasktotle')}",{'autoid':id},function(data){
    if(data==1) location.href='?';
    else if(data==0) location.href='/Home/Login/login';
    else layer.msg(data, {time: 2000,});
  },'text');
}

function addoneselfsubmite(){
  var msg=document.getElementById('oneselfsubmit');
  $.post('{:U("Oneself/submit")}',$('#addoneselfform').serialize(),function(data){
    //console.log(data);
    if(data==1) location.href='/Admin/Oneself/done';
    else msg.innerHTML=data;
  },'text');
  
}

function logoutuser(){
          location.href = "{:U('Public/index')}";
        }

function sadduser(){
          var countryname=$('#srealname').val().replace(/\s/gi,'');
          var msg=document.getElementById('uaddmsg');
          if(countryname.length<=20 && countryname.length>=2){
            $.post('{:U("State/sadd")}',{'countryname':countryname},function(data){
              if(data==1){
                location.href="{:U('State/slist')}";
              }else{
                msg.innerHTML=data;
              }
            },'text');
          }else{
            msg.innerHTML="¹ú¼ÒÃû³Æ³¤¶ÈÔÚ2-20×Ö";
          }
        }

function delcountry(id){
          layer.confirm("ÄúÈ·¶¨ÒªÉ¾³ý´Ë¼ÇÂ¼Ã´?", {
              btn: ['È·¶¨','È¡Ïû'] //°´Å¥
            }, function(){
              $.post("{:U('State/delcountry')}",{'id':id},function(data){
                //console.log(data);return 1;
                if(data==1){
                  layer.closeAll();
                  location.href = "{:U('State/slist')}";
                }else if(data==0){
                  layer.msg('Êý¾ÝÉ¾³ý³ö´í', {
                    time: 2000, //2sºó×Ô¶¯¹Ø±Õ
                  });
                }else{
                  layer.msg('ÄúÃ»ÓÐÈ¨ÏÞ·ÃÎÊ', {
                    time: 2000, //2sºó×Ô¶¯¹Ø±Õ
                  });
                }
                  
              },'text')
            }, function(){
              layer.msg('Çë½÷É÷²Ù×÷', {
                time: 2000, //2sºó×Ô¶¯¹Ø±Õ
              });
            })
        }

function countryupuser(){
  var autoid=$('#countryid').val();
 // alert(autoid);return 1;
  var countryname=$('#srealname').val().replace(/\s/gi,'');
  var msg=document.getElementById('saddmsg');
  if(countryname.length<=20 && countryname.length>=2){
            $.post('{:U("State/countryupdate")}',{'countryname':countryname,'autoid':autoid},function(data){
              if(data==1){
                location.href="{:U('State/slist')}";
              }else{
                msg.innerHTML=data;
                window.setInterval(function(){
                  location.href="{:U('State/slist')}";
                }, 2000)
              }
            },'text');
          }else{
            msg.innerHTML="¹ú¼ÒÃû³Æ³¤¶ÈÔÚ2-20×Ö";
          }
}
function sumuser(){
          var loginpass1 = $("#loginpass1").val().replace(/\s/gi,'');
          var loginpass2 = $("#loginpass2").val().replace(/\s/gi,'');
          var realname = $("#realname").val().replace(/\s/gi,'');
          var telnumber = $("#telnumber").val().replace(/\s/gi,'');
          var commons = $("#commons").val().replace(/\s/gi,'') ? $("#commons").val().replace(/\s/gi,'') : 'ÔÝÎÞ±¸×¢ÐÅÏ¢';
          var usermsg = document.getElementById('usermsg');
          //alert(usermsg.innerHTML);
          if(loginpass1 != loginpass2) {
            usermsg.innerHTML = 'Á½´ÎÊäÈëµÄÃÜÂë²»Ò»ÖÂ';
            return false;
            
          }else if(!(/[a-z,A-Z,_]+/gi.test(loginpass2) && loginpass2.length >= 6 && loginpass2.length  <= 15)){
            usermsg.innerHTML = 'ÃÜÂë±ØÐë°üº¬ÖÁÉÙÒ»Î»Ó¢ÎÄ×ÖÄ¸»òÏÂ»®Ïß';
            return false;
          }else if(!(/^[\u4e00-\u9fa5]+$/gi.test(realname) && realname.length >= 2)){
            usermsg.innerHTML = 'ÕæÊµÐÕÃû±ØÐëÎªÖÐÎÄ£¬ÇÒ²»Ð¡ÓÚÁ½Î»';
            return false;
          }else if(!(/^1{1}[0-9]+$/.test(telnumber) && telnumber.length == 11)){
            usermsg.innerHTML='ÊÖ»úºÅÂë±ØÐëÎª11Î»´¿Êý×Ö';
          }else{
            $.post("{:U('Public/updateuser')}",{'loginpass':loginpass2,'realname':realname,'tel':telnumber,'commons':commons},function(data){
                if(data==1){
                  location.href = "{:U('Home/Login/index')}";
                }else{
                  usermsg.innerHTML=data;
                }
            },'text');
          }
          return false;

        }

        function adduser(){
           var loginname = $('#addloginname').val().replace(/\s/gi,'');
           var realname = $("#addrealname").val().replace(/\s/gi,'');
           var usermsg = document.getElementById('addusermsg');
           //console.log(loginname);return 1;
           if( !(/^[a-z,A-Z,_]+$/gi.test(loginname) && loginname.length>=5 && loginname.length<=9)){
           // alert(1);
            usermsg.innerHTML = 'ÓÃ»§ÃûÖ»ÄÜ°üº¬×ÖÄ¸ºÍÏÂ»®Ïß£¬ÇÒÔÚ5-9Î»Ö®¼ä';
            return false;
          }else if(!(/^[\u4e00-\u9fa5]+$/gi.test(realname) && realname.length >= 2)){
            usermsg.innerHTML = 'ÕæÊµÐÕÃû±ØÐëÎªÖÐÎÄ£¬ÇÒ²»Ð¡ÓÚÁ½Î»';
            return false;
          }else{
            $.post('{:U("Staff/sadd")}',$('#adduserforms').serialize(),function(data){
               console.log(data);
               /* if(data==1){
                  location.href = "{:U('Staff/slist')}";
                }else{
                  usermsg.innerHTML=data;
                }*/
            },'text');
          }
          return false;
        }

        function uadduser(){
          var countryid = $('#countryid').val();
         //return  console.log(countryid);
           var qq = $('#uqq').val().replace(/\s/gi,'');
           var realname = $.trim($("#urealname").val());
           var tel = $("#utel").val().replace(/\s/gi,'');
           var common = $("#ucommon").val().replace(/\s/gi,'') ? $("#ucommon").val().replace(/\s/gi,'') : 'ÔÝÎÞ±¸×¢ÐÅÏ¢';
           var umsg = document.getElementById('uaddmsg');
           //console.log(qq,realname,tel,common);return 1;
           if(countryid==0){
              umsg.style.color='red';
              umsg.innerHTML='ÇëÏÈÑ¡Ôñ¹ú¼Ò';
           }else if(realname.length<=2 || realname.length >= 20){
              umsg.style.color='red';
              umsg.innerHTML='ÐÕÃû³¤¶È±ØÐëÔÚ2-20Î»Ö®¼ä';
           }else if (!(/^\d+$/gi.test(tel) && tel.length == 11)) {
              umsg.style.color='red';
              umsg.innerHTML='µç»°ºÅÂë±ØÐëÌîÐ´´¿Êý×Ö£¬³¤¶ÈÎª11Î»';
           }else if (!(/^\d+$/gi.test(qq) && qq.length >= 5 && qq.length <= 15)) {
              umsg.style.color='red';
              umsg.innerHTML='QQºÅ±ØÐëÌîÐ´´¿Êý×Ö£¬³¤¶ÈÔÚ5-15Î»';
           }else{
              $.post("{:U('User/uadd')}",{'countryid':countryid,'qq':qq,'realname':realname,'tel':tel,'common':common},function(data){
                  if(data==1){
                    location.href = "{:U('User/ulist')}";
                  }else{
                    umsg.style.color='red';
                    umsg.innerHTML=data;
                  }
              },'text');
           }
        }

        

        function uupuser(){
          var countryid=$('#countryid').val();
           var qq = $('#uqq').val().replace(/\s/gi,'');
           var id = $('#uid').val();
           var realname = $.trim($("#urealname").val());
           var tel = $("#utel").val().replace(/\s/gi,'');
           var common = $("#ucommon").val().replace(/\s/gi,'') ? $("#ucommon").val().replace(/\s/gi,'') : 'ÔÝÎÞ±¸×¢ÐÅÏ¢';
           var umsg = document.getElementById('uaddmsg');
           //console.log(qq,realname,tel,common);
           if(countryid == 0){
              umsg.style.color='red';
              umsg.innerHTML='¹ú¼ÒÎª±ØÑ¡Ïî';
           }else if(realname.length<=2 || realname.length >= 20){
              umsg.style.color='red';
              umsg.innerHTML='ÐÕÃû³¤¶È±ØÐëÔÚ2-20Î»Ö®¼ä';
           }else if (!(/^\d+$/gi.test(tel) && tel.length == 11)) {
              umsg.style.color='red';
              umsg.innerHTML='µç»°ºÅÂë±ØÐëÌîÐ´´¿Êý×Ö£¬³¤¶ÈÎª11Î»';
           }else if (!(/^\d+$/gi.test(qq) && qq.length >= 5 && qq.length <= 15)) {
              umsg.style.color='red';
              umsg.innerHTML='QQºÅ±ØÐëÌîÐ´´¿Êý×Ö£¬³¤¶ÈÔÚ5-15Î»';
           }else{
              $.post("{:U('User/uupdate')}",{'qq':qq,'countryid':countryid,'autoid':id,'realname':realname,'tel':tel,'common':common},function(data){
                  if(data==1){
                    location.href = "{:U('User/ulist')}";
                  }else if (data=='Î´ÐÞ¸ÄÈÎºÎÊý¾Ý') {
                    location.href = "{:U('User/ulist')}";
                  }else{
                    umsg.style.color='red';
                    umsg.innerHTML=data;
                  }
              },'text');
           }
        }

        function delus(id){
          layer.confirm("ÄúÈ·¶¨ÒªÉ¾³ý´Ë¼ÇÂ¼Ã´?", {
              btn: ['È·¶¨','È¡Ïû'] //°´Å¥
            }, function(){
              $.post("{:U('User/deluser')}",{'id':id},function(data){
                if(data==1){
                  layer.closeAll();
                  location.href = "{:U('User/ulist')}";
                }else if (data==0) {
                  layer.msg('Êý¾ÝÉ¾³ý³ö´í', {
                time: 2000, //2sºó×Ô¶¯¹Ø±Õ
                 });
                }else{
                  layer.msg('ÄúÃ»ÓÐÈ¨ÏÞ·ÃÎÊ', {
                time: 2000, //2sºó×Ô¶¯¹Ø±Õ
                 });
                }
              },'text')
            }, function(){
              layer.msg('Çë½÷É÷²Ù×÷', {
                time: 2000, //2sºó×Ô¶¯¹Ø±Õ
              });
            })
        }

        

        function delstaff(obj,id,name,ids){
          //console.log(name);
          if(id==ids){
            layer.msg('²»ÄÜÉ¾³ýÄú×Ô¼ºµÄÕËºÅ', {
                time: 2000, //2sºó×Ô¶¯¹Ø±Õ
              });
          }else{
            layer.confirm("ÄúÈ·¶¨ÒªÉ¾³ý"+name+"Ã´?", {
              btn: ['È·¶¨','È¡Ïû'] //°´Å¥
            }, function(){
              $.post("{:U('Staff/delstaff')}",{'id':id},function(data){
                if(data==1){
                  layer.closeAll();
                  location.href = "{:U('Staff/slist')}";
                }else{
                  layer.msg('ÄúÃ»ÓÐÈ¨ÏÞ·ÃÎÊ', {
                time: 2000, //2sºó×Ô¶¯¹Ø±Õ
              });
                }
              },'text')
            }, function(){
              layer.msg('Çë½÷É÷²Ù×÷', {
                time: 2000, //2sºó×Ô¶¯¹Ø±Õ
              });
            })
          }
          
        }
$(function(){
  $('#countryname').change(function(){
     addshopsubmite();
  })
});
function addshopsubmite(){
        var msg=document.getElementById('shopaddmsg');
        var shopname=$("#shopname").val();
        var country=$("#countryname").val();
            if(country==0 && shopname==''){
              msg.innerHTML='ÇëÏÈÑ¡Ôñ¹ú¼Ò¡£';
            }else{
              if(country != 0 && shopname==''){
                 $.post("{:U('Shop/shopadd')}",$('#addshopform').serialize(),function(data){
                    setshopuser(eval(data));
                  },'json');
               }else if(shopname!=''){
                  $.post("{:U('Shop/shopadd')}",$('#addshopform').serialize(),function(d){
                  if(d==1){
                    location.href="{:U('Shop/shoplist')}";
                  }else{
                    msg.innerHTML=d;
                  }
               },'text');
}}}

       function setshopuser(jsonData){
           var jsonLength = 0;
           $("#shopusername").empty();//Çå¿Õ
            for(var item in jsonData){
              if(jsonData[item]){
                $('#shopusername').append("<option value='"+item+"'>"+jsonData[item]+"</option>");
                jsonLength++;

              }else{
                $('#shopusername').append("<option value='"+item+"'>"+ÔÝÎÞÑ¡Ïî+"</option>");
              }
                
                            }
            return jsonLength;      
      }

$(function(){
  $('#goodscountryname').change(function(event) {
    addgoodssubmite();
  });
  /*alert(document.getElementById('twonav').value);*/
}); 
       function addgoodssubmite(){
        var msg=document.getElementById('goodsaddmsg');//ÐÅÏ¢¿ò
        var goodsid=$('#goodsid').val();
        var goodsusername=$('#goodsusername').val();
        if(!goodsid){
          if(goodsusername==0){       
            msg.innerHTML='ÇëÏÈÑ¡Ôñ¿Í»§';
          }else{
              $.post("{:U('Goods/goodsadd')}",$('#addgoodsform').serialize(),function(data){
                //return console.log(data);
                setselectgoods(data);
              },'json');  
            }//endelse
          }else{
          $.post("{:U('Goods/goodsadd')}",$('#addgoodsform').serialize(),function(data){
                //return console.log(data);
                if(data==1){
                  location.href="{:U('Goods/goodslist')}";
                }else if(data==0){
                  msg.innerHTML='Êý¾ÝÌí¼Ó´íÎó';
                }else{
                  msg.innerHTML=data;
                }
              },'text');
}}

      function setselectgoods(jsonData){
           var jsonLength = 0;
           $("#goodsshopname").empty();//Çå¿Õ
           $('#goodsshopname').append("<option value='0'>ÇëÑ¡Ôñ¿Í»§</option>");
            for(var item in jsonData.shop){
              
                $('#goodsshopname').append("<option value='"+item+"'>"+jsonData.shop[item]+"</option>");
                jsonLength++;
            }
            
            return jsonLength;      
      }

       function addtasksubmite(){
        var msg=document.getElementById('taskaddmsg');
        document.getElementById('imgupdate').onsubmit();
        alert(1);
        $.post("{:U('Task/taskadd')}",$('#addtaskform').serialize(),function(data){
          if(data==1){
            location.href="{:U('Goods/goodslist')}";
          }else{
            msg.innerHTML=data;
          }
          //console.log(data);
        },'text');       
       }

       function updategoodssubmite(){
        var msg=document.getElementById('goodsupdatemsg');
        $.post("{:U('Goods/goodsupdate')}",$('#addgoodsform').serialize(),function(data){
          if(data==1){
            location.href="{:U('Goods/goodslist')}";
          }else{
            msg.innerHTML=data;
          }
        },'text');       
       }


       function updateshopsubmite(){
          var msg=document.getElementById('shopaddmsg');
        $.post("{:U('Shop/shopupdate')}",$('#addshopform').serialize(),function(data){
          if(data==1){
            location.href="{:U('Shop/shoplist')}";
          }else{
            msg.innerHTML=data;
          }
          //console.log(data);
        },'text');
       }

       function deltask(autoid){
          layer.confirm("ÄúÈ·¶¨ÒªÉ¾³ý´Ë¼ÇÂ¼Ã´?", {
              btn: ['È·¶¨','È¡Ïû'] //°´Å¥
            }, function(){
              $.post("{:U('Task/taskdelete')}",{'id':autoid},function(data){
                if(data==1){
                  layer.closeAll();
                  location.href = "{:U('Task/tasklist')}";
                }else if (data==0) {
                  layer.msg('Êý¾ÝÉ¾³ý³ö´í', {
                    time: 2000, //2sºó×Ô¶¯¹Ø±Õ
                  });
                }else{
                  layer.msg(data, {
                    time: 2000, //2sºó×Ô¶¯¹Ø±Õ
                  });
                }
                console.log(data);
              },'text')
            }, function(){
              layer.msg('Çë½÷É÷²Ù×÷', {
                time: 2000, //2sºó×Ô¶¯¹Ø±Õ
              });
            })
       }

       function delgoods(shopid){
          layer.confirm("ÄúÈ·¶¨ÒªÉ¾³ý´ËÉÌÆ·Ã´?", {
              btn: ['È·¶¨','È¡Ïû'] //°´Å¥
            }, function(){
              $.post("{:U('Goods/goodsdelete')}",{'id':shopid},function(data){
                if(data==1){
                  layer.closeAll();
                  location.href = "{:U('Goods/goodslist')}";
                }else if (data==0) {
                  layer.msg('Êý¾ÝÉ¾³ý³ö´í', {
                    time: 2000, //2sºó×Ô¶¯¹Ø±Õ
                  });
                }else{
                  layer.msg('ÄúÃ»ÓÐÈ¨ÏÞ·ÃÎÊ', {
                    time: 2000, //2sºó×Ô¶¯¹Ø±Õ
                  });
                }
                //console.log(data);
              },'text')
            }, function(){
              layer.msg('Çë½÷É÷²Ù×÷', {
                time: 2000, //2sºó×Ô¶¯¹Ø±Õ
              });
            })
       }

       function delshop(shopid){
          layer.confirm("ÄúÈ·¶¨ÒªÉ¾³ý´ËµêÆÌÃ´?", {
              btn: ['È·¶¨','È¡Ïû'] //°´Å¥
            }, function(){
              $.post("{:U('Shop/shopdelete')}",{'id':shopid},function(data){
                if(data==1){
                  layer.closeAll();
                  location.href = "{:U('Shop/shoplist')}";
                }else if(data==0){
                  layer.msg('Êý¾ÝÉ¾³ý³ö´í', {
                    time: 2000, //2sºó×Ô¶¯¹Ø±Õ
                  });
                }else{
                  layer.msg("ÄúÃ»ÓÐÈ¨ÏÞ·ÃÎÊ", {
                    time: 2000, //2sºó×Ô¶¯¹Ø±Õ
                  });
                }
                //console.log(data);
              },'text')
            }, function(){
              layer.msg('Çë½÷É÷²Ù×÷', {
                time: 2000, //2sºó×Ô¶¯¹Ø±Õ
              });
            })
       }

       function addtasksubmite(){
          var msg=document.getElementById('taskaddmsg');
          $.post("{:U('Task/taskadd')}",$('#addtaskform').serialize(),function(data){
            //console.log(data);
            if(!isNaN(data)){
              msg.innerHTML='Êý¾ÝÌí¼ÓÍê³É£¬Çëµã»÷ÉÏ´«Í¼Æ¬°´Å¥ÉÏ´«Ò»ÕÅÍ¼Æ¬';//location.href="{:U('Task/tasklist')}";
              $('#uploadimg').click(function(event) {
                uploadimg(data);
              });
            }else  msg.innerHTML=data;
          },'text');
       }

       function uploadimg(data){
        //alert(data);
        layer.open({
          type: 2,
          skin: 'layui-layer-lan', //ÑùÊ½ÀàÃû
          title: 'Í¼Æ¬ÉÏ´«',
          closeBtn: 1, //²»ÏÔÊ¾¹Ø±Õ°´Å¥
          anim: 5,
          area:['300px','280px'],
          shadeClose: true, //¿ªÆôÕÚÕÖ¹Ø±Õ
          content: '/Admin/Task/taskimg?i='+data
        });
          
       }


       function getJsonLength(jsonData){
           var jsonLength = 0;
           $("#taskuser").empty();//Çå¿Õ
            for(var item in jsonData){
                $('#taskuser').append("<option value='"+item+"'>"+jsonData[item]+"</option>");jsonData[item];
                jsonLength++;
            }
            return jsonLength;      
      }

      function taskjson(){
         $.post("{:U('Task/taskadd')}",$('#addtaskform').serialize(),function(data){
           getJsonLength(eval(data));//eval()º¯ÊýÊÇ½«json×Ö·û´®×ª»»³Éjs¶ÔÏó
          },'json')
      }

//1.taskcountry °ó¶¨onchangeÊÂ¼þ ajaxÇëÇóÏÂÒ»²ãÊý¾Ý ²ãÊýÊÇÒ» 
$(function(){
  //Ò»¼¶
  $("#taskcountry").change(function(){
      if(this.value>0) ajaxquery(this.value,'¿Í»§','#taskuser');
      //·µ»ØÖµ$("#taskuser")
  });
  //¶þ¼¶
  $('#taskuser').change(function(){
    if(this.value>0) ajaxquery(this.value,'ÉÌµê','#taskshop');
  });
  //Èý¼¶
  $("#taskshop").change(function(){
    //alert(this.value);
    if(this.value>0) ajaxquery(this.value,'ÉÌÆ·','#taskgoods');
  });
});
function ajaxquery(val,level,obj){
  $.post("{:U('Task/taskadd')}",{'val':val,'level':level},function(data){
    if(data){
      //return console.log(data);
      $(obj).empty();
      $(obj).append(data);
    }
  },'json');
}


$(function(){
  //Ò»¼¶
  $("#taskcountrys").change(function(){
      if(this.value>0) ajaxquery(this.value,'¿Í»§','#taskusers');
      //·µ»ØÖµ$("#taskuser")
  });
  //¶þ¼¶
  $('#taskusers').change(function(){
    if(this.value>0) ajaxquery(this.value,'ÉÌµê','#taskshops');
  });
  //Èý¼¶
  $("#taskshops").change(function(){
    //alert(this.value);
    if(this.value>0) ajaxquery(this.value,'ÉÌÆ·','#taskgoodss');
  });
  $("#taskgoodss").change(function(){
      location.href='/Admin/Task/taskquerylist?i='+this.value;
    
  });
});

function updatetasksubmite(){
  var msg=document.getElementById('taskupdatemsg');
  $.post('{:U("Task/taskupdate")}',$('#updatetaskform').serialize(),function(data){
    //console.log(data);
    if(data==1) location.href="/Admin/Task/tasklist";
    else if(data==0) msg.innerHTML='Êý¾ÝÐÞ¸ÄÒì³£';
    else msg.innerHTML=data;
  },'text')
}