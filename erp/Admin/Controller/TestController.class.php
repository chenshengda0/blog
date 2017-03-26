<?php
namespace Admin\Controller;
use Think\Controller;
class TestController extends Controller {
    public function index(){
        $str=base64_encode('admin');
        $s=base64_decode($str);
        echo $s;
    }
}