from app.models import User

def get_userid(email):
    user=User.query.filter_by(email=email).first()

    if not user:
        return -1
    return user.user_id