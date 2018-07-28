use djangobms;

create table bms_app_user
(
	user_id integer auto_increment primary key,
    user_name varchar(30) not null, unique(user_name),
    pass_word varchar(30)
);

create table bms_app_reader
(	
	reader_id integer auto_increment primary key,
    name varchar(30) not null,
    user_id integer,
    address varchar(50),
    occupation varchar(30),
    email varchar(50) not null,
    
    foreign key (user_id) references bms_app_user(user_id)
    on delete cascade
    on update cascade
);

/*
SET FOREIGN_KEY_CHECKS=1;
drop table bms_app_class_info;
drop table bms_app_book_info;
*/
create table bms_app_admin
(
	admin_id integer auto_increment primary key,
    user_id integer,
    
    foreign key(user_id) references bms_app_user(user_id)
    on delete cascade
    on update cascade    
);

create table bms_app_class_info
(
	class_info_id integer auto_increment primary key,
    class_intro varchar(30)
);

create table bms_app_book_info
(
	book_id integer auto_increment primary key,
    book_name varchar(30) not null,
    author varchar(30) not null,
    publisher varchar(30) not null,
    introduction varchar(100),
    pub_date date not null,
    class_info_id integer not null,
    remain smallint default 0,
    
    foreign key(class_info_id) references bms_app_class_info(class_info_id)
    on delete cascade
    on update cascade
);

create table bms_app_card
(
	card_id integer auto_increment primary key,
    reader_id integer not null,
    #due_date timestamp(0),
    
    foreign key(reader_id) references bms_app_reader(reader_id)
    on delete cascade
    on update cascade
);

create table bms_app_borrow
(
	borrow_id integer auto_increment primary key,
    card_id integer not null,
    book_id integer not null,
    when_ timestamp(0),
    create_back smallint default 0,

    foreign key(card_id) references bms_app_card(card_id)
    on delete cascade
    on update cascade,
    
    foreign key(book_id) references bms_app_book_info(book_id)
    on delete cascade
    on update cascade
);
/*
drop table bms_app_card;
drop table bms_app_user;
drop table bms_app_reader;
drop table bms_app_class_info;
drop table bms_app_borrow;
drop table bms_app_book_info;
drop table bms_app_admin;
*/

insert into bms_app_class_info(class_intro) values('A马克思列宁主义');#1
insert into bms_app_class_info(class_intro) values('AA毛泽东思想');#2
insert into bms_app_class_info(class_intro) values('B宗教哲学');#3
insert into bms_app_class_info(class_intro) values('C社会科学');#4
insert into bms_app_class_info(class_intro) values('D政治法律');#5
insert into bms_app_class_info(class_intro) values('E军事');#6
insert into bms_app_class_info(class_intro) values('F经济');#7
insert into bms_app_class_info(class_intro) values('G文化体育');#8
insert into bms_app_class_info(class_intro) values('H自然语言');#9
insert into bms_app_class_info(class_intro) values('I文学艺术');#10
insert into bms_app_class_info(class_intro) values('K自然地理');#11
insert into bms_app_class_info(class_intro) values('N自然科学总论');#12
insert into bms_app_class_info(class_intro) values('O数理科学');#13
insert into bms_app_class_info(class_intro) values('P天文学');#14
insert into bms_app_class_info(class_intro) values('Q生物科学');#15
insert into bms_app_class_info(class_intro) values('R医学卫生');#16
insert into bms_app_class_info(class_intro) values('S农业科学');#17
insert into bms_app_class_info(class_intro) values('TD矿业工程');#18
insert into bms_app_class_info(class_intro) values('TE石油天然气');#19
insert into bms_app_class_info(class_intro) values('TL原子能');#20
insert into bms_app_class_info(class_intro) values('TM电工技术');#21
insert into bms_app_class_info(class_intro) values('TN无线电电信');#22
insert into bms_app_class_info(class_intro) values('TP自动化计算机技术');#23
insert into bms_app_class_info(class_intro) values('U交通运输');#24
insert into bms_app_class_info(class_intro) values('Z综合性图书');#25


insert into bms_app_book_info(book_name, author, publisher, introduction, pub_date, class_info_id, remain)
values('函数式编程入门', 'John Xiao', '机械工业出版社', '以Haskel为例, 深入浅出, 数据映射是核心', '2000-01-01', 23, 1);
insert into bms_app_book_info(book_name, author, publisher, introduction, pub_date, class_info_id, remain)
values('C++ primer', 'VCZH Lee', '人民邮电出版社', '精通C++, 不再是梦想', '2010-12-01', 23, 2);
insert into bms_app_book_info(book_name, author, publisher, introduction, pub_date, class_info_id, remain)
values('深入理解对象模型', 'Michael Qiang', '机械工业出版社', 'Java是世界上最好的语言', '2010-11-01', 23, 10);
insert into bms_app_book_info(book_name, author, publisher, introduction, pub_date, class_info_id, remain)
values('dot NET开发指南', 'John Clienberg', '蓝田出版社', 'C#是世界上最好的语言', '2010-12-01', 23, 5);
insert into bms_app_book_info(book_name, author, publisher, introduction, pub_date, class_info_id, remain)
values('JavaScript高级教程', 'Xiaoqiang Wang', '浙江大学出版社', 'Web世界属于JavaScript', '2018-4-20', 23, 2);
insert into bms_app_book_info(book_name, author, publisher, introduction, pub_date,class_info_id, remain)
values('Introduction to Algorithm', 'Thomas H. Corman', 'Cornell University Press', 'tutorial to algorithm and analysis performance' , '2018-4-21', 23, 10);

insert into bms_app_book_info(book_name, author, publisher, introduction, pub_date, class_info_id, remain)
values('齐民要术', 'Xiao Q. Wang', '蓝田出版社', '这不是贾思勰的作品', '2018-2-20', 17, 1);
insert into bms_app_book_info(book_name, author, publisher, introduction, pub_date, class_info_id, remain)
values('浓缩铀的提炼', 'Xiao Q. Wang', '蓝田出版社', '核无疑依旧是21世纪的热点', '2018-3-21', 20, 2);
insert into bms_app_book_info(book_name, author, publisher, introduction, pub_date, class_info_id, remain)
values('普通物理学II(H)', 'Xiao Q. Wang', '蓝田出版社', '你永远不要怀疑物理的魅力', '2018-5-31', 13, 2);
insert into bms_app_book_info(book_name, author, publisher, introduction, pub_date, class_info_id, remain)
values('数学分析', 'Xiao Q. Wang', '蓝田出版社', '超过毛子, 不再是我们的目标', '2018-6-1', 13, 4);
insert into bms_app_book_info(book_name, author, publisher, introduction, pub_date, class_info_id, remain)
values('共产党宣言', 'Karl Marx', '中国社会科学院出版社', '全世界无产阶级一起联合起来', '2018-7-20', 1, 10);
insert into bms_app_book_info(book_name, author, publisher, introduction, pub_date, class_info_id, remain)
values('资本论', 'Karl Marx', '中国社会科学院出版社', '被剥削者自由的一无所有, 劳动因此成为商品', '2018-8-20', 1, 4);
insert into bms_app_book_info(book_name, author, publisher, introduction, pub_date, class_info_id, remain)
values('论持久战', '毛泽东', '人民日报出版社', '敌进我退，敌驻我扰，敌疲我打，敌退我追', '2018-9-11', 2, 4);
insert into bms_app_book_info(book_name, author, publisher, introduction, pub_date, class_info_id, remain)
values('农村包围城市', '毛泽东', '人民日报出版社', '历史证明, 这是天才的举措', '2018-10-28', 2, 2);






