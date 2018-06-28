from flask import request, jsonify
from . import api
from ..models.Clients import Clients
from .. import db


@api.route('/api/client', methods=["POST"])
def add_client():
    data = request.get_json()
    name = data.get("name")
    phone = data.get("phone")
    if name and phone:
        response_object = {'status': 'success'}
        print(name, phone, flush=True)
        is_existing = Clients.query.filter_by(phone=phone).first()
        if is_existing is None:
            client = Clients(name=name, phone=phone)
            db.session.add(client)
            db.session.commit()
    else:
        response_object = {'status': 'error'}
    return jsonify(response_object)


@api.route('/api/clients', methods=["GET"])
def get_clients():
    clients = Clients.query.all()
    clients_json_list = [client.as_dict() for client in clients]
    print(clients_json_list, flush=True)
    return jsonify(clients_json_list)
