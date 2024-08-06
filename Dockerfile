FROM python:3.9-slim

RUN mkdir -p  /bot

COPY . /bot

RUN python3 -m pip install -r /bot/requirements.txt

EXPOSE 5000

CMD ["python","/bot/main.py"]
