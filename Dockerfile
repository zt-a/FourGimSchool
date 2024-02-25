# syntax=docker/dockerfile:1
FROM python:3.10.11

# set environment variables
ENV APP_HOME=/home/ubuntu/FourGimSchool
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR $APP_HOME

# update pip, install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt $APP_HOME
RUN pip install -r requirements.txt
RUN pip install gunicorn

# copy app folder
COPY . $APP_HOME


# run python command
RUN python manage.py makemigrations
RUN python manage.py collectstatic --noinput --clear


# specify the command to run on container start
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi:application"]