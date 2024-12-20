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
  min_side_dish INT,
  max_side_dish INT,
  description VARCHAR(255) NULL
);

CREATE TABLE IF NOT EXISTS side_dish (
  side_dish_id VARCHAR(255),
  name VARCHAR(255),
  extra_price FLOAT,
  description VARCHAR(255) NULL,
  product_id VARCHAR(255) NULL
);

CREATE TABLE IF NOT EXISTS order_item_side_dish (
  order_item_id VARCHAR(255),
  side_dish_id VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS order_item (
  order_item_id VARCHAR(255),
  order_id VARCHAR(255),
  product_id VARCHAR(255),
  quantity INT,
  total_price FLOAT
);

CREATE TABLE IF NOT EXISTS order (
  order_id VARCHAR(255),
  user_id VARCHAR(255),
  customer_id VARCHAR(255),
  delivery_date TIMESTAMP,
  delivery_address VARCHAR(255),
  is_paid BOOLEAN,
  total_price FLOAT,
  status VARCHAR(255),
);
