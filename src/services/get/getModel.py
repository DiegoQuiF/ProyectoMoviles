from src.database.db import connection
from src.models.Model import Model

def getModel():
  try:
    conn = connection()
    models = []
    inst =  '''
                SELECT * FROM Test;
            '''
    with conn.cursor() as cursor:
      cursor.execute(inst, )
      for row in cursor.fetchall():
        model = Model(row[1], row[2])
        model.id_test = row[0]
        models.append(model.to_json())
      conn.commit()
      cursor.close()
    conn.close()
    return models
  except Exception as e:
    print("(SISTEMA)   Error: "+e)
    return ''