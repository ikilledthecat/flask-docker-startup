FROM python:3.6-stretch
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD gunicorn -b 0.0.0.0:5000 --access-logfile - 'src.app:create_app()'
