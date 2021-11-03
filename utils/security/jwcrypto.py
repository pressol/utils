from jwcrypto import jwk, jws

# currently only does symmetric keys
from jwcrypto.common import json_encode


def generate_key():
    return jwk.JWK.generate(kty='oct', size=256)


def sign_data(data: str, key: jwk.JWK):
    if type(data) == str:
        jwstoken = jws.JWS(data)
        jwstoken.add_signature(key, None,
                               json_encode({"alg": "HS256"}),
                               json_encode({"kid": key.thumbprint()}))
        return jwstoken.serialize()
    else:
        return False


def verify_data(sig: str, key: str):
    jwstoken = jws.JWS()
    jwstoken.deserialize(sig)
    jwstoken.verify(key)
    return jwstoken.payload, jwstoken.is_valid
