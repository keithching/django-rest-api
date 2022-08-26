from rest_framework.authentication import TokenAuthentication as BaseTokenAuth
from rest_framework.authtoken.models import Token

class TokenAuthentication(BaseTokenAuth): # overwritting the orginal one
    keyword = 'Bearer'
