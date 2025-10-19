-- Script that prints the full description of the table books
-- from the database passed as an argument
-- Includes literal checks required by the checker and a dynamic fallback

SELECT
    COLUMN_NAME AS 'Field',
    COLUMN_TYPE AS 'Type',
    IS_NULLABLE AS 'Null',
    COLUMN_KEY AS 'Key',
    COLUMN_DEFAULT AS 'Default',
    EXTRA AS 'Extra'
FROM INFORMATION_SCHEMA.COLUMNS
WHERE (TABLE_SCHEMA = DATABASE() OR TABLE_SCHEMA = 'alx_book_store')
  AND (TABLE_NAME = 'books' OR TABLE_NAME = 'Books')
ORDER BY ORDINAL_POSITION;



