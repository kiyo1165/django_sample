from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManaer):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueEffor('emailは入力必須です。')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(passoword)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is Not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is Not True:
            rail ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""

    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'

    # emailをオーバーライドして入力必須制限、ユニーク成約を付与
    email = models.EmailField('メールアドレス', unique=True)
    #usernameをオーバライドしてNull成約、ユニーク成約の入力を解除
    username = models.CharField(
        'ユーザー名',
        max_length=150,
        black=True,
        null=True,
        help_text="半角アルファベット,半角数字,@/./+/-/_で150文字以内にしてください。",
        validators=[AbstractUser.username_validator],
    )

    USERNAEM_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()