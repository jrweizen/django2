from django.db import models
from stdimage.models import StdImageField

# Signals
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateField('Data de criacao', auto_now_add=True)
    modificado = models.DateField('Data de atualizacao', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    # Abstract classes are not implemented on databases, only for draft
    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
