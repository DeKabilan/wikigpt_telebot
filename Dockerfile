FROM python:3.9-alpine

RUN mkdir -p  /bot

COPY . /bot

RUN python3 -m pip install -r /bot/requirements.txt

EXPOSE 5000

CMD ["python","/bot/main.py"]
