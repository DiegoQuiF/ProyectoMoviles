from flask import Blueprint, jsonify, request

from src.services.post.postLogin import postLogin
from src.services.post.postRegister import postRegister
from src.services.get.getCuestionarios import getCuestionarios
from src.services.post.postObtenerCuestionario import postObtenerCuestionario

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

@main.route("/cuestionarios")
def cuestionarios():
  try:
    cuestionarios = getCuestionarios()
    if(cuestionarios!=''):
      return jsonify({'message':'COMPLETE', 'success':True, 'data':cuestionarios})
    else:
      return jsonify({'message':'NOT FOUND', 'success':True})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False})

@main.route("/cuestionarioCompleto", methods = ['POST'])
def cuestionario():
  try:
    data = request.get_json()
    id_cuest = data['id_cuest']
    cuestionario = postObtenerCuestionario(id_cuest)
    if(cuestionario!=''):
      return jsonify({'message':'COMPLETE', 'success':True, 'data':cuestionario})
    else:
      return jsonify({'message':'NOT FOUND', 'success':True})
  except Exception as e:
    return jsonify({'message':'ERROR', 'success':False})