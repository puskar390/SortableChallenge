FROM python:3
#RUN pip install -f

COPY auction auction
CMD ["python", "auction/auction.py"]