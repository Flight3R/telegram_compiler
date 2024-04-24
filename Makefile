build:
	docker build -t telegram_compiler_image:$(shell ./increment_version.sh) .

tag:
	docker tag telegram_compiler_image:$(shell cat version) 192.168.0.2:5000/telegram_compiler_image:$(shell cat version)

push:
	docker push 192.168.0.2:5000/telegram_compiler_image:$(shell cat version)

update:
	sed -i -r "s/telegram_compiler_image:[0-9]+\.[0-9]+\.[0-9]+/telegram_compiler_image:$(shell cat version)/g" telegram_compiler_deployment.yaml

run:
	docker run -d -p 60005:8000 --name telegram_compiler_container telegram_compiler_image:$(shell cat version)

commit:
	git add .
	git commit -m "deployment $(shell cat version)"

prod:
	$(MAKE) build tag push update commit
