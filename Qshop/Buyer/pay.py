from alipay import AliPay
import time
def Pay(order_id,money):
    alipay_public_key_string = '''-----BEGIN PUBLIC KEY-----
        MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwyzMdv9vTHhHIaV3LdU9MjMGTs3soeYoDmnFlNipD+iTDtczQXI/mC/t+EsdC6ngeh1ciMjFuU9oMV1LG2LzdWhXDzF+quDrZMBTT42V5S5VEiKxz6xvS94rbVN+aB4xb4lU2GB0HybjJ1YD4lJ4fPge+7ERgDKYc+jwxt03iJBi8m1/ztYMTA3koQaKmZMBrhxMRtykSLmC3lXZ613g88HN440i9nLieJGO1zK2r548H/+Zc9RpJzWGnjokoevRuivwrFoXvH13DGzum+PW0HD8ospxbms5xpmSypvnsok2cDE++DjeFnUQgkaND3jzXBhlCZiWkCb5LOxaYyzNdwIDAQAB
    -----END PUBLIC KEY-----'''

    app_private_key_string = '''-----BEGIN RSA PRIVATE KEY-----
        MIIEogIBAAKCAQEAwyzMdv9vTHhHIaV3LdU9MjMGTs3soeYoDmnFlNipD+iTDtczQXI/mC/t+EsdC6ngeh1ciMjFuU9oMV1LG2LzdWhXDzF+quDrZMBTT42V5S5VEiKxz6xvS94rbVN+aB4xb4lU2GB0HybjJ1YD4lJ4fPge+7ERgDKYc+jwxt03iJBi8m1/ztYMTA3koQaKmZMBrhxMRtykSLmC3lXZ613g88HN440i9nLieJGO1zK2r548H/+Zc9RpJzWGnjokoevRuivwrFoXvH13DGzum+PW0HD8ospxbms5xpmSypvnsok2cDE++DjeFnUQgkaND3jzXBhlCZiWkCb5LOxaYyzNdwIDAQABAoIBAE9oYqfntTi/lvExiRO0tnk+GUrmrWgRZCq5DhJJND+suGhJVilCem1I0uE6bk7YhuQoHgXo6clDbXjoJC64S6VxFjqwQID1kdAkD8FGMb5U43fFdeKwnXeYpMKOPdfOsP5YOZTvaU9jWvgeHuZt92eg67oriJtH+o7uL0g5qOZ+YkcSMWVx/A87+7ujDYMrG8/DKxs8pz/+y1ZFDlrqW9pdM4zXfMXCVmHnS7tgsutr1tNdrZiZDEzNDNT0RgP6b0nCgG35T3s48j7y5SU4UHSA9RrLkEDxcHEDN4oGPpjAT7adXfPIVDtxsDe5igHAEeARtsLyesMxYyLXRJ3GOAECgYEA5vGM+AdjxzZT+rkJ+pHxGJ33K2RJ92/VRMcPwKlfplRzjzeGj4fef86JQKIy3uiHYnr288V/QPe0GDggeDfeaRW8ywPAfrAW1rVwPoBsljxrNd2x/kybmwWWZjRIHzg/AfgRdQjPpo5fOn9qYtiZJBH9leeSE3vcy4S+UVYlgIECgYEA2FnHBpeQDooqj+QoaKUBZGN9vKqVG/F9Infk5H2+Gz1J9q799TwMeQ0i+v+m/iRYf8mNDezxpN12R0jTcVjELf9vIEcJm53LMR+PMpo5D3OsR7GoIKyWE/BeG/JJj82i/Xw5F2xRGWMB1LEeqen4Rs0HAQNeBJlvNzeiLHzVUfcCgYA/GEVMSjCPb59YA4/fXloBQL8Tos22hV498SizmVKhjbcYrLHdquA2CMZk2yuMzPiYBkJL7WxL4qDYcRUl4xWnniG7UWYY9qD2vhFRciK4lP8xc0U61dE5dDhX6fa+WM6WCiEy2VpqBcGsqLz3Dngga63dc6vsGM4E6FpavG94gQKBgEOgBFLuKwwwac9iTLMw6Hd9lb7UPxll6WxNt5EoMLUI+kaOOjleVLO9xHJaWNNVfwgqctmod3vF8YOkotrqGSAbmJupOLqYnvuy1qrFhBJtYKtkP54+9AY1euUXXaECcPD01E+a/tqFlPvrhR8tT/qpeYf6ine7kgTbceif+HnPAoGANCFW3dJxym2FqeuzfLylfDaeDur3Q3LRA065OzpQBD13qfDikLCKpYza8jEeMVJqAi9tJcus5KSjqtyHBeN4pRzjgrCtb/nq0lY9AUv5fbIKynEC2IipjOa3gpLHQV0FD0FDpadZwmnVjZMrg3uUFTq72WhArhPtxDOzlOWCBLE=
    -----END RSA PRIVATE KEY-----'''

    alipay = AliPay(
        appid="2088102179753618",  # 支付宝app的id
        app_notify_url="",  # 回调视图
        app_private_key_string=app_private_key_string,  # 私钥字符
        alipay_public_key_string=alipay_public_key_string,  # 公钥字符
        sign_type="RSA2",  # 加密方法
    )
    # 发起支付
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=order_id,
        total_amount=str(money),  # 将Decimal类型转换为字符串交给支付宝
        subject="商贸商城",
        return_url=None, #完成之后返回
        notify_url=None  # 可选, 不填则使用默认notify url
    )

    # 让用户进行支付的支付宝页面网址
    return "https://openapi.alipaydev.com/gateway.do?" + order_string

if __name__ == '__main__':
    print(time.time())
    print(Pay("10000000","100"))