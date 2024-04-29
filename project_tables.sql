drop table if exists order_items;
drop table if exists menu_items;
drop table if exists any_order;
drop table if exists reservation;
drop table if exists customers;

create table customers (
    -- for a variety of reasons, we changed the primary key to PhoneNumber.
    name varchar(20) not null,
    email varchar(50),
    PhoneNumber varchar(10) not null primary key,
    address varchar(50),
    dob date DEFAULT '2100-01-01',
    membership boolean DEFAULT false
);

create table reservation (
    reservationID int not null auto_increment primary key,
    PhoneNumber varchar(10),
    reservationDateTime datetime,
    size int,
    tableNumber int,
    specialRequests varchar(100),

    foreign key(PhoneNumber) references customers(PhoneNumber)
    -- default settings for reacting to changes.
);

create table any_order (
    orderID int not null auto_increment primary key,
    reservationID int,
    PhoneNumber varchar(10),
    totalBill decimal(10,2),
    server varchar(20),

    foreign key(reservationID) references reservation(reservationID),
    foreign key(PhoneNumber) references customers(PhoneNumber),
    -- default settings for reacting to changes.

    check (reservationID is not null or PhoneNumber is not null),
    check (reservationID is null or PhoneNumber is null)
    -- these constraints ensure that each order is associated with
    -- either a reservation or a customer, and not (directly) with both.
);

create table menu_items (
    itemID int not null auto_increment primary key,
    itemName varchar(20) UNIQUE,
    description varchar(500),
    price decimal(10,2),
    category varchar(20)
);

create table order_items (
    orderID int,
    itemID int, 
    quantity int, 
    primary key(orderID, itemID),
    foreign key(orderID) references any_order(orderID),
    foreign key(itemID) references menu_items(itemID)
    -- default settings for reacting to changes.
);

-- Populate tables:

INSERT INTO customers (name, email, PhoneNumber, address, dob, membership)
VALUES
    ('George Washington', 'gwashington@mountvernon.org', '7035551776', 'Mount Vernon', '1732-02-22', true),
    ('John Adams', 'jadams@quincy.org', '6175551797', 'The Old House, Quincy', '1735-10-30', false),
    ('Thomas Jefferson', 'tjefferson@monticello.org', '4345551809', 'Monticello, Charlottesville', '1743-04-13', true),
    ('James Madison', 'jmadison@montpelier.org', '5405551751', 'Montpelier, Orange', '1751-03-16', true),
    ('Alexander Hamilton', 'ahamilton@theconst.org', '2125551789', 'Hamilton Grange, NYC', '1755-01-11', true),
    ('Abigail Adams', 'aadams@boston.org', '6175551764', 'Peacefield, Braintree', '1744-11-22', true);

INSERT INTO reservation (PhoneNumber, reservationDateTime, size, tableNumber, specialRequests)
VALUES
    ('7035551776', '2024-04-12 18:00:00', 4, 1, ''),
    ('2125551789', '2024-04-15 19:30:00', 2, 2, 'Please ensure the table is as sturdy as the Constitution'),
    ('4345551809', '2024-04-18 20:00:00', 6, 3, 'Birthday celebration, bringing own cake'),
    ('6175551764', '2024-04-19 18:30:00', 3, 4, 'Need a table with enough room for Bill of Rights'),
    ('2125551789', '2024-04-20 19:00:00', 5, 5, ''),
    ('2125551789', '2024-04-21 17:00:00', 2, 6, 'Quiet table for two, where we can ponder the preamble');

INSERT INTO any_order (reservationID, PhoneNumber, totalBill, server)
VALUES
    (1, NULL, 19.44, 'Alice'),
    (NULL, '7035551776', 14.04, 'Bob'),
    (3, NULL, 17.28, 'Charlie'),
    (2, NULL, 00.00, 'Edward'),
    (2, NULL, 00.00, 'Edward'),
    (NULL, '2125551789', 00.00, 'Fiona');

INSERT INTO menu_items (itemName, description, price, category)
VALUES
    ('Hamburger', 'Classic beef burger with lettuce, tomato, and pickles', 9.99, 'Main'),
    ('Caesar Salad', 'Fresh romaine lettuce with Caesar dressing and croutons', 7.99, 'Salad'),
    ('Spaghetti Carbonara', 'Pasta with creamy sauce, bacon, and Parmesan cheese', 12.99, 'Pasta'),
    ('Cheesecake', 'New York-style cheesecake with strawberry topping', 5.99, 'Dessert'),
    ('Constitution Cooler', 'Refreshing blend of lemonade and parchment', 6.49, 'Drink'),
    ('Freedom Fizz', 'A patriotic mix of vodka, cranberry juice, and soda', 8.49, 'Drink');

INSERT INTO order_items (orderID, itemID, quantity)
VALUES
    (1, 1, 1),
    (1, 2, 1),
    (2, 3, 1),
    (3, 1, 1),
    (3, 4, 1),
    (4, 5, 1),
    (5, 6, 1),
    (6, 1, 1);

