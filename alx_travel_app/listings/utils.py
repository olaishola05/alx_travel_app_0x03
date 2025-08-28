def generate_tx_ref():
    """
    Generate a unique transaction reference.
    """
    import uuid
    return f"booking_tx_{uuid.uuid4().hex}"