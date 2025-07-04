from uuid import uuid4


def custom_upload_to(instance, filename):
    return f"{uuid4().hex}.{filename.split('.')[-1]}"
