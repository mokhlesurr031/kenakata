FROM python:3.7-buster 
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app/ 
WORKDIR /app 

RUN pip install -r requirements.txt 


RUN python apps/core/manage.py makemigrations authentication 
RUN python apps/core/manage.py makemigrations product 
RUN python apps/core/manage.py migrate

EXPOSE 8000
 

CMD ["python", "apps/core/manage.py", "runserver" , "0.0.0.0:8000"]
