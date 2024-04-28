from passlib.hash import pbkdf2_sha256


def hash_function(value: str) -> str:
    hash_value = pbkdf2_sha256.hash(value)
    return str(hash_value)


def verify_hash(value: str, hash_value: str) -> bool:
    result = pbkdf2_sha256.verify(value, hash_value)
    return result
