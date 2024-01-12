FROM python:3.12

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc libffi-dev

RUN pip install --no-cache-dir -r requirements.txt

ENV RECAPTCHA_PRIVATE_KEY = 6Lfer0kpAAAAAEAtPP1igzvVEtUySFK8UpOCN57X

EXPOSE 80

CMD ["python", "main.py"]
