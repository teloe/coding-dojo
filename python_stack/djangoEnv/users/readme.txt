# __ import User model
>>> from apps.user_login.models import User

# __ insert some data (with out validations) some of these will fail
>>> User.objects.create(first_name="Michael", last_name="Jordan", email="mike@jumpman.com", age=23)
>>> User.objects.create(first_name="Larry", last_name="Bird", email="celtics rule!!!", age=23)

# __ import helper function to validate data being passed
>>> from shell_helpers import create_valid_user
>>> create_valid_user()

# __ create a few valid users using helper function

# __ retreive all users
>>> all_users = User.objects.all()
>>> first_user = User.objects.first()

# __ retreive first user
>>> User.objects.first()

# __ retreive last user
>>> User.objects.last()

# __ sort users by last_name DESC
>>> User.objects.all().order_by("last_name")

# __ get user with id=3 and UPDATE to something else
>>> user3 = User.objects.get(id=3)
>>> user3.last_name = "something"
>>> user3.save()

# __ delete user with id=4
>>> User.objects.get(id=4).delete()
