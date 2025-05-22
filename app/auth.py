from flask import request, abort, current_app
from functools import wraps

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token_header = request.headers.get("Authorization")
        token_query = request.args.get("token")
        expected = f"Bearer {current_app.config['AUTH_TOKEN']}"
        expected_raw = current_app.config['AUTH_TOKEN']

        if token_header == expected or token_query == expected_raw:
            return f(*args, **kwargs)

        abort(401, description="Unauthorized: Invalid or missing token")
    return decorated
