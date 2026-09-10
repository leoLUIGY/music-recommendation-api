FROM python:3.9

WORKDIR /app

COPY dependencies.txt .

RUN pip install --no-cache-dir -r dependencies.txt

COPY . .

EXPOSE 5001

CMD ["python", "app.py"]