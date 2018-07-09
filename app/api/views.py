from flask import request, jsonify, current_app
import os
from . import api
from ..models.Clients import Clients
from ..models.Reviews import Reviews
from ..models.Users import Users
from ..models.Content import Content
from .. import db
from functools import wraps
from datetime import datetime, timedelta
import jwt
import smtplib
from email.message import EmailMessage
from smsapi.client import SmsApiPlClient


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


def send_mail(subject, text):
    if not current_app.config['DEBUG']:
        message = EmailMessage()

        message_text = """Dodano nowego klienta ({})""".format(datetime.now().strftime("%Y-%m-%d %H:%M"))
        message_text += text

        message.set_content(message_text)

        message['Subject'] = subject
        message['From'] = "info@barbonanza.pl"
        message['To'] = ["miks.szymon@gmail.com", "aga.miks03@gmail.com"]

        try:
            smtp_obj = smtplib.SMTP("mail26.mydevil.net")
            smtp_obj.send_message(message)
            print("Successfully sent email")
            smtp_obj.quit()
        except smtplib.SMTPException:
            print("Error: unable to send an e-mail")


def send_welcome_sms(name, number):
    if not current_app.config['DEBUG']:
        access_token = os.getenv('SMSAPI_ACCESS_TOKEN')
        client = SmsApiPlClient(access_token=access_token)
        sms_message = "{}! Bar Bonaza dziekuje za dolaczenie do programu, wkrotce dostaniesz " \
                      "od nas kolejne SMS z promocjami i rabatami!".format(name)
        client.sms.send(to=number, message=sms_message)


@api.route('/api/client', methods=["POST"])
def add_client():
    data = request.get_json()
    name = data.get("name")
    phone = data.get("phone")
    if name and phone:
        response_object = {'status': 'success'}
        # calculating 7 day before
        date_before = datetime.today() - timedelta(days=7)
        date_midnight = datetime.combine(date_before, datetime.min.time())
        is_existing = Clients.query.filter_by(phone=phone).filter(Clients.created_at > date_midnight).first()
        if is_existing is None:
            client = Clients(name=name, phone=phone)
            db.session.add(client)
            db.session.commit()
            # send mail with info about register
            subject = "Nowy klient w pyszne.barbonanza.pl"
            mail_text = "Nowy klient:\n Imię: {} \n Numer tel: {}".format(name, phone)
            send_mail(subject, mail_text)
            # send SMS with welcome
            send_welcome_sms(name, phone)
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

    if name and phone and opinion:
        valid_client = Clients.query.filter_by(phone=phone).first()
        valid_review = Reviews.query.filter_by(phone=phone).first()
        if valid_client and valid_review is None:
            response_object = {'status': 'success'}
            client_opinion = Reviews(name=name, phone=phone, opinion=opinion, rating=rating)
            db.session.add(client_opinion)
            db.session.commit()

            mail_text = "Dodano nową opinię od {} \n opinia: {} \n gwiazdki: {}".format(name, opinion, rating)
            subject = "Nowa opinia na pyszne.barbonanza.pl"
            send_mail(subject, mail_text)
        else:
            response_object = {'status': 'duplicate'}

    return jsonify(response_object)


@api.route('/api/reviews', methods=["GET"])
def get_reviews():
    reviews = Reviews.query.order_by(Reviews.created_at.desc()).all()
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
