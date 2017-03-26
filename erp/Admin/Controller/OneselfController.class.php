<?php
namespace Admin\Controller;
use Think\Controller;
class OneselfController extends CommontController{
//任务表
	public function batch(){
		if(IS_AJAX){
			$number=I('post.num');
			//$_SESSION[md5('admin')]['task']=array();
			if(count($_SESSION[md5('admin')]['task'])>=1)die("检测到还有未完成任务，请先完成后在重新接收");
			else{
					$shops=M($_SESSION[md5('admin')]['loginname'])->field('manager')->select();
					$managers='';
					foreach ($shops as $k => $v) {
							$managers.=$v['manager'].',';
						}//关联任务表id查询出shopid
					$manager_shopids=M('manager')->where(array('autoid'=>array('in',$managers)))->field('shopid')->select();
					$manager_shopid='';
					foreach ($manager_shopids as $km => $vm) {
							$manager_shopid.=$vm['shopid'].',';
						}
					$data=M('manager')->where(array('shopid'=>array('not in',$manager_shopid),'status'=>array('neq',3)))->group('shopid')->getField('shopid,autoid');
					//p(M('manager')->getLastSql());
					if(count($data) > $number){
						$arr=array_rand($data,$number);
						for ($i=0; $i < $number; $i++) $session[$arr[$i]]=$data[$arr[$i]];
					}else $session=$data;
					$_SESSION[md5('admin')]['task']=$session;
					$manager_ids=implode(',',array_values($_SESSION[md5('admin')]['task']));

					$data=M('manager')->where(array('autoid'=>array('in',$manager_ids),'status'=>1))->getField('autoid,userid');
					for($i=0;$i<count($data);$i++){
						$str=$data[$i].$_SESSION[md5('admin')]['autoid'].',';
						M('manager')->where(array('autoid'=>$i,'status'=>1))->save(array('userid'=>$str));
					}
					echo 1;


			//die($manager_shopid);
			}
		}
	}

	public function searchoneself(){
		if(IS_AJAX){
			$shopname=I('post.content');
			$data=M('shop')->field("autoid,shopname")->where(array('isdel'=>0,'shopname'=>array('like','%'.$shopname.'%')))->select();
			if(count($data)>=1){
				$str='';
				foreach ($data as $key => $value) {
					$str.='<a href="#" onclick="javascript:selectoneselfdata(this,'.$data[$key]["autoid"].');" class="list-group-item" style="background:#1AD6D6;">'.$data[$key]["shopname"].'</a>';
				}
			}else $str='<span style="color:red;">未查询到记录</span>';
			echo $str;
		}
	}

	public function tasktotle(){
		$oneself=D('Oneself');
		$oneself->refreshdata();
		if($_SESSION[md5('admin')]['loginname']!='admin')
		$shops=M($_SESSION[md5('admin')]['loginname'])->field('manager')->select();
		$managers='';
		foreach ($shops as $k => $v) {
			$managers.=$v['manager'].',';
		}//关联任务表id查询出shopid
		$manager_shopids=M('manager')->where(array('autoid'=>array('in',$managers)))->field('shopid')->select();
		$manager_shopid='';
		foreach ($manager_shopids as $km => $vm) {
			$manager_shopid.=$vm['shopid'].',';
		}
		//{"autoid":"3","loginname":"hellos","realname":"\u521b\u5efa\u6570\u636e","loginpassword":"af8f9dffa5d420fbc249141645b962ee","tel":"","remark":"","isdel":"0"}
		if(IS_AJAX){
			$autoid=I('post.autoid');
			$shopid=M('manager')->where(array('autoid'=>$autoid,'status'=>array('neq',3)))->getField('shopid');
			if(!strpos($manager_shopid,$shopid)){
				if(count($_SESSION[md5('admin')]['task']) >= 1)
					die('系统检测到有未完成任务，请提交任务后在重新接收');
				else $_SESSION[md5('admin')]['task'][$shopid]=$autoid;
				if($oneself->writeacc($autoid,$_SESSION[md5('admin')]['autoid'])) echo 1;
				else echo 0;
			}else die('每个商店只能接收一个商品，请勿重复接收任务');

		}else{
			//die;
		$data['tree']=parent::$tree;
		if(I('post.oneselfautoid') >= 1){
			if(count($_SESSION[md5('admin')]['task']) >= 1){
				$onetask=$_SESSION[md5('admin')]['task'];	
				$shopkey=implode(',',array_keys($onetask)).','.$manager_shopid;
				$data['data']=$oneself->tasktotle($shopkey,'','',I('post.oneselfautoid'));
			}
			else{
				$data['data']=$oneself->tasktotle($manager_shopid,'','',I('post.oneselfautoid'));
				//p($data['data']);die;
			}
		}else{
			if(count($_SESSION[md5('admin')]['task']) >= 1){
				$onetask=$_SESSION[md5('admin')]['task'];	
				$shopkey=implode(',',array_keys($onetask)).','.$manager_shopid;
				$data['data']=$oneself->tasktotle($shopkey);

			}
			else $data['data']=$oneself->tasktotle($manager_shopid);
		}

		
		$this->assign($data);
		$this->display();
	}

}


