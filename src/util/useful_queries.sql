SELECT * FROM mydb.fee where account_id = 1005890;

SELECT b.fee_type, count(*)
FROM mydb.fee a
join mydb.account b on (a.account_id = b.id)
GROUP BY b.fee_type
