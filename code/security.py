from werkzeug.security import safe_str_cmp
from models.user import UserModel

# function which authenticates a user
def authenticate(username,password):
    user = UserModel.find_by_username(username) #finds the User by username
    if user and safe_str_cmp(user.password, password):
        return user


#which takes in a payload where we extract user_id from the payload. If user matches the payload, we return user_id
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id) #find the User by th id
