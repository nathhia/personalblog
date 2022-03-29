from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, username, name, email, password=None):
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, name=name, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, email, password=None):
        user = self.create_user(username, name, email, password=password)
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    SEX_CHOICES = (
        ('FEM', 'Feminino'),
        ('MAS', 'Masculino'),
        ('NOI', 'Não Informado')
    )

    name = models.CharField(max_length=70, null=False, blank=False)
    email = models.EmailField(_('email address'), unique=True, null=False, blank=False)
    username = models.CharField(max_length=30, null=False, blank=False, unique=True)
    moderator = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=200, null=False, blank=False)
    sex = models.CharField(max_length=3, choices=SEX_CHOICES, null=False, default='NOI')
    birthdate = models.DateField(auto_now=False, auto_now_add=False,  null=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as active. \
                   Unselect this instead of deleting accounts.'))

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def get_short_name(self):
        return self.name.split(" ")[0]

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.username

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email'], name='Restricao de email'),
            models.UniqueConstraint(fields=['username'], name='Restricao de nome de usuario')
        ]
        verbose_name = _('user')
        verbose_name_plural = _('users')
