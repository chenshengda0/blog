#系统管理员
create table rep_admin(
	autoid int primary key auto_increment comment 'id', 
	loginName varchar(20) not null comment '登录名',
	realName varchar(10) not null comment '员工姓名', 
	loginPassword char(32) not null comment '登陆密码',
	tel char(11) default '' comment '联系电话', 
	remark varchar(50) default '' comment '备注',
	isDel Tinyint(1) default 0 comment '0默认正常，1删除'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into rep_admin values(0,'admin','管理员','e3d84a1d7ef21efa8293f6d2566b1fa3','','',0);


##国家
create table rep_country(
	autoid int primary key auto_increment comment '国家id', 
	countryname varchar(30) not null comment '国家名',
	isdel Tinyint(1) not null default 0 comment '0为正常，1为软删除'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into rep_country values(0,'CHINA');

#客户
create table rep_user(
	autoid int primary key auto_increment comment '客户id',
	countryid int not null  comment '关联国家id',
	realname varchar(10) default '' comment '客户姓名',
	qq varchar(20) default '' comment '客户qq', 
	tel char(11) default '' comment '客户电话', 
	remark varchar(50) default '' comment '客户备注',
	isdel Tinyint(1) default 0 comment '0默认正常，1软删除'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


insert into rep_user values(0,1,'lucy','991669904','13500082594','',0);	

#商店
create table rep_shop(
	autoid int primary key auto_increment comment '店铺id', 
	customerid int not null comment '关联客户id', 
	shopname varchar(50) not null comment '商店名',
	shopurl varchar(100) default '' comment '商店链接', 
	remark varchar(20) default '' comment '备注',
	isdel Tinyint(1) default 0 comment '0默认正常，1软删除'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into rep_shop values(0,1,'荷兰咯','wwww.olnote.com','',0);


##商店
create table rep_goods(
	autoid int primary key auto_increment comment '商品id', 
	shopid int not null comment '关联店铺id', 
	goodsasin varchar(100) not null comment '商品id号', 
	goodsname varchar(50) not null comment '商品名',
	goodsurl varchar(100) default '' comment '商品链接', 
	remark varchar(20) default '' comment '备注',
	isdel Tinyint(1) default 0 comment '0默认正常，1软删除'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table rep_task(
	autoid int primary key auto_increment comment '任务id',
	goodsid int not null comment '关联商品id',
	keywords varchar(40) not null default '' comment '搜索关键词', 
	goodsprice decimal(10,2) not null comment '商品价格', 
	tasktype tinyint not null default 0 comment '任务类型，0为自发货，1FBA', 
	iscomment Tinyint(1) not null default 0 comment '是否留评,0不用，1要留',
	startdate int not null comment '任务起始时间',
	tasktotals int not null comment '任务总量',
	everydayquantity int not null comment '每日发布量', 
	goodspic varchar(100) not null default '' comment '产品图片，图片上传',
	isdel Tinyint(1) not null default 0 comment '0为正常，1为软删除',
	isstat Tinyint(1) default 0 comment '0为未完成，1为已完成', 
	remark text comment '备注'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

#创建员工数据表
create table rep_lilianjie(
	autoid int primary key auto_increment comment '主键id', 
	manager int not null comment '关联任务表', 
	buyerid varchar(100) not null comment '买家邮箱', 
	orderid varchar(50) not null comment '订单号',
	orderprice decimal(10,2) comment '订单完成金额',
	createtime int not null comment '订单完成时间'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into rep_tests values(0,7,'305522509@qq.com','1212122323423',1234.92,1217182212);

#创建任务表
create table rep_manager(
	autoid int primary key auto_increment comment '任务id', 
	userid text comment 'num,num', 
	taskid int not null comment '关联任务id',
	nottotle int not null comment '已发布的总数',
	day int not null default 1 comment '第几天',
	onetime int not null default 1 comment '首次查询时间',
	istask text comment '员工-主键',
	shopid int not null comment '关联商店id',
	status Tinyint(1) default 1 comment '1为继续发布，2为发布完成,3为已完成'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


create table rep_gift(
	autoid int primary key auto_increment comment '任务id', 
	userid int default 0 comment '领取人id', 
	giftprice decimal(10,2) not null comment '礼品卡金额',
	giftcard varchar(50) not null comment '礼品卡号',
	pubdate int default 0 comment '领取时间',
	status Tinyint(1) default 0 comment '0为未领取，1为已领取'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
#规则表
CREATE TABLE `rep_auth_rule` (  
    `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,  
    `name` char(80) NOT NULL DEFAULT '',
    `pid` char(2) default '',
    `title` char(20) NOT NULL DEFAULT '',  
    `type` tinyint(1) NOT NULL DEFAULT '1',    
    `status` tinyint(1) NOT NULL DEFAULT '1',  
    `condition` char(100) NOT NULL DEFAULT '',  # 规则附件条件,满足附加条件的规则,才认为是有效的规则
    PRIMARY KEY (`id`),  
    UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;
insert into rep_auth_rule values
	(1,'Admin/Login/index','','登陆首页',1,1,''),
	(2,'Admin/Public/pass','','修改密码',1,1,''),
	(3,'Admin/Public/logout','','注销用户',1,1,''),
	(4,'Admin/Public/updateuser','','修改密码',1,1,''),
	(5,'Admin/Staff','0','员工管理',1,1,''),
	(6,'Admin/Staff/slist','5','员工列表',1,1,''),
	(7,'Admin/Staff/sadd','5','添加员工',1,1,''),
	(8,'Admin/Staff/delstaff','','删除员工',1,1,''),
	(9,'Admin/State','0','国家管理',1,1,''),
	(10,'Admin/State/slist','9','国家列表',1,1,''),
	(11,'Admin/State/sadd','9','添加国家',1,1,''),
	(12,'Admin/State/countryupdate','','修改国家',1,1,''),
	(13,'Admin/State/delcountry','','删除国家',1,1,''),
	(14,'Admin/User','0','客户管理',1,1,''),
	(15,'Admin/User/ulist','14','客户列表',1,1,''),
	(16,'Admin/User/uadd','14','添加客户',1,1,''),
	(17,'Admin/User/uupdate','','修改客户',1,1,''),
	(18,'Admin/User/deluser','','删除客户',1,1,''),
	(19,'Admin/Shop','0','店铺管理',1,1,''),
	(20,'Admin/Shop/shoplist','19','店铺列表',1,1,''),
	(21,'Admin/Shop/shopuserlist','','店铺查询',1,1,''),
	(22,'Admin/Shop/shopadd','19','添加店铺',1,1,''),
	(23,'Admin/Shop/shopupdate','','修改店铺',1,1,''),
	(24,'Admin/Shop/shopdelete','','删除店铺',1,1,''),
	(25,'Admin/Goods','0','商品管理',1,1,''),
	(26,'Admin/Goods/goodslist','25','商品列表',1,1,''),
	(27,'Admin/Goods/goodsshoplist','','商品查询',1,1,''),
	(28,'Admin/Goods/goodsadd','25','添加商品',1,1,''),
	(29,'Admin/Goods/goodsupdate','','修改商品',1,1,''),
	(30,'Admin/Goods/goodsdelete','','删除商品',1,1,''),
	(31,'Admin/Task','0','发布任务管理',1,1,''),
	(32,'Admin/Task/tasklist','31','发布任务列表',1,1,''),
	(33,'Admin/Task/tasklistcont','','任务详情页',1,1,''),
	(34,'Admin/Task/taskquerylist','','搜索发布任务',1,1,''),
	(35,'Admin/Task/taskadd','31','添加发布任务',1,1,''),
	(36,'Admin/Task/taskimg','','发布任务图片',1,1,''),
	(37,'Admin/Task/taskupdate','','修改发布任务',1,1,''),
	(38,'Admin/Task/taskdelete','','删除发布任务',1,1,''),
	(39,'Admin/Oneself','0','接收任务管理',1,1,''),
	(40,'Admin/Oneself/tasktotle','39','任务列表',1,1,''),
	(41,'Admin/Oneself/accept','39','接收任务列表',1,1,''),
	(42,'Admin/Oneself/submit','','提交任务',1,1,''),
	(43,'Admin/Oneself/done','39','完成任务列表',1,1,''),
	(44,'Admin/Gift','0','礼品卡管理',1,1,''),
	(45,'Admin/Gift/giftlist','44','礼品卡列表',1,1,''),
	(46,'Admin/Gift/giftadd','44','礼品卡添加',1,1,''),
	(47,'Admin/Gift/giftcard','44','领取记录',1,1,''),
	(48,'Admin/Oneself/batch','','批量接收',1,1,''),
	(49,'Admin/Goods/goodsseach','','搜索商品',1,1,''),
	(50,'Admin/Shop/shopseach','','搜索商店',1,1,''),
	(51,'Admin/User/userseach','','搜索客户',1,1,''),
	(52,'Admin/Task/searchtask','','搜索任务',1,1,''),
	(53,'Admin/Oneself/searchoneself','','搜索接收任务',1,1,''),
	(54,'Admin/Gift/searchgift','','搜索礼品卡',1,1,'');
insert into rep_auth_rule values(54,'Admin/Gift/searchgift','','搜索礼品卡',1,1,'');
#用户组
CREATE TABLE `rep_auth_group` ( 
    `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT, 
    `title` char(100) NOT NULL DEFAULT '', 
    `status` tinyint(1) NOT NULL DEFAULT '1', 
    `rules` char(200) NOT NULL, 
    PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;
insert into rep_auth_group values(0,'业务组', '1', '1,2,3,4,5,6,9,10,14,15,19,20,21,25,26,27,33,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54');
insert into rep_auth_group values(0,'编辑组','1','1,2,3,4,5,6,9,10,11,14,15,16,19,20,21,22,25,26,27,28,31,32,33,34,35,36,39,40,44,45,47,49,50,51,52,53,54');
insert into rep_auth_group values(0,'管理组', '1', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,44,45,47,49,50,51,52,53,54');
insert into rep_auth_group values(0,'报表组','1','1,2,3,4,5,6,9,10,14,15,19,20,21,25,26,27,31,32,33,34,35,36,39,40,44,45,47,49,50,51,52,53,54');
insert into rep_auth_group values(0,'财务组','1','1,2,3,4,5,6,9,10,14,15,19,20,21,25,26,27,31,32,33,34,35,36,39,40,44,45,46,47,49,50,51,52,53,54');
#用户、组关联表
CREATE TABLE `rep_auth_group_access` (  
    `uid` mediumint(8) unsigned NOT NULL,  
    `group_id` mediumint(8) unsigned NOT NULL, 
    UNIQUE KEY `uid_group_id` (`uid`,`group_id`),  
    KEY `uid` (`uid`), 
    KEY `group_id` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
INSERT INTO `rep_auth_group_access` VALUES ('1', '3');
