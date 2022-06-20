def normalize_floatings(obj):
    divisor = 1000000000  # (units=5, nano=300000000) => units + nano / divisor = 5.30
    return obj.units + obj.nano / divisor