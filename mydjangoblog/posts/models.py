from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    titulo =  models.CharField(max_length=120)
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now= False, auto_now_add=True)
    slug = models.SlugField()

#python2
#    def __unicode__(self):
#        return self.titulo

#python3
    def _str_(self):
        return  self.titulo

#best practices to obtain url
    def get_absolut_url(self):
        return  reverse("unico", kwargs={"id":self.id, "slug": self.slug})