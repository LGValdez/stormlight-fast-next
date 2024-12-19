CREATE TABLE IF NOT EXISTS customer (
  customer_id VARCHAR(255),
  name VARCHAR(255),
  address VARCHAR(255) NULL,
  note VARCHAR(255) NULL
);

CREATE TABLE IF NOT EXISTS product (
  product_id VARCHAR(255),
  name VARCHAR(255),
  price FLOAT,
  description VARCHAR(255) NULL
);

CREATE TABLE IF NOT EXISTS side_dish (
  side_dish_id VARCHAR(255),
  name VARCHAR(255),
  extra_price FLOAT,
  description VARCHAR(255) NULL,
  product_id VARCHAR(255) NULL
);
