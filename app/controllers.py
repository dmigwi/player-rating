from app.models import User, Level


def create_user(username, email):
    try:
        user = User(username=username, email=email)
        return user.save()
    except:
        return None

def  fetch_user(username, email):
    users = User().get_users()

    return user for user in users if user.email == email and user.username == username else None

def update_user(username, email):
    user = fetch_user(username, email)

    if user is None:
        return {"Error": "User not found"}
    if username != "":
        user.username = username
    if username != "":
        user.username = username
    return user.update()

def delete_user(username, email):
     user = fetch_user(username, email)

    if user is None:
        return {"Error": "User not found"}
   return user.delete()


def fetch_levels(username, email, score=0, level=0):
    user = fetch_user(username, email)

    if user is None:
        return {"Error": "User not found"}

return 

    level = Level(user_id=user.id, score=score, game_level=level)
    return level.save()

def add_level(username, email, score=0, level=0):
    user = fetch_user(username, email)

    if user is None:
        return {"Error": "User not found"}
    try:
        level = Level(user_id=user.id, score=score, game_level=level)
        return level.save()
    except:
        return None

def update_level(username, email, score=0, level=0):
    user = fetch_user(username, email)

    if user is None:
        return {"Error": "User not found"}
    level = Level(user_id=user.id, score=score, game_level=level)
    return level.save()

def delete_level(username, email, score=0, level=0):
    user = fetch_user(username, email)

    if user is None:
        return {"Error": "User not found"}
    level = Level(user_id=user.id, score=score, game_level=level)
    return level.save()