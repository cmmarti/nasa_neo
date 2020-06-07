TAG=nasa_neo

build:
	podman build -t $(TAG) .

run:
	podman run --rm -v $(PWD):/app:z -p 8000:8000 --name $(TAG) --env-file=$(PWD)/.env $(TAG)
	podman logs -f $(TAG)

stop:
	podman stop $(TAG)
