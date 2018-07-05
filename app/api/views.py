from flask import request, jsonify
from . import api
from ..models.Clients import Clients
from ..models.Reviews import Reviews
from .. import db


@api.route('/api/client', methods=["POST"])
def add_client():
    data = request.get_json()
    name = data.get("name")
    phone = data.get("phone")
    if name and phone:
        response_object = {'status': 'success'}
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


@api.route('/api/add-opinion', methods=["POST"])
def add_opinion():
    data = request.get_json()
    name = data.get("name")
    phone = data.get("phone")
    opinion = data.get("opinion")
    rating = data.get("rating")

    print("phone: ", phone, flush=True)

    if name and phone and opinion:
        valid_client = Clients.query.filter_by(phone=phone).first()
        valid_review = Reviews.query.filter_by(phone=phone).first()
        if valid_client and valid_review is None:
            response_object = {'status': 'success'}
            opinion = Reviews(name=name, phone=phone, opinion=opinion, rating=rating)
            db.session.add(opinion)
            db.session.commit()
        else:
            response_object = {'status': 'duplicate'}

    return jsonify(response_object)


@api.route('/api/reviews', methods=["GET"])
def get_reviews():
    reviews = Reviews.query.all()
    reviews_list = [opinion.as_dict() for opinion in reviews]
    print(reviews_list, flush=True)
    return jsonify(reviews_list)
