from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser

class CustomUsrAdomin(UserAdmin):
    # 「まずユーザー名とパスワードを登録してください。」の文言を非表示にする。
    add_form_template = None
    # 表示項目から'username'を削除してemailに変更
    fieldsets = ()