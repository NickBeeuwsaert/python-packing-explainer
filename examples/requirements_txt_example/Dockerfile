FROM python:3.9.2-alpine

# prevent python from creating __pycache__, and turn off output buffering
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# First copy over our requirements file so we don't
# reinstall dependencies every time we run docker
# It is a lot harder to specify which requirements files to copy over
# so we are jsut copying each one
COPY requirements.txt requirements-test.txt ./
RUN pip3 install -U pip && \
    pip3 install -r requirements.txt -r requirements-test.txt

# Now copy application source over
COPY . .

CMD ["python3", "main.py"]
