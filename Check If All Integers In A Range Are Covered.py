covered = set()
        for start, end in ranges:
            covered.update(range(start, end + 1))
        return all(x in covered for x in range(left, right + 1))
    
