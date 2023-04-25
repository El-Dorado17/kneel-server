CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    `timestamp` CURRENT_TIMESTAMP not null,
    FOREIGN KEY (`metal_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY (`size_id`) REFERENCES `Sizes`(`id`),
    FOREIGN KEY (`style_id`) REFERENCES `Styles`(`id`)
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NUMERIC(5,2) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);







INSERT INTO `Metals` VALUES (null, 'Sterling Silver', 12.42);
INSERT INTO `Metals` VALUES (null, '14K Gold', 736.40);
INSERT INTO `Metals` VALUES (null, '24K Gold', 1258.9);
INSERT INTO `Metals` VALUES (null, 'Platinum', 795.45);
INSERT INTO `Metals` VALUES (null, 'Palladium', 1241.0);

INSERT INTO `Orders` VALUES (null, 5, 5, 3, 20230402);
INSERT INTO `Orders` VALUES (null, 1, 1, 1, 20230314);
INSERT INTO `Orders` VALUES (null, 1, 1, 1, 20230101);
INSERT INTO `Orders` VALUES (null, 1, 1, 1, 20230805);
INSERT INTO `Orders` VALUES (null, 1, 1, 1, 20230704);
INSERT INTO `Orders` VALUES (null, 1, 1, 1, 20230107);
INSERT INTO `Orders` VALUES (null, 1, 1, 1, 20230131);
INSERT INTO `Orders` VALUES (null, 1, 1, 1, 20221225);

INSERT INTO `Sizes` VALUES (null, 0.5, 405);
INSERT INTO `Sizes` VALUES (null, 0.75, 782);
INSERT INTO `Sizes` VALUES (null, 1, 1470);
INSERT INTO `Sizes` VALUES (null, 1.5, 1997);
INSERT INTO `Sizes` VALUES (null, 2, 3638);


INSERT INTO `Styles` VALUES (null, "Classic", 500);
INSERT INTO `Styles` VALUES (null, "Modern", 710);
INSERT INTO `Styles` VALUES (null, "Vintage", 965);

