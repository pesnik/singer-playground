# WAREHOUSE
build:
	docker build -t singer-etl .
run:
	docker run --rm -it -v "$$(pwd):/app" singer-etl
dwh:
	docker run --name alpine-datawarehouse -p 54321:5432 -e POSTGRES_PASSWORD=hackmeifyoucan -d postgres:15-alpine3.20

# TAP-MYSQL
discover:
	tap-mysql --config config/mysql_config.json --discover
gen_properties:
	tap-mysql --config config/mysql_config.json --discover > properties/mysql_properties.json
sync:
	tap-mysql --config config/mysql_config.json --properties properties/mysql_properties.json
state:
	tap-mysql --config config/mysql_config.json --properties properties/mysql_properties.json | grep STATE | tail -n 1 > state.json
backup:
	tap-mysql --config config/mysql_config.json --properties properties/mysql_properties.json > src/spec_exploration/state.json

# ETL
etl:
	tap-mysql --config config/mysql_config.json --properties properties/mysql_properties.json --state state.json | target-postgres --config config/postgres_config.json

