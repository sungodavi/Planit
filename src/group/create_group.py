from google.cloud import firestore

from src.errors.input_error import InputError


def create_group(class_id, date, location, description):
    db = firestore.Client()
    class_ref = db.document('Classes/{}'.format(class_id))
    if not class_ref.exists:
        raise InputError('Invalid classes')

    groups_ref = class_ref.collection('Groups'.format(class_id))
    groups_ref.add({
        'date': date,
        'location': location,
        'descrption': description,
    })
