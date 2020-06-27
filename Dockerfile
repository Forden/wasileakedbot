FROM python:3.7-slim

EXPOSE 5156

WORKDIR /wasileakedbot

COPY requirements.txt /wasileakedbot/
RUN pip install -r /wasileakedbot/requirements.txt
COPY . /wasileakedbot/

CMD python3 /wasileakedbot/bot.py
