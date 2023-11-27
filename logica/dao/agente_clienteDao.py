import logica.conexion as con

cx = con.cursor()
conn = con.connection()
#dao de agente_cliente para la base de datos

def get_by_id(id_agente:int, id_cliente:int):
    cx.execute("""SELECT * FROM agente_cliente WHERE id_agente = %s and id_cliente = %s""", (id_agente, id_cliente))
    query_results = cx.fetchall()
    return query_results

def get_by_cliente(id_cliente:int):
    cx.execute("""SELECT * FROM agente_cliente WHERE id_cliente = %s""", (id_cliente,))
    query_results = cx.fetchall()
    return query_results

def get_by_cliente(id_agente:int):
    cx.execute("""SELECT * FROM agente_cliente WHERE id_agente = %s""", (id_agente,))
    query_results = cx.fetchall()
    return query_results

def get_all():
    cx.execute("""SELECT * FROM agente_cliente""")
    query_results = cx.fetchall()
    return query_results


