alter table inventory_part
add foreign key (part_num) references part(part_num);