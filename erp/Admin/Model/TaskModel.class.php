<?php
namespace Admin\Model;
use Think\Model;
class TaskModel extends Model{
	protected $fields = array('autoid','goodsid','keywords','goodsprice', 'tasktype','iscomment','startdate', 'tasktotals','everydayquantity','goodspic','isdel','isstat','remark','_pk'=>'autoid'
	);
	/*autoid int primary key auto_increment comment '任务id',
	goodsid int not null comment '关联商品id',
	keywords varchar(40) not null default '' comment '搜索关键词', 
	goodsprice decimal(10,2) not null comment '商品价格', 
	tasktype tinyint not null default 0 comment '任务类型，0为自发货，1FBA', 
	iscomment Tinyint(1) not null default 0 comment '是否留评,0不用，1要留',
	startdate int not null comment '任务起始时间',
	tasktotals int not null comment '任务总量',
	everydayquantity int not null comment '每日发布量', 
	goodspic varchar(100) not null default '' comment '产品图片，图片上传',
	isdel Tinyint(1) not null default 0 comment '0为正常，1为软删除',
	isstat Tinyint(1) default 0 comment '0为未完成，2为已完成', 
	remark text comment '备注'*/

	protected $_map=array(
		'goods'=>'goodsid',
		'keyword'=>'keywords',
		'starttime'=>'startdate',
		'price'=>'goodsprice',
		'totle'=>'tasktotals',
		'everyday'=>'everydayquantity',
		'comment' => 'remark',
	);
/*{"country":"1","user":"3","shop":"5","goods":"5","keyword":"fhjhgkjkhkjh","price":"231.75","tasktype":"0","iscomment":"0","starttime":"2017-03-08","totle":"500","everyday":"20","comment":""}*/
	protected $_validate = array(
		array('goodsid','goodsidnull','商品ID为必填项',1,'callback',1),
		array('keywords','keywordslength','关键词长度不在3-40个字',1,'callback',3),
		array('startdate','contentnull','任务起始时间不能为空',1,'callback',1),
		array('startdate','contenttyle','任务起始时间格式不正确，正确格式为（年-月-日 时:分:秒）',1,'callback',2),
		array('goodsprice','isnumberrange','数字大小范围在1000W以下，小数点后保留2位小数',1,'callback',3),
		array('tasktotals','isnumber','任务总量必须为数字',1,'callback',3),
		array('everydayquantity','isnumber','每日任务量必须为数字',1,'callback',3),
		array('remark','remarkisnull','备注长度必须在3-20字之间',1,'callback',3),
	);
	public function goodsidnull($str){
		if(preg_match('/^\d+$/', $str) && $str != 0) return true;
		else return false;
	}

	public function keywordslength($str){
		$length=mb_strlen(trim($str));
		if($length >= 3 && $length <= 40)return true;
		else return false;
	}

	public function contentnull($str){
		if($str) return true;
		else return false;
	}

	public function contenttyle($str){
		if(preg_match('/^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$/',$str)) return true;
		else return false;
	}

	public function isnumberrange($str){
		if(preg_match('/^\d{1,8}\.\d{2}$/i', $str))return true;
		else return false;
	}

	public function isnumber($str){
		if(preg_match('/^\d+$/i', $str))return true;
		else return false;
	}

	public function remarkisnull($str){
		$length=mb_strlen(trim($str));
		if($length==0)return true;
		elseif($length >= 3 && $length <= 20)return true;
		else return false;
	}

	public function selectdata(){
		$country=M('country')->getField('autoid,countryname');
		/*$data['user']=M('user')->where(array('isdel'=>0))->getField('autoid,realname');
		$data['shop']=M('shop')->where(array('isdel'=>0))->getField('autoid,customerid,countryid,shopname');
		$data['goods']=M('goods')->where(array('isdel'=>0))->getField('autoid,customerid,countryid,shopid,goodsname');*/
		return $country;
	}

	public function admindata($goodsid=0){
		if($goodsid==0)
			$data['task']=get_page_data(M('Task'),array('isdel'=>0),$order='autoid',$limit=4);
		/*M('Task')->where()->getField('autoid,goodsprice,startdate,tasktotals,everydayquantity,goodspic,isstat');*/
		else
			$data['task']=get_page_data(M('Task'),array('isdel'=>0,'goodsid'=>$goodsid),$order='autoid',$limit=4);
		/*M('Task')->where(array('isdel'=>0,'goodsid'=>$goodsid))->getField('autoid,goodsprice,startdate,tasktotals,everydayquantity,goodspic,isstat');*/
		$data['country']=M('country')->getField('autoid,countryname');
		return $data;
		
	}

	public function selectcountrydata($country){
		$data['shop']=M('shop')->where(array('isdel'=>0,'countryid'=>$country))->getField('autoid,customerid,countryid,shopname');
		//return $data['shop'];
		foreach ($data['shop'] as $key => $value) {
			if(!in_array($value['customerid'],$arr)){
				$arr[]=$value['customerid'];
			}
		}
		if($arr){
			$data['user']=M('user')->where(array('isdel'=>0,'autoid'=>array('in',$arr)))->getField('autoid,realname');
			return $data['user'];
		}
		
		else{
			return $data['shop'];
		}
	}

}