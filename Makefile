compile:
	prototool compile

install:
	go get -u github.com/golang/protobuf/protoc-gen-go
	brew install prototool

gen:
	prototool generate


.PHONY: compile install gen
