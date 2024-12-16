from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from itsdangerous import SignatureExpired, BadData
from common import constants as c

class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTH_TOKEN',None)
        if not token:
            raise AuthenticationFailed(f"TOKEN不能为空{c.ERROR_TOKEN_EMPTY}")
        
        from project.settings import JWT_TOKEN_SECRET_KEY
        s = Serializer(
            secret_key=JWT_TOKEN_SECRET_KEY,
            algorithm_name='HS256',
        )
        try:
            detoken = s.loads(token)
            return detoken['mobile'],detoken
        except SignatureExpired:
            raise AuthenticationFailed(f"Token过期请重新登录{c.ERROR_TOKEN_TIMEOUT}")
        except BadData:
            raise AuthenticationFailed(f"Token被篡改{c.ERROR_TOKEN_TAMPERED}")
        except Exception as e:
            raise AuthenticationFailed(f"Token未知错误{c.ERROR_TOKEN_UNKNOWN}:{e}")