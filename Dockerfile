FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN python3 -m pip install -r /bot/requirements.txt

EXPOSE 5000

CMD ["python","main.py"]
