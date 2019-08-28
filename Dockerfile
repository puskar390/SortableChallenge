FROM python:3
COPY auction auction
CMD ["python", "auction/auction.py"]