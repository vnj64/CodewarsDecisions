# * url = "https://www.cnet.com" -> domain name = cnet"
# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"

def domain_name(url):
    static_symbols = ['//', '.']
    url = url.split(static_symbols[0])
    url = str(url[1]).split(static_symbols[1])
    return url[0]

print(domain_name("http://google.com"))