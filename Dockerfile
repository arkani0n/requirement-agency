FROM python:3

WORKDIR home/dev

COPY . .

RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh

ENV DB_NAME=db
ENV DB_USER=admin
ENV DB_PASSWORD=db_password
ENV DB_PORT=5432

ENTRYPOINT ["/home/dev/entrypoint.sh"]