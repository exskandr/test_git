from django.db import models


class Repair(models.Model):
    objects = models.Manager()
    repair_name = models.CharField(max_length=150)
    repair_address = models.CharField(max_length=300)
    repair_telephone = models.IntegerField()
    repair_email = models.EmailField()
    repair_other = models.TextField()


    def __str__(self):
        return "%s - address: %s" % (self.repair_name, self.repair_address)


class ServiceClient(models.Model):
    first_name_client = models.CharField(max_length=100)
    second_name_client = models.CharField(max_length=100)
    phone_client = models.IntegerField()
    email_client = models.EmailField()

    def __str__(self):
        return "Name: %s Surname : %s" % (self.first_name_client, self.second_name_client)


class TerminalClient(models.Model):
    CHOISE_ESTIMATE = (
        ('cheap', "Cheap"),
        ('middle', "Middle"),
        ('expensive', "Expensive"),
    )
    client = models.ForeignKey(ServiceClient, on_delete=models.CASCADE)
    terminal_client = models.CharField(max_length=50)
    model_terminal_client = models.CharField(max_length=20)
    sn_terminal_client = models.IntegerField()
    pic_terminal_client = models.ImageField(upload_to='pics')
    problem_terminal_client = models.TextField()
    estimate_terminal_client = models.CharField(max_length=50, choices=CHOISE_ESTIMATE)
    date_time_reception_client = models.DateField(auto_now=False)

    def __str__(self):
        return "Client: %s. Terminal : %s" % (self.client, self.terminal_client)


class ServiceWork(models.Model):
    terminal_work = models.ForeignKey(TerminalClient, on_delete=models.CASCADE)
    s_work = models.TextField()
    price_work = models.FloatField()
    action_work = models.BooleanField(default=False)
    associate_work = models.BooleanField(default=False)
    date_time_reception_work = models.DateField(auto_now=False)

    def __str__(self):
        return "Work: %s Price : %s" % (self.terminal_work, self.price_work)
