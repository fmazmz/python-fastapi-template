from uuid import UUID, uuid4


def generate_op_id() -> UUID:
    return uuid4()