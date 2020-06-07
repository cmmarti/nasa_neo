
build:
	podman build -t nasa_neo .

run:
	podman run --rm -v $(PWD):/app:z -p 8000:8000 --name nasa_neo -d nasa_neo

stop:
	podman stop nasa_neo
