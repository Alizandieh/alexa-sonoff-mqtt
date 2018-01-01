docker rm -f  mqtt

docker build -t ashleymaloney/mqtt .

docker run -d -p 80:80 \
    --name mqtt \
    --env-file ./env.list \
    ashleymaloney/mqtt
