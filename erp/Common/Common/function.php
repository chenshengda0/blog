<?php
header("Content-type:text/html;charset=utf-8");

//传递数据以易于阅读的样式格式化后输出
function p($data){
    // 定义样式
    $str='<pre style="display: block;padding: 9.5px;margin: 44px 0 0 0;font-size: 13px;line-height: 1.42857;color: #333;word-break: break-all;word-wrap: break-word;background-color: #F5F5F5;border: 1px solid #CCC;border-radius: 4px;">';
    // 如果是boolean或者null直接显示文字；否则print
    if (is_bool($data)) {
        $show_data=$data ? 'true' : 'false';
    }elseif (is_null($data)) {
        $show_data='null';
    }else{
        $show_data=print_r($data,true);
    }
    $str.=$show_data;
    $str.='</pre>';
    die($str);
}
/**
 * 检测是否登录
 * @return boolean 是否登录
 */
function check_login(){
    if (!empty($_SESSION[md5('admin')]['id'])){
        return true;
    }else{
        return false;
    }
}


/**
 * 获取分页数据
 * @param  subject  $model  model对象
 * @param  array    $map    where条件
 * @param  string   $order  排序规则
 * @param  integer  $limit  每页数量
 * @return array            分页数据
 */



function get_page_data($model,$map,$order='',$limit=5){
     	 $count= $model->where($map)->count();
         // 查询满足要求的总记录数
         $Page       = new \Think\Page($count,$limit);
         // 实例化分页类 传入总记录数和每页显示的记录数(25)
         $show       = $Page->show();
         // 分页显示输出// 进行分页数据查询 注意limit方法的参数要使用Page类的属性
         $list = $model->where($map)->order($order)->limit($Page->firstRow.','.$Page->listRows)->select();
        $data['page']=$show;
        $data['list']=$list;
        return $data;
}

