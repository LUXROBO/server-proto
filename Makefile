compile:
	prototool compile

mac_install:
	brew install prototool

linux_install:
	curl -sSL \
      https://github.com/uber/prototool/releases/download/v1.10.0/prototool-Linux-x86_64 \
      -o /usr/local/bin/prototool && \
      chmod +x /usr/local/bin/prototool

gen:
	prototool generate


.PHONY: compile install gen
