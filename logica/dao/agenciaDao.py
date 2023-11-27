import logica.conexion as conexion

conn = conexion.connection()
cx = conexion.cursor()


def get_all():
    cx.execute("SELECT * FROM agencia")
    return cx.fetchall()


def get_by_id(id):
    cx.execute("SELECT * FROM agencia WHERE id = %s", (id,))
    return cx.fetchone()


def insert(agencia):
    cx.execute("INSERT INTO agencia (nombre, direccion, telefono) VALUES (%s, %s, %s)",
               (agencia.nombre, agencia.direccion, agencia.telefono))
    conn.commit()


def update(agencia):
    cx.execute("UPDATE agencia SET nombre = %s, direccion = %s, telefono = %s WHERE id = %s",
               (agencia.nombre, agencia.direccion, agencia.telefono, agencia.id))
    conn.commit()


def delete(id):
    cx.execute("DELETE FROM agencia WHERE id = %s", (id,))
    conn.commit()

