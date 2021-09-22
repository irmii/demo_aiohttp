from .views import fronend


def setup_routes(app):
    app.router.add_route('GET', '/', fronend.index)
