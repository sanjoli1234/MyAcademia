from django.db import models
class Sbranch(models.Model):
    branches = models.CharField(primary_key=True, max_length=20)
    credits = models.IntegerField(blank=True, null=True)
    no_of_courses = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'sbranch'
class Student(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=1)
    email = models.CharField(max_length=30)
    dob = models.DateField()
    branch =  models.ForeignKey(Sbranch, models.DO_NOTHING, db_column='branch')
    fathers_name = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=30)
    mothers_name = models.CharField(max_length=20, blank=True, null=True)
    total_years = models.IntegerField(blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'student'
# Create your models here.



class Slib(models.Model):
    id = models.AutoField(primary_key=True)
    roll_no = models.ForeignKey('Student', models.DO_NOTHING, db_column='roll_no', blank=True, null=True)
    book_id = models.IntegerField(blank=True, null=True)
    book_name = models.CharField(max_length=30)
    issue_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
   

    class Meta:
        managed = True
        db_table = 'slib'
        unique_together = (('issue_date', 'book_id'),)





class Sfine(models.Model):
    age=(('yes','yes'),('no','no'))
    roll_n0 = models.ForeignKey('Student', models.DO_NOTHING, db_column='roll_n0', blank=True, null=True)
    fine = models.IntegerField(blank=True, null=True)
    id = models.OneToOneField('Slib', models.DO_NOTHING, db_column='id', primary_key=True)
    fine_paid = models.CharField(max_length=10, blank=True, null=True,choices=age)

    class Meta:
        managed = True
        db_table = 'sfine'

class Scourse(models.Model):
    course_code = models.CharField(primary_key=True, max_length=20)
    course_name = models.CharField(max_length=20)
    credit = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'scourse'       
class Steach(models.Model):
    iddd = models.AutoField(primary_key=True)
    teacher = models.ForeignKey('Steacher', models.DO_NOTHING, blank=True, null=True)
    course_code = models.ForeignKey(Scourse, models.DO_NOTHING, db_column='course_code', blank=True, null=True)        
    branches = models.ForeignKey(Sbranch, models.DO_NOTHING, db_column='branches', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'steach'


class Steacher(models.Model):
    teacher_id = models.CharField(primary_key=True, max_length=20)
    teacher_name = models.CharField(max_length=20)
    contact = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed =True
        db_table = 'steacher'




class Semester(models.Model):
    idd = models.AutoField(primary_key=True)
    course_code = models.ForeignKey(Scourse, models.DO_NOTHING, db_column='course_code', blank=True, null=True)        
    branches = models.ForeignKey(Sbranch, models.DO_NOTHING, db_column='branches', blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'semester'
        unique_together = (('course_code', 'semester', 'branches'),)
        


class Ucs444Est(models.Model):
    roll_no = models.OneToOneField(Student, models.DO_NOTHING, db_column='roll_no', primary_key=True)
    maximum_marks = models.IntegerField(blank=True, null=True)
    obtained_marks = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ucs444_est'


class Ucs444Mst(models.Model):
    roll_no = models.OneToOneField(Student, models.DO_NOTHING, db_column='roll_no', primary_key=True)
    maximum_marks = models.IntegerField(blank=True, null=True)
    obtained_marks = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ucs444_mst'


class Ucs444Sessional(models.Model):
    roll_no = models.OneToOneField(Student, models.DO_NOTHING, db_column='roll_no', primary_key=True)
    maximum_marks = models.IntegerField(blank=True, null=True)
    obtained_marks = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ucs444_sessional'


class Ucs768Est(models.Model):
    roll_no = models.OneToOneField(Student, models.DO_NOTHING, db_column='roll_no', primary_key=True)
    maximum_marks = models.IntegerField(blank=True, null=True)
    obtained_marks = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ucs768_est'


class Ucs768Mst(models.Model):
    roll_no = models.OneToOneField(Student, models.DO_NOTHING, db_column='roll_no', primary_key=True)
    maximum_marks = models.IntegerField(blank=True, null=True)
    obtained_marks = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ucs768_mst'


class Ucs768Sessional(models.Model):
    roll_no = models.OneToOneField(Student, models.DO_NOTHING, db_column='roll_no', primary_key=True)
    maximum_marks = models.IntegerField(blank=True, null=True)
    obtained_marks = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ucs768_sessional'