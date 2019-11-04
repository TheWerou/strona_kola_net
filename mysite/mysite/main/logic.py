from .models import UserNet


class Logic:
    all_users_objecs = UserNet.objects.all()

    def get_sorted(self):
        return self.all_users_objecs.all()
