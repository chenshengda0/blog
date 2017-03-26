<?php
namespace Admin\Model;
use Think\Model;
class ShopModel extends Model {
	protected $fields = array('autoid', 'customerid', 'countryid', 'shopname','shopurl','remark','isdel','_pk'=>'autoid'
	);

	protected $_map = array(
		'shopid'=>'autoid',
		'user' => 'customerid',	
		'country' => 'countryid',
		'shopcommon' => 'remark',		
	);

	protected $_validate=array(
		array('shopname','shoplength','商店名必须在5-20字之间',1,'callback',3),
		array('shopname','shopisset','商店名已存在',1,'callback',1),
		array('shopurl','shopurllength','商店链接必须在5-80字之间',1,'callback',3),
		array('shopurl','shopurlisset','链接重复',1,'callback',1),
		array('remark','remarks','备注不小于5个字',1,'callback',3),
	);

	public function shopautoid($str){
		if(M('shop')->where(array('autoid'=>$str))->find()) return true;
		else return false;
	}

	public function shoplength($str){
		$length=mb_strlen(trim($str));
		if($length >= 5 && $length <= 20) return true;
		else return false;
	}

	public function shopisset($str){
		if(M('shop')->where(array('shopname'=>$str))->find()) return false;
		else return true;
	}

	public function shopurllength($str){
		$length=strlen(trim($str));
		if($length >=5 && $length <= 80) return true;
		else return false;
	}

	public function shopurlisset($str){
		if(M('shop')->where(array('shopurl'=>$str))->find()) return false;
		else return true;
	}

	public function remarks($str){
		if($str){
			$length = mb_strlen(trim($str));
			if($length >= 5) return true;
			else return false;
		}else return true;
	}

	public function showadd($shop=0){
		if($shop) $data['shop']=M('shop')->where(array('autoid'=>$shop))->find();
		$data['country']=M('country')->getField('autoid,countryname');
        $data['user']=M('user')->where(array('isdel'=>0))->getField('autoid,realname,countryid');
        foreach ($data['user'] as $ku => $vu) {
        	foreach ($data['country'] as $kc => $vc) {
        		if($vu['countryid']==$kc) $data['country'][$vc]=$vu;
        	}
        }
        return $data['country'];
	}

	public function selectuserdata($country){
		$data=M('user')->where(array('isdel'=>0,'countryid'=>$country))->getField('autoid,realname');
		return $data;
	}

	public function showlist($u=0,$autoid=0){
		if($u==0)
			if($autoid==0) $shop=get_page_data(M('shop'),array('isdel'=>0),$order='autoid',$limit=10);
			else $shop=get_page_data(M('shop'),array('isdel'=>0,'autoid'=>$autoid),$order='autoid',$limit=10);
		//$shop = M('shop')->where(array('isdel'=>0))->getField('autoid,customerid,shopname,shopurl');
		else $shop=get_page_data(M('shop'),array('isdel'=>0,'customerid'=>$u),$order='autoid',$limit=10);
		$user = M('user')->where(array('isdel'=>0))->getField('autoid,realname,countryid');
		$country = M('country')->getField('autoid,countryname');
		foreach ($shop['list'] as $k => $v){
			foreach ($user as $ke => $va) {
				if($v['customerid'] == $ke){
					$shop['list'][$k]['customername']=$va['realname'];
					foreach ($country as $key => $value) {
						if($va['countryid']==$key) $shop['list'][$k]['countryname']=$value;
					}
				}
		}
			
	}
	//return $shop;
		$data['shop']=$shop;
		$data['user']=$user;
		$data['country']=$country;	
		return $data;
	}

}