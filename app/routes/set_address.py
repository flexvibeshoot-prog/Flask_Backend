from flask import Blueprint,request,jsonify
from flask_jwt_extended import jwt_required,get_jwt_identity
from app.models import Address
from app import db

address=Blueprint('address',__name__,url_prefix='/set_address')

@address.route('/address_set',methods=['POST'])
@jwt_required()
def set_address():
    user_email=get_jwt_identity()
    data=request.get_json()

    #background task.
    from app.tasks.simple_task.get_userID import get_userid
    from app.tasks.simple_task.get_userName import get_userName
    new_address=Address(
        user_id=get_userid(user_email),
        full_name=get_userName(user_email),
        phone=data['phone'],
        address_line1=data['address_line1'],
        address_line2=data['address_line2'],
        city=data['city'],
        state=data['state'],
        country=data['country'],
        postal_code=data['pin_code']
    )
    try:
        db.session.add(new_address)
        db.session.commit()
        return jsonify({"message":"Address is added sucessfully...!!!"})
    except:
        db.session.rollback()
        return jsonify({"message":"Somthing is wrong in data...!!!"})