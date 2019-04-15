from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

import os
from keras.models import load_model
import numpy as np

# Create your models here.


class Recommendation(models.Model):
    liked_movie1 = models.IntegerField()
    liked_movie2 = models.IntegerField()
    liked_movie3 = models.IntegerField()
    rec_movie1 = models.IntegerField(blank=True)
    rec_movie2 = models.IntegerField(blank=True)
    rec_movie3 = models.IntegerField(blank=True)
    rec_movie4 = models.IntegerField(blank=True)
    rec_movie5 = models.IntegerField(blank=True)
    rec_movie6 = models.IntegerField(blank=True)
    rec_movie7 = models.IntegerField(blank=True)
    rec_movie8 = models.IntegerField(blank=True)
    rec_movie9 = models.IntegerField(blank=True)
    rec_movie10 = models.IntegerField(blank=True)
    rec_movie11 = models.IntegerField(blank=True)
    rec_movie12 = models.IntegerField(blank=True)
    rec_movie13 = models.IntegerField(blank=True)
    rec_movie14 = models.IntegerField(blank=True)
    rec_movie15 = models.IntegerField(blank=True)
    rec_movie16 = models.IntegerField(blank=True)
    rec_movie17 = models.IntegerField(blank=True)
    rec_movie18 = models.IntegerField(blank=True)
    rec_movie19 = models.IntegerField(blank=True)
    rec_movie20 = models.IntegerField(blank=True)
    rec_movie21 = models.IntegerField(blank=True)
    rec_movie22 = models.IntegerField(blank=True)
    rec_movie23 = models.IntegerField(blank=True)
    rec_movie24 = models.IntegerField(blank=True)
    rec_movie25 = models.IntegerField(blank=True)

    def __str__(self):
        return '%s, %s, %s' % (self.liked_movie1, self.liked_movie2, self.liked_movie3)


# def predict(sender, instance, *args, **kwargs):
#     instance.fourth_movie = instance.first_movie
#
#
# post_save.connect(predict, sender=Recommendation)


@receiver(pre_save, sender=Recommendation)
def predict(sender, instance, *args, **kwargs):

    x = np.array([[instance.liked_movie1, instance.liked_movie2, instance.liked_movie3]])

    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'v_0.h5')

    model = load_model(file_path)

    y = model.predict(x)[0]

    predictions = y.argsort()[-25:][::-1]+1

    instance.rec_movie1 = predictions[0]
    instance.rec_movie2 = predictions[1]
    instance.rec_movie3 = predictions[2]
    instance.rec_movie4 = predictions[3]
    instance.rec_movie5 = predictions[4]
    instance.rec_movie6 = predictions[5]
    instance.rec_movie7 = predictions[6]
    instance.rec_movie8 = predictions[7]
    instance.rec_movie9 = predictions[8]
    instance.rec_movie10 = predictions[9]
    instance.rec_movie11 = predictions[10]
    instance.rec_movie12 = predictions[11]
    instance.rec_movie13 = predictions[12]
    instance.rec_movie14 = predictions[13]
    instance.rec_movie15 = predictions[14]
    instance.rec_movie16 = predictions[15]
    instance.rec_movie17 = predictions[16]
    instance.rec_movie18 = predictions[17]
    instance.rec_movie19 = predictions[18]
    instance.rec_movie20 = predictions[19]
    instance.rec_movie21 = predictions[20]
    instance.rec_movie22 = predictions[21]
    instance.rec_movie23 = predictions[22]
    instance.rec_movie24 = predictions[23]
    instance.rec_movie25 = predictions[24]

