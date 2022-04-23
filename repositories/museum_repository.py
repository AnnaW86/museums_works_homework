from db.run_sql import run_sql

from models.work import Work
from models.museum import Museum

# Write your functions here

def save(museum):
    sql = """
    INSERT INTO museums (name, address)
    VALUES (%s, %s)
    RETURNING *
    """
    values = [museum.name, museum.address]
    results = run_sql(sql, values)
    id = results[0]['id']
    museum.id = id
    return museum

def select_all():
    museums = []
    sql = "SELECT * FROM museums"
    results = run_sql(sql)
    for row in results:
        museum = Museum(row['name'], row['address'], row['id'])
        museums.append(museum)
    return museums

def select(id):
    museum = None
    sql = """
        SELECT * FROM museums
        WHERE id = %s
    """
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        museum = Museum(result['name'], result['address'], result['id'])
    return museum

def update(museum):
    sql = """
        UPDATE museums
        SET (name, address) = (%s, %s)
        WHERE id = %s
    """
    values = [museum.name, museum.address, museum.id]
    run_sql(sql, values)

def delete(id):
    sql = """
        DELETE FROM museums
        WHERE id = %s
    """
    values = [id]
    run_sql(sql, values)

def select_works(id):
    museum_works = []
    sql = """
        SELECT * FROM works
        WHERE museum_id = %s 
    """
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        museum = select(row['museum_id'])
        work = Work(row['title'], row['artist'], row['year'], museum, row['id'])
        museum_works.append(work)
    return museum_works

def delete_museums_works(id):
    sql = """
        DELETE FROM works
        WHERE museum_id = %s
    """
    values = [id]
    run_sql(sql, values)

