discover:
	tap-mysql --config config/mysql_config.json --discover
gen_properties:
	tap-mysql --config config/mysql_config.json --discover > properties/mysql_properties.json
backup:
	tap-mysql --config config/mysql_config.json --properties properties/mysql_properties.json > src/spec_exploration/state.json
