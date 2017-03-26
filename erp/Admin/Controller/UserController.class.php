<?php
namespace Admin\Controller;
use Think\Controller;
class UserController extends CommontController {
   public function ulist(){
   		$data['tree']=parent::$tree;
   		//$user=M('user')->where(array('isdel'=>0))->getField('autoid,countryid,realname,qq,tel');
         $User = M('user'); 
         if(IS_POST)  $data['page']=get_page_data($User,array('isdel'=>0,'autoid'=>I('post.autoid')),$order='autoid',$limit=10);
         else $data['page']=get_page_data($User,array('isdel'=>0),$order='autoid',$limit=10);
         // 实例化User对象
         $country = M('country')->getField('autoid,countryname');
         foreach ($data['page']['list'] as $key => $value) {
            foreach ($country as $kc => $vc) {
               if($value['countryid'] == $kc) $data['page']['list'][$key]['countryid']=$vc;
            }
         }
         //dump($data['page']['page']);die;
        $this->assign($data);
        $this->display();
   }

   public function userseach(){
      if(IS_AJAX){
         $content=I('post.content');
         //echo($content);
         $data=M('user')->field('realname,autoid')->where(array('isdel'=>0,'realname'=>array('like','%'.$content.'%')))->select();
         if(count($data)==0) echo '<span style="color:red;">未查询到记录</span>';
         else{
            $str='';
            foreach ($data as $key => $value) {
               $str.='<a href="#" onclick="javascript:selectuserdata(this,'.$data[$key]["autoid"].');" class="list-group-item" style="background:#1AD6D6;">'.$data[$key]["realname"].'</a>';
            }
            echo($str);
         }
         
      }
   }

   public function uadd(){
   		if(IS_AJAX){
   			$data['realname']=I('post.realname');
   			$data['qq']=I('post.qq');
   			$data['tel']=I('post.tel');
   			$data['remark']=I('post.common');
            $data['countryid']=I('post.countryid');
            //echo 'hello';die;
   			if(M('user')->where(array('realname'=>$data['realname']))->find()) echo '姓名重复';
   			elseif(M('user')->where(array('qq'=>$data['qq']))->find()) echo 'qq号码重复';
   			elseif(M('user')->where(array('tel'=>$data['tel']))->find()) echo '电话号码重复';
   			else{
   				if(M('user')->add($data)) echo 1;
   				else echo '数据添加出错';
   			}
   		}else{
   			$data['tree']=parent::$tree;
            $data['country']=M('country')->getField('autoid,countryname');
   			$this->assign($data);
   			$this->display();
   		}
   }

   public function uupdate(){
   		if(IS_AJAX){
   			$data['realname']=I('post.realname');
            $data['countryid']=I('post.countryid');
   			$data['qq']=I('post.qq');
   			$data['autoid']=I('post.autoid');
   			$data['tel']=I('post.tel');
   			$data['remark']=I('post.common');
   			/*$a=M('user')->where(array('realname'=>$data['realname'],'autoid'=>array('neq',$data['autoid'])))->find();
   			dump(M('user')->getLastSql());die();*/
   			if(M('user')->where(array('realname'=>$data['realname'],'autoid'=>array('neq',$data['autoid'])))->find()) echo '姓名重复';
   			elseif(M('user')->where(array('qq'=>$data['qq'],'autoid'=>array('neq',$data['autoid'])))->find()) echo 'qq号码重复';
   			elseif(M('user')->where(array('tel'=>$data['tel'],'autoid'=>array('neq',$data['autoid'])))->find()) echo '电话号码重复';
   			else{
   				if(M('user')->where(array('autoid'=>$data['autoid']))->save($data)) echo 1;
   				else echo '未修改任何数据';
   			}
   		}else{
   			$autoid=I('get.i');
   			$data['tree']=parent::$tree;
   			if($data['data']=M('user')->where(array('autoid'=>$autoid))->find()){
               $data['country'] = M('country')->getField('autoid,countryname');
   				$this->assign($data);
   				$this->display();
   			}else $this->redirect('Public/index');
   		}

   		
   }

   function deluser(){
   		if(IS_AJAX){
   			$autoid = I('post.id');
   			$data['isdel'] = 1;
            if(M('shop')->where(array('isdel'=>0,'customerid'=>$autoid))->find()){
               echo '该用户名下有商店，不能删除';
            }else{
               if(M('user')->where(array('autoid'=>$autoid))->save($data)) echo 1;
               else echo 0;
            }	
   		}
   }

}