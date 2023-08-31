import os
def get_profile_upload_path(instance, filename):
    user_pk = instance.user.pk
    filename = os.path.basename(filename)
    return f"user/{user_pk}/profile/{filename}"