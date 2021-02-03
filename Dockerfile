FROM python:3.8

WORKDIR /usr/local/src

# Copy code
COPY . .

# Don't use a virtualenv
ARG POETRY_VIRTUALENVS_CREATE=False

# Upgrade pip and install dependencies
RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry install --no-dev


CMD ["python", "main.py"]
