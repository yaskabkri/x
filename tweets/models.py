from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    features = models.TextField()
    benefits = models.TextField()
    usps = models.TextField()

class TargetMarket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    demographics = models.JSONField()
    psychographics = models.JSONField()
    segmentation = models.TextField()

class CompetitiveAnalysis(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    competitors = models.TextField()
    swot_analysis = models.JSONField()
    unique_value_proposition = models.TextField()

class PricingStrategy(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cost_analysis = models.DecimalField(max_digits=10, decimal_places=2)
    market_research = models.TextField()
    pricing_model = models.CharField(max_length=50)

class DistributionChannels(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    channels = models.TextField()
    partnerships = models.TextField()
    logistics_fulfillment = models.TextField()

class PromotionalTactics(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    marketing_mix = models.JSONField()
    advertising_promotion = models.TextField()
    sales_promotions = models.TextField()

class CustomerFeedbackIteration(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_feedback = models.TextField()
    market_monitoring = models.TextField()
    continuous_improvement = models.TextField()
