--Aquellas usadas para insertar, modificar y eliminar un Customer, Staff y Actor
--(Customer)
insert into public.customer(
	customer_id, 
	store_id, 
	first_name, 
	last_name, 
	email, 
	address_id, 
	activebool, 
	create_date, 
	last_update, 
	active)
values ('600','2','Juanito','Perez','j.perez@sakilacustomer.org','30','v','2006-02-14','','1');

update public.customer 
set customer_id=600, 
	store_id=2, 
	firs_name='Juanito',	
	last_name='Perez', 
	email='j.perez@sakilacustomer.org', 
	adress_id=30, 
	activebool='v', 
	create_date='2006-02-14',	
	last_update='now', 
	active='1'
where <condition >;

delete from public.customer 
where <condition>;

--(Staff)
insert into public.staff (
	staff_id,
	store_id,
	first_name,
	last_name,
	email,
	address_id,
	username,
	password,
	last_update,
	picture)
values ('3','2','Anacleto','Dinosaurious','anacleto@sakilastaff.org','6','AnaDi','123455','now','null');

update public.staff  
set staff_id=3, 
	store_id=2, 
	firs_name='Anacleto', 
	last_name='Dinosaurious', 
	email='anacleto@sakilastaff.org', 
	adress_id='6',
	username='Anadi',
	password=123455,
	last_update='now',
	picture='null'
where <condition >;

delete from public.staff  
where <condition>;

--(Actor)
insert into public.actor (
	actor_id,
	first_name,
	last_name,
	last_update)
values ('2','Leonardo','Dicaprio','now');

update public.actor 
set actor_id=2,
	first_name='Leonardo',
	last_name='Dicaprio',
	last_update=now() 
where <condition>;

delete from public.actor 
where <condition >;


--Listar todas las “rental” con los datos del “customer” dado un año y mes
select rental.rental_id, 
	rental.rental_date,  
	customer.customer_id, 
	customer.first_name, 
	customer.last_name,
	customer.store_id,
	customer.address_id,
	customer.email 
from rental r 
join customer c on rental.costumer_id = customer.customer_id
where year (rental.rental_date) = 2006
  and month(rental.rental_date) = 12;

--Listar Número, Fecha (payment_date) y Total (amount) de todas las “payment”.
SELECT payment.payment_date, SUM(payment.amount) AS total_amount
FROM payment
GROUP BY payment.payment_date;

 
--Listar todas las “film” del año 2006 que contengan un (rental_rate) mayor a 4.0.
SELECT film.title, film.rental_rate
FROM film
WHERE YEAR(film.release_year) = 2006
  AND film.rental_rate > 4.0;



--Realiza un Diccionario de datos que contenga el nombre de las tablas y columnas, si éstas pueden ser nulas, y su tipo de dato correspondiente
SELECT
 t1.TABLE_NAME AS tabla_nombre,
 t1.COLUMN_NAME AS columna_nombre,
 t1.COLUMN_DEFAULT AS columna_defecto,
 t1.IS_NULLABLE AS columna_nulo,
 t1.DATA_TYPE AS columna_tipo_dato,
 COALESCE(t1.NUMERIC_PRECISION,
 t1.CHARACTER_MAXIMUM_LENGTH) AS columna_longitud,
 PG_CATALOG.COL_DESCRIPTION(t2.OID,
 t1.DTD_IDENTIFIER::int) AS columna_descripcion,
 t1.DOMAIN_NAME AS columna_dominio
FROM
 INFORMATION_SCHEMA.COLUMNS t1
 INNER JOIN PG_CLASS t2 ON (t2.RELNAME = t1.TABLE_NAME)
WHERE
 t1.TABLE_SCHEMA = 'public'
ORDER BY
 t1.TABLE_NAME;


