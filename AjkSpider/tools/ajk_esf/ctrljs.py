import execjs

token1 = 'YmFkZjc3Y2U4MThjMzFiYTFjMDc5MzRlZDM4ZmE3ZDY='
token2 = execjs.compile(open(r"ajk.js").read().decode("utf-8")).call('captcha', token1)
print 'token2:', token2
