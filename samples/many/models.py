from django.db import models

class Person(models.Model):
    email = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128, null=True)
    # courses will be placed here by Course

    def __str__(self):
        return self.email

class Course(models.Model):
    title = models.CharField(max_length=128, unique=True)
    members = models.ManyToManyField(Person,
            through='Membership', related_name='courses')

    def __str__(self):
        return self.title

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    LEARNER = 1
    IA = 1000
    GSI = 2000
    INSTRUCTOR = 5000
    ADMIN = 10000

    MEMBER_CHOICES = (
        ( LEARNER, 'Learner'),
        ( IA, 'Instructional Assistant' ),
        ( GSI, 'Grad Student Instructor' ),
        ( INSTRUCTOR, 'Instructor' ),
        ( ADMIN, 'Administrator' ),
    )
    
    role = models.IntegerField(
        choices=MEMBER_CHOICES,
        default=LEARNER,
    )

    def __str__(self):
        return "Person "+ str(self.person.id) + " <--> Course " + str(self.course.id)

# References

# https://docs.djangoproject.com/en/2.1/topics/db/models/#extra-fields-on-many-to-many-relationships

# https://docs.djangoproject.com/en/2.1/ref/models/fields/#choices

# https://docs.djangoproject.com/en/2.1/topics/db/examples/many_to_many/

# https://docs.djangoproject.com/en/2.1/ref/models/fields/#datefield

