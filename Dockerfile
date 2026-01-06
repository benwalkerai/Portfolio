FROM python:3.11-slim-buster
WORKDIR /home/ben/git/newportfoliosite
COPY . /home/ben/git/newportfoliosite
COPY requirements.txt /home/ben/git/newportfoliosite/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 9001
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:9001", "-m", "007", "wsgi:app"]
