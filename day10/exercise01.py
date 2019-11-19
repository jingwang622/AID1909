"""
练习：
1.创建数据库books
2.在数据库中创建表book结构如下
id   title   author price publication comment
int  varchar(10) varchar
3.插入若干数据
price        30-80
publication  中国教育 机械工业 人民教育 中国文学
作者

4.查找所有40多元的图书
select * from book where price between 40 and 49.9;
查找鲁迅写的机械工业出版设的图书
select * from book where author = '老师' and publication = '机械工业';
超找备注不为空的图书
select * from book where comment is not null;
查找价格大于60的图书，只看署名和价格
select title,price from book where price > 60;
查找老舍或者出版社是中国文学的图书
select * from book where author='老舍' or publication = '中国文学';
"""



"""
1,将骆驼祥子的价格改为45
update book set price = 45 where title = '水壶';
2.增加一个字段出版日期，类型为date 放在出版社字段后面
alter table book add publication_time date after publication;
3.修改鲁迅写的图书出版日期2000-10-1
update book set publication = '2000-10-1' where author = '老舍';
4.其他图书出版日期均为2005-1-1
update book set publication = '2005-1-1' where not '老舍';
5.删除价格在60元以上或者49元以下的图书
delete from book where price > 60 or price < 49;


练习：
1.创建表：sanguo
2.id name gender(性别) country(魏蜀吴三选一) attack(攻击)>100 
defense(防御力) 0-100
3.插入若干数据
魏：  司马懿  夏侯渊 张辽 甄姬
蜀：  诸葛亮  孙尚香 张飞 赵云 黄忠
吴：  周瑜 陆逊 小乔 大乔
4.综合练习：
查找所有蜀国人信息
select * from sanguo where country = "蜀";
将赵云攻击力设置为360 防御力68
update sanguo set attack = 360,defense = 68 where name = '赵云';
将吴国英雄攻击力超过300的改为300,防御改为60
update sanguo set attack = 300,defense = 60 where country = '吴' and attack>300;
查找攻击高于250的英雄名字和攻击力
select name,attack from sanguo where attack > 250;
将所有英雄按照攻击力排名，攻击力如果相同按照防御排名（降序）
select * from sanguo order by attack desc,defense desc;
查找魏蜀两国名字为三个字的英雄，防御按照升序排序，
select * from (select * from sanguo where name like "___" and country in ('魏','蜀')) as a order by a.defense desc;
找到吴国攻击力前2名的英雄且性别不为null
select * from sanguo where country='吴' and gender is not null order by atta limit 2
找到蜀国中攻击力比魏国中攻击力最大的英雄还强大的所有英雄
select * from sanguo where attack >(select attack from sanguo where country = '魏' order by attack desc limit 1)
and country = '蜀'

"""

"""
查看报兴趣办的同学他们的姓名和兴趣
select i.name,i.hobby from interest as i;
获取班级所有同学的姓名，并且查看那些同学包了兴趣办，兴趣办是什么
select class1.name,interest.hobby from class1 left join interest on class1.name = interest.name;
查看所有兴趣办类型和价格，并且看一下那些同学包了名
select interest.level,interest.price,class1.name from class1 right join interest on class1.name = interest.name;
"""


