"""
Definition of models.
"""

from django.db import models
from django.db.models.fields import related
from django.db.models.fields.files import FileField
from django.contrib.auth.models import User, BaseUserManager 
from django.db.models.signals import post_save

from django.utils import timezone

# Company model

class Company(models.Model):
    company_name = models.CharField(max_length = 254, verbose_name = 'Company name')
    company_address = models.TextField(verbose_name = 'Company address')
    company_tax_no = models.CharField(max_length = 254, verbose_name = 'Company tax number')

    # @Override
    def __str__(self):
        return self.company_name

class Branch(models.Model):
    company = models.ForeignKey(Company, on_delete = models.DO_NOTHING)
    branch_name = models.CharField(max_length = 254, verbose_name = 'Branch name')
    branch_address = models.TextField(verbose_name = 'Branch address')
    branch_tax_no = models.CharField(max_length = 254, verbose_name = 'Branch tax number')
    is_head_office = models.BooleanField(default = False)
    is_sub_branch = models.BooleanField(default = False)

    # @Override
    def __str__(self):
        return self.branch_name

class Department(models.Model):
    department_code = models.CharField(max_length = 10, verbose_name = 'Department code')
    department_name = models.CharField(max_length = 254, verbose_name = 'Department name')
    description = models.TextField()

# User model
class User(BaseUserManager):
    def create_user_base(self, email, password, is_admin, is_hr, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('Email address is required')
        email = self.normalize_email(email)
        user = self.model(email = email,
                               is_admin = is_admin,
                               is_hr = is_hr,
                               last_login = now,
                               join_date = now,
                               **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        user = self.create_user_base(email, password, False, False, **extra_fields)
        return user

    def create_hr(self, email, password, **extra_fields):
        user = self.create_user_base(email, password, False, True, **extra_fields)
        return user

    def create_admin(self, email, password, **extra_fields):
        user = self.create_user_base(email, password, True, False, **extra_fields)
        return user


# Employee model

class Employee(models.Model):
    user = models.OneToOneField(User, related_name = 'user')
    full_name = models.CharField(max_length = 254, verbose_name = 'Full name')
    address = models.TextField(verbose_name = 'Home address')
    phone = models.CharField(max_length = 30, verbose_name = 'Phone number')
    work_email = models.CharField(max_length = 254, verbose_name = 'Work e-mail')
    joindate = models.DateField(verbose_name = 'Join date                                                                                                                                                                                        ')
    resigndate = models.DateField(verbose_name = 'Resign date')
    identity_no = models.CharField(max_length = 100, verbose_name = 'ID card number')
    tax_no = models.CharField(max_length = 254, verbose_name = 'Income tax number')

    company = models.ForeignKey(Company, on_delete = models.DO_NOTHING)


    # @Override
    def __str__(self):
        return self.full_name

    # Save validation
    # @Override
    def save(self, *args, **kwargs):
        if (self.full_name == None or self.user_name == None):
            return
        else:
            super().save(*args, **kwargs)








