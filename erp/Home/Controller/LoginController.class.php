<?php
namespace Home\Controller;
use Think\Controller;
class LoginController extends Controller {
//首页        
    public function login(){
    	if(IS_AJAX){
            $username=I('post.username');
            $password=I('post.password');
            $code=I('post.codes');
            echo $this->yanz($username,$password,$code);
        }else{
        	$this->display();
        }
    }
//参数验证
    public function yanz($username,$password,$code){
        if(strlen($username)<5 || strlen($username)>9 )
            return '用户名必须在5-9位';
        elseif (strlen($password)<6 || strlen($u)>15)
            return '密码必须在6-15位之间';
        elseif(strlen($code) != 3)
            return '验证码必须为3位';
        elseif(strlen($code)==3){
            if($this->codes($code)){
                //查询数据库
                if($data=M('admin')->where(array('loginName'=>$username,'loginPassword'=>md5($password)))->find()){
                    $authority=M('auth_group_access')->where(array('uid'=>$data['autoid']))->select();
                    $str='';
                    foreach ($authority as $row) {
                        $str.=(M('auth_group')->where(array('id'=>$row['group_id']))->getField('rules')).',';
                    }
                    $str = implode(',',array_unique(explode(',',$str)));
                    //echo $str;die;
                    $data['authority']=$str;
                    $data['task']=array();
                    $_SESSION[md5('admin')]=$data;
                    echo 1;
                }
                else return '用户名或密码错误';
            }else return "验证码输入错误";
        }
    }
//验证码及输入的验证码验证
    public function codes($code='',$id=''){
    	$config =    array(    
    		'fontSize'    =>    17,    // 验证码字体大小    
    		'length'      =>    3,     // 验证码位数    
            'useNoise'    =>    true, // 关闭验证码杂点
            'useCurve'    =>    false, // 是否关闭干扰线
            'bg'    =>    array(48,213,246), // 背景色
            'codeSet'    => 'ABCDdEeFfGgHhKLMNnPQXYZ', //指定字符范围
            'fontSize'    => 25, // 字体大小
    		'expire'    => 60, // 过期时间
    	);
    	$Verify =     new \Think\Verify($config);
        if($code)
            return $Verify->check($code, $id);
    	else
          $Verify->entry();  
    }

    public function _empty(){        
        //空控制器输入登录页面        
        $this->display('Login/login');    
    }
}