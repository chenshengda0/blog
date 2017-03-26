<?php
namespace Admin\Controller;
use Think\Controller;
class StaffController extends CommontController {
    public function slist(){
        $data['tree']=parent::$tree;
        $data['data']=M('admin')->getField('autoid,realname,loginname,tel');
        //dump($data);die;
        $this->assign($data);
        $this->display();
    }

    public function sadd(){
        if(IS_AJAX){
            $data=I('post.');
            //echo (json_encode($data));die;
            /*{"loginname":"lilianjie","realname":"\u674e\u8fde\u6770","authority":"1"}*/
            $data['loginName']=I('post.loginname');
            $data['loginPassword']=md5('a12345');
            $data['realName']=I('post.realname');
            $data['group']=$data['authority'];
            if(M('admin')->where(array('loginName'=>$data['loginName']))->find()) echo "用户名已经存在";
            elseif(M('admin')->where(array('realName'=>$data['realName']))->find()) echo "真实姓名已经存在";
            else{
                /*$id=M('admin')->data($data)->add();
                echo M('admin')->getLastSql();die;*/
                $autoid=M('admin')->add($data);
                if($autoid && $data['group']==1){
                    //创建员工数据表
                    $sql="create table rep_".$data['loginName']."(
                        autoid int primary key auto_increment comment '主键id', 
                        manager int not null comment '关联任务表', 
                        buyerid varchar(100) not null comment '买家邮箱', 
                        orderid varchar(50) not null comment '订单号',
                        orderprice decimal(10,2) comment '订单完成金额',
                        createtime int not null comment '订单完成时间'
                    )ENGINE=InnoDB DEFAULT CHARSET=utf8;";
                    M()->execute($sql);
                    if(M('auth_group_access')->add(array('uid'=>$autoid,'group_id'=>$data['group'])))
                    echo 1;
                    else echo '分配权限出错';
                }elseif($autoid && $data['group']!=1){
                     if(M('auth_group_access')->add(array('uid'=>$autoid,'group_id'=>$data['group'])))
                    echo 1;
                    else echo '分配权限出错';
                }else echo "数据添加错误";
            }
        }else{
        $data['tree']=parent::$tree;
          $this->assign($data);
          $this->display();  
        }   
    }

    public function delstaff(){
        if(IS_AJAX){
            $autoid = I("post.id");
            if(M('admin')->where(array('autoid'=>$autoid))->delete()) echo 1;
            else echo 0;
        }
    }

}