<?php
namespace Admin\Controller;
use Think\Controller;
class StateController extends CommontController {
   public function slist(){
   		$data['tree']=parent::$tree;
   		$data['data']=M('country')->getField('autoid,countryname');
   	//dump($data);die;
        $this->assign($data);
        $this->display();
   }

   public function sadd(){
   		if(IS_AJAX){
   			$data['countryname']=I('post.countryname');
            //echo $data['countryname'];die;
   			if(M('country')->where(array('countryname'=>$data['countryname']))->find()) echo '记录重复';
   			else{
   				if(M('country')->add($data)) echo 1;
   				else echo '数据添加出错';
   			}
   		}else{
   			$data['tree']=parent::$tree;
   			$this->assign($data);
   			$this->display();
   		}
   }

   public function countryupdate(){
      if(IS_AJAX){
         $autoid=I('post.autoid');
         $countryname=I('post.countryname');
         //echo $autoid;die;
         if(M('country')->where(array('autoid'=>$autoid))->save(array('countryname'=>$countryname))) echo 1;
         else echo '数据修改错误,2秒后自动跳转';

      }else{
         $autoid = I("get.i");
         $data['tree']=parent::$tree;
         //dump($data);die;
         if($data['data']=M('country')->where(array('autoid'=>$autoid))->find()){
            $this->assign($data);
            $this->display();
         }
      }
      //echo $autoid;
   		
   }

   function delcountry(){
   		if(IS_AJAX){
   			$autoid = I('post.id');
            //echo $autoid;die;
            if(M('user')->where(array('countryid'=>$autoid,'isdel'=>0))->find()) echo "国家下面有关联客户名，不允许删除";
            else{
               if(M('country')->where(array('autoid'=>$autoid))->delete()) echo 1;
               else echo 0;
            }
   		}
   }

}