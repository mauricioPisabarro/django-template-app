from django.db import models


class AppModel(models.Model):
    class Meta:
        abstract = True

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


# class OtherModel(AppModel):
#     class Meta:
#         app_label = "app"
