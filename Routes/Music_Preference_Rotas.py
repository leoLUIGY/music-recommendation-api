from app import app
from sqlalchemy.exc import IntegrityError
from flask_openapi3 import Tag
from Schemas.MusicPreferenceBuscaSchema import MusicPreferenceBuscaSchema
from Schemas.MusicPreferenceSchema import MusicPreferenceSchema
from Schemas.MusicPreferenceUpdateSchema import MusicPreferenceUpdateSchema
from Model import *
from flask import redirect

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
preferences_tag = Tag(name="MusicPreference", description="Adição, edição, visualização e remoção de uma preferencia")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.get('/preferences', tags=[preferences_tag])
def get_preferences():
    """Buscar preferencias
    """
    session = Session()
    try:
        preferences = session.query(MusicPreference).all()

        if not preferences:
            return {"MusicPreference":[]} , 200
        else:
            return [preference.to_dict() for preference in preferences]
    finally:
        session.close()

@app.get('/preference', tags=[preferences_tag])
def get_preference(query: MusicPreferenceBuscaSchema):
    """Buscar uma preferencia especifica
    """
    preference_id = query.id
    session = Session()
    try:
        preference = session.query(MusicPreference).filter(MusicPreference.id == preference_id).first()
        if not preference:
            error_msg = "Preferencia não encontrado na base :/"
            return {"mesage": error_msg}, 404
        else:
            return preference.to_dict()
    finally:
        session.close()

@app.post('/preference', tags=[preferences_tag])
def add_preference(form: MusicPreferenceSchema):
    """ Adicionar uma nova preferencia
    """
    
    preference = MusicPreference(
        nome = form.nome,
        genero = form.genero,
        artista = form.artista,
        data_criacao = form.data_criacao
    )
    session = Session()
    try:
       
        session.add(preference)
        session.commit()
        return preference.to_dict(), 200
    except IntegrityError as e:        
        error_msg = "Preferencia de mesmo nome já salvo na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar nova preferencia:/"
        return {"mesage": error_msg}, 400
    finally:
        session.close()

@app.put('/preference', tags=[preferences_tag])
def update_preference(form: MusicPreferenceUpdateSchema):
    """Editar informações de uma preferencia
    """
    preference_id = form.id
    session = Session()
    try:
        preference = session.query(MusicPreference).filter(MusicPreference.id == preference_id).first()
        if not preference:
            error_msg = "Preferencia não encontrada na base :/"
            return {"mesage": error_msg}, 404
        else:
            
            preference.nome = form.nome
            preference.genero = form.genero
            preference.artista = form.artista
            preference.data_criacao = form.data_criacao

        
            session.commit()
            return preference.to_dict(), 200
    except IntegrityError as e:        
        error_msg = "Preferencia de mesmo nome já salvo na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar nova preferencia:/"
        return {"mesage": error_msg}, 400
    finally:
        session.close()

@app.delete('/preference', tags=[preferences_tag])
def delete_preference(query: MusicPreferenceBuscaSchema):
    """Deletar uma preferencia a partir do id informado
    """
    preference_id = query.id
    session = Session()
    try:
        count = session.query(MusicPreference).filter(MusicPreference.id == preference_id).delete()
        session.commit()

        if count:
            return {"mesage": "preferencia removido", "id": preference_id}
        else:
            error_msg = "preferencia não encontrada na base :/"
            return {"mesage": error_msg}, 404
    finally:
        session.close()