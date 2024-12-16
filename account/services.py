import time
import hashlib
from account import models
from django.db.models import Q
from common import constants as c
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def __random_salt() -> str:
    #TODO
    raise

def __salt_password(salt:str,password:str) -> str:
    if salt is None:
        salt=''
    return hashlib.md5((salt + password).encode('utf8')).hexdigest()

def login(account:str,password:str) -> tuple:
    m = models.Account.objects.filter(Q(Mobile=account)|Q(WordId=account)|Q(AccountNumber=account))
    if not m.exists():
        return False,c.ACCOUNT_ERROR_DICT[c.ERROR_ACCOUNT_NOT_EXIT]
    if m[0].Deleted==c.AccountDeleted:
        return False,c.ACCOUNT_ERROR_DICT[c.ERROR_ACCOUNT_IS_DELETED]
    if __salt_password(m[0].Salt,password=password) != m[0].PassWord:
        return False,c.ACCOUNT_ERROR_DICT[c.ERROR_ACCOUNT_PASSWORD_FAILE]
    return True,create_token(m[0].WordId,m[0].AccountNumber,m[0].Mobile)

def create_token(workid:str,accountnumber:str,mobile:str) -> str:
    from project.settings import JWT_TOKEN_SECRET_KEY
    s = Serializer(
        secret_key=JWT_TOKEN_SECRET_KEY,
        expires_in=7*24*60*60,
        algorithm_name='HS256',
    )
    timestamp = int(time.time())
    payload = {
        'wordid':workid,
        'mobile':mobile,
        'account':accountnumber,
        'iat':timestamp,
        'exp': (timestamp + 7*24*60*60),
    }
    token = s.dumps(payload)
    return token.decode('ascii')