def NULL_not_found(object: any) -> int:
    if type(object) is type(None):
        print("Nothing: None ", type(object))
        return 0

    elif type(object) is float:
        print("Cheese: nan ", type(object))
        return 0

    elif type(object) is int :
        print("Zero : 0 ", type(object))
        return 0

    elif type(object) is str :
        print("Empty : ", type(object))
        return 0

    elif type(object) is bool:
        print("Fake: False ",type(object))
        return 0

    else :
        print("Type not Found")
    return 1
