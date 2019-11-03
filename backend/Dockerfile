FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /quajoo
WORKDIR /quajoo
ADD . /quajoo/
RUN pip install -r requirements.txt
ENV FLASK_APP=server.py
CMD ["flask", "run", "--host=0.0.0.0"]
