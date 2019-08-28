FROM python:3

ADD auction.py /

# COPY requirements.txt requirements.txt
# RUN pip install -f requirements.txt

COPY . .
CMD ["python3", "./auction.py"]
