from google.cloud import firestore


def join_group(class_id, group_id, user_id, ride):
    db = firestore.Client()

    class_ref = db.collection('Classes/{}/Groups/{}/Users/{}'.format(class_id, group_id, user_id))
    class_ref.set({
        'ride': ride
    })
