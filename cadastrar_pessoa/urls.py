from django.urls import path
from . import views


urlpatterns = [
    path("", views.cadastrar_pessoa, name="cadastrar_pessoa"),
    path("deletar_pessoa/<int:id>", views.deletar_pessoa, name="deletar_pessoa"),
    path("editar_pessoa/<int:id>", views.editar_pessoa, name="editar_pessoa" ),
]