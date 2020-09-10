FROM python:3.8-alpine
WORKDIR /app
ADD . /app
RUN pip3 install --upgrade pip \
	&& pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3" ] 
CMD [ "app.py" ] 