<?php
namespace Admin\Model;
use Think\Model;
class GoodsModel extends Model{
	protected $fields = array('autoid', 'customerid', 'countryid','shopid','goodsasin', 'goodsname','goodsurl','remark','isdel','_pk'=>'autoid'
	);

	protected $_map=array(
		'goodsid' => 'autoid',
		'shop' => 'shopid',
		'goodsid' => 'goodsasin',
		'goodscommon' => 'remark',
	);

	protected $_validate = array(
		array('shopid','isnotnull','商店名为必选项',1,'callback',1),
		array('goodsasin','goodsidlength','商品ID号必须为5-80字符',1,'callback',3),
		array('goodsasin','goodsidisset','商品ID号重复',1,'callback',1),
		array('goodsname','goodsnamelength','商品名长度必须为2-40字符',1,'callback',3),
		//array('goodsname','goodsnameisset','商品名重复',1,'callback',1),
		array('goodsurl','goodsurllength','商品链接必须为5-80字符',1,'callback',1),
		array('goodsurl','goodsurlisset','商品链接重复',1,'callback',1),
		array('remark','remarkisnull','备注长度必须在3-20字之间',1,'callback',3),
	);

	public function isnotnull($str){
		if($str==0) return false;
		else return true;
	}

	public function goodsidlength($str){
		$length=strlen(trim($str));
		if($length >= 5 && $length <= 80) return true;
		else return false;
	}

	public function goodsidisset($str){
		if(M('goods')->where(array('goodsasin'=>$str))->find()) return false;
		else return true;
	}

	public function goodsnamelength($str){
		$length = mb_strlen(trim($str));
		if($length >= 2 && $length <= 40) return true;
		else return false;
	}

	public function goodsurllength($str){
		$length = strlen(trim($str));
		if($length >= 5 && $length <= 80) return true;
		else return false;
	}

	public function goodsurlisset($str){
		if(M('goods')->where(array('goodsurl'=>$str))->find()) return false;
		else return true;
	}

	public function remarkisnull($str){
		$length=mb_strlen(trim($str));
		if($length==0)return true;
		elseif($length >= 3 && $length <= 20)return true;
		else return false;
	}

	public function listdata($u=0,$autoid=0){
		if($u==0){
			if($autoid==0) $data['goods']=get_page_data(M('goods'),array('isdel'=>0),$order='autoid',$limit=10);
			else $data['goods']=get_page_data(M('goods'),array('isdel'=>0,'autoid'=>$autoid),$order='autoid',$limit=10);
		}
			//->where()->getField('autoid,shopid,goodsasin,goodsname,goodsurl');
		else $data['goods']=get_page_data(M('goods'),array('isdel'=>0,'shopid'=>$u),$order='autoid',$limit=10);
		$data['country'] = M('country')->getField('autoid,countryname');
		$data['user']=M('user')->where(array('isdel'=>0))->getField('autoid,realname,countryid');
		$data['shop']=M('shop')->where(array('isdel'=>0))->getField('autoid,shopname,customerid');
			foreach($data['user'] as $ku => $vu){//客户
				foreach ($data['country'] as $kc => $vc) {
					if($vu['countryid']==$kc) $data['user'][$ku]['countryname']=$vc;
					}
				}
			foreach ($data['shop'] as $ks => $vs) {
				foreach ($data['user'] as $ku => $vu) {
					if($vs['customerid']==$ku){
						$data['shop'][$ks]['username']=$vu['realname'];
						$data['shop'][$ks]['countryname']=$vu['countryname'];
					}
				}
			}
			foreach ($data['goods']['list'] as $kg => $vg) {
				foreach ($data['shop'] as $ks => $vs) {
					if($vg['shopid']==$ks){
						$data['goods']['list'][$kg]['shopname']=$vs['shopname'];
						$data['goods']['list'][$kg]['username']=$vs['username'];
						$data['goods']['list'][$kg]['countryname']=$vs['countryname'];
					}
				}
			}
		return $data;
	}


	public function updatedata($i){
		$data['goods']=M('goods')->where(array('isdel'=>0,'autoid'=>$i))->getField('autoid,shopid,goodsasin,goodsname,goodsurl,remark');
		$data['country'] = M('country')->getField('autoid,countryname');
		$data['user']=M('user')->where(array('isdel'=>0))->getField('autoid,realname');
		$data['shop']=M('shop')->where(array('isdel'=>0))->getField('autoid,shopname');
		return $data;
	}

	public function selectnav($user){
		$data['shop']=M('shop')->where(array('isdel'=>0,'customerid'=>$user))->getField('autoid,shopname');
		return $data;
	}

	public function goodsforeign(){
		$data['user']=M('user')->getField('autoid,realname');
		return $data;
	}
}