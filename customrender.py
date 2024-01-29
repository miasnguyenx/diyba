from rest_framework import renderers
import json

class CustomRenderer(renderers.JSONRenderer):
    charset = 'utf-8'
    # media_type = 'application/json'
    # format = 'json'
    def render(self, data, accepted_media_type=None, renderer_context=None):
        print(data)
        print(accepted_media_type)
        print(renderer_context)
        status_code = renderer_context['response'].status_code
        print(type(renderer_context['response'].status_code))
        response = {
          "status": "success",
          "code": "",
          "data": data,
          "message": ""
        }
        if not str(status_code).startswith('2'):
            response["status"] = "error"
            response["data"] = None
            try:
                response["message"] = data["detail"]
            except KeyError:
                response["data"] = data
        return super().render(data=response, accepted_media_type=accepted_media_type)