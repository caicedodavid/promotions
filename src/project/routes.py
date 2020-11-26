from project.endpoints import HealthAPI


def register(app):
    app.add_url_rule(
        "/health",
        view_func=HealthAPI.as_view("health"))
