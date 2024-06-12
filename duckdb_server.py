import duckdb

# Start DuckDB server
con = duckdb.connect(database=':memory:', port=5432)

# Keep the server running
con.execute('SELECT 1')
input("Press Enter to stop the server...")