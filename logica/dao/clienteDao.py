import logica.conexion as con

cx = con.cursor()
conn = con.connection()

#dao de cliente para la base de datos
def get_by_id(id:int):
    cx.execute("""SELECT * FROM cliente WHERE ci_nit = %s""", (id,))
    query_results = cx.fetchall()
    return query_results

def get_all():
    cx.execute("""SELECT * FROM cliente""")
    query_results = cx.fetchall()
    return query_results

def insert(ci:int,nombre:str, apellido:str, correo:str, telefono:str):
    cx.execute("""INSERT INTO cliente(ci_nit,nombre, apellido, correo, telefono) VALUES (%s,%s, %s, %s, %s)""", (ci,nombre, apellido, correo, telefono))
    conn.commit()
    return cx.statusmessage

def update(id:int, nombre:str, apellido:str, telefono:str, correo:str):
    cx.execute("""UPDATE cliente SET nombre = %s, apellido = %s, telefono = %s, correo = %s WHERE ci_nit = %s""", (nombre, apellido, telefono, correo, id))
    conn.commit()
    return cx.statusmessage

def delete(id:int):
    cx.execute("""DELETE FROM cliente WHERE ci_nit = %s""", (id,))
    conn.commit()
    return cx.statusmessage
