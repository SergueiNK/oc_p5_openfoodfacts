SET NAMES utf8;

CREATE DATABASE purbeurre

USE purbeurre;

CREATE TABLE [IF NOT EXISTS] Food(
        id INT UNSIGNED AUTO_INCREMENT,
        generic_name_fr VARCHAR(250),
        product_name_fr_imported VARCHAR(250),
        ingredients_text_with_allergens_fr TEXT,
        code INT UNSIGNED,
        url VARCHAR(250),
        nutrition_grade_fr VARCHAR(5),
        PRIMARY KEY (id)
)ENGINE=INNODB;

CREATE TABLE [IF NOT EXISTS] Category(
        id INT UNSIGNED AUTO_INCREMENT,
        categories VARCHAR(250),
        code INT UNSIGNED,
        PRIMARY KEY (id)
)ENGINE=INNODB;

CREATE TABLE [IF NOT EXISTS] Place_to_buy(
        id INT UNSIGNED AUTO_INCREMENT,
        stores VARCHAR (250),
        code INT UNSIGNED,
        PRIMARY KEY (id)
)ENGINE=INNODB;

CREATE TABLE [IF NOT EXISTS] Favorites(
        id INT UNSIGNED AUTO_INCREMENT,
        generic_name_fr VARCHAR(250),
        product_name_fr_imported VARCHAR(250),
        ingredients_text_with_allergens_fr TEXT,
        code INT UNSIGNED,
        url VARCHAR(250),
        nutrition_grade_fr VARCHAR(5),
        PRIMARY KEY (id)
)ENGINE=INNODB;

ALTER TABLE Category ADD CONSTRAINT fk_code FOREIGN KEY (code) REFERENCES Category(code) # à vérifier

