FROM ansible/ansible:ubuntu1604
COPY . /opt/src/
ENTRYPOINT ["bootstrap.py"]
