from application.features import core


def register_base_routes(app):
    @app.route("/", methods=["GET", "POST", "PATCH"])
    def hello():
        return "Hello world", 200

    @app.route("/test-deletion", methods=["GET"])
    def test_deletion():
        response = core.test_deletion()
        return response, 200

    @app.route("/test-overwrite", methods=["GET"])
    def test_overwrite():
        response = core.test_overwrite()
        return response, 200




