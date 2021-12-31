
CREATE TABLE test_table ( A VARCHAR2(26),  B NUMBER(38));
create table test_table (A varchar(26), B number(38) );
INSERT INTO test_table (A, B) VALUES ('a',1);
INSERT INTO test_table (A, B) VALUES ('b',2);
INSERT INTO test_table (A, B) VALUES ('c',3);

drop table test_table;

