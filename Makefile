compile:
	prototool compile

mac_install:
	brew install prototool

linux_install:
	curl -sSL \
      https://github.com/uber/prototool/releases/download/v1.8.0/prototool-$(uname -s)-$(uname -m) \
      -o /usr/local/bin/prototool && \
			ls -al && \
			ls -al /usr/local/bin && \
			ls -al /usr/local/bin | grep prototool && \
      chmod +x /usr/local/bin/prototool && \
			ls -al /usr/local/bin | grep prototool && \
			/usr/local/bin/prototool

gen:
	prototool generate


.PHONY: compile install gen
