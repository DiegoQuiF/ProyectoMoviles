from flask import Blueprint, jsonify, request

from src.services.post.postLogin import postLogin
from src.services.post.postRegister import postRegister

from src.models.Paciente import Paciente


main = Blueprint('index_blueprint', __name__)

@main.route("/iniciarSesion", methods = ['POST'])
def iniciarSesion():
  try:
    data = request.get_json()
    email = data['email']
    contra = data['contra']
    paciente = postLogin(email, contra)
    if(paciente!=''):
      paciente = paciente.to_json()
      return jsonify({'message':'COMPLETE', 'success':True, 'data':paciente})
    else:
      return jsonify({'message':'NOT FOUND', 'success':True})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False})

@main.route("/registrar", methods = ['POST'])
def register():
  try:
    data = request.get_json()
    nom_comp = data['nom_comp']
    direc = data['direc']
    email = data['email']
    contra = data['contra']
    registrado = postRegister(nom_comp, direc, email, contra)
    if(registrado):
      return jsonify({'message':'COMPLETE', 'success':True})
    else:
      return jsonify({'message':'NOT FOUND', 'success':True})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False})