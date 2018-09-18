from google.cloud import firestore

from src.errors.auth_error import AuthError


def delete_class(class_id, user_id):
    db = firestore.Client()
    class_ref = db.document('Classes/{}'.format(class_id))
    owner = next(class_ref.collection('Users').where('owner', '==', True).get())
    if owner.id == user_id:
        batch = db.batch()

        delete_collection(batch, class_ref.collection('Users'))
        delete_collection(batch, class_ref.collection('Groups'))
        batch.delete(class_ref)

        batch.commit()
    else:
        raise AuthError(message='User is not owner')


def delete_collection(batch, ref):
    for doc in ref.get():
        batch.delete(doc.reference)
    return batch
