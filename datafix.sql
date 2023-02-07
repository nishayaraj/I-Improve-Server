ALTER TABLE iimproveapi_goal
DROP COLUMN tag;

DELETE FROM iimproveapi_user WHERE uid='3TPIXql2WBaHWEBXxI9obJsvEcs1';

ALTER TABLE iimproveapi_tag
ADD user_id;
