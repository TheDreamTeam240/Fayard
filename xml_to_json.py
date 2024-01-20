import xmltodict

def xml_to_json(file_path: str) -> dict:
    data    = open(file=file_path, mode='r')
    xpars   = xmltodict.parse(data.read())

    return xpars
