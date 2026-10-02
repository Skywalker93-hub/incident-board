FROM nginx:1.30-trixie
COPY index.html /usr/share/nginx/html/index.html
COPY nginx.conf /etc/nginx/nginx.conf
RUN apt update -y && apt upgrade -y && apt install -y iproute2 net-tools curl 
RUN mkdir -p /etc/nginx/sites-available /etc/nginx/sites-enabled && rm -f /etc/nginx/conf.d/default.conf \
    && ln -s /etc/nginx/conf.d/mysite.conf /etc/nginx/sites-enabled/mysite.conf 

