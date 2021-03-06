FROM python:3.8
RUN mkdir /app
WORKDIR /app
# Get and install dependencies
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
# Copy app directory
COPY gui-main.py /app/main.py
COPY templates/ /app/templates
COPY /static/ /app/static
COPY guest/ /app/guest
COPY admin/ /app/admin
COPY addons/ /app/addons
# expose and run app on specified port
EXPOSE 4444
CMD [ "python3", "./main.py" ]
