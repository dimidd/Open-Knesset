from knesset.api.resources.base import BaseResource
from links.models import Link

class LinkResource(BaseResource):
    ''' Link API
    '''
    class Meta:
        queryset = Link.objects.select_related('link_type')
        allowed_methods = ['get']
        excludes = ["active", "object_pk", "id"]
        include_resource_uri = False
