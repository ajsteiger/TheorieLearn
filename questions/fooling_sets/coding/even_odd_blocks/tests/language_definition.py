NUM_ELEMENTS_TO_CHECK = 50


def isInLanguage(x):
    block_lengths = [len(s) for s in x.split("1") if len(s) != 0]
    return sum(le % 2 == 0 for le in block_lengths) == sum(
        le % 2 == 1 for le in block_lengths
    )