	public function accept(){
		$oneself=D('Oneself');
		$data['tree']=parent::$tree;
		$managerids=implode(',',array_values($_SESSION[md5('admin')]['task']));//managerids
		if($managerids) $data['data']=$oneself->tasktotle('',$managerids);
/*		D:\wamp\www\thinkphp3\ThinkPHP\Common\functions.php:842:
array (size=2)
  'page' => string '<div>    </div>' (length=15)
  'list' => 
    array (size=1)
      0 => 
        array (size=13)
          'autoid' => string '2' (length=1)
          'userid' => string '2,' (length=2)
          'taskid' => string '38' (length=2)
          'nottotle' => string '123' (length=3)
          'day' => string '1' (length=1)
          'onetime' => string '2017-03-15 00:03' (length=16)
          'istask' => null
          'shopid' => string '7' (length=1)
          'status' => string '发布中' (length=9)
          'img' => string '/Uploads/2017-03-09/58c0f14bb9def.png' (length=37)
          'shopname' => string 'lucy的店铺' (length=13)
          'acceptance' => string '0.008%' (length=6)
          'done' => string '0%' (length=2)*/
		$this->assign($data);
		$this->display();
	}

	public function submit(){
		if(IS_AJAX){
			$data=I('post.');
			/*'orderid' => string '' (length=0)
			  'manager' => string '2' (length=1)
			  'buyerid' => string '' (length=0)
			  'orderprice' => string '' (length=0)*/
			 // p($data);
			if(!$data['manager']) echo '数据丢失，提交失败';
			else{
				if(strlen($data['orderid']) <=5 || strlen($data['orderid']) >=50) echo '订单号长度必须在5-50位之间';
				elseif(!preg_match('/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/', $data['buyerid'])) echo '邮箱号填写错误';
				elseif(!preg_match('/^\d{1,8}\.\d{2}$/i',$data['orderprice'])) echo '价格填写错误';
				else{
					//入库
					$data['createtime']=time();
					//添加到当前用户表，返回id值
					if($adminid=M($_SESSION[md5('admin')]['loginname'])->add($data)){
						//查询原始值
						$managerdata=M('manager')->where(array('autoid'=>$data['manager'],'status'=>array('neq',3)))->field('istask,nottotle')->select();
						/*Array
(
    [0] => Array
        (
            [istask] => lilianjie_5,
            [nottotle] => 10
        )*/				//修改任务表数据
        				if($managerdata[0]['nottotle'] >= 1){
        					$managerdata[0]['istask'].=$_SESSION[md5('admin')]['loginname'].'_'.$adminid.',';
        					$managerdata[0]['nottotle']-=1;
        					if($managerdata[0]['nottotle']==0) $managerdata[0]['status']=3;
        					M('manager')->where(array('autoid'=>$manager))->save($managerdata[0]);
        				}else{
        					M('manager')->where(array('autoid'=>$manager))->save(array('status'=>3));
        				}
        				//重设session
        				$manager_ids=$_SESSION[md5('admin')]['task'];
					foreach ($manager_ids as $key => $value) {
						if($key==$data['manager']) unset($manager_ids[$key]);
						
						$_SESSION[md5('admin')]['task']=$manager_ids;
						//p($manager_ids);
					}
					echo(1);
					
			}else echo('数据添加到员工表出错');
		}}}else{
			$manager_id=I('get.i');
			$oneself=D('Oneself');
			if(strpos(implode(',', array_values($_SESSION[md5('admin')]['task'])),$manager_id)===false) die("记录不存在");
			else $data['data']=$oneself->tasktotle('','',$manager_id);
			//else 
/*D:\wamp\www\thinkphp3\ThinkPHP\Common\functions.php:842:
array (size=2)
  'page' => string '<div>    </div>' (length=15)
  'list' => 
    array (size=1)
      0 => 
        array (size=13)
          'autoid' => string '2' (length=1)
          'userid' => string '2,' (length=2)
          'taskid' => string '38' (length=2)
          'nottotle' => string '123' (length=3)
          'day' => string '1' (length=1)
          'onetime' => string '2017-03-15 00:03' (length=16)
          'istask' => null
          'shopid' => string '7' (length=1)
          'status' => string '发布中' (length=9)
          'img' => string '/Uploads/2017-03-09/58c0f14bb9def.png' (length=37)
          'shopname' => string 'lucy的店铺' (length=13)
          'acceptance' => string '0.008%' (length=6)
          'done' => string '0%' (length=2)
			dump($data['data']);die;*/
			//dump($data);die;
			$data['manager_id']=$manager_id;
			$data['tree']=parent::$tree;
			$this->assign($data);
			$this->display();
		}
		
	}

	public function done(){
		$oneself=D('Oneself');
		$data['tree']=parent::$tree;
		//dump($data);die;
		$dats=M($_SESSION[md5('admin')]['loginname'])->select();
		$str='';
		foreach ($dats as $key => $value) {
			$str.=$value['manager'].',';
		}
		if($str)
		$data['data']=$oneself->tasktotle('',$str);
		//dump($str);die;
		$this->assign($data);
		$this->display();
	}

}