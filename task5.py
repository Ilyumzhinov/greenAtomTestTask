def compare_versions(A, B):
    # Раздели в подверсии и преврати в числа
    asections = list(map(int, A.split('.')))
    bsections = list(map(int, B.split('.')))

    for i in range(len(max(asections, bsections))):
        a = asections[i] if len(asections) > i else 0
        b = bsections[i] if len(bsections) > i else 0
        # Return -1 if version A is older than version B
        if a < b: return -1
        # Return 1 if version A is newer than version B
        if a > b: return 1
    
    # Return 0 if versions A and B are equivalent
    return 0

A, B = "1.10", "1.1"
print(f'Сравнение версий {A} и {B}: {compare_versions(A, B)}')