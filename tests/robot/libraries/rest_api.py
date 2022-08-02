def extract_logger_level(logger_name, list_jsons):
    print(f"Extracting logger level for {logger_name}")
    try:
        list_jsons = eval(list_jsons)
        if not isinstance(list_jsons, list):
            print("Given object is not instance of list.")
            return None
    except SyntaxError:
        print("Error: Cannot eval given string to list.")
        return None
    print(f"Given list is {list_jsons}")
    return next(
        (
            item['level']
            for item in list_jsons
            if item['logger'] == logger_name
        ),
        None,
    )
