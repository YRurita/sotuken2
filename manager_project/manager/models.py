from django.db import models


class Photo(models.Model):

    MAN = 0
    WOMAN = 1

    HOKKAIDO = 0
    TOHOKU = 5
    TOKYO = 10
    CHIBA = 11
    KANAGAWA = 12
    SAITAMA = 13
    TOCHIGI = 14
    IBARAGI = 15
    CHUBU = 20
    KANSAI = 25
    CHUGOKU = 30
    SHIKOKU = 35
    KYUSHU = 40
    OKINAWA = 45

    # 名前
    name = models.CharField(max_length=128)
    # 誕生日
    birthday = models.DateTimeField()
    # 性別
    sex = models.IntegerField(editable=False)
    # 出身地
    address_from = models.IntegerField()
    # 現住所
    current_address = models.IntegerField()
    # メールアドレス
    email = models.EmailField()
