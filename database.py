from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']


engine = create_engine(
  db_connection_string,
   pool_pre_ping=True,
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
      jobs.append(row._asdict())
    return jobs



  
  # print("type result:", type(result))
  # print("type result.all:", type(result.all()))
  # print("result.all():", result_all)

