from django.db import models

# Create your models here.


class Banner(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

class AboutUsImage(models.Model):
    image = models.ImageField(upload_to='about_us/')

    def __str__(self):
        return f"About Us Image {self.id}"
    
    class Meta:
        verbose_name = 'About Us Image'
        verbose_name_plural = 'About Us Images'


class TrustedPartner(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255,null=True, blank=True)
    mail = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Trusted Partner'
        verbose_name_plural = 'Trusted Partners'


class Service(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class News(models.Model):
    heading = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='news/')

    def __str__(self):
        return self.heading
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Testimonials(models.Model):
    name = models.CharField(max_length=255)
    feedback = models.TextField()
    rating = models.IntegerField()
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

