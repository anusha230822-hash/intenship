from mysql_helper import connect


def setup(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_candidates (id INT PRIMARY KEY, name VARCHAR(100), skills VARCHAR(255))")
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_companies (id INT PRIMARY KEY, name VARCHAR(100))")
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_jobs (id INT PRIMARY KEY, company_id INT, title VARCHAR(100), salary DECIMAL(10,2))")
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_applications (id INT PRIMARY KEY, candidate_id INT, job_id INT, status VARCHAR(30))")
    cursor.execute("CREATE TABLE IF NOT EXISTS mini_interviews (id INT PRIMARY KEY, application_id INT, interview_date DATE)")
    connection.commit()
    cursor.close()


def apply_for_job(connection, application_id, candidate_id, job_id):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO mini_applications VALUES (%s, %s, %s, %s)", (application_id, candidate_id, job_id, "APPLIED"))
    connection.commit()
    cursor.close()


def list_jobs(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT j.title, c.name, j.salary FROM mini_jobs j JOIN mini_companies c ON c.id = j.company_id")
    jobs = cursor.fetchall()
    cursor.close()
    return jobs


if __name__ == "__main__":
    database = connect()
    setup(database)
    print("Job Portal Database System ready.")
    database.close()
