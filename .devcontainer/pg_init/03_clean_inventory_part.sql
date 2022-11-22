delete from inventory_part ip
where not exists (select * from part p where ip.part_num = p.part_num);
