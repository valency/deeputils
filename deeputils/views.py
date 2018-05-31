def get_id_or_all(pp, model, account=None):
    """
    Return Django model instance(s) by ID or all
    :param pp: Django rest framework serializer validated data
    :param model: Django model
    :param account: Django account model assigned to the designated model
    :return: Django model instance if ID is provided in pp, or all instances if not
    """
    resp = model.objects
    if account is not None:
        resp = resp.filter(account=account)
    else:
        resp = resp.all()
    if 'id' in pp.validated_data:
        return resp.get(id=pp.validated_data['id']), False
    else:
        return resp, True
