<?php
return array(
	//'配置项'=>'配置值'
	'DEFAULT_V_LAYER'       =>  'View', // 设置默认的视图层名称
	'TMPL_TEMPLATE_SUFFIX'	=>	'.html',//定义文本后缀
	//'TMPL_FILE_DEPR'		=>	'_',//把目录结构定义成下划线
	'TMPL_PARSE_STRING'  	=>	array(     
			'__FONTS__' => '/Public/fonts', // 更改默认的/Public 替换规则     
			'__JS__'     => '/Public/js', // 增加新的JS类库路径替换规则     
			'__CSS__'     => '/Public/css', // 增加新的JS类库路径替换规则     
			'__IMG__'     => '/Public/images', // 增加新的JS类库路径替换规则     
			'__UPLOAD__' => '/Uploads', // 增加新的上传路径替换规则
            '__ACOMMON__'=> '/Admin/View/Common',
            '__HTML__'=> '/Public/html',
		),
	'URL_MODEL'             =>  2,       // URL访问模式,可选参数0、1、2、3,代表以下四种模式：
    // 0 (普通模式); 1 (PATHINFO 模式); 2 (REWRITE  模式); 3 (兼容模式)  默认为PATHINFO 模式
    'DEFAULT_MODULE'        =>  'Home',  // 默认模块
    'DEFAULT_CONTROLLER'    =>  'Login', // 默认控制器名称
    'DEFAULT_ACTION'        =>  'login', // 默认操作名称
    'URL_CASE_INSENSITIVE'  =>  true,//url不区分大小写
    //mysql配置
    'DB_TYPE'               =>  'mysql',     // 数据库类型
    'DB_HOST'               =>  'localhost', // 服务器地址
    'DB_NAME'               =>  'rep_sys',          // 数据库名
    'DB_USER'               =>  'root',      // 用户名
    'DB_PWD'                =>  '231510622abc',          // 密码
    'DB_PORT'               =>  '3306',        // 端口
    'DB_PREFIX'             =>  'rep_',    // 数据库表前缀
    'DB_FIELDS_CACHE'=>false,//关闭字段缓存
    //'READ_DATA_MAP' =>  true,//开启查询出来的字段对应字段映射
);