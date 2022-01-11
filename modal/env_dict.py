from .object import Object
from .proto import api_pb2


class EnvDict(Object):
    """A dictionary of environment variables for images"""

    def __init__(self, env_dict, session=None):
        """Initialize using a dictionary"""
        super()._init_dynamic(session=session)
        self.env_dict = env_dict

    async def _create_impl(self, session):
        req = api_pb2.EnvDictCreateRequest(session_id=session.session_id, env_dict=self.env_dict)
        resp = await session.client.stub.EnvDictCreate(req)
        return resp.env_dict_id
