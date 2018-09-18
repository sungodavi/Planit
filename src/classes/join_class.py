from google.cloud import firestore

from src.errors.input_error import InputError


def join_class(user_id, class_code):
    db = firestore.Client()
    classes = db.collection('Classes').where('code', '==', class_code).get()
    for doc in classes:
        class_ref = classes.document('{}/Users/{}'.format(doc.id, user_id))
        class_ref.set({
            'owner': False
        })
        break

    else:
        raise InputError('Invalid classes code')
