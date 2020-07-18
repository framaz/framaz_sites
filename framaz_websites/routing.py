from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import yet_another_pixel_draw.chann.routing as yapd_routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': URLRouter(yapd_routing.websocket_urlpatterns),
})
