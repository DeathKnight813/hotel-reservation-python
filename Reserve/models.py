# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    adminid = models.AutoField(db_column='AdminID', primary_key=True)  # Field name made lowercase.
    adminname = models.CharField(db_column='AdminName', max_length=50, default='giru',verbose_name='Name')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Admin'


class Bill(models.Model):
    billid = models.AutoField(db_column='BillID', primary_key=True)  # Field name made lowercase.
    resid = models.ForeignKey('Booking', models.DO_NOTHING, db_column='ResID', blank=True, null=True)  # Field name made lowercase.
    rentid = models.ForeignKey('Rent', models.DO_NOTHING, db_column='RentId', blank=True, null=True)  # Field name made lowercase.
    total = models.CharField(db_column='Total', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Bill'


class Billpay(models.Model):
    billpayid = models.AutoField(db_column='BillPayID', primary_key=True)  # Field name made lowercase.
    billid = models.ForeignKey(Bill, models.DO_NOTHING, db_column='BillId', blank=True, null=True)  # Field name made lowercase.
    paytypeid = models.ForeignKey('Paytype', models.DO_NOTHING, db_column='PaytypeId', blank=True, null=True,verbose_name='Type')  # Field name made lowercase.
    dateid = models.DateTimeField(db_column='DateId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'BillPay'


class Booking(models.Model):
    bookingid = models.AutoField(db_column='BookingID', primary_key=True)  # Field name made lowercase.
    admin = models.ForeignKey(Admin, models.DO_NOTHING, db_column='Admin_ID' ,default='1')  # Field name made lowercase.
    customer = models.ForeignKey('Customer', models.DO_NOTHING, db_column='Customer_ID',default='1')  # Field name made lowercase.
    cin_date = models.DateTimeField(db_column='CIN_Date', blank=True, null=True,verbose_name='Check-In Date')  # Field name made lowercase.
    cout_date = models.DateTimeField(db_column='COUT_Date', blank=True, null=True, verbose_name='Check-Out Date')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Booking'


class Customer(models.Model):
    customer_id = models.AutoField(db_column='Customer_ID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=30, blank=True, null=True, verbose_name='First')  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=30, blank=True, null=True,verbose_name='Last')  # Field name made lowercase.
    list_display=('First_Name','Last_Name')
    def __str__(self):
        return self.first_name,self.last_name
    class Meta:
        managed = True
        db_table = 'Customer'


class Paytype(models.Model):
    payid = models.AutoField(db_column='PayID', primary_key=True)  # Field name made lowercase.
    ptype = models.CharField(db_column='PType', max_length=50)  # Field name made lowercase.
    def __str__(self):
        return self.ptype
    class Meta:
        managed = True
        db_table = 'PayType'


class Room(models.Model):
    roomid = models.AutoField(db_column='RoomID', primary_key=True)  # Field name made lowercase.
    roomtype = models.ForeignKey('Roomtype', models.DO_NOTHING, db_column='RoomType', verbose_name='Room Type')  # Field name made lowercase.
    is_reserved = models.NullBooleanField(db_column='IS_Reserved')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ROOM'


class Ratings(models.Model):
    ratingid = models.AutoField(db_column='RatingID', primary_key=True)  # Field name made lowercase.
    rat_description = models.CharField(db_column='Rat_Description', max_length=100, blank=True, null=True, verbose_name='Ratings')  # Field name made lowercase.
    def __str__(self):
        return self.rat_description
    class Meta:
        managed = True
        db_table = 'Ratings'


class Rent(models.Model):
    rentid = models.AutoField(db_column='RentID', primary_key=True)  # Field name made lowercase.
    roomtypeid = models.ForeignKey('Roomtype', models.DO_NOTHING, db_column='RoomTypeID', blank=True, null=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=1, blank=True, null=True)  # Field name made lowercase.
    from_date = models.DateTimeField(db_column='From_Date', blank=True, null=True,verbose_name='Check-In Date')  # Field name made lowercase.
    to_date = models.DateTimeField(db_column='To_Date', blank=True, null=True, verbose_name='Check-Out Date')  # Field name made lowercase.
    isactive = models.NullBooleanField(db_column='ISactive')  # Field name made lowercase.
    def __str__(self):
        return self.account
    class Meta:
        managed = True
        db_table = 'Rent'


class Roomratings(models.Model):
    roomratingid = models.AutoField(db_column='RoomRatingID', primary_key=True)  # Field name made lowercase.
    roomno = models.ForeignKey(Room, models.DO_NOTHING, db_column='RoomNo', blank=True, null=True)  # Field name made lowercase.
    r_code = models.ForeignKey(Ratings, models.DO_NOTHING, db_column='R_Code', blank=True, null=True)  # Field name made lowercase.
    from_date = models.DateTimeField(db_column='From_Date', blank=True, null=True,verbose_name='Check-In Date')  # Field name made lowercase.
    to_date = models.DateTimeField(db_column='To_Date', blank=True, null=True, verbose_name='Check-Out Date')  # Field name made lowercase.
    isactive = models.NullBooleanField(db_column='ISactive')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'RoomRatings'


class Roomtype(models.Model):
    roomtypeid = models.AutoField(db_column='RoomTypeID', primary_key=True)  # Field name made lowercase.
    roomtype = models.CharField(db_column='RoomType', max_length=20, blank=True, null=True,verbose_name='Type')  # Field name made lowercase.
    def __str__(self):
        return self.roomtype
    class Meta:
        managed = True
        db_table = 'RoomType'
