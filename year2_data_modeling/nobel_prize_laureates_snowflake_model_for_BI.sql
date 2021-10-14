CREATE TABLE "f_nobel_prizes" (
  "year" int,
  "id_category" int,
  "id_laureate" int,
  "counter" int,
  PRIMARY KEY ("year", "id_category", "id_laureate")
);

CREATE TABLE "d_category" (
  "id_category" int PRIMARY KEY,
  "category" varchar
);

CREATE TABLE "d_laureates" (
  "id_laureate" int PRIMARY KEY,
  "id_laureate_type" int,
  "id_sex" int,
  "id_birth_city" int,
  "id_death_city" int,
  "id_organization" int,
  "birth_date" date,
  "death_date" date,
  "full_name" varchar
);

CREATE TABLE "d_organization" (
  "id_organization" int PRIMARY KEY,
  "id_organization_city" int,
  "organization_name" varchar
);

CREATE TABLE "d_laureate_type" (
  "id_laureate_type" int PRIMARY KEY,
  "laureate_type" varchar
);

CREATE TABLE "d_sex" (
  "id_sex" int PRIMARY KEY,
  "sex" varchar
);

CREATE TABLE "d_city" (
  "id_city" int PRIMARY KEY,
  "id_country" int,
  "city_name" varchar,
  "city_population" int,
  "latitude" float,
  "longitude" float
);

CREATE TABLE "d_country" (
  "id_country" int PRIMARY KEY,
  "id_region" int,
  "id_continent" int,
  "country_name" varchar,
  "country_population" int,
  "gdp_usd_per_capita" float
);

CREATE TABLE "d_region" (
  "id_region" int PRIMARY KEY,
  "country_name" varchar,
  "country_population" int
);

CREATE TABLE "d_continent" (
  "id_continent" int PRIMARY KEY,
  "continent_name" varchar
);

CREATE TABLE "d_date" (
  "dt_date" date PRIMARY KEY,
  "year" int,
  "year_month" int,
  "year_quarter" int,
  "year_week" int,
  "week_number" int,
  "day_number" int,
  "month_name" varchar,
  "day_name" varchar
);

ALTER TABLE "f_nobel_prizes" ADD FOREIGN KEY ("id_category") REFERENCES "d_category" ("id_category");

ALTER TABLE "f_nobel_prizes" ADD FOREIGN KEY ("id_laureate") REFERENCES "d_laureates" ("id_laureate");

ALTER TABLE "d_laureates" ADD FOREIGN KEY ("id_laureate_type") REFERENCES "d_laureate_type" ("id_laureate_type");

ALTER TABLE "d_laureates" ADD FOREIGN KEY ("id_sex") REFERENCES "d_sex" ("id_sex");

ALTER TABLE "d_laureates" ADD FOREIGN KEY ("id_birth_city") REFERENCES "d_city" ("id_city");

ALTER TABLE "d_laureates" ADD FOREIGN KEY ("id_death_city") REFERENCES "d_city" ("id_city");

ALTER TABLE "d_laureates" ADD FOREIGN KEY ("id_organization") REFERENCES "d_organization" ("id_organization");

ALTER TABLE "d_laureates" ADD FOREIGN KEY ("birth_date") REFERENCES "d_date" ("dt_date");

ALTER TABLE "d_laureates" ADD FOREIGN KEY ("death_date") REFERENCES "d_date" ("dt_date");

ALTER TABLE "d_organization" ADD FOREIGN KEY ("id_organization_city") REFERENCES "d_city" ("id_city");

ALTER TABLE "d_city" ADD FOREIGN KEY ("id_country") REFERENCES "d_country" ("id_country");

ALTER TABLE "d_country" ADD FOREIGN KEY ("id_region") REFERENCES "d_region" ("id_region");

ALTER TABLE "d_country" ADD FOREIGN KEY ("id_continent") REFERENCES "d_continent" ("id_continent");

