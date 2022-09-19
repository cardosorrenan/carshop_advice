template = {
    "info": {
        "title": "Carshop Advice",
        "description": "API for manage carshop",
        "contact": {
            "responsibleOrganization": "",
            "responsibleDeveloper": "",
            "email": "renanhc96@gmail.com",
            "url": "www.github.com/cardosorrenan",
        },
        "termsOfService": "www.github.com/cardosorrenan",
        "version": "1.0"
    },
    "basePath": "/api/",  # base bash for blueprint registration
    "schemes": [
        "http",
        "https"
    ],
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
        }
    },
}