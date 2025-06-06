.PHONY: default docker-build kind-load

CLUSTER_NAME ?= kind
IMAGE_PREFIX ?= drasi-project
DOCKER_TAG_VERSION ?= latest
DOCKERX_OPTS ?= --load --cache-to type=inline

default: docker-build

docker-build:
	docker buildx build ../../.. -f ./Dockerfile -t $(IMAGE_PREFIX)/source-change-dispatcher:$(DOCKER_TAG_VERSION) $(DOCKERX_OPTS)

docker-build-debug:
	docker buildx build ../../.. -f ./Dockerfile.debug -t $(IMAGE_PREFIX)/source-change-dispatcher:$(DOCKER_TAG_VERSION) $(DOCKERX_OPTS)

kind-load:
	kind load docker-image $(IMAGE_PREFIX)/source-change-dispatcher:$(DOCKER_TAG_VERSION) --name $(CLUSTER_NAME)

k3d-load: CLUSTER_NAME=k3s-default
k3d-load:
	k3d image import $(IMAGE_PREFIX)/source-change-dispatcher:$(DOCKER_TAG_VERSION) -c $(CLUSTER_NAME)

test:
	@echo "No tests to run yet"

lint-check:
	cargo fmt -- --check
	cargo clippy --all-targets --all-features -- -D warnings -W clippy::print_stdout -A unused -A clippy::module_inception -A clippy::ptr_arg -A clippy::type_complexity