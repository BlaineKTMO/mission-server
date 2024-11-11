# Use Ubuntu 22.04 as the base image
FROM ubuntu:22.04

# Set env variables
ENV SHELL=$SHELL
ENV FLASK_APP="mission-server"

# Install deps
RUN apt-get update && apt-get install -y \
    curl \
    python3 \
    python3-pip \
    python3-venv \
    git \
    && rm -rf /var/lib/apt/lists*

# Install poetry with installation script
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add poetry to path
ENV PATH="/root/.local/bin:$PATH"

# Check if poetry is isntalled
RUN poetry --version

# Set working directory
WORKDIR /mission-server

# Copy application
COPY . /mission-server

# Install poetry deps
RUN poetry install

# Run poetry shell and flaskapp
ENTRYPOINT ["bash", "-c", "poetry run flask run --host=0.0.0.0 --port=5000"]
