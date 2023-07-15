from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       pool_pre_ping=True,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def loads_jobs_from_db():
  # connecting the data with the engine
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs



def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"),{'val': id})
    row = result.fetchone()
    return row._asdict()


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO application (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES(:job_id, :full_name,:email, :linkedin_url, :education,:work_experience, :resume_url) ")

    conn.execute(query, 
             {
                 'job_id': job_id,
                 'full_name': data['full_name'],
                 'email': data['email'],
                 'linkedin_url': data['linkedin_url'],
                 'education': data['education'],
                 'work_experience': data['work_experience'],
                 'resume_url': data['resume_url']
                 })
      
# def load_job_from_db(id):
#   with engine.connect() as conn:
#     result = conn.execute(
#       text(f"select * from jobs WHERE id = {id}") )


#     rows = []
#     for row in result.all():
#       rows.append(row._mapping)
#     if len(rows) == 0:
#       return None
#     else:
#       return row
      
    # rows = result.all()
    # if len(rows) == 0:
    #   return None
    # else:
    #   return dict(rows[0])
      

  # print("type result:", type(result))
  # print("type result.all:", type(result.all()))
  # print("result.all():", result_all)
