-- Write your query below
select seller.seller_name
from seller
where seller_id not in (
    select seller.seller_id 
    from seller join orders
    on seller.seller_id = orders.seller_id
    where extract(year from orders.sale_date) = 2020
)
order by seller.seller_name ASC;