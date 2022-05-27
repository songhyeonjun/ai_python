# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Favorite(models.Model):
    favorite_idx = models.AutoField(primary_key=True)
    member_idx = models.IntegerField()
    place_idx = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'favorite'


class Itinerary(models.Model):
    itinerary_idx = models.IntegerField(primary_key=True)
    member_idx = models.ForeignKey('Member', models.DO_NOTHING, db_column='member_idx')
    itinerary_title = models.CharField(max_length=100)
    itinerary_date = models.DateTimeField()
    itinerary_places = models.CharField(max_length=100)
    itinerary_details = models.CharField(max_length=100, blank=True, null=True)
    itinerary_view = models.IntegerField(blank=True, null=True)
    itinerary_like = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itinerary'


class Itinerarycomment(models.Model):
    itinerarycomment_idx = models.AutoField(db_column='itineraryComment_idx', primary_key=True)  # Field name made lowercase.
    itinerary_idx = models.ForeignKey(Itinerary, models.DO_NOTHING, db_column='itinerary_idx', blank=True, null=True)
    itinerarycomment_comment = models.CharField(db_column='itineraryComment_comment', max_length=100)  # Field name made lowercase.
    member_idx = models.ForeignKey('Member', models.DO_NOTHING, db_column='member_idx')
    itinerarycomment_rgstdate = models.DateTimeField(db_column='itineraryComment_rgstdate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itinerarycomment'


class Member(models.Model):
    member_idx = models.AutoField(primary_key=True)
    member_id = models.CharField(max_length=100, blank=True, null=True)
    member_pw = models.CharField(max_length=100, blank=True, null=True)
    member_naver_token = models.CharField(max_length=100, blank=True, null=True)
    member_google_token = models.CharField(max_length=100, blank=True, null=True)
    member_name = models.CharField(max_length=100)
    member_birth = models.DateField()
    member_addr = models.CharField(max_length=100)
    member_gender = models.IntegerField()
    member_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'member'
        unique_together = (('member_id', 'member_naver_token', 'member_google_token', 'member_name'),)


class Memberstatistics(models.Model):
    memberstatistics_idx = models.AutoField(primary_key=True)
    memberstatistics_name = models.CharField(max_length=100)
    memberstatistics_count = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'memberstatistics'


class Place(models.Model):
    place_idx = models.IntegerField()
    place_big = models.CharField(max_length=100, blank=True, null=True)
    place_number = models.CharField(max_length=100, blank=True, null=True)
    place_small = models.CharField(max_length=100, blank=True, null=True)
    place_city = models.CharField(max_length=100, blank=True, null=True)
    place_dong = models.CharField(max_length=100, blank=True, null=True)
    place_info = models.CharField(max_length=100, blank=True, null=True)
    place_addr = models.CharField(max_length=100, blank=True, null=True)
    place_middle = models.CharField(max_length=100, blank=True, null=True)
    place_area = models.CharField(max_length=100, blank=True, null=True)
    place_img = models.CharField(max_length=100, blank=True, null=True)
    place_mapx = models.CharField(max_length=100, blank=True, null=True)
    place_mapy = models.CharField(max_length=100, blank=True, null=True)
    place_detail = models.CharField(max_length=10000, blank=True, null=True)
    place_view = models.CharField(max_length=100, blank=True, null=True)
    place_like = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'place'


class Placecomment(models.Model):
    placecomment_idx = models.IntegerField(db_column='placeComment_idx', primary_key=True)  # Field name made lowercase.
    memeber_id = models.IntegerField(blank=True, null=True)
    place_idx = models.IntegerField(blank=True, null=True)
    placecomment_mdfydate = models.DateTimeField(db_column='placeComment_mdfydate', blank=True, null=True)  # Field name made lowercase.
    placecomment_traveldate = models.DateTimeField(db_column='placeComment_traveldate', blank=True, null=True)  # Field name made lowercase.
    placecomment_relationship = models.CharField(db_column='placeComment_relationship', max_length=100, blank=True, null=True)  # Field name made lowercase.
    placecomment_title = models.CharField(db_column='placeComment_title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    placecomment_content = models.CharField(db_column='placeComment_content', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'placecomment'


class Placereview(models.Model):
    placereview_idx = models.IntegerField(primary_key=True)
    member_idx = models.ForeignKey(Member, models.DO_NOTHING, db_column='member_idx')
    placereview_title = models.CharField(max_length=100, blank=True, null=True)
    placereview_content = models.CharField(max_length=100, blank=True, null=True)
    placereview_read_cnt = models.IntegerField(blank=True, null=True)
    placereview_rgstdate = models.DateField(blank=True, null=True)
    placereview_rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'placereview'


class Survey(models.Model):
    survey_idx = models.AutoField(primary_key=True)
    survey_question = models.CharField(max_length=100)
    survey_choices = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'survey'


class Surveyresult(models.Model):
    surveyresult_idx = models.AutoField(db_column='surveyResult_idx', primary_key=True)  # Field name made lowercase.
    member_idx = models.ForeignKey(Member, models.DO_NOTHING, db_column='member_idx')
    surveyresult_date = models.DateTimeField(db_column='surveyResult_date')  # Field name made lowercase.
    surveyresult_recommendation = models.CharField(db_column='surveyResult_recommendation', max_length=100)  # Field name made lowercase.
    surveyresult_answers = models.CharField(db_column='surveyResult_answers', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'surveyresult'
