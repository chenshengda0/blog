<?php
namespace Admin\Controller;
use Think\Controller;
class PublicController extends CommontController {
    public function pass(){
    		$autoid=I('get.i');
    		$data=M('admin')->where(array('autoid'=>$autoid))->find();
    		$data['tree']=parent::$tree;
    		if($data['autoid']==$_SESSION[md5('admin')]['autoid']){
    			$this->assign($data);
    			$this->display();
    		}else $this->redirect('Login/index');	
}

    public function logout(){
    	session(md5('admin'),null);
    	$this->redirect('Home/Login/login');
    }

    public function updateuser(){
    	if(IS_AJAX){
    		$data=I('post.');//{"loginpass":"231510622abc","realname":"\u6d4b\u8bd5\u53f7","tel":"18680201107","commons":"\u6682\u65e0\u5907\u6ce8\u4fe1\u606f"}
    		$autoid = $_SESSION[md5('admin')]['autoid'];
    		if(M('admin')->where(array('realName'=>$data['realname'],'autoid'=>array('neq',$autoid)))->find()) echo "真实姓名已经存在";
    		else{
                $data['realName']=$data['realname'];
                $data['loginPassword']=md5($data['loginpass']);
                $data['remark']=$data['commons'];
    			if(M('admin')->where(array('autoid'=>$autoid))->save($data)){
    				echo 1;
    			}
    			else echo '未知错误';
    		}
    	}
    }
}