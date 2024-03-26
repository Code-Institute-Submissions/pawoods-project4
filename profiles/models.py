from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import Product


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True,
                                            blank=True)
    default_street_address_1 = models.CharField(max_length=40, null=True,
                                                blank=True)
    default_street_address_2 = models.CharField(max_length=40, null=True,
                                                blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True,
                                            blank=True)
    default_county = models.CharField(max_length=40, null=True,
                                      blank=True)
    default_country = CountryField(blank_label="Country",
                                   null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True,
                                        blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """ Create or update the users profile """
    if created:
        UserProfile.objects.create(user=instance)
    # For existing users, save the profile
    instance.userprofile.save()


class WishList(models.Model):
    profile = models.ForeignKey(UserProfile, null=False, blank=False,
                                on_delete=models.CASCADE,
                                related_name='wishlist')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
