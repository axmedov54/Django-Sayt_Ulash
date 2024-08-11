



from django.db import models


class Joy(models.Model):
    name = models.CharField(max_length=50)

    def str(self):
        return f"{self.name} the place"


class Restaurant(models.Model):
    place = models.OneToOneField(
       Joy,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_osh = models.BooleanField(default=False)
    serves_shashlik = models.BooleanField(default=False)

    def str(self):
        return "%s the restaurant" % self.place.name


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def str(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)