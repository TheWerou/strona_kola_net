from .models import UserNet


class Logic:
    all_users_objecs = UserNet.objects.all()

    def get_rest(self):
        #helepr = self.all_users_objecs.all()
        return self.all_users_objecs.all()[2:]

    def get_boss(self):
        return UserNet.objects.order_by('kolejnosc')[:2]
