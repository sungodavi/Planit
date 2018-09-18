from google.cloud import firestore, exceptions

from src.errors.input_error import InputError


def leave_class(user_id, class_id):
    db = firestore.Client()
    classes = db.collection('Classes')
    try:
        class_doc = next(classes.document(class_id).get())
        user_ref = classes.document('{}/Users/{}'.format(class_id, user_id))
        if user_ref.exists:
            user_ref.delete()
        else:
            raise InputError('user not in classes')
    except exceptions.NotFound:
        raise InputError('Invalid classes code')
