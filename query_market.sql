show databases;
-- drop database market;

create database market;

use market;

create table user (
	user_id varchar(20) not null primary key,
    name varchar(20) not null,
    e_mail varchar(30) not null,
    phone_number varchar(30) not null,
    password varchar(30) not null,
    self_qaurantine boolean);
    
create table user_address (
	user_id varchar(20) not null,
    recipent_name varchar(20) not null,
    recipent_number varchar(30) not null,
    delivery_address varchar(40) not null,
    foreign key (user_id) references user (user_id),
    primary key (user_id));
    
create table user_payment (
	user_id varchar(20) not null,
    account_holder varchar(20) not null,
    bank varchar(20) not null,
    bank_account varchar(20) not null,
    foreign key (user_id) references user (user_id),
    primary key (user_id));
    
create table p_category (
	category_id varchar(20),
    name varchar(20),
    description varchar(50),
    primary key (category_id));
    

create table product (
	product_id varchar(20),
    category_id varchar(20),
    name varchar(20) not null,
    description varchar(50),
    price int not null,
    early_delivery boolean,
    soldout boolean,
    foreign key (category_id) references p_category (category_id),
    primary key (product_id)
    
 );
 
 create table p_inventory (
	product_id varchar(20),
    quantity int,
    primary key (product_id),
    foreign key (product_id) references product (product_id));
   
create table order_product (
	order_id varchar(50),
    user_id varchar(20),
    order_date date,
    primary key (order_id, user_id),
    foreign key (user_id) references user (user_id));   

create table shopping_cart (
	cart_id varchar(50),
    user_id varchar(20),
    product_id varchar(20),
    price int,
    quantity int,
    order_id varchar(50),
    primary key (cart_id, user_id, product_id),
    foreign key (user_id) references user (user_id),
    foreign key (product_id) references product (product_id),
    foreign key (order_id) references order_product (order_id));
    
-- insert
desc user;
insert into user values ('xxxx593', '???xx', 'ldfd12@naver.com', '010-5456-9589','123456', 1);
insert into user values ('xx123678', '???cd', 'leyv@gmail.com', '010-1234-5678','5497821', 1);
insert into user values ('xxs2678', '???dec', 'pdd@naver.com', '010-2352-9493','968213', 0);
insert into user values ('xx23478', '???dy', 'ssh@hanmail.net', '010-4851-4518','6789123', 0);

desc user_address;
insert into user_address values ('xxxx593', 'name', '010-1234-5678', '????????? xx????????? 100??? 8202???');
insert into user_address values ('xx123678', 'fded', '010-1234-5678', '??????????????? ?????? 704???');
insert into user_address values ('xxs2678', 'vbfe', '010-2534-5678', '??????????????? ????????? ???????????????');
insert into user_address values ('xx23478', 'ryov', '010-1254-5478', '???????????? ???????????? ????????????');

desc user_payment;
insert into user_payment values ('xxxx593', 'name', 'xx??????', '1213-419218');
insert into user_payment values ('xx123678', 'dfec', 'xx??????', '94158915-323');
insert into user_payment values ('xxs2678', 'mother', 'xx??????', '23-5-4353434');
insert into user_payment values ('xx23478', 'father', 'xx??????', 2353-323343);

desc p_category;
insert into p_category values ('ggsp', '????????????', '????????? ?????? ????????????!');
insert into p_category values ('mpc', '??????/??????/??????', '??? ????????? ???????????? ????????? ??? ?????? ?????? ?????????!');
insert into p_category values ('hdg', '?????????/?????????/??????', '?????? ???????????? ????????? ?????????!');
insert into p_category values ('sssp','????????????','???????????? ?????? ????????? ???????????? ?????? ??? ?????????!');
insert into p_category values ('mkt','?????????', '????????? ???????????? ?????????, ?????? ??? ??????!');

