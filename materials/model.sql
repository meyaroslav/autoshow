create table users (
    id serial primary key,
    login varchar(50) not null unique,
    password varchar(255) not null,
    role varchar(25) not null
);

insert into users values (1, 'admin', 'admin', 'admin');
insert into users values (2, 'manager', 'manager', 'manager');
insert into users values (3, 'viewer', 'viewer', 'viewer');

create table clients (
    id serial primary key,
    full_name varchar(255) not null,
    phone varchar(255),
    email varchar(255)
);

insert into clients values (1, 'Ильин Ярослав Станиславович', '+79161234567', 'yaroslav@example.com');
insert into clients values (2, 'Павлов Ян Владимирович', '+79261234567', 'yan@example.com');
insert into clients values (3, 'Латышев Андрей Сергеевич', '+79371234567', 'andrey@example.com');

create table brands (
    id serial primary key,
    name varchar(255) not null unique
);

insert into brands values (1, 'Toyota');
insert into brands values (2, 'BMW');
insert into brands values (3, 'Ford');
insert into brands values (4, 'Audi');
insert into brands values (5, 'Mercedes-Benz');
insert into brands values (6, 'Volkswagen');

create table models (
    id serial primary key,
    name varchar(255) not null unique,
    brand_id int not null references brands(id) on delete cascade
);

insert into models values (1, 'Camry', 1);
insert into models values (2, 'X5', 2);
insert into models values (3, 'Focus', 3);
insert into models values (4, 'A3', 4);
insert into models values (5, 'A4', 4);
insert into models values (6, 'A6', 4);
insert into models values (7, 'C-Class', 5);
insert into models values (8, 'E-Class', 5);
insert into models values (9, 'S-Class', 5);
insert into models values (10, 'Polo', 6);
insert into models values (11, 'Jetta', 6);
insert into models values (12, 'Tiguan', 6);

create table colors (
    id serial primary key,
    name varchar(255) not null unique
);

insert into colors values (1, 'Чёрный');
insert into colors values (2, 'Белый');
insert into colors values (3, 'Красный');

create table transmissions (
    id serial primary key,
    name varchar(255) not null unique
);

insert into transmissions values (1, 'Механическая');
insert into transmissions values (2, 'Автоматическая');

create table status (
    id serial primary key,
    name varchar(255) not null unique
);

insert into status values (1, 'В наличии');
insert into status values (2, 'Продан');
insert into status values (3, 'Зарезервирован');

create table cars (
    id serial primary key,
    vin varchar(17) not null unique,
    brand_id int not null references brands(id) on delete cascade,
    model_id int not null references models(id) on delete cascade,
    color_id int not null references colors(id) on delete cascade,
    transmission_id int not null references transmissions(id) on delete cascade,
    year int not null,
    mileage int not null,
    price numeric(12, 2) not null,
    status_id int not null references status(id) on delete cascade
);

insert into cars values (1, 'JTNBB46K083012345', 1, 1, 1, 2, 2022, 15000, 2000000.00, 1);
insert into cars values (2, 'WBAXY01020F123456', 2, 2, 2, 2, 2023, 5000, 4500000.00, 1);
insert into cars values (3, 'WF0GXXGBBGHE12345', 3, 3, 3, 1, 2021, 30000, 1500000.00, 3);

create table sales (
    id serial primary key,
    car_id int not null references cars(id) on delete cascade,
    client_id int not null references clients(id) on delete cascade,
    date date not null,
    price numeric(12, 2) not null
);

insert into sales values (1, 1, 1, '2025-03-20', 1950000.00);
insert into sales values (2, 2, 2, '2025-04-01', 4400000.00);
insert into sales values (3, 3, 3, '2025-04-15', 1450000.00);