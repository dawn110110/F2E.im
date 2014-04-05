#encoding=utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Favorite(models.Model):
    id = models.IntegerField(primary_key=True)
    owner_user_id = models.IntegerField(blank=True, null=True)
    involved_type = models.IntegerField(blank=True, null=True)
    involved_topic_id = models.IntegerField(blank=True, null=True)
    involved_reply_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'favorite'

    def __repr__(self):
        return 'favorite user=%r topic_id=%r reply_id=%r (%r..)' % (self.owner_user_id, self.involved_topic_id, self.reply_id, self.created)
    def __unicode__(self):
        return self.__repr__()

class Node(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True)
    slug = models.TextField(blank=True)
    thumb = models.TextField(blank=True)
    introduction = models.TextField(blank=True)
    created = models.TextField(blank=True)
    updated = models.TextField(blank=True)
    plane_id = models.IntegerField(blank=True, null=True)
    topic_count = models.IntegerField(blank=True, null=True)
    custom_style = models.TextField(blank=True)
    limit_reputation = models.IntegerField(blank=True, null=True)
    class Meta:
        db_table = 'node'

    def __repr__(self):
        return 'node_%r_%r (%r, %r)' % (self.id, self.name, self.introduction, self.plane_id)
    def __unicode__(self):
        return self.__repr__()

class Notification(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.TextField(blank=True)
    status = models.IntegerField(blank=True, null=True)
    involved_type = models.IntegerField(blank=True, null=True)
    involved_user_id = models.IntegerField(blank=True, null=True)
    involved_topic_id = models.IntegerField(blank=True, null=True)
    involved_reply_id = models.IntegerField(blank=True, null=True)
    trigger_user_id = models.IntegerField(blank=True, null=True)
    occurrence_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'notification'

    def __repr__(self):
        return 'notification_%r_%s (%r..)' % (self.id, self.content, self.occurrence_time)
    def __unicode__(self):
        return self.__repr__()

class Plane(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True)
    created = models.TextField(blank=True)
    updated = models.TextField(blank=True)
    class Meta:
        db_table = 'plane'

    def __repr__(self):
        return '%r' % self.id
#        return 'plane_%r_%r (%r, %r)' % (self.id, self.name, self.created, self.updated)
    def __unicode__(self):
        return self.__repr__()

class Reply(models.Model):
    id = models.IntegerField(primary_key=True)
    topic_id = models.IntegerField(blank=True, null=True)
    author_id = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    up_vote = models.IntegerField(blank=True, null=True)
    down_vote = models.IntegerField(blank=True, null=True)
    last_touched = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'reply'

    def __repr__(self):
        return 'reply topic_id=%r author_id=%r content=%s' % (self.topic_id, self.author_id, self.content)
    def __unicode__(self):
        return self.__repr__()

class Topic(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(blank=True)
    content = models.TextField(blank=True)
    status = models.IntegerField(blank=True, null=True)
    hits = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    node_id = models.IntegerField(blank=True, null=True)
    author_id = models.IntegerField(blank=True, null=True)
    reply_count = models.IntegerField(blank=True, null=True)
    last_replied_by = models.TextField(blank=True)
    last_replied_time = models.DateTimeField(blank=True, null=True)
    up_vote = models.IntegerField(blank=True, null=True)
    down_vote = models.IntegerField(blank=True, null=True)
    last_touched = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'topic'

    def __repr__(self):
        return 'topic_%r_%s (%s..)' % (self.id, self.title, self.content)
    def __unicode__(self):
        return self.__repr__()

class Transaction(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.IntegerField(blank=True, null=True)
    reward = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    current_balance = models.IntegerField(blank=True, null=True)
    involved_user_id = models.IntegerField(blank=True, null=True)
    involved_topic_id = models.IntegerField(blank=True, null=True)
    involved_reply_id = models.IntegerField(blank=True, null=True)
    occurrence_time = models.TextField(blank=True)
    class Meta:
        db_table = 'transaction'

    def __repr__(self):
        return 'transaction_id=%r_type=%r (%r..)' % (self.id, self.type, self.occurrence_time)
    def __unicode__(self):
        return self.__repr__()

class User(models.Model):
    uid = models.IntegerField(primary_key=True)
    email = models.TextField(blank=True)
    password = models.TextField(blank=True)
    username = models.TextField(blank=True)
    nickname = models.TextField(blank=True)
    avatar = models.TextField(blank=True)
    signature = models.TextField(blank=True)
    location = models.TextField(blank=True)
    website = models.TextField(blank=True)
    company = models.TextField(blank=True)
    role = models.IntegerField(blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)
    reputation = models.IntegerField(blank=True, null=True)
    self_intro = models.TextField(blank=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    twitter = models.TextField(blank=True)
    github = models.TextField(blank=True)
    douban = models.TextField(blank=True)
    last_login = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'user'

    def __repr__(self):
        return 'user_%r_%s (%r..)' % (self.id, self.username, self.email)
    def __unicode__(self):
        return self.__repr__()

class Vote(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.IntegerField(blank=True, null=True)
    involved_type = models.IntegerField(blank=True, null=True)
    involved_user_id = models.IntegerField(blank=True, null=True)
    involved_topic_id = models.IntegerField(blank=True, null=True)
    involved_reply_id = models.IntegerField(blank=True, null=True)
    trigger_user_id = models.IntegerField(blank=True, null=True)
    occurrence_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'vote'

    def __repr__(self):
        return 'vote_%r_%r (%r)' % (self.id, self.status, self.occurrence_time)
    def __unicode__(self):
        return self.__repr__()
