FROM ubuntu:latest

# Install required packages
RUN apt-get update && apt-get install -y \
    wget \
    unzip

# Download and install DuckDB
RUN wget https://github.com/duckdb/duckdb/releases/download/v0.7.1/duckdb_cli-linux-amd64.zip && \
    unzip duckdb_cli-linux-amd64.zip && \
    rm duckdb_cli-linux-amd64.zip && \
    mv duckdb /usr/local/bin/

# Set the entrypoint to run DuckDB
ENTRYPOINT ["/usr/local/bin/duckdb"]