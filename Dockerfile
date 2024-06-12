FROM arm64v8/ubuntu:latest

# Install required packages
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    python3 \
    python3-pip \
    python3-venv

# Download and install DuckDB (ARM64 version)
RUN wget https://github.com/duckdb/duckdb/releases/download/v0.7.1/duckdb_cli-linux-aarch64.zip && \
    unzip duckdb_cli-linux-aarch64.zip && \
    rm duckdb_cli-linux-aarch64.zip && \
    mv duckdb /usr/local/bin/

# Create a virtual environment
RUN python3 -m venv /opt/venv

# Activate the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Install DuckDB Python package within the virtual environment
RUN pip3 install duckdb

# Expose the DuckDB server port
EXPOSE 5432

# Copy the Python script
COPY duckdb_server.py /app/duckdb_server.py

# Set the entrypoint to run the Python script
ENTRYPOINT ["python3", "/app/duckdb_server.py"]