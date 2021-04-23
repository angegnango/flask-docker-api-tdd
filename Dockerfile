FROM python:3.6-alpine

ENV HOST 0.0.0.0
ENV PORT 3000
ENV DEBUG true

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 3000

RUN pip install gunicorn

CMD ["gunicorn", "--bind", "0.0.0.0:3000", "--workers", "3", "app:app"]