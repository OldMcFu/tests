FROM registry.access.redhat.com/ubi9/ubi 

RUN dnf install python3 iproute -y

CMD [ "ip", "a" ]