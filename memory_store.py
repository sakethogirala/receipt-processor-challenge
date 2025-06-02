import uuid

_store = {}

def save_receipt(points: int) -> str:
    """
    Generates a UUID and stores the points associated with that receipt.
    Returns the generated UUID as a string.
    """
    receipt_id = str(uuid.uuid4())
    _store[receipt_id] = points
    return receipt_id

def get_points(receipt_id: str) -> int | None:
    """
    Looks up and returns the points for the given receipt ID.
    Returns None if the ID is not found.
    """
    return _store.get(id)