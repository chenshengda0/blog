<?php
namespace Admin\Controller;
use Think\Controller;
class CommontController extends Controller {
	static $tree;
	protected function _initialize()
	{
		$auth=new \Think\Auth();
		$rule_name=MODULE_NAME.'/'.CONTROLLER_NAME.'/'.ACTION_NAME;
		$result=$auth->check($rule_name,$_SESSION[md5('admin')]['autoid']);
		if(!$result){
		$this->error('您没有权限访问');
		}else{
			$tree=M('auth_rule')->where(array('id'=>array('in',$_SESSION[md5('admin')]['authority']),'pid'=>array('neq','')))->select();

    		self::$tree=\Org\Nx\Data::channelLevel($tree,0,'&nbsp;','id');
    		
		}
	}
}