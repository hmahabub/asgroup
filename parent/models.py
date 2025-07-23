from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='company_logos/', blank=True)
    website_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    description = models.TextField()
    price_min = models.DecimalField(max_digits=10, decimal_places=2)
    price_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def price_range(self):
        if self.price_max and self.price_max != self.price_min:
            return f"${self.price_min} - ${self.price_max}"
        return f"${self.price_min}"

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    author_title = models.CharField(max_length=100)
    rating = models.IntegerField(choices=RATING_CHOICES)
    review_text = models.TextField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author_name} - {self.rating} stars"

    @property
    def star_display(self):
        return '★' * self.rating + '☆' * (5 - self.rating)

class ContactInfo(models.Model):
    whatsapp_number = models.CharField(max_length=20, help_text="Include country code without + or spaces")
    whatsapp_message = models.TextField(default="Hello! I'm interested in your services.")
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return "Contact Information"