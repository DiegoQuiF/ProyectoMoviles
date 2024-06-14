from flask import Blueprint, jsonify, request

from src.services.post.postModel import postModel


main = Blueprint('index_blueprint', __name__)

@main.route("/iniciarSesion", methods = ['POST'])
def iniciarSesion():
  try:
    data = request.get_json()
    email = data['email_usu']
    contra = data['contra_usu']
    id_usu = postModel(email, contra)
    if(id_usu!=""):
      datos = {'id_usu':id_usu,}
      return jsonify({'message':'COMPLETE', 'success':True, 'data':datos})
    else:
      return jsonify({'message':'NOT FOUND', 'success':True})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False})