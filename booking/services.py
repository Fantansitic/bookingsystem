import re
def check_real_phone(phone:str) -> bool:
    if(len(phone) != 11):
        return False
    mobile = '(134|135|136|137|138|139|150|151|\
            152|157|158|159|182|183|184|187|188|\
            147|178|1705)[1-9]+'
    union = '(130|131|132|155|156|185|186|145|176|1709)[1-9]+'
    telecom = '(13|153|180|181|189|177|1700)[1-9]+'
    return re.search(mobile,phone) or re.search(union,phone) or re.search(telecom,phone)