from aiohttp import payload_type
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from securite import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="недействительный токен")
    return payload

