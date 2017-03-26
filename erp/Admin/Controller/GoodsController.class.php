<?php
namespace Admin\Controller;
use Think\Controller;
class GoodsController extends CommontController {
   public function goodslist(){
      $data['tree']=parent::$tree;
      $goods=D('Goods');
      if(IS_POST){
         $autoid=I('post.autoid');
         $data['data']=$goods->listdata(0,$autoid);
      }else{
         $data['data']=$goods->listdata(0);
       //dump($data['data']);die;
      }
      $this->assign($data);
         $this->display();
     
   }

   public function goodsshoplist(){
      $shops=I('get.u');
      if(M('shop')->where(array('autoid'=>$shops,'isdel'=>0))->find()){
         $data['tree']=parent::$tree;
      $goods=D('Goods');
      $data['data']=$goods->listdata($shops);
      //dump($data);die;
      $this->assign($data);
      $this->display('goodslist');
   }else $this->redirect('Public/index');
      
   }

   public function goodsadd(){
       $goods=D('Goods');
      if(IS_AJAX){
         $forms=I('post.');
         //echo(json_encode($forms));die;
         if ($forms['user'] && !$forms['goodsid'])
            echo(json_encode($data['data']=$goods->selectnav($forms['user'])));
         else{
            //正常请求
             if(!($data=$goods->create())) echo $goods->getError();
             else{
            //判断同一家店铺下商品名是否已存在
            if(M('goods')->where(array('goodsname'=>$data['goodsname'],'shopid'=>$data['shopid']))->find()) echo '商品名重复';
            else{
               //添加纪录
               if(M('goods')->add($data)) echo 1;
               else echo 0;
            }
         }
      }
   }else{
         $data['tree']=parent::$tree;
         $data['data']=$goods->goodsforeign();
         //dump($data);die;
         $this->assign($data);
         $this->display();
      }     
   }

   public function goodsupdate(){
      if(IS_AJAX){
         $goods=D('Goods');
         if(!($data=$goods->create(I('post.'),2))) echo $goods->getError();
         else{
            //商品id重复
            if(M('goods')->where(array('autoid'=>array('neq',$data['autoid']),'goodsasin'=>$data['goodsasin']))->find()) echo '商品id重复'; 
            //商品名重复
            elseif(M('goods')->where(array('autoid'=>array('neq',$data['autoid']),'goodsname'=>$data['goodsname'],'shopid'=>$data['shopid']))->find()) echo '商品名重复';
            //商品url重复
            elseif(M('goods')->where(array('autoid'=>array('neq',$data['autoid']),'goodsurl'=>$data['goodsurl']))->find()) echo '商品url重复';
            else{
               if(M('goods')->save($data)) echo 1;
               else echo '参数修改出错';
            }
         }
      }else{
         $autoid=I('get.i');
         if(M('goods')->where(array('autoid'=>$autoid,'isdel'=>0))->find()){
            //echo $autoid;die;
           $data['tree']=parent::$tree;
            $data['goodsid']=$autoid;
            $data['data']=D('Goods')->updatedata($autoid);
            //dump($data['data']);die;
            $this->assign($data);
            $this->display();
         }else $this->redirect('Public/index');
      }
      
   }

   public function goodsseach(){
      if(IS_AJAX){
         $content=I('post.content');
         //echo($content);
         $data=M('goods')->field('goodsname,autoid')->where(array('isdel'=>0,'goodsname'=>array('like','%'.$content.'%')))->select();
         if(count($data)==0) echo '<span style="color:red;">未查询到记录</span>';
         else{
            $str='';
            foreach ($data as $key => $value) {
               $str.='<a href="#" onclick="javascript:selectdata(this,'.$data[$key]["autoid"].');" class="list-group-item" style="background:#1AD6D6;">'.$data[$key]["goodsname"].'</a>';
            }
            echo($str);
         }
         
      }
   }

   function goodsdelete(){
      if(IS_AJAX){
         $autoid=I('post.id');
         if(M('goods')->where(array('autoid'=>$autoid))->find()){
            if(M('task')->where(array('goodsid'=>$autoid,'isdel'=>0))->find()) echo '该商品下有任务记录';
            else{
               if(M('goods')->where(array('autoid'=>$autoid))->save(array('isdel'=>1))) echo 1;
               else echo 0;
            }
            
         }else{
            $this->redirect('Public/index');
         }
      }
   }

}