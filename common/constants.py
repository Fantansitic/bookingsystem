from model_utils.choices import Choices

Form_Status_Wait = 0
Form_Status_Reject = 1
Form_Status_Accept = 2
Form_Status_OutTime = 3

Form_Status_Choices = Choices(
    (Form_Status_Wait,'等待'),
    (Form_Status_Reject,'拒绝'),
    (Form_Status_Accept,'同意'),
    (Form_Status_OutTime,'超时')
)

API_MESSAGE_OK = 200
API_MESSAGE_FORBIDDEN = 403
API_MESSAGE_PARAM_ERROR = 400
API_MESSAGE_NOT_FOUND = 404
API_MESSAGE_SERVER_ERROR = 500

API_MESSAGE_TABLE = Choices(
    (API_MESSAGE_OK, 'OK'),
    (API_MESSAGE_FORBIDDEN, '权限不足'),
    (API_MESSAGE_PARAM_ERROR, '参数错误'),
    (API_MESSAGE_NOT_FOUND, '资源未找到'),
    (API_MESSAGE_SERVER_ERROR, '服务端异常,请稍后再试'),
)

Manager_Level_Admin = 10086
Manager_Level_Visitor = 10085

Manager_Level_Choices = Choices(
    (Manager_Level_Admin,'可读可写'),
    (Manager_Level_Admin,'只读'),
)

AccountDeleted=1
AccountAlive=0

Account_Status_Choices = Choices(
    (AccountDeleted,'删除'),
    (AccountAlive,'存在'),
)

ERROR_ACCOUNT_NOT_EXIT = 4096
ERROR_ACCOUNT_IS_DELETED = 4098
ERROR_ACCOUNT_PASSWORD_FAILE = 4097

ACCOUNT_ERROR_DICT = {ERROR_ACCOUNT_IS_DELETED:"账号已删除",
                      ERROR_ACCOUNT_NOT_EXIT:"账号不存在",
                      ERROR_ACCOUNT_PASSWORD_FAILE:"密码错误"}


ERROR_TOKEN_EMPTY = 12135
ERROR_TOKEN_TIMEOUT = 12131
ERROR_TOKEN_UNKNOWN = 12133
ERROR_TOKEN_TAMPERED = 12138

ERROR_TOKEN_TABLE = Choices(
    (ERROR_TOKEN_EMPTY,'Token为空'),
    (ERROR_TOKEN_TIMEOUT,'Token过期'),
    (ERROR_TOKEN_UNKNOWN,'Token未知错误'),
    (ERROR_TOKEN_TAMPERED,'Token被篡改'),
)


