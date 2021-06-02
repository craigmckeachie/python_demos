# kwargs

def get_url(**kwargs):
    
    protocal = kwargs.get("protocal") or "http://"
    host= kwargs.get("host") or "localhost"
    port = kwargs.get("port") or "80"

    return f"{protocal}{host}:{port}"

print(get_url())
print(get_url(host="127.0.0.1"))
print(get_url(protocal='https://', port="3000"))

