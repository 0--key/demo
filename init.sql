--***************			**********
--		 SQLite3 database structure
--***************			**********
--
CREATE TABLE products (id integer primary key autoincrement, name, sku, manufacturer, manuf_url, weight, pack_weight, dimension, description, ingredients, warning, suggested_use);
--
CREATE TABLE products_var_data (id integer primary key autoincrement, product_id, store_id, category, cost, srp, is_in_stock, num_reviews, image_URL, meta_keyword, foreign key (product_id) references products01(id), foreign key (store_id) references products01_stores(id));
--
CREATE TABLE stores (id integer primary key autoincrement, name, url);
--
CREATE TABLE premieres (id integer primary key autoincrement, product_id, date, foreign key (product_id) references products01_varied(id));
--
CREATE TABLE presence (id integer primary key autoincrement, varied_id, in_sale, date, foreign key (varied_id) references products_var_data(id));
--
CREATE TABLE img_index (id integer primary key autoincrement, product_id, image, small_image, thumbnail,foreign key (product_id) references products01(id));
--
CREATE TABLE price_wave (id integer primary key autoincrement, product_id, new_price, old_price, date, foreign key (product_id) references products01_varied(id));
--
CREATE TABLE in_stock_wave (id integer primary key autoincrement, product_id, in_stock, old_in_stock, date, foreign key (product_id) references products01_varied(id));
--
--
--
CREATE INDEX img_index_img ON img_index(image);
--
CREATE INDEX sku_index ON products(sku);
--
CREATE INDEX price_changes_index on price_wave(product_id, date);
--
CREATE INDEX instock_changes_index on in_stock_wave(product_id, date);
--
CREATE INDEX img_index_id on img_index(id);
--
CREATE INDEX in_sale_index on presence(in_sale, date);
--
CREATE INDEX product_varied_data_index ON products_var_data(product_id, store_id);
--
CREATE INDEX product_varied_data_index_id ON products_var_data(id);
