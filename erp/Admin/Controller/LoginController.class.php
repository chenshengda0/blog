<?php
namespace Admin\Controller;
use Think\Controller;
class LoginController extends Controller {
    public function index(){
    	//$data=getTreeData($type='tree',$order='')
    	$tree=M('auth_rule')->where(array('id'=>array('in',$_SESSION[md5('admin')]['authority']),'pid'=>array('neq','')))->select();
    	$data['tree']=\Org\Nx\Data::channelLevel($tree,0,'&nbsp;','id');
    	$this->assign($data);
        $this->display();
    }
    public function _empty(){             
        $this->redirect('/Home/Login/login');    
    }
}