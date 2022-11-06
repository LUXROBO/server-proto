# luxrobo GRPC 서비스 protobuf 정의 
 
## Install for compile proto
https://github.com/uber/prototool#installation
mac : brew install prototool

```

# lint execute
prototool lint 
# proto compile then golang, python generated file
prototool compile
# gernerate proto
prototool generate 
cd gen

```

## Deploy CI/CD 
gitlab CI/CD로 자동화 배포되며 protobuf_build master로 빌드되어 프로젝트 업데이트 됩니다. 
