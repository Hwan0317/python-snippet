def get_formater_vaiables(query:str) -> list[str]:
    parsed_query = Formatter().parse(query)
    result = [val for _, val, _, _  in parsed_query if val is not None]
    return result
