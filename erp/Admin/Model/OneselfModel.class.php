<?php
namespace Admin\Model;
use Think\Model;
class OneselfModel extends Model{
	protected $trueTableName = 'rep_manager';
	//自动刷新任务
	public function refreshdata(){
		$time=time();
		$data=M('task')->where(array('startdate'=>array('elt',$time),'isdel'=>0,'isstat'=>0))->getField('autoid,goodsid,startdate,tasktotals,everydayquantity,goodspic');
		foreach ($data as $key => $value) {
			$days=intval(ceil($value['tasktotals']/$value['everydayquantity']));
			if($value['tasktotals']%$value['everydayquantity']==0) $ends=$value['everydayquantity'];
			else $ends=$value['tasktotals']%$value['everydayquantity'];
			if($manager=M('manager')->where(array('taskid'=>$key,'status'=>array('neq',3)))->getField('autoid,day,onetime,status')){
				foreach ($manager as $km => $vm) {
					if(($vm['onetime']+($vm['day'])*3600*24) <= $time){
						if($vm['day'] == ($days-1)){
							$man['status']=2;
							$man['nottotle']=$vm['nottotle']+$ends;
							$man['day']=$vm['day']+1;
						}else{
							$man['nottotle']=$vm['nottotle'] + $value['everydayquantity'];
							$man['day']=$vm['day']+1;
						}
						if(M('manager')->where(array('autoid'=>$km,'status'=>array('neq',2)))->save($man));
					} //更新数据	
				}
			}
				//检查时间
			else{
				$goods=M('goods')->where(array('isdel'=>0,'autoid'=>$value['goodsid']))->getField('shopid');
				//创建数组
				$dat['taskid']=$key;
				if($days==1){
					$dat['nottotle']=$ends;
					$dat['status']=2;
				}else{
					$dat['nottotle']=$value['everydayquantity'];
					$dat['status']=1;
				}
				$dat['day']=1;
				$dat['onetime']=$time;
				$dat['shopid']=$goods;
				M('manager')->add($dat);
			}
		}
	}

	public function tasktotle($shopkey='',$managerids='',$managerid='',$oneselfautoid=''){
		if($managerid) $manager=get_page_data(M('manager'),array('status'=>array('neq',3),'autoid'=>$managerid),$order='autoid',$limit=3);
			/*$manager=M('manager')->where()->getField('autoid,userid,istask,taskid,nottotle,onetime,shopid,status');*/
		elseif($managerids) $manager=get_page_data(M('manager'),array('status'=>array('neq',3),'autoid'=>array('in',$managerids)),$order='autoid',$limit=3);
			/*M('manager')->where(array('status'=>array('neq',3),'autoid'=>array('in',$autoids)))->getField('autoid,userid,istask,taskid,nottotle,onetime,shopid,status');*/
		elseif($shopkey)
			if($oneselfautoid) $manager=get_page_data(M('manager'),array('status'=>array('neq',3),'shopid'=>array('not in',$shopkey),'shopid'=>$oneselfautoid),$order='autoid',$limit=3);
			else
			$manager=get_page_data(M('manager'),array('status'=>array('neq',3),'shopid'=>array('not in',$shopkey)),$order='autoid',$limit=3);
/*			$manager=M('manager')->where()->getField('autoid,userid,istask,taskid,nottotle,onetime,shopid,status');*/
		else 
			if($oneselfautoid) $manager=get_page_data(M('manager'),array('status'=>array('neq',3),'shopid'=>$oneselfautoid),$order='autoid',$limit=3);
			else
				$manager=get_page_data(M('manager'),array('status'=>array('neq',3)),$order='autoid',$limit=3);
			/*M('manager')->where(array('status'=>array('neq',3)))->getField('autoid,userid,istask,taskid,nottotle,onetime,shopid,status');*/
		foreach ($manager['list'] as $key => $value) {
			$manager['list'][$key]['img']=M('task')->where(array('isdel'=>0,'autoid'=>$value['taskid']))->getField('goodspic'); 
			$manager['list'][$key]['shopname']=M('shop')->where(array('isdel'=>0,'autoid'=>$value['shopid']))->getField('shopname');
			$atimes=preg_match_all('/\d+/i',$manager['list'][$key]['userid']);
			$dtimes=preg_match_all('/\d+/i',$manager['list'][$key]['istask']);
			$manager['list'][$key]['onetime']=date('Y-m-d H:i',$manager['list'][$key]['onetime']);
			$manager['list'][$key]['acceptance']= round($atimes/$manager['list'][$key]['nottotle'],3).'%';
			$manager['list'][$key]['done']= round($dtimes/$manager['list'][$key]['nottotle']*100,3).'%';
			if($value['status']==1) $manager['list'][$key]['status']='发布中';
			if($value['status']==2) $manager['list'][$key]['status']='发布完成';
			if($value['status']==3) $manager['list'][$key]['status']='已完成';
		}
		return $manager;
	}


	public function writeacc($taskid,$adminid){
		$userid = M('manager')->where(array('status'=>array('neq',3),'autoid'=>$taskid))->getField('userid');
		$userid .= $adminid.',';
		if(M('manager')->where(array('status'=>array('neq',3),'autoid'=>$taskid))->save(array('userid'=>$userid))) return 1;
		else return 0;
	}
}