def replace_empty_with_zero(series):
    """
    Replaces empty values with zeros
    """
    return series.replace('', 0)

def feature_names(transformer, feature_names):
    """
    Outputs feature names
    """
    return [f'{col}' for col in feature_names]