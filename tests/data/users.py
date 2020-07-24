DETAIL_INFO = {
    "id": 3,
    "name": "Алексей Поимцев",
    "email": "test@example.com",
    "lang": "ru",
    "rights": {
        "leads": {
            "view": "M",
            "edit": "M",
            "add": "D",
            "delete": "M",
            "export": "M"
        },
        "contacts": {
            "view": "M",
            "edit": "M",
            "add": "D",
            "delete": "M",
            "export": "M"
        },
        "companies": {
            "view": "M",
            "edit": "M",
            "add": "D",
            "delete": "M",
            "export": "M"
        },
        "tasks": {
            "edit": "A",
            "delete": "A"
        },
        "mail_access": False,
        "catalog_access": True,
        "status_rights": [
            {
                "entity_type": "leads",
                "pipeline_id": 3166396,
                "status_id": 142,
                "rights": {
                    "view": "D",
                    "edit": "D",
                    "delete": "D",
                    "export": "D"
                }
            },
            {
                "entity_type": "leads",
                "pipeline_id": 3166396,
                "status_id": 32311027,
                "rights": {
                    "view": "D",
                    "edit": "D",
                    "delete": "D"
                }
            },
            {
                "entity_type": "leads",
                "pipeline_id": 3104455,
                "status_id": 31881115,
                "rights": {
                    "view": "D",
                    "edit": "D",
                    "delete": "D"
                }
            }
        ],
        "is_admin": False,
        "is_free": False,
        "is_active": True,
        "group_id": None,
        "role_id": None
    },
    "_links": {
        "self": {
            "href": "https://example.amocrm.ru/api/v4/users/185848"
        }
    }
}