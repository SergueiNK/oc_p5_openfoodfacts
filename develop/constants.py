create_tables_cmd = [
"CREATE TABLE  Products(id INT UNSIGNED AUTO_INCREMENT, generic_name_fr VARCHAR(250), product_name_fr_imported VARCHAR(250), ingredients_text_with_allergens_fr TEXT, code VARCHAR(50), url VARCHAR(250), nutrition_grade_fr VARCHAR(5), PRIMARY KEY (id) )ENGINE=INNODB;",
"CREATE TABLE  Categories(id INT UNSIGNED AUTO_INCREMENT, categories VARCHAR(250), code VARCHAR(50), PRIMARY KEY (id))ENGINE=INNODB;",
"CREATE TABLE  Places_to_buy(id INT UNSIGNED AUTO_INCREMENT, stores VARCHAR (250), code VARCHAR(50), PRIMARY KEY (id))ENGINE=INNODB;",
"CREATE TABLE  Favorites(id INT UNSIGNED AUTO_INCREMENT, generic_name_fr VARCHAR(250), product_name_fr_imported VARCHAR(250), ingredients_text_with_allergens_fr TEXT, code VARCHAR(50), url VARCHAR(250), nutrition_grade_fr VARCHAR(5), PRIMARY KEY (id))ENGINE=INNODB;",
"ALTER TABLE Categories ADD CONSTRAINT fk_code FOREIGN KEY (id) REFERENCES Products(id)"]