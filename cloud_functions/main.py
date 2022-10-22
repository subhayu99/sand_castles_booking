def get_removable_files(request):
    request_json = request.get_json()
    objects = request_json.get("items")
    full_paths: list[str] = list(map(lambda object: object.get('name'), objects))
    unique_invoice_names = { x[:-19]: x for x in full_paths }
    return {"objects": list(set(full_paths) - set(unique_invoice_names.values()))}