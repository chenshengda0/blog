<?php
namespace Admin\Controller;
use Think\Controller;
class TaskController extends CommontController{
//管理员任务页
	public function tasklist(){
		$data['tree']=parent::$tree;
		$task=D('Task');
		if(IS_POST) $data['data']=$task->admindata( I('post.autoid') );
		else $data['data']=$task->admindata();
		//p(json_encode($data));
			$this->assign($data);
			$this->display();
		
	}

	public function searchtask(){
		if(IS_AJAX){
			$goodsname=I('post.content');
			$goodsdata=M('goods')->field('autoid,goodsname')->where(array('isdel'=>0,'goodsname'=>array('like','%'.$goodsname.'%')))->select();
			//echo(json_encode($goodsdata));
			if(count($goodsdata)>=1){
				$str='';
				foreach ($goodsdata as $key => $value) {
					$str.='<a href="#" onclick="javascript:selecttaskdata(this,'.$goodsdata[$key]["autoid"].');" class="list-group-item" style="background:#1AD6D6;">'.$goodsdata[$key]["goodsname"].'</a>';
				}
			}else $str='<span style="color:red;">未查询到记录</span>';
			echo $str;
		}
	}
	public function tasklistcont(){
		$id=I('get.i');
		$data['tree']=parent::$tree;
		if(!$data['data']=M('task')->where(array('isdel'=>0,'autoid'=>$id))->find()) $this->redirect('Login/index');//echo(M('task')->getLastSql());die;
		else{
			$this->assign($data);
			$this->display();
		}
	}

	public function taskquerylist(){
			$goodsid=I('get.i');
			$data['tree']=parent::$tree;
			//dump($data);die;
			$data['data']=D('Task')->admindata($goodsid);
			$this->assign($data);
			$this->display('tasklist');
		
	}
//员工任务页
//四级联动

	public function taskadd(){
		$data['tree']=parent::$tree;
		$task=D('Task');
		if(IS_AJAX){
			if(I('post.val')){
			$val=I('post.val');	
			$level=I('post.level');
			if($level=='客户') $data = M('user')->where(array('countryid'=>$val,'isdel'=>0))->getField('autoid,realname');
			elseif($level=='商店') $data = M('shop')->where(array('customerid'=>$val,'isdel'=>0))->getField('autoid,shopname');
			elseif($level=='商品') $data = M('goods')->where(array('isdel'=>0,'shopid'=>$val))->getField('autoid,goodsname');
			$option="<option value=''>请选择".$level."</option>";
				foreach ($data as $key => $value) {
					$option.="<option value='".$key."'>".$value."</option>";
				}
				echo(json_encode($option));
			}else{
				//$forms=I('post.');
				if(!$data=$task->create()) echo $task->getError();
				else{
					$data['startdate']=strtotime($data['startdate']);
					//echo(json_encode($data));
					if(!M('task')->where(array('startdate'=>$data['startdate'],'goodsid'=>$data['goodsid']))->find()){
						if($id=M('task')->add($data)) echo $id;
						else echo '数据添加出错';
					}else echo '请勿重复提交';
					
				}
				//echo(json_encode($forms));die;
			}	
			//echo(json_encode($level));
			/*if($data['data']=$task->selectcountrydata($country = $forms['country'])){
				echo(json_encode($data['data']));
			}
			else echo 0;*/
		}else{
			//显示任务管理表单
			//dump($data['data']);die;
			$data['data']=$task->selectdata();
			$this->assign($data);
			$this->display();
		}
		
	}
//弹出层图片上传
	public function taskimg(){
		$id=I('get.i');
		//echo ($id);die;
		$dat=array('id'=>$id);
		if(IS_POST){
			$data['autoid']=I('post.imgautoid');
			$upload = new \Think\Upload();
			// 实例化上传类    
			$upload->maxSize   =     3145728 ;// 设置附件上传大小    
			$upload->exts      =     array('jpg', 'gif', 'png', 'jpeg');// 设置附件上传类型    
			$upload->savePath  =      ''; // 设置附件上传目录    // 上传单个文件     
			$info   =   $upload->uploadOne($_FILES['photo']);    
			if(!$info) {
			// 上传错误提示错误信息        
			$this->error($upload->getError());
		    }
			else{
			// 上传成功 获取上传文件信息
				if(M('task')->where($data)->find()){
					$data['goodspic']="/Uploads/".$info['savepath'].$info['savename'];
					if(M('task')->save($data))  echo("<script>parent.location.href='/Admin/Task/tasklist'</script>");
					else  echo("<script>parent.layer.closeAll()</script>");
				}//php 传递到前端的script脚本会直接被执行
				else echo("<script>parent.location.href='/Admin/Public/index'</script>");
	    	}
	}
		
		$this->assign($dat);
		$this->display();
}

	/*public function upload(){    
		$upload = new \Think\Upload();
		// 实例化上传类    
		$upload->maxSize   =     3145728 ;// 设置附件上传大小    
		$upload->exts      =     array('jpg', 'gif', 'png', 'jpeg');// 设置附件上传类型    
		$upload->savePath  =      './Public/Uploads/'; // 设置附件上传目录    // 上传单个文件     
		$info   =   $upload->uploadOne($_FILES['photo1']);    
		if(!$info) {
		// 上传错误提示错误信息        
		$this->error($upload->getError());
	    }
		else{
		// 上传成功 获取上传文件信息         
			echo $info['savepath'].$info['savename'];
    }}*/

	public function taskupdate(){
		$task=D('Task');
		$autoid=I('get.i');
		$data['tree']=parent::$tree;
		if(IS_AJAX){
			$data=I('post.');
			if(!$dat=$task->create($data,2)) echo $task->getError();
			else{
				$dat['startdate']=strtotime($dat['startdate']);
				if(M('task')->where(array('autoid'=>$dat['autoid']))->save($dat)) echo 1;
				else echo 0;
				//echo(json_encode($dat));
			}
			//echo(json_encode($data));die;
		}else{
			if($data['data']=M('task')->where(array('isdel'=>0,'autoid'=>$autoid))->find()){
			$this->assign($data);
			//dump($data);die;
			$this->display();
			} 
			else $this->redirect('Public/index');
		}
		
	}
	public function taskdelete(){
		if(IS_AJAX){
			$autoid=I('post.id');
			if(M('task')->where(array('autoid'=>$autoid,'isstat'=>0))->find()){
				if(M('task')->where(array('autoid'=>$autoid,'isdel'=>0))->save(array('isdel'=>1))) echo 1;
				else echo 0;
			}
			else  echo '任务在进行状态下不能删除';
		}
	}
	
}