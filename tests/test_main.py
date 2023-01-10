from graphs.main import initalization, querying

def test_initalization():
    inputs = [
        (3, 1, 2, 3),
        (2, 4, 5),
        (4, 6, 7, 8, 9),
    ]

    list_set, len_set, disjointSet = initalization(inputs)

    assert disjointSet.count() == 3

    inputs = [
        (5, 1, 2, 3, 4, 5),
        (7, 6, 7, 8, 9, 10, 11, 12),
        (10, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22),
        (3, 23, 24, 25),
        (1, 26),
    ]

    list_set, len_set, disjointSet = initalization(inputs)

    assert disjointSet.count() == 5


def test_init_query():
    inputs = [
        (3, 1, 2, 3),
        (2, 4, 5),
        (4, 6, 7, 8, 9),
    ]

    list_set, len_set, disjointSet = initalization(inputs)

    queries = [
        (2, 2, 4),
        (2, 4, 5),
        (2, 7, 8),
    ]

    for query in queries:
        querying(len_set, list_set, disjointSet, query[0], query[1:])

    assert disjointSet.count() == 2

    inputs = [
        (5, 1, 2, 3, 4, 5),
        (7, 6, 7, 8, 9, 10, 11, 12),
        (10, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22),
        (3, 23, 24, 25),
        (1, 26),
    ]

    list_set, len_set, disjointSet = initalization(inputs)
    
    queries = [
        # (1, 27),
        (3, 6, 7, 8),
        (3, 2, 8, 15),
        (2, 24, 26),
    ]
    
    for query in queries:
        querying(len_set, list_set, disjointSet, query[0], query[1:])

    assert disjointSet.count() == 2

