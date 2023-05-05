FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY requirements.txt /src/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /src/

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]