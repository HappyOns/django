from alipay import AliPay
def Pay(order_id,money):
    alipay_public_key_string='''-----BEGIN PUBLIC KEY-----
        MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsLDofX93PGVStfpI4/R3mX22p7EWct0b9TutpGrj/XnukV+ZtkBUez7t6IKa13nBOuMM1RMeUw06FHAX6xhoHK/Uf4HRZmV718M/JTodrsucEKe9OUNDcOPIjPooqLim2W6m7FW/XRLcZFK8yasEDNoCj7W6UPdwBnCvTCpPLOur+lNmgPTEGQRo+5qvcNEKYKJHeZEOzwGTUzyT+fT3LIISLgAK/vKjNg9m2mMlKuT47M1nNpOnaI4sp2SVzQ6Lx/STg301SOmxyvVFM2Uq4hksyIw1xdVa0rDH5vBU+C/M0AfYx8rOOkDB6TyechoDOqOPAXKZ22Zk/Ms/alJxAwIDAQAB
    -----END PUBLIC KEY-----
    '''
    app_private_key_string='''-----BEGIN RSA PRIVATE KEY-----
        MIIEowIBAAKCAQEAhBZrq3NuWXKF7BRjDemkMps3CjUWeub59mcIJ0poDKWQrovIRhXF0+HS4JVWfTwU4Eg/V5mldrGZk4DL52u7jrqkoL+L/bcaxMhQRITQjcZOx8Mw+5MDnaHQ/M0hq4CmG6pW17RBvJvDNxF9+yfgAA65Ipttu1WyazWM25Ff4TaqmyZURqmmyKT4H29xUEgKaAwHY+vuvlF/7IDIZaRl1AOsWJ2m2Xa3shU167KJwCpJ+gWxC1Njhc46W3g8xkI3c0QqDNZOC4kwh9WZcRPevb7GBMfyNjdHVIexy3Hb5kqNyAHYt81LCchj0YC8OTmnfoQ4amDH+6h/4hQEdGvx7wIDAQABAoIBAHX7vOLhcYDuPdd5Al2MA8G8SPaSIulW5ZGFyI+n87bQMKLoctS/X/x5qy411pJ4l0Ea55FsyZJy4vYRRpEI9vhvmNuJHRdcdcmuD5yUceEhcH8Yx+j/EWy8/HrDFD8n47e0eGumNE2vaDkJI9mybXA/tnjGEscRrhP7Oj1p5hW4sUlDCJupm6eJJ9z7y8pN4NAVHjUMUL5fRLm8B6qv5QpajvSptzELIL7UQr/CYNk9oCMX4gTs3CcDq7eRFX+Jye/i6k1soo7udGuy+A2vifAV+JX07ORKeDb3VX0T90H2DO/PgNMLL0N/rm4GUnriDx/vl9En35Ia3wUCQiB3cvkCgYEA+sxbNqDmpXv2iFLJyZIYHS5s7Yqcl05hl6FE302GB04bHPnO2G2TGe9z4O25ScwuU8rF3i0xPJj2dLY7NEOH04Wa24b9tWs4VtRYDIAIgGIcHDaWu2IC1wijedBWveSahaTsZpFPkQtNMg3RfyarOkyzHSQlpw3q0t4EJkSvtRUCgYEAhtPBa80r8R5FG4qPvgup10Wjo5f9f7hAZRTwIpkZExSq2n7qvh+uYN+AcYAmEm0Ddt7FJKWBh7m3k/y93/JqyuHu5ndv0wObsyI1TYKwjq22DQl2toYn1UDOuP7vUHJlQpN7CktZF176vfksc+2s2bx8gkxVNzbgJzqAjOQIk/MCgYB9GkEJn/tNYueYGsvjS4fRzp2xZCo2Y3fU/jHvvaj0reZibs3aMdZl4ocIFS0O/dXCIGzRJfPgiWCu2VPw/xqazZNwnAakX2aMEYIWQit7dvUUsbpAoGRQRVPeaKlMMeNOdPUjOKra7CtGo5Pz/CL/gtD54VUS3qNbKjohqLOI/QKBgFUPTx21qR1LXYoMlrbtIM+BTcWt4+4pzeZ3mTAaqmkRRuDl5S7hSeAv4Ra6JErHn8HktTdzew6nqhug/iFFDP7GHzQi8deMlTQkRsCJzN2W1h3PdKeeZ47wffrUSyLTqPKhnKRX+PL3pvUnOFZDAiOz+FEz2yckZbIaBHPegVLlAoGBAODPRlLzxgIbfhvh/hYL/sZh7b3qa4KGvRx/PRAYinzRuDvj5Sjo72gh/sSeNKjeMK3fM1Y28UTxBJj45N63+GmTlusMYTssbghRgKYmiLKisad6TCBorMRc1+grEyYvdI5k6jhifSvMnZEpWGmuEauwoxSCQA5PgWo3EbuQtxDU
    -----END RSA PRIVATE KEY-----'''
    alipay = AliPay(
        appid="2016101500695777",  # 支付宝app的id
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
        return_url=None,  # 完成之后返回
        notify_url=None  # 可选, 不填则使用默认notify url
    )

    # 让用户进行支付的支付宝页面网址
    return "	https://openapi.alipaydev.com/gateway.do?" + order_string


if __name__ == '__main__':
    print(Pay("100000002", "1000"))