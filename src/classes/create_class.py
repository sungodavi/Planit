import random
import string

from google.cloud import firestore


def create_class(user_id, name):
    db = firestore.Client()
    classes_ref = db.collection('Classes')
    _, doc = classes_ref.add({
        'name': name,
        'code': generate_code()
    })
    db.document('Classes/{}/Users/{}'.format(doc.id, user_id)).set({
        'owner': True
    })


def generate_code(size=7):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))