desc product;
insert into product values ('fedfe', 'ggsp','?????????????????? 30???', '????????? ??????????????? ?????? ????????????!', 19800, 1,0);
insert into product values ('fdedc', 'ggsp','??????????????? 30???', '?????? ?????? ?????????! ????????????!', 20500, 0,0);
insert into product values ('aksen', 'mpc','????????? ????????? 1kg', '??????????????? ?????? ????????? ???????????????', 9980, 1,0);
insert into product values ('prdec', 'mpc','????????? ???????????? 384g * 2???', '???????????? ?????? ??? ????????? ???????????????!', 8480, 0,0);
insert into product values ('dfed', 'mpc','????????? ?????????????????? 200g', '???????????? ???????????? ?????? ?????? ??? ?????????!', 3500, 1,0);
insert into product values ('mjm', 'hdg','????????? ?????? ?????? 2???', '????????? ????????? ?????????!', 4680, 1,0);
insert into product values ('made', 'hdg','????????? ??????????????? 346g', '????????? ?????? ????????? ?????? ?????????', 3200, 0,0);
insert into product values ('goph', 'hdg','?????? ?????????????????? ????????? 400g', '????????? ????????? ??????~!', 8480, 1,0);
insert into product values ('smk', 'sssp','??????????????? ?????? 2kg', '???????????? ???????????? ???????????????', 50000, 1,0);
insert into product values ('abkd', 'sssp','???????????? 1kg', '????????? ?????? ?????? ????????????~', 20300, 0,0);
insert into product values ('slm', 'sssp','????????? 10???', '????????? ???????????? ???????????????', 19300, 1,0);
insert into product values ('dgk', 'mkt','[?????????] ??????????????? ?????????', '????????? ?????? ????????? ????????? ????????????!', 23800, 1,0);
insert into product values ('pysab', 'mkt','[?????????] ????????? ????????????', '?????? ????????? ????????? ?????? ????????????!', 34800, 0,0);
insert into product values ('gcsb', 'mkt','[?????????] ????????????????????? ?????????', '???????????? ?????? ??????!', 13680, 1,0);

desc p_inventory;
insert into p_inventory values ('fedfe', 1500);
insert into p_inventory values ('fdedc', 43);
insert into p_inventory values ('aksen', 160);
insert into p_inventory values ('prdec', 50);
insert into p_inventory values ('dfed', 0);
insert into p_inventory values ('mjm', 40);
insert into p_inventory values ('made', 20);
insert into p_inventory values ('goph', 26);
insert into p_inventory values ('smk', 0);
insert into p_inventory values ('abkd', 24);
insert into p_inventory values ('slm', 52);
insert into p_inventory values ('dgk', 22);
insert into p_inventory values ('pysab', 0);
insert into p_inventory values ('gcsb', 40);



insert into order_product values ('1105fedfe', 'lsh9593', '21-11-05');
insert into order_product values ('1105fedfe2', 'ljh5678', '21-11-05');
insert into order_product values ('1105aksen', 'ssh5678', '21-11-01');
insert into order_product values ('1105prdec', 'ssh5678', '21-11-05');
insert into order_product values ('1105prdec2', 'ssh5678', '21-11-01');
insert into order_product values ('1105prdec3', 'ssh5678', '21-11-01');
insert into order_product values ('1105prdec4', 'ssh5678', '21-11-06');
insert into order_product values ('1105prdec5', 'ssh5678', '21-11-01');
insert into order_product values ('1105prdec6', 'ssh5678', '21-11-01');
insert into order_product values ('1105prdec7', 'ssh5678', '21-11-09');
insert into order_product values ('1105prdec8', 'ssh5678', '21-11-07');
insert into order_product values ('1109prdec7', 'pdg5478', '21-11-09');


insert into shopping_cart values ('asd123', 'pdg5478', 'fdedc', '41000', 2, null);
insert into shopping_cart values ('asd125', 'pdg5478', 'aksen', '19960', 2, null);
insert into shopping_cart values ('zxc123', 'ssh5678', 'fdedc', '6325100', 3, null);
insert into shopping_cart values ('zxc124', 'ssh5678', 'fdedc', '20500', 1, '1105aksen');
insert into shopping_cart values ('zxc125', 'ssh5678', 'aksen', '911110', 1, '1105aksen');
insert into shopping_cart values ('zxc126', 'ssh5678', 'prdec', '8480', 1, '1105aksen');
insert into shopping_cart values ('zxc127', 'lsh9593', 'dfed', '3500', 1, '1105aksen');
insert into shopping_cart values ('zxc128', 'pdg5478', 'prdec', '8480', 1, '1109prdec7');


