upload_photo = {
    "type": "object",
    "properties": {
        "success": {
            "type": "object",
            "properties": {
                "value": {
                    "type": "string"
                },
                "imageUrl": {
                    "type": "string"
                },
                "imageWidth": {
                    "type": "string"
                },
                "imageHeight": {
                    "type": "string"
                },
                "ratio": {
                    "type": "string"
                }
            },
            "required": [
                "value",
                "imageUrl",
                "imageWidth",
                "imageHeight",
                "ratio"
            ]
        }
    },
    "required": [
        "success"
    ]
}

frequent_foods = {
    "type": "object",
    "properties": {
        "recipes": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "title": {
                        "type": "string"
                    },
                    "portion_id": {
                        "type": "integer"
                    },
                    "portion_amount": {
                        "type": "number"
                    },
                    "portion_description": {
                        "type": "string"
                    },
                    "energy": {
                        "type": "integer"
                    }
                },
                "required": [
                    "id",
                    "title",
                    "portion_id",
                    "portion_amount",
                    "portion_description",
                    "energy"
                ]
            }
        }
    },
    "required": [
        "recipes"
    ]
}
