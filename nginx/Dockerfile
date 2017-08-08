FROM nginx:1.13.3
COPY nginx.conf /etc/nginx/
RUN mkdir /etc/nginx/sites-enabled/
RUN mkdir /etc/nginx/logs
RUN touch error.log
COPY default.conf /etc/nginx/sites-enabled/
