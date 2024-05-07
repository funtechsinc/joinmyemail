from collections import defaultdict


def decode_yearly(docs: list) -> list:
    # Dictionary to store counts for each month
    month_counts = defaultdict(int)

    # Map numerical month representation to month names
    month_names = {
        1: 'jan', 2: 'feb', 3: 'mar', 4: 'apr', 5: 'may', 6: 'jun',
        7: 'jul', 8: 'aug', 9: 'sep', 10: 'oct', 11: 'nov', 12: 'dec'
    }

    # Count documents for each month
    for doc in docs:
        month_name = month_names.get(doc.month_number)
        if month_name:
            month_counts[month_name] += 1

    # Serialize the counts into the desired format
    serialized_data = [{'x': month_name, 'y': count} for month_name, count in month_counts.items()]

    # Fill in missing months with count 0
    for month_name in ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']:
        if month_name not in month_counts:
            serialized_data.append({'x': month_name, 'y': 0})

    # Sort serialized_data by month
    serialized_data.sort(key=lambda x: ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'].index(x['x']))

    # Output the serialized data
    return serialized_data
