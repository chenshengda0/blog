<?php
namespace Admin\Controller;
use Think\Controller;
class GiftController extends CommontController {
    public function giftlist(){
        $data['tree']=parent::$tree;
       // dump($data);die;
        if(IS_AJAX){
            $autoid=I('post.autoid');

            if(M('gift')->where(array('autoid'=>$autoid))->save(array('userid'=>$_SESSION[md5('admin')]['autoid'],'status'=>1,'pubdate'=>time()))) echo 1;
            else echo 0;
        }else{

            if(I('post.autoid') >= 1)  $gift=get_page_data(M('gift'),array('userid'=>I('post.autoid')),$order='status',$limit=10);
            else $gift=get_page_data(M('gift'),'',$order='status',$limit=10);
            /*M('gift')->order('status')->select();*/
        for ($i=0; $i < count($gift['list']); $i++) { 
            if($gift['list'][$i]['userid']!=0) $gift['list'][$i]['username']=M('admin')->where(array('autoid'=>$gift['list'][$i]['userid']))->getField('realname');
            else $gift['list'][$i]['username']='可领取';
            //echo($gift[$i]['username']);die;//$gift[$i]['userid']
            if($gift['list'][$i]['status']==0){
                $gift['list'][$i]['status']='未领取';
                $gift['list'][$i]['handle']=1;
            }
            else{
                $gift['list'][$i]['status']='已领取';
                $gift['list'][$i]['handle']=0;
            }
        }
        $data['data']=$gift;
        //dump($data);die;
        $this->assign($data);
        $this->display();
        }
        
    }

    public function searchgift(){
        if(IS_AJAX){
            $realname=I('post.content');
            //p($realname);
            $data=M('admin')->field('autoid,realName')->where(array('realName'=>array('like','%'.$realname.'%')))->select();
            //P(json_encode($data));
            if(count($data)>=1){
                $str='';
                foreach ($data as $key => $value) {
                    $str.='<a href="#" onclick="javascript:selectgiftdata(this,'.$data[$key]["autoid"].');" class="list-group-item" style="background:#1AD6D6;">'.$data[$key]["realname"].'</a>';
                }
            }else $str='<span style="color:red;">未查询到记录</span>';
            echo $str;
        }
    }


    public function giftadd(){
        $data['tree']=parent::$tree;
        if(IS_AJAX){
            $price=I('post.cardprice');
            $cardnumber=I('post.cardnumber');
            if(!$price && !$cardnumber) echo '价格和卡号都不能留空';
            elseif(preg_match('#^\d{1,8}\.\d{2}$#i',$price)){
            $cardnumber=preg_match_all('#.+(?=\r)#i', $cardnumber,$arr);//('#\s+#',',', $cardnumber);
            for($i=0;$i<count($arr[0]);$i++){
                if(strlen($arr[0][$i])<=10 || strlen($arr[0][$i]) >= 50){
                    echo('第'.($i+1).'行记录长度不符合规范');die;
                }
                else{
                     if(M('gift')->where(array('giftcard'=>$arr[0][$i]))->find()){
                        echo($i++.'记录重复');die;
                     }
                    else {
                        $dat=array('giftprice'=>$price,'giftcard'=>$arr[0][$i]);
                        M('gift')->add($dat);
                    }
                }
               
            }
        }else echo '价格格式错误';
            
        }else{
            $this->assign($data);
            $this->display();
        }
        
    }

    public function giftcard(){
       $data['tree']=parent::$tree;
        $data['data']=get_page_data(M('gift'),array('userid'=>$_SESSION[md5('admin')]['autoid']),$order='pubdate',$limit=10);
        $this->assign($data);
        $this->display();
    }

}