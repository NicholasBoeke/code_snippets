-- update pwd;   double quote is necessary, no single quote
alter user                -- username with no quotes
identified by ""           --"new_pwd" 
replace ""                 --"old_pwd"
;


-- see when password expires for logged in user (expiry_date), account status, etc.
select * from user_users;


-- see if password set to expire or unlimited, grace period, login attempts, etc. for logged in user
select * from user_password_limits;


-- see what other static views are available to logged in USER
select * from all_views where view_name like '%USER%' order by view_name;


-- see what SQL is used to create a View (TEXT field is actually TEXT_VC)
select text_vc from all_views where view_name = '[view_name]';


-- see Oracle versions
-- [major].[maint].[appserver].[component].[platform/patch]
COL PRODUCT FORMAT A35
COL VERSION FORMAT A15
COL STATUS FORMAT A15 
SELECT * FROM PRODUCT_COMPONENT_VERSION;


-- see database links available to this user
select * 
from all_db_links
order by host, db_link;


-- see how much space is free in USERS table space
select u.*, u.bytes/1024/1024 as mb from user_free_space u;
select * from user_tablespaces order by tablespace_name;


-- get oracle instant client version
SELECT
  DISTINCT
  s.client_version
FROM
  v$session_connect_info s
WHERE
  s.sid = SYS_CONTEXT('USERENV', 'SID');
  

-- query oracle processes running
select s.sid, s.serial#, p.spid, s.username, s.schemaname, s.program, s.terminal, s.osuser
  from v$session s
  join v$process p
    on s.paddr = p.addr
 where s.type != 'BACKGROUND'
 and s.username = ''    -- username
;


-- see what privileges this user has
select * from all_views
where view_name like '%PRIV%'
order by view_name;



-- =========== work with database links ===========
-- create the link (need create db link capability)
create database link [DBLINK]                                 -- private link will supercede public link
connect to [USER] identified by "pwd here in double quotes"     -- use USER on remote DW
using '[host]:[port]/[service]';                                -- connection string to DW


-- update database link if it alreay exists
alter database link [DBLINK]
connect to [USER] identified by "new pwd here in  double quotes";   -- new password

-- verify private link was created & that THIS schema owns it
select * from all_db_links;

-- drop private link if needed 
drop database link [DBLINK];

-- =======================================================



