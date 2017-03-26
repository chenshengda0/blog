#ϵͳ����Ա
create table rep_admin(
	autoid int primary key auto_increment comment 'id', 
	loginName varchar(20) not null comment '��¼��',
	realName varchar(10) not null comment 'Ա������', 
	loginPassword char(32) not null comment '��½����',
	tel char(11) default '' comment '��ϵ�绰', 
	remark varchar(50) default '' comment '��ע',
	isDel Tinyint(1) default 0 comment '0Ĭ��������1ɾ��'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into rep_admin values(0,'admin','����Ա','e3d84a1d7ef21efa8293f6d2566b1fa3','','',0);


##����
create table rep_country(
	autoid int primary key auto_increment comment '����id', 
	countryname varchar(30) not null comment '������',
	isdel Tinyint(1) not null default 0 comment '0Ϊ������1Ϊ��ɾ��'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into rep_country values(0,'CHINA');

#�ͻ�
create table rep_user(
	autoid int primary key auto_increment comment '�ͻ�id',
	countryid int not null  comment '��������id',
	realname varchar(10) default '' comment '�ͻ�����',
	qq varchar(20) default '' comment '�ͻ�qq', 
	tel char(11) default '' comment '�ͻ��绰', 
	remark varchar(50) default '' comment '�ͻ���ע',
	isdel Tinyint(1) default 0 comment '0Ĭ��������1��ɾ��'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


insert into rep_user values(0,1,'lucy','991669904','13500082594','',0);	

#�̵�
create table rep_shop(
	autoid int primary key auto_increment comment '����id', 
	customerid int not null comment '�����ͻ�id', 
	shopname varchar(50) not null comment '�̵���',
	shopurl varchar(100) default '' comment '�̵�����', 
	remark varchar(20) default '' comment '��ע',
	isdel Tinyint(1) default 0 comment '0Ĭ��������1��ɾ��'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into rep_shop values(0,1,'������','wwww.olnote.com','',0);


##�̵�
create table rep_goods(
	autoid int primary key auto_increment comment '��Ʒid', 
	shopid int not null comment '��������id', 
	goodsasin varchar(100) not null comment '��Ʒid��', 
	goodsname varchar(50) not null comment '��Ʒ��',
	goodsurl varchar(100) default '' comment '��Ʒ����', 
	remark varchar(20) default '' comment '��ע',
	isdel Tinyint(1) default 0 comment '0Ĭ��������1��ɾ��'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table rep_task(
	autoid int primary key auto_increment comment '����id',
	goodsid int not null comment '������Ʒid',
	keywords varchar(40) not null default '' comment '�����ؼ���', 
	goodsprice decimal(10,2) not null comment '��Ʒ�۸�', 
	tasktype tinyint not null default 0 comment '�������ͣ�0Ϊ�Է�����1FBA', 
	iscomment Tinyint(1) not null default 0 comment '�Ƿ�����,0���ã�1Ҫ��',
	startdate int not null comment '������ʼʱ��',
	tasktotals int not null comment '��������',
	everydayquantity int not null comment 'ÿ�շ�����', 
	goodspic varchar(100) not null default '' comment '��ƷͼƬ��ͼƬ�ϴ�',
	isdel Tinyint(1) not null default 0 comment '0Ϊ������1Ϊ��ɾ��',
	isstat Tinyint(1) default 0 comment '0Ϊδ��ɣ�1Ϊ�����', 
	remark text comment '��ע'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

#����Ա�����ݱ�
create table rep_lilianjie(
	autoid int primary key auto_increment comment '����id', 
	manager int not null comment '���������', 
	buyerid varchar(100) not null comment '�������', 
	orderid varchar(50) not null comment '������',
	orderprice decimal(10,2) comment '������ɽ��',
	createtime int not null comment '�������ʱ��'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into rep_tests values(0,7,'305522509@qq.com','1212122323423',1234.92,1217182212);

#���������
create table rep_manager(
	autoid int primary key auto_increment comment '����id', 
	userid text comment 'num,num', 
	taskid int not null comment '��������id',
	nottotle int not null comment '�ѷ���������',
	day int not null default 1 comment '�ڼ���',
	onetime int not null default 1 comment '�״β�ѯʱ��',
	istask text comment 'Ա��-����',
	shopid int not null comment '�����̵�id',
	status Tinyint(1) default 1 comment '1Ϊ����������2Ϊ�������,3Ϊ�����'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


create table rep_gift(
	autoid int primary key auto_increment comment '����id', 
	userid int default 0 comment '��ȡ��id', 
	giftprice decimal(10,2) not null comment '��Ʒ�����',
	giftcard varchar(50) not null comment '��Ʒ����',
	pubdate int default 0 comment '��ȡʱ��',
	status Tinyint(1) default 0 comment '0Ϊδ��ȡ��1Ϊ����ȡ'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
#�����
CREATE TABLE `rep_auth_rule` (  
    `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT,  
    `name` char(80) NOT NULL DEFAULT '',
    `pid` char(2) default '',
    `title` char(20) NOT NULL DEFAULT '',  
    `type` tinyint(1) NOT NULL DEFAULT '1',    
    `status` tinyint(1) NOT NULL DEFAULT '1',  
    `condition` char(100) NOT NULL DEFAULT '',  # ���򸽼�����,���㸽�������Ĺ���,����Ϊ����Ч�Ĺ���
    PRIMARY KEY (`id`),  
    UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;
insert into rep_auth_rule values
	(1,'Admin/Login/index','','��½��ҳ',1,1,''),
	(2,'Admin/Public/pass','','�޸�����',1,1,''),
	(3,'Admin/Public/logout','','ע���û�',1,1,''),
	(4,'Admin/Public/updateuser','','�޸�����',1,1,''),
	(5,'Admin/Staff','0','Ա������',1,1,''),
	(6,'Admin/Staff/slist','5','Ա���б�',1,1,''),
	(7,'Admin/Staff/sadd','5','���Ա��',1,1,''),
	(8,'Admin/Staff/delstaff','','ɾ��Ա��',1,1,''),
	(9,'Admin/State','0','���ҹ���',1,1,''),
	(10,'Admin/State/slist','9','�����б�',1,1,''),
	(11,'Admin/State/sadd','9','��ӹ���',1,1,''),
	(12,'Admin/State/countryupdate','','�޸Ĺ���',1,1,''),
	(13,'Admin/State/delcountry','','ɾ������',1,1,''),
	(14,'Admin/User','0','�ͻ�����',1,1,''),
	(15,'Admin/User/ulist','14','�ͻ��б�',1,1,''),
	(16,'Admin/User/uadd','14','��ӿͻ�',1,1,''),
	(17,'Admin/User/uupdate','','�޸Ŀͻ�',1,1,''),
	(18,'Admin/User/deluser','','ɾ���ͻ�',1,1,''),
	(19,'Admin/Shop','0','���̹���',1,1,''),
	(20,'Admin/Shop/shoplist','19','�����б�',1,1,''),
	(21,'Admin/Shop/shopuserlist','','���̲�ѯ',1,1,''),
	(22,'Admin/Shop/shopadd','19','��ӵ���',1,1,''),
	(23,'Admin/Shop/shopupdate','','�޸ĵ���',1,1,''),
	(24,'Admin/Shop/shopdelete','','ɾ������',1,1,''),
	(25,'Admin/Goods','0','��Ʒ����',1,1,''),
	(26,'Admin/Goods/goodslist','25','��Ʒ�б�',1,1,''),
	(27,'Admin/Goods/goodsshoplist','','��Ʒ��ѯ',1,1,''),
	(28,'Admin/Goods/goodsadd','25','�����Ʒ',1,1,''),
	(29,'Admin/Goods/goodsupdate','','�޸���Ʒ',1,1,''),
	(30,'Admin/Goods/goodsdelete','','ɾ����Ʒ',1,1,''),
	(31,'Admin/Task','0','�����������',1,1,''),
	(32,'Admin/Task/tasklist','31','���������б�',1,1,''),
	(33,'Admin/Task/tasklistcont','','��������ҳ',1,1,''),
	(34,'Admin/Task/taskquerylist','','������������',1,1,''),
	(35,'Admin/Task/taskadd','31','��ӷ�������',1,1,''),
	(36,'Admin/Task/taskimg','','��������ͼƬ',1,1,''),
	(37,'Admin/Task/taskupdate','','�޸ķ�������',1,1,''),
	(38,'Admin/Task/taskdelete','','ɾ����������',1,1,''),
	(39,'Admin/Oneself','0','�����������',1,1,''),
	(40,'Admin/Oneself/tasktotle','39','�����б�',1,1,''),
	(41,'Admin/Oneself/accept','39','���������б�',1,1,''),
	(42,'Admin/Oneself/submit','','�ύ����',1,1,''),
	(43,'Admin/Oneself/done','39','��������б�',1,1,''),
	(44,'Admin/Gift','0','��Ʒ������',1,1,''),
	(45,'Admin/Gift/giftlist','44','��Ʒ���б�',1,1,''),
	(46,'Admin/Gift/giftadd','44','��Ʒ�����',1,1,''),
	(47,'Admin/Gift/giftcard','44','��ȡ��¼',1,1,''),
	(48,'Admin/Oneself/batch','','��������',1,1,''),
	(49,'Admin/Goods/goodsseach','','������Ʒ',1,1,''),
	(50,'Admin/Shop/shopseach','','�����̵�',1,1,''),
	(51,'Admin/User/userseach','','�����ͻ�',1,1,''),
	(52,'Admin/Task/searchtask','','��������',1,1,''),
	(53,'Admin/Oneself/searchoneself','','������������',1,1,''),
	(54,'Admin/Gift/searchgift','','������Ʒ��',1,1,'');
insert into rep_auth_rule values(54,'Admin/Gift/searchgift','','������Ʒ��',1,1,'');
#�û���
CREATE TABLE `rep_auth_group` ( 
    `id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT, 
    `title` char(100) NOT NULL DEFAULT '', 
    `status` tinyint(1) NOT NULL DEFAULT '1', 
    `rules` char(200) NOT NULL, 
    PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;
insert into rep_auth_group values(0,'ҵ����', '1', '1,2,3,4,5,6,9,10,14,15,19,20,21,25,26,27,33,39,40,41,42,43,44,45,47,48,49,50,51,52,53,54');
insert into rep_auth_group values(0,'�༭��','1','1,2,3,4,5,6,9,10,11,14,15,16,19,20,21,22,25,26,27,28,31,32,33,34,35,36,39,40,44,45,47,49,50,51,52,53,54');
insert into rep_auth_group values(0,'������', '1', '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,44,45,47,49,50,51,52,53,54');
insert into rep_auth_group values(0,'������','1','1,2,3,4,5,6,9,10,14,15,19,20,21,25,26,27,31,32,33,34,35,36,39,40,44,45,47,49,50,51,52,53,54');
insert into rep_auth_group values(0,'������','1','1,2,3,4,5,6,9,10,14,15,19,20,21,25,26,27,31,32,33,34,35,36,39,40,44,45,46,47,49,50,51,52,53,54');
#�û����������
CREATE TABLE `rep_auth_group_access` (  
    `uid` mediumint(8) unsigned NOT NULL,  
    `group_id` mediumint(8) unsigned NOT NULL, 
    UNIQUE KEY `uid_group_id` (`uid`,`group_id`),  
    KEY `uid` (`uid`), 
    KEY `group_id` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
INSERT INTO `rep_auth_group_access` VALUES ('1', '3');
