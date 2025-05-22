from flasgger import swag_from
from .auth import require_auth

def doc_auth(doc_path):
    def wrapper(fn):
        print(f"[DEBUG] Loading Swagger doc from: {doc_path}")
        fn = swag_from(doc_path)(fn)
        fn = require_auth(fn)
        return fn
    return wrapper