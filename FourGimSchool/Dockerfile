FROM python:3.10.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/FourGimSchool

COPY ./requirements.txt /usr/src/FourGimSchool/requirements.txt
RUN pip install -r /usr/src/FourGimSchool/requirements.txt

COPY . /usr/src/FourGimSchool

EXPOSE 8000

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
