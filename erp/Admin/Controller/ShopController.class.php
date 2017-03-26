<?php
namespace Admin\Controller;
use Think\Controller;
class ShopController extends CommontController {
   public function shoplist(){
      $data['tree']=parent::$tree;
      $shop=D('Shop');
      if(IS_POST) $data['data']=$shop->showlist(0,I("post.autoid")); 
      else   $data['data']=$shop->showlist(0,0);     
      $this->assign($data);
      $this->display();
   }

   public function shopseach(){
      if(IS_AJAX){
         $content=I('post.content');
         //echo($content);
         $data=M('shop')->field('shopname,autoid')->where(array('isdel'=>0,'shopname'=>array('like','%'.$content.'%')))->select();
         if(count($data)==0) echo '<span style="color:red;">未查询到记录</span>';
         else{
            $str='';
            foreach ($data as $key => $value) {
               $str.='<a href="#" onclick="javascript:selectshopdata(this,'.$data[$key]["autoid"].');" class="list-group-item" style="background:#1AD6D6;">'.$data[$key]["shopname"].'</a>';
            }
            echo($str);
         }
      }
   }

   public function shopuserlist(){
      $user=I('get.u');
      if(M('user')->where(array('autoid'=>$user,'isdel'=>0))->find()){
      $data['tree']=parent::$tree;
      $data['data']=D('Shop')->showlist($user);
      //dump($data['data']);die;
      $this->assign($data);
      $this->display('shoplist');
   }else{
      $this->redirect('Home/Login/login');
   }
}

   public function shopadd(){
   		$shop = D('Shop');
         if(IS_AJAX){
   			$dat=I('post.');
            if($dat['shopname']==''){
               $data = $shop->selectuserdata($dat['country']);
               echo(json_encode($data));
            }else{
               if(!$data=$shop->create($dat)) echo $shop->getError();
               else{
                  if(M('shop')->add($data)) echo 1;
                     else echo 0;
                  }
            }
   		}else{
   			$data['tree']=parent::$tree;
            $data['data']=$shop->showadd();
            //dump($data['data']);die;
   			$this->assign($data);
   			$this->display();
   		}
   }

   public function shopupdate(){
      if(IS_AJAX){
         $shop = D('Shop');
            if(!$shop->create(I('post.'),2)) echo $shop->getError();
            else{
               
               $data=$shop->create(I('post.'),2);
               //echo(json_encode($data));die;
               if(M('shop')->where(array('autoid'=>array('neq',$data['autoid']),'shopname'=>$data['shopname']))->find()) echo '店铺名重复';
               elseif(M('shop')->where(array('autoid'=>array('neq',$data['autoid']),'shopurl'=>$data['shopurl']))->find()) echo '链接重复';
               else{
                  if(M('shop')->save($data)) echo 1;
                  else echo '数据修改出错';
               };
            }
      }else{
         $shopid=I('get.i');
         //echo $shopid;die;
         if(M('Shop')->where(array('autoid'=>$shopid,'isdel'=>0))->find()){
           $data['tree']=parent::$tree;
            $data['data']=M('shop')->where(array('autoid'=>$shopid,'isdel'=>0))->find();
            //dump($data);die;
            $this->assign($data);
            $this->display();
         }else   $this->redirect('Public/index');
      }  
   		
   }

   function shopdelete(){
   		if(IS_AJAX){
   			$autoid = I('post.id');
            //echo $autoid;die;
            if(M('goods')->where(array('isdel'=>0,'shopid'=>$autoid))->find()) echo '商店下面有商品，无法删除.';
            else{
      			if(M('shop')->where(array('autoid'=>$autoid))->find()){
                  if(M('shop')->where(array('autoid'=>$autoid))->save(array('isdel'=>1))) echo 1;
                  else echo 0;
               }else $this->redirect('Public/index');
      		}
         }
   }

}