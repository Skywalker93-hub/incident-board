FROM nginx:1.30-trixie
COPY index.html /usr/share/nginx/html/index.html
RUN apt update -y && apt upgrade -y && apt install -y iproute2 net-tools curl 
RUN rm -f /etc/nginx/conf.d/default.conf
