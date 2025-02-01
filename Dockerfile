FROM python:3.10-alpine

WORKDIR /app

COPY ./app .

RUN python3 -m venv venv
RUN source venv/bin/activate
RUN pip3 install -r requirements.txt
RUN pip3 install "fastapi[all]"

EXPOSE 8000

CMD ["fastapi", "run", "--port", "8000", "main.py"]