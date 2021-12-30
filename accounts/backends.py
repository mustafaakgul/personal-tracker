from django.contrib.auth.models import User


class EmailAuthBackend(object):
    def authenticate(self, request, email, password):
        try:
            user = User.objects.get(email = email)
            success = user.check_password(password)
            if success:
                return user
        except User.MultipleObjectsReturned:
            user = User.objects.filter(email=email).order_by('id').first()
        except User.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None