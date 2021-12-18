build:
	@docker build -t fdl-mc/api/servers_stats .
deploy:
	@docker-compose up -d
