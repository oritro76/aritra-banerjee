category = {
    'id': {'type': 'string'},
    'name': {'type': 'string'},
    'createdAt': {'type': 'string'},
    'updatedAt': {'type': 'string'},
}

service = {
    'id': {'type': 'number'},
    'name': {'type': 'string'},
    'createdAt': {'type': 'string'},
    'updatedAt': {'type': 'string'},
}

product = {
    'id': {'type': 'number'},
    'name': {'type': ['string', 'null']},
    'type': {'type': ['string', 'null']},
    'price': {'type': 'number'},
    'shipping': {'type': ['number', 'null']},
    'upc': {'type': ['string', 'null']},
    'description': {'type': ['string', 'null']},
    'manufacturer': {'type': ['string', 'null']},
    'model': {'type': ['string', 'null']},
    'url': {'type': ['string', 'null']},
    'image': {'type': ['string', 'null']},
    'categories': {'type': 'array',
                   'items': {
                        'type': 'object',
                        'properties': {**category},
                        }
                   },
    'createdAt': {'type': 'string'},
    'updatedAt': {'type': 'string'},
}

store = {
    'id': {'type': 'number'},
    'name': {'type': ['string', 'null']},
    'type': {'type': ['string', 'null']},
    'address': {'type': ['string', 'null']},
    'address2': {'type': ['string', 'null']},
    'city': {'type': ['string', 'null']},
    'state': {'type': ['string', 'null']},
    'zip': {'type': ['string', 'null']},
    'lat': {'type': ['number', 'null']},
    'lng': {'type': ['number', 'null']},
    'hours': {'type': ['string', 'null']},
    'services': {'type': 'array',
                 'items': {
                    'type': 'object',
                    'properties': {**service},
                    }
                 },
    'storeservices': {'type': 'object',
                      'properties': {
                            'createdAt': {'type': 'string'},
                            'updatedAt': {'type': 'string'},
                            'storeId': {'type': 'number'},
                            'serviceId': {'type': 'number'},
                        },
                      },
    'createdAt': {'type': ['string', 'null']},
    'updatedAt': {'type': ['string', 'null']},
}

fetch_common = {
    'total': {'type': 'number'},
    'limit': {'type': 'number'},
    'skip': {'type': 'number'},
}

response_create_product = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {**product},
    'required': ['name', 'type', 'upc', 'description', 'model']
}

response_create_store = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {**store},
    'required': ['name', 'address', 'city', 'state', 'zip']
}

response_create_service = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {**service},
    'required': ['name']
}

response_create_category = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {**category},
    'required': ['id', 'name']
}

response_error_400 = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'message': {'type': 'string'},
        'code': {'type': 'number'},
        'className': {'type': 'string'},
        'data': {'type': 'object'},
        'errors': {
            'type': 'array',
            'items': {
                'type': 'string',
            }
        }
    }
}

response_error_500 = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'message': {'type': 'string'},
        'code': {'type': 'number'},
        'className': {'type': 'string'},
        'errors': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'},
                    'type': {'type': 'string'},
                    'path': {'type': 'string'},
                    'value': {'type': 'string'}
                }
            }
        }
    }
}

response_fetch_products = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        **fetch_common,
        'data': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {**product}
            }
        }
    }
}

response_fetch_services = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        **fetch_common,
        'data': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {**service}
            }
        }
    }
}

response_fetch_stores = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        **fetch_common,
        'data': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {**store}
            }
        }
    }
}

response_fetch_categories = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        **fetch_common,
        'data': {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {**category}
            }
        }
    }
}

response_fetch_api_version = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        'version': {'type': 'string'}
    },
    'required': ['version']
}
