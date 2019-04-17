FROM python:3.6.8-slim-jessie

RUN pip install ibm_cos_sdk cos_aspera

ENV HOME /home
WORKDIR $HOME
ADD cosio cosio
ADD main.py .

ENTRYPOINT ["python", "main.py"]
