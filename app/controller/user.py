from app.application.services.user import create_user

def signup():
    user = create_user(user_name="grab")
    return user

if __name__ == "__main__":
    user = signup(user_name="grab")
    print(user)