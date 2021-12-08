/*
// creating table marks
create table marks(roll_no integer,name
varchar2(20),total_marks varchar2(20));
*/

/*
select 
 ROLL_NO,
 NAME,
 TOTAL_MARKS
 from MARKS
 */
 
 /*
 
// creating table result
 create table result(roll_no integer,name varchar2(20),class
varchar2(20));

*/

1-->
/*
insert into marks values(1,"Sumeet",1350);
insert into marks values(2,"Ravi",980);
insert into marks values(3,"Amit",890);
insert into marks values(4,"Ajay",740);
insert into marks values(5,"Rahul",900);
insert into marks values(6,"Sneha",965);
insert into marks values(7,"Savita",1400);
insert into marks values(8,"Dulquer",500);
insert into marks values(9,"Sagar",910);
insert into marks values(10,"Arjun",815);
*/
2--->
/*

begin
insert into marks values(1,'Ankit',1350);
insert into marks values(6,'Arya',965);
insert into marks values(2,'Ravi',980);
insert into marks values(3,'Amit',890);
insert into marks values(10,'Amtul',815);
insert into marks values(4,'Ajay',740);
insert into marks values(5,'Rahul',900);
insert into marks values(7,'Savita',1400);
insert into marks values(8,'Sumeet',500);
insert into marks values(9,'Shikha',910);
end;

*/


1-->
/*
delimiter //
create procedure proc_result1(in marks int,out class char(20))
begin
if(marks<=1500 && marks>=990)
then
set class='Distinction';
end if;
if(marks<=989 && marks>=890)
then
set class='First Class';
end if;
if(marks<=889 && marks>=825)
then
set class='Higher Second Class';
end if;
if(marks<=824 && marks>=750)
then
set class='Second Class';
end if;
if(marks<=749 && marks>=650)
then
set class='Passed';
end if;
if(marks<=649)
then
set class='Fail';
end if;
end;
//


*/

2--->
/*
create or replace function proc_result2 ( grade integer) return varchar2 is
designation varchar2(20) ;
begin
if(grade <=1500 and grade>=990) then
designation := 'Distinction';
end if;
if(grade<=989 and grade>=890) then 
designation := 'First Class';
end if;
if(grade<=889 and grade>=825) then
designation := 'Higher Second Class';
end if;
if(grade<=824 and grade>=750) then
designation := 'Second Class';
end if;
if(grade<=749 and grade>=650) then
designation := 'Passed';
end if;
if(grade<=649) then
designation := 'Fail';
end if;
return designation;
end;


*/

1--->
/*
delimiter //
create function final_result5(R1 int)returns int deterministic
begin
declare fmarks integer;
declare grade varchar(20);
declare stud_name varchar(20);
select marks.total_marks,marks.name into fmarks,stud_name from marks
where marks.roll_no=R1;
call proc_result1(fmarks,@grade);
insert into result values(R1,stud_name,@grade);
return R1;
end;
//
*/

2--->
/*
create or replace function final_result1(R1 integer) return integer  is
fmarks integer;
grade varchar2(20);
stud_name varchar2(20);
begin
select total_marks,name into fmarks,stud_name from marks
where marks.roll_no = R1;
grade := proc_result2(fmarks);
insert into result values(R1,stud_name, grade);
return R1;
end;
*/

/*
DECLARE 
   x number := 3;
   temp integer; 
BEGIN 
   LOOP
    temp := final_result1(x);
    x := x + 1; 
    exit WHEN x > 10; 
   END LOOP; 
END;

*/


