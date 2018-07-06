from flask import request, jsonify, current_app
from . import api
from ..models.Clients import Clients
from ..models.Reviews import Reviews
from ..models.Users import Users
from ..models.Content import Content
from .. import db
from functools import wraps
from datetime import datetime, timedelta
import jwt


def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            user = Users.query.filter_by(email=data['sub']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401  # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify


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
# @token_required
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


@api.route('/api/login', methods=["POST"])
def login_user():
    data = request.get_json()
    print("login data", data, flush=True)
    user = Users(**data)
    print(user, flush=True)

    if not user:
        return jsonify({'message': 'Invalid credentials', 'authenticated': False}), 401

    token = jwt.encode({
        'sub': user.email,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        current_app.config['SECRET_KEY'])
    return jsonify({'token': token.decode('UTF-8')})


@api.route('/api/get-chef-desc', methods=["GET"])
def get_chef_desc():
    chef_desc = db.session.query(Content.chef_desc).order_by(Content.id.desc()).first()
    return jsonify(chef_desc[0])


@api.route('/api/set-chef-desc', methods=["POST"])
def set_chef_desc():
    data = request.get_json()
    desc = data.get('chef_desc')
    content = Content(chef_desc=desc)
    db.session.add(content)
    db.session.commit()
    response_object = {'status': 'success'}
    return jsonify(response_object)

