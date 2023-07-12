from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://dp1mc2p7n8d3mtj3oqrt:pscale_pw_oz7VkSNRWjW46w3FYzmORHnK7MD7dtJdegsVzWV7dVG@aws.connect.psdb.cloud/joviancareer?charset=utf8mb4"


engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
    })

def loads_jobs_from_db():
# connecting the data with the engine
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row))
    return jobs



  
  # print("type result:", type(result))
  # print("type result.all:", type(result.all()))
  # print("result.all():", result_all)

