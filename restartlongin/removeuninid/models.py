# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class ActivityDiscount(models.Model):
    activity_id = models.CharField(max_length=64)
    activity_name = models.CharField(max_length=200)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    discount = models.CharField(max_length=5, blank=True, null=True)
    activity_status = models.IntegerField(blank=True, null=True)
    activity_type = models.IntegerField(blank=True, null=True)
    is_push = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    vfrom = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_discount'


class ActivityDiscountGood(models.Model):
    activity_id = models.CharField(max_length=64)
    goods_id = models.CharField(max_length=64)
    discount = models.CharField(max_length=10, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_discount_good'


class AdsBanner(models.Model):
    ads_banner_id = models.CharField(unique=True, max_length=64)
    ads_position_id = models.CharField(max_length=64)
    media_type = models.IntegerField()
    media_url = models.CharField(max_length=200)
    video_url = models.CharField(max_length=200, blank=True, null=True)
    media_link_type = models.IntegerField()
    data_from = models.IntegerField(blank=True, null=True)
    media_link_object = models.CharField(max_length=200, blank=True, null=True)
    media_link_object_desc = models.CharField(max_length=200, blank=True, null=True)
    is_scope = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    ads_status = models.IntegerField()
    seq = models.IntegerField()
    creator = models.CharField(max_length=64)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ads_banner'


class AdsBannerPosition(models.Model):
    position_id = models.CharField(unique=True, max_length=64)
    position_code = models.CharField(max_length=10)
    position_name = models.CharField(max_length=50)
    media_max_count = models.IntegerField(blank=True, null=True)
    position_desc = models.CharField(max_length=100)
    interval_time = models.DecimalField(max_digits=3, decimal_places=1)
    pic_width = models.IntegerField(blank=True, null=True)
    pic_height = models.IntegerField(blank=True, null=True)
    use_scope = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ads_banner_position'


class AdsBulletin(models.Model):
    bulletin_id = models.CharField(unique=True, max_length=64)
    position_id = models.CharField(max_length=64)
    content = models.CharField(max_length=100)
    media_link_type = models.IntegerField()
    media_link_object = models.CharField(max_length=200, blank=True, null=True)
    data_from = models.IntegerField(blank=True, null=True)
    ads_status = models.IntegerField()
    seq = models.IntegerField()
    creator = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    media_link_object_desc = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ads_bulletin'


class AdsBulletinPosition(models.Model):
    position_id = models.IntegerField(unique=True)
    position_desc = models.CharField(max_length=100)
    interval_time = models.IntegerField()
    media_max_count = models.IntegerField()
    use_scope = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ads_bulletin_position'


class AgentActive(models.Model):
    active_id = models.CharField(unique=True, max_length=64)
    column_id = models.CharField(max_length=64, blank=True, null=True)
    position_id = models.CharField(max_length=64)
    active_name = models.CharField(max_length=50, blank=True, null=True)
    active_type = models.IntegerField()
    active_object = models.IntegerField()
    has_expiry = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    active_status = models.IntegerField()
    column_seq = models.IntegerField()
    create_time = models.DateTimeField()
    creator = models.CharField(max_length=64)
    modify_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_active'


class AgentActiveApply(models.Model):
    active_apply_id = models.CharField(unique=True, max_length=64)
    active_id = models.CharField(max_length=64)
    has_expiry = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    apply_person = models.CharField(max_length=64)
    apply_time = models.DateTimeField()
    flow_step = models.IntegerField()
    active_status = models.IntegerField()
    is_valid = models.IntegerField()
    create_time = models.DateTimeField()
    creator = models.CharField(max_length=64)
    modify_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_active_apply'


class AgentActiveApplyGoods(models.Model):
    active_apply_id = models.CharField(unique=True, max_length=64)
    active_id = models.CharField(max_length=64)
    goods_id = models.CharField(max_length=64)
    goods_quatity = models.IntegerField()
    calc_type = models.IntegerField(blank=True, null=True)
    concessional_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_distance = models.CharField(max_length=64, blank=True, null=True)
    delivery_time = models.DateTimeField(blank=True, null=True)
    is_recommend = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'agent_active_apply_goods'


class AgentActiveApplyGoodsSpec(models.Model):
    active_apply_id = models.CharField(max_length=64)
    active_id = models.CharField(max_length=64)
    goods_id = models.CharField(max_length=64)
    spec_id = models.CharField(max_length=64)
    spec_count = models.IntegerField()
    spec_sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'agent_active_apply_goods_spec'


class AgentActiveAuditLog(models.Model):
    active_apply_id = models.CharField(unique=True, max_length=64)
    audit_type = models.IntegerField()
    audit_person_id = models.CharField(max_length=64)
    audit_time = models.DateTimeField()
    audit_result = models.IntegerField()
    reject_reason = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_active_audit_log'


class AgentActiveGoods(models.Model):
    id = models.BigIntegerField(primary_key=True)
    active_goods_id = models.CharField(max_length=64)
    active_id = models.CharField(max_length=64)
    goods_id = models.CharField(max_length=64)
    is_recommend = models.IntegerField()
    price_distance = models.CharField(max_length=64, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    seq = models.IntegerField()
    active_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_active_goods'


class AgentActiveGoodsSpec(models.Model):
    active_goods_id = models.CharField(max_length=64)
    goods_id = models.CharField(max_length=64)
    spec_id = models.CharField(max_length=64)
    spec_count = models.IntegerField()
    spec_price = models.DecimalField(max_digits=10, decimal_places=2)
    spec_sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'agent_active_goods_spec'


class AgentActiveOrder(models.Model):
    id = models.BigIntegerField(primary_key=True)
    active_order_id = models.CharField(unique=True, max_length=64)
    active_id = models.CharField(max_length=64)
    order_id = models.CharField(max_length=64)
    goods_id = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'agent_active_order'


class AgentDeductrate(models.Model):
    province_id = models.CharField(max_length=11)
    city_id = models.CharField(max_length=11, blank=True, null=True)
    county_id = models.CharField(max_length=11, blank=True, null=True)
    percent = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_deductrate'
        unique_together = (('province_id', 'city_id', 'county_id'),)


class AgentGoodsApply(models.Model):
    goods_change_id = models.CharField(unique=True, max_length=64)
    proposer_id = models.CharField(max_length=64)
    goods_id = models.CharField(max_length=64)
    event_type = models.IntegerField()
    apply_time = models.DateTimeField()
    flow_status = models.IntegerField()
    is_valid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'agent_goods_apply'


class AgentGoodsAudit(models.Model):
    goods_change_id = models.CharField(unique=True, max_length=64)
    audit_type = models.IntegerField()
    audit_person_id = models.CharField(max_length=64)
    audit_time = models.DateTimeField()
    audit_result = models.IntegerField()
    reject_reason = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_goods_audit'


class AgentMenu(models.Model):
    menu_id = models.CharField(max_length=64)
    menu_name = models.CharField(max_length=100, blank=True, null=True)
    parent_menu = models.CharField(max_length=64, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    disp_order = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_menu'


class AgentRoles(models.Model):
    role_id = models.CharField(max_length=64, blank=True, null=True)
    role_name = models.CharField(max_length=100, blank=True, null=True)
    role_desc = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_roles'


class AgentRolesPrivilege(models.Model):
    role_id = models.CharField(max_length=64, blank=True, null=True)
    menu_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_roles_privilege'


class AgentSalesperson(models.Model):
    salesperson_id = models.CharField(max_length=64)
    agent_user_id = models.CharField(max_length=64, blank=True, null=True)
    username = models.CharField(max_length=64)
    true_name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=300)
    salt = models.CharField(max_length=64, blank=True, null=True)
    token = models.CharField(max_length=64, blank=True, null=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    user_type = models.IntegerField()
    mobile = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.CharField(max_length=100, blank=True, null=True)
    user_level = models.IntegerField()
    status = models.IntegerField()
    province = models.CharField(max_length=100, blank=True, null=True)
    province_code = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    city_code = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    county_code = models.CharField(max_length=50, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    last_login_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_salesperson'


class AgentShop(models.Model):
    agent_user_id = models.CharField(unique=True, max_length=64)
    shop_id = models.CharField(unique=True, max_length=64)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_shop'


class AgentTemplateResource(models.Model):
    resource_id = models.CharField(unique=True, max_length=64)
    css_details = models.TextField(blank=True, null=True)
    css_path = models.CharField(max_length=100, blank=True, null=True)
    district_details = models.TextField(blank=True, null=True)
    specialty_details = models.TextField(blank=True, null=True)
    district_logo = models.CharField(max_length=255, blank=True, null=True)
    province_code = models.CharField(max_length=50, blank=True, null=True)
    city_code = models.CharField(max_length=50, blank=True, null=True)
    county_code = models.CharField(max_length=50, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_template_resource'


class AgentTopMenu(models.Model):
    menu_id = models.CharField(max_length=64)
    menu_name = models.CharField(max_length=100, blank=True, null=True)
    parent_menu = models.CharField(max_length=64, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    disp_order = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_top_menu'


class AgentTopRoles(models.Model):
    role_id = models.CharField(max_length=64, blank=True, null=True)
    role_name = models.CharField(max_length=100, blank=True, null=True)
    role_desc = models.CharField(max_length=100, blank=True, null=True)
    role_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_top_roles'


class AgentTopRolesPrivilege(models.Model):
    role_id = models.CharField(max_length=64, blank=True, null=True)
    menu_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_top_roles_privilege'


class AgentTopUser(models.Model):
    user_id = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    true_name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=300)
    salt = models.CharField(max_length=64, blank=True, null=True)
    token = models.CharField(max_length=64, blank=True, null=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    user_type = models.IntegerField()
    mobile = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.CharField(max_length=100, blank=True, null=True)
    user_level = models.IntegerField()
    id_card_no = models.CharField(max_length=30, blank=True, null=True)
    status = models.IntegerField()
    province = models.CharField(max_length=100, blank=True, null=True)
    province_code = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    city_code = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    county_code = models.CharField(max_length=50, blank=True, null=True)
    creater = models.CharField(max_length=64)
    created_time = models.DateTimeField()
    modifier = models.CharField(max_length=64, blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    last_login_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_top_user'


class AgentTopUserRole(models.Model):
    user_id = models.CharField(max_length=64, blank=True, null=True)
    role_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_top_user_role'


class AgentUser(models.Model):
    agent_user_id = models.CharField(unique=True, max_length=64)
    username = models.CharField(max_length=64)
    true_name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=300)
    salt = models.CharField(max_length=64, blank=True, null=True)
    token = models.CharField(max_length=64, blank=True, null=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    user_type = models.IntegerField()
    mobile = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.CharField(max_length=100, blank=True, null=True)
    user_level = models.IntegerField()
    status = models.IntegerField()
    province = models.CharField(max_length=100, blank=True, null=True)
    province_code = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    city_code = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    county_code = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    cs_role_code = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    last_login_time = models.DateTimeField(blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    operation_model = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_user'


class AgentUserRelation(models.Model):
    fk_user_id = models.CharField(max_length=64)
    province = models.CharField(max_length=100)
    province_code = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    city_code = models.CharField(max_length=50)
    county = models.CharField(max_length=100)
    county_code = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'agent_user_relation'


class AgentUserRole(models.Model):
    user_id = models.CharField(max_length=64, blank=True, null=True)
    role_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_user_role'


class Article(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    article_id = models.CharField(max_length=255, blank=True, null=True)
    cover_id = models.CharField(max_length=64, blank=True, null=True)
    authour = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    article_content = models.TextField(blank=True, null=True)
    author_icon = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    province = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    district = models.CharField(max_length=500, blank=True, null=True)
    province_code = models.CharField(max_length=50, blank=True, null=True)
    city_code = models.CharField(max_length=50, blank=True, null=True)
    district_code = models.CharField(max_length=50, blank=True, null=True)
    article_tag = models.CharField(max_length=64, blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)
    is_index = models.IntegerField(blank=True, null=True)
    goods_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'


class ArticleCover(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    article_id = models.CharField(max_length=64, blank=True, null=True)
    cover_src = models.CharField(max_length=225, blank=True, null=True)
    article_type = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_cover'


class ArticleMeyki(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    article_id = models.CharField(max_length=255, blank=True, null=True)
    cover_src = models.CharField(max_length=255, blank=True, null=True)
    authour = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    article_content = models.TextField(blank=True, null=True)
    author_icon = models.CharField(max_length=255, blank=True, null=True)
    cover_w = models.CharField(max_length=255, blank=True, null=True)
    cover_h = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    ico = models.CharField(max_length=500, blank=True, null=True)
    province = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    district = models.CharField(max_length=500, blank=True, null=True)
    province_code = models.CharField(max_length=50, blank=True, null=True)
    city_code = models.CharField(max_length=50, blank=True, null=True)
    district_code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_meyki'


class BankAuthenticationInfo(models.Model):
    auth_id = models.CharField(max_length=64)
    bank_id = models.CharField(max_length=64, blank=True, null=True)
    bank_owner_type = models.IntegerField(blank=True, null=True)
    identity_front = models.CharField(max_length=255, blank=True, null=True)
    identity_reverse = models.CharField(max_length=255, blank=True, null=True)
    bank_front = models.CharField(max_length=255, blank=True, null=True)
    bank_reverse = models.CharField(max_length=255, blank=True, null=True)
    bank_status = models.IntegerField(blank=True, null=True)
    refusal_reason = models.CharField(max_length=200, blank=True, null=True)
    remark = models.CharField(max_length=1000, blank=True, null=True)
    overdue_time = models.DateTimeField(blank=True, null=True)
    overdue_status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_authentication_info'


class BankAuthenticationLog(models.Model):
    auth_id = models.CharField(max_length=64)
    bank_id = models.CharField(max_length=64, blank=True, null=True)
    bank_status = models.IntegerField(blank=True, null=True)
    refusal_reason = models.CharField(max_length=200, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_authentication_log'


class BizSwitcherT(models.Model):
    biz_name = models.IntegerField()
    biz_main_id = models.CharField(max_length=64)
    mgt_app = models.IntegerField(blank=True, null=True)
    target_app = models.IntegerField(blank=True, null=True)
    field_type = models.CharField(max_length=3)
    status = models.IntegerField()
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'biz_switcher_t'


class Category(models.Model):
    category_id = models.CharField(unique=True, max_length=50)
    category_cn_name = models.CharField(max_length=40)
    category_en_name = models.CharField(max_length=40, blank=True, null=True)
    category_desc = models.CharField(max_length=200, blank=True, null=True)
    category_path = models.CharField(max_length=500)
    parent_id = models.CharField(max_length=50, blank=True, null=True)
    is_leaf = models.CharField(max_length=1)
    is_show = models.CharField(max_length=1)
    sort_order = models.IntegerField()
    layer_1 = models.CharField(max_length=64, blank=True, null=True)
    layer_2 = models.CharField(max_length=64, blank=True, null=True)
    layer_3 = models.CharField(max_length=64, blank=True, null=True)
    layer_4 = models.CharField(max_length=64, blank=True, null=True)
    layer_5 = models.CharField(max_length=64, blank=True, null=True)
    layer_6 = models.CharField(max_length=64, blank=True, null=True)
    layer_7 = models.CharField(max_length=64, blank=True, null=True)
    layer_8 = models.CharField(max_length=64, blank=True, null=True)
    layer_9 = models.CharField(max_length=64, blank=True, null=True)
    layer_10 = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class CategoryApply(models.Model):
    category_apply_id = models.CharField(max_length=64)
    catact_name = models.CharField(max_length=60, blank=True, null=True)
    catact_phone = models.CharField(max_length=18, blank=True, null=True)
    category_desc = models.CharField(max_length=500, blank=True, null=True)
    remark = models.CharField(max_length=300, blank=True, null=True)
    shop_id = models.CharField(max_length=64)
    apply_status = models.CharField(max_length=1, blank=True, null=True)
    handle_status = models.CharField(max_length=1, blank=True, null=True)
    handle_time = models.DateTimeField(blank=True, null=True)
    feedback = models.CharField(max_length=255, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_apply'


class CategoryApplyImg(models.Model):
    category_apply_img_id = models.CharField(max_length=64)
    fk_category_apply_id = models.CharField(max_length=64)
    apply_img_url = models.CharField(max_length=200, blank=True, null=True)
    apply_img_desc = models.CharField(max_length=500, blank=True, null=True)
    img_sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_apply_img'


class CategoryAttr(models.Model):
    category_attr_id = models.CharField(unique=True, max_length=50)
    fk_category_id = models.CharField(max_length=50)
    attr_alias = models.CharField(max_length=40, blank=True, null=True)
    attr_name = models.CharField(max_length=40)
    parent_id = models.CharField(max_length=50, blank=True, null=True)
    placeholder = models.CharField(max_length=40, blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    is_parent = models.CharField(max_length=1)
    is_show = models.CharField(max_length=1)
    is_must_input = models.CharField(max_length=1)
    is_input = models.CharField(max_length=1)
    is_enum_prop = models.CharField(max_length=1)
    is_key_prop = models.CharField(max_length=1)
    is_sale_prop = models.CharField(max_length=1)
    is_color_prop = models.CharField(max_length=1)
    is_item_prop = models.CharField(max_length=1)
    multi = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'category_attr'


class CategoryAttrValue(models.Model):
    category_attr_value_id = models.CharField(unique=True, max_length=50)
    fk_category_attr_id = models.CharField(max_length=50)
    attr_value = models.CharField(max_length=200)
    is_show = models.CharField(max_length=1)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'category_attr_value'


class CategoryBrand(models.Model):
    category_brand_id = models.CharField(unique=True, max_length=50)
    fk_category_id = models.CharField(max_length=50)
    brand_cn_name = models.CharField(max_length=40, blank=True, null=True)
    brand_en_name = models.CharField(max_length=40, blank=True, null=True)
    brand_desc = models.TextField(blank=True, null=True)
    is_open = models.CharField(max_length=1)
    brand_logo = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_brand'


class CategoryConfChild(models.Model):
    fk_category_conf_master_id = models.CharField(max_length=64, blank=True, null=True)
    column_name = models.CharField(max_length=50)
    sort_order = models.IntegerField()
    state = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_conf_child'


class CategoryConfChildDetail(models.Model):
    fk_category_conf_child_id = models.CharField(max_length=64, blank=True, null=True)
    classification_name = models.CharField(max_length=50)
    classification_img = models.CharField(max_length=200)
    classification_link_type = models.IntegerField(blank=True, null=True)
    classification_link_id = models.CharField(max_length=5000, blank=True, null=True)
    classification_link_name = models.CharField(max_length=200, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    sort_order = models.IntegerField()
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_conf_child_detail'


class CategoryConfMaster(models.Model):
    column_name = models.CharField(max_length=50)
    sort_order = models.SmallIntegerField()
    state = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_conf_master'


class ChatGroup(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    main_user_id = models.CharField(max_length=64, blank=True, null=True)
    manage_user_id = models.CharField(max_length=64, blank=True, null=True)
    chat_group_name = models.CharField(max_length=64, blank=True, null=True)
    chat_group_logo = models.CharField(max_length=128, blank=True, null=True)
    chat_group_type = models.SmallIntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_group'


class ChatGroupRegion(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_user_id = models.CharField(max_length=64, blank=True, null=True)
    fk_chat_group_id = models.CharField(max_length=64, blank=True, null=True)
    province = models.CharField(max_length=32, blank=True, null=True)
    province_code = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    city_code = models.IntegerField(blank=True, null=True)
    district = models.CharField(max_length=32, blank=True, null=True)
    district_code = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_group_region'


class ChatGroupUser(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_user_id = models.CharField(max_length=64, blank=True, null=True)
    fk_chat_group_id = models.CharField(max_length=64, blank=True, null=True)
    group_user_name = models.CharField(max_length=64, blank=True, null=True)
    group_user_role = models.SmallIntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_group_user'


class ChatRecord(models.Model):
    user_a = models.CharField(max_length=20, blank=True, null=True)
    user_b = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_record'


class ChatSaleGoods(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    goods_origin_id = models.CharField(max_length=64)
    goods_name = models.CharField(max_length=200)
    goods_img = models.CharField(max_length=150, blank=True, null=True)
    goods_status = models.IntegerField(blank=True, null=True)
    sku_origin_id = models.CharField(max_length=64)
    sku_name = models.CharField(max_length=64, blank=True, null=True)
    sku_img = models.CharField(max_length=150, blank=True, null=True)
    is_valid = models.IntegerField()
    sku_stock = models.IntegerField(blank=True, null=True)
    brand_name = models.CharField(max_length=50, blank=True, null=True)
    user_origin_id = models.CharField(max_length=64, blank=True, null=True)
    shop_origin_id = models.CharField(max_length=50, blank=True, null=True)
    shop_origin_type = models.IntegerField(blank=True, null=True)
    tax_price_amount = models.CharField(max_length=50, blank=True, null=True)
    price_amount = models.CharField(max_length=50, blank=True, null=True)
    profit_percent = models.CharField(max_length=10, blank=True, null=True)
    profit_amount = models.CharField(max_length=50, blank=True, null=True)
    vol = models.IntegerField(blank=True, null=True)
    shelves_time = models.DateTimeField(blank=True, null=True)
    down_shelves_time = models.DateTimeField(blank=True, null=True)
    column_id = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_sale_goods'


class ChatUser(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    login_name = models.CharField(max_length=64, blank=True, null=True)
    pwd = models.CharField(max_length=64, blank=True, null=True)
    account_user_id = models.CharField(max_length=64, blank=True, null=True)
    user_type = models.SmallIntegerField(blank=True, null=True)
    user_from = models.SmallIntegerField(blank=True, null=True)
    salt = models.CharField(max_length=64, blank=True, null=True)
    nick_name = models.CharField(max_length=64, blank=True, null=True)
    company_name = models.CharField(max_length=64, blank=True, null=True)
    amount_total = models.CharField(max_length=32, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    sex = models.SmallIntegerField(blank=True, null=True)
    logo = models.CharField(max_length=128, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_user'


class ChatUserCommission(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_user_id = models.CharField(max_length=64, blank=True, null=True)
    fk_sale_goods_id = models.CharField(max_length=64, blank=True, null=True)
    goods_origin_id = models.CharField(max_length=64)
    sku_origin_id = models.CharField(max_length=64)
    shop_origin_id = models.CharField(max_length=50, blank=True, null=True)
    order_origin_id = models.CharField(max_length=64, blank=True, null=True)
    order_origin_type = models.IntegerField(blank=True, null=True)
    price_amount = models.CharField(max_length=32, blank=True, null=True)
    amount = models.CharField(max_length=32, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_user_commission'


class ChatUserCustomer(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_user_id = models.CharField(max_length=64, blank=True, null=True)
    fk_user_customer_id = models.CharField(max_length=64, blank=True, null=True)
    user_customer_name = models.CharField(max_length=64, blank=True, null=True)
    user_customer_img = models.CharField(max_length=200, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_user_customer'


class ChatUserFriends(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_user_id = models.CharField(max_length=64, blank=True, null=True)
    fk_user_friend_id = models.CharField(max_length=64, blank=True, null=True)
    vol = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_user_friends'


class ChatUserFriendsSaleVol(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_chat_user_friend_id = models.CharField(max_length=64, blank=True, null=True)
    fk_user_id = models.CharField(max_length=64, blank=True, null=True)
    fk_sale_goods_id = models.CharField(max_length=64, blank=True, null=True)
    vol = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_user_friends_sale_vol'


class ChatUserGoods(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_user_id = models.CharField(max_length=64, blank=True, null=True)
    fk_sale_goods_id = models.CharField(max_length=64, blank=True, null=True)
    goods_origin_id = models.CharField(max_length=64)
    sku_origin_id = models.CharField(max_length=64)
    shop_origin_id = models.CharField(max_length=50, blank=True, null=True)
    share_count = models.IntegerField(blank=True, null=True)
    is_sale = models.CharField(max_length=1, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_user_goods'


class ChatUserIdentity(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    identity_no = models.CharField(max_length=20, blank=True, null=True)
    identity_name = models.CharField(max_length=20, blank=True, null=True)
    identity_img1 = models.CharField(max_length=200, blank=True, null=True)
    identity_img2 = models.CharField(max_length=200, blank=True, null=True)
    auth_platform = models.SmallIntegerField(blank=True, null=True)
    auth_no = models.CharField(max_length=20, blank=True, null=True)
    auth_lv = models.SmallIntegerField(blank=True, null=True)
    verify_state = models.SmallIntegerField(blank=True, null=True)
    verify_fail_cause = models.CharField(max_length=200, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(db_column='MODIFIER', max_length=64, blank=True, null=True)  # Field name made lowercase.
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_user_identity'


class ChatUserIntegral(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_user_id = models.CharField(max_length=64, blank=True, null=True)
    integral = models.CharField(max_length=64, blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_user_integral'


class ChatUserRule(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    rule_code = models.CharField(max_length=32, blank=True, null=True)
    rule_name = models.CharField(max_length=64, blank=True, null=True)
    rule_integral = models.CharField(max_length=64, blank=True, null=True)
    rule_explain = models.CharField(max_length=255, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_user_rule'


class ChatUserWsWithdraw(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_user_id = models.CharField(max_length=64, blank=True, null=True)
    fk_apply_withdraw_id = models.CharField(max_length=64, blank=True, null=True)
    amount = models.CharField(max_length=64, blank=True, null=True)
    spbill_create_ip = models.CharField(max_length=64, blank=True, null=True)
    partner_trade_no = models.CharField(max_length=64, blank=True, null=True)
    desc = models.CharField(max_length=200, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_user_ws_withdraw'


class CommissionAccount(models.Model):
    account_id = models.CharField(unique=True, max_length=64)
    account_name = models.CharField(max_length=50)
    account = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'commission_account'


class CommissionAccountRelation(models.Model):
    fk_commission_pool_id = models.CharField(max_length=64)
    fk_account_id = models.CharField(max_length=64)
    divide_percent = models.DecimalField(max_digits=5, decimal_places=2)
    creator = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modified_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'commission_account_relation'


class CommissionDivideBatch(models.Model):
    batch_id = models.CharField(max_length=64)
    fk_commission_pool_id = models.CharField(max_length=64)
    batch_year = models.CharField(max_length=10)
    batch_no = models.CharField(max_length=20)
    batch_money = models.DecimalField(max_digits=10, decimal_places=2)
    batch_money_remainder = models.DecimalField(max_digits=10, decimal_places=2)
    batch_status = models.IntegerField()
    creator = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modified_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commission_divide_batch'


class CommissionDivideItem(models.Model):
    divide_item_id = models.CharField(max_length=64)
    fk_commission_pool_id = models.CharField(max_length=64)
    fk_account_id = models.CharField(max_length=64)
    account_name = models.CharField(max_length=50)
    account = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    fk_batch_id = models.CharField(max_length=64, blank=True, null=True)
    batch_no = models.CharField(max_length=20, blank=True, null=True)
    divide_percent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    divide_money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    received_money = models.DecimalField(max_digits=10, decimal_places=2)
    fk_pay_account_id = models.CharField(max_length=64, blank=True, null=True)
    pay_account = models.CharField(max_length=20, blank=True, null=True)
    pay_account_name = models.CharField(max_length=50, blank=True, null=True)
    divide_status = models.IntegerField(blank=True, null=True)
    divide_time = models.DateTimeField(blank=True, null=True)
    creator = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commission_divide_item'


class CommissionIncomeItem(models.Model):
    fk_commission_pool_id = models.CharField(max_length=64)
    fk_order_id = models.CharField(max_length=64)
    order_no = models.CharField(max_length=64)
    order_money = models.DecimalField(max_digits=10, decimal_places=2)
    commission_percent = models.DecimalField(max_digits=5, decimal_places=2)
    commission_money = models.DecimalField(max_digits=10, decimal_places=2)
    recording_time = models.DateTimeField()
    creator = models.CharField(max_length=64)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'commission_income_item'


class CommissionPool(models.Model):
    commission_pool_id = models.CharField(unique=True, max_length=64)
    commission_type = models.IntegerField()
    commission_from = models.CharField(max_length=64)
    percent = models.DecimalField(max_digits=10, decimal_places=2)
    account_of_money = models.DecimalField(max_digits=10, decimal_places=2)
    batch_no = models.CharField(max_length=20, blank=True, null=True)
    creator = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commission_pool'


class CsUser(models.Model):
    cs_user_account = models.CharField(max_length=32, blank=True, null=True)
    cs_user_pwd = models.CharField(max_length=32, blank=True, null=True)
    cs_user_nickname = models.CharField(max_length=32, blank=True, null=True)
    cs_user_name = models.CharField(max_length=32, blank=True, null=True)
    cs_user_tel = models.CharField(max_length=20, blank=True, null=True)
    cs_user_img = models.CharField(max_length=100, blank=True, null=True)
    cs_user_lv = models.CharField(max_length=1, blank=True, null=True)
    cs_user_type = models.CharField(max_length=64, blank=True, null=True)
    cs_user_state = models.CharField(max_length=1, blank=True, null=True)
    cs_role_name = models.CharField(max_length=64, blank=True, null=True)
    is_online = models.CharField(max_length=1, blank=True, null=True)
    start_work_dt = models.CharField(max_length=10, blank=True, null=True)
    end_work_dt = models.CharField(max_length=10, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cs_user'


class CsUserHistory(models.Model):
    cs_order_no = models.CharField(max_length=50, blank=True, null=True)
    app_user_id = models.CharField(max_length=50, blank=True, null=True)
    app_chat_id = models.CharField(max_length=50, blank=True, null=True)
    app_user_domain = models.CharField(max_length=30, blank=True, null=True)
    app_user_address = models.CharField(max_length=200, blank=True, null=True)
    app_visit_count = models.IntegerField(blank=True, null=True)
    cs_user_id = models.CharField(max_length=30, blank=True, null=True)
    service_flow_state = models.CharField(max_length=1, blank=True, null=True)
    service_type = models.CharField(max_length=64, blank=True, null=True)
    visit_dt = models.DateTimeField(blank=True, null=True)
    service_dt = models.DateTimeField(blank=True, null=True)
    end_dt = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cs_user_history'


class CsUserTotal(models.Model):
    id = models.IntegerField(primary_key=True)
    cs_user_id = models.CharField(max_length=30, blank=True, null=True)
    cs_chat_id = models.CharField(max_length=30, blank=True, null=True)
    today_count = models.IntegerField(blank=True, null=True)
    history_count = models.IntegerField(blank=True, null=True)
    now_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cs_user_total'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class EhAliPayLog(models.Model):
    ali_pay_log_id = models.CharField(max_length=64)
    notify_time = models.DateTimeField()
    notify_type = models.CharField(max_length=64)
    notify_id = models.CharField(max_length=64)
    sign_type = models.CharField(max_length=64)
    sign = models.TextField()
    out_trade_no = models.CharField(max_length=64, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    payment_type = models.CharField(max_length=4, blank=True, null=True)
    trade_no = models.CharField(max_length=64)
    trade_status = models.CharField(max_length=64)
    seller_id = models.CharField(max_length=30)
    seller_email = models.CharField(max_length=100)
    buyer_id = models.CharField(max_length=30)
    buyer_email = models.CharField(max_length=100)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    body = models.CharField(max_length=512, blank=True, null=True)
    gmt_create = models.DateTimeField(blank=True, null=True)
    gmt_payment = models.DateTimeField(blank=True, null=True)
    is_total_fee_adjust = models.CharField(max_length=1, blank=True, null=True)
    use_coupon = models.CharField(max_length=1, blank=True, null=True)
    discount = models.CharField(max_length=64, blank=True, null=True)
    refund_status = models.CharField(max_length=64, blank=True, null=True)
    gmt_refund = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_ali_pay_log'


class EhAliRefundLog(models.Model):
    order_id = models.CharField(max_length=64, blank=True, null=True)
    code = models.CharField(max_length=60, blank=True, null=True)
    msg = models.CharField(max_length=60, blank=True, null=True)
    buyer_logon_id = models.CharField(max_length=60, blank=True, null=True)
    buyer_user_id = models.CharField(max_length=60, blank=True, null=True)
    fund_change = models.CharField(max_length=60, blank=True, null=True)
    gmt_refund_pay = models.CharField(max_length=60, blank=True, null=True)
    open_id = models.CharField(max_length=60, blank=True, null=True)
    out_trade_no = models.CharField(max_length=60, blank=True, null=True)
    refund_fee = models.CharField(max_length=60, blank=True, null=True)
    send_back_fee = models.CharField(max_length=60, blank=True, null=True)
    trade_no = models.CharField(max_length=60, blank=True, null=True)
    refund_detail_item_list = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_ali_refund_log'


class EhArtical(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    artical_id = models.CharField(max_length=255, blank=True, null=True)
    artical_src = models.CharField(max_length=255, blank=True, null=True)
    authour = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    artical_content = models.TextField(blank=True, null=True)
    artical_icon = models.CharField(max_length=255, blank=True, null=True)
    src_width = models.CharField(max_length=255, blank=True, null=True)
    src_length = models.CharField(max_length=255, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    ico = models.CharField(max_length=500, blank=True, null=True)
    province = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    district = models.CharField(max_length=500, blank=True, null=True)
    province_code = models.CharField(max_length=50, blank=True, null=True)
    city_code = models.CharField(max_length=50, blank=True, null=True)
    district_code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_artical'


class EhArticalAds(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    artical_id = models.CharField(max_length=255, blank=True, null=True)
    artical_src = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_artical_ads'


class EhArticalPhoto(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    artical_id = models.CharField(max_length=255, blank=True, null=True)
    artical_photo = models.CharField(max_length=255, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_artical_photo'


class EhDeliveryAddress(models.Model):
    delivery_address_id = models.CharField(max_length=64)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    address_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    post_code = models.CharField(max_length=255, blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_delivery_address'


class EhGoodsTicket(models.Model):
    id = models.BigIntegerField(primary_key=True)
    goods_ticket_id = models.CharField(max_length=64, blank=True, null=True)
    ticket_name = models.CharField(max_length=64)
    fk_ticket_id = models.CharField(max_length=64)
    goods_id = models.CharField(max_length=64)
    shop_id = models.CharField(max_length=64)
    ticket_percent = models.CharField(max_length=64, blank=True, null=True)
    ticket_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ticket_use_type = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'eh_goods_ticket'


class EhHomepageItem(models.Model):
    id = models.IntegerField(primary_key=True)
    item_id = models.CharField(max_length=64, blank=True, null=True)
    item_name = models.CharField(max_length=200, blank=True, null=True)
    item_ico = models.CharField(max_length=255, blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    sort_no = models.IntegerField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_homepage_item'


class EhIdentity(models.Model):
    user_id = models.CharField(max_length=64, blank=True, null=True)
    identity_id = models.CharField(max_length=64, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    id_number = models.CharField(max_length=18, blank=True, null=True)
    front = models.CharField(max_length=255, blank=True, null=True)
    back = models.CharField(max_length=255, blank=True, null=True)
    license = models.CharField(max_length=255, blank=True, null=True)
    license_number = models.CharField(max_length=64, blank=True, null=True)
    is_check = models.IntegerField(blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    reject_reason = models.CharField(max_length=2000, blank=True, null=True)
    final_check = models.CharField(max_length=64, blank=True, null=True)
    verifier_role = models.CharField(max_length=64, blank=True, null=True)
    verifier_id = models.CharField(max_length=64, blank=True, null=True)
    back_img_befor = models.CharField(max_length=255, blank=True, null=True)
    back_img_after = models.CharField(max_length=255, blank=True, null=True)
    identity_type = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    back_number = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_identity'


class EhIndexAds(models.Model):
    ads_id = models.CharField(max_length=64)
    category = models.CharField(max_length=2)
    province_id = models.IntegerField(blank=True, null=True)
    province_name = models.CharField(max_length=255, blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    city_name = models.CharField(max_length=255, blank=True, null=True)
    county_id = models.IntegerField(blank=True, null=True)
    county_name = models.CharField(max_length=255, blank=True, null=True)
    img_url = models.CharField(max_length=255, blank=True, null=True)
    push_province_id = models.CharField(max_length=11, blank=True, null=True)
    push_province_name = models.CharField(max_length=40, blank=True, null=True)
    push_city_id = models.CharField(max_length=11, blank=True, null=True)
    push_city_name = models.CharField(max_length=40, blank=True, null=True)
    push_county_id = models.CharField(max_length=11, blank=True, null=True)
    push_county_name = models.CharField(max_length=40, blank=True, null=True)
    proxy_id = models.CharField(max_length=64, blank=True, null=True)
    begin_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    days = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    shop_name = models.CharField(max_length=200, blank=True, null=True)
    goods_id = models.CharField(max_length=64, blank=True, null=True)
    goods_name = models.CharField(max_length=200, blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_index_ads'


class EhIndexAdsCopy(models.Model):
    ads_id = models.CharField(max_length=64)
    category = models.CharField(max_length=2)
    province_id = models.IntegerField(blank=True, null=True)
    province_name = models.CharField(max_length=255, blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    city_name = models.CharField(max_length=255, blank=True, null=True)
    county_id = models.IntegerField(blank=True, null=True)
    county_name = models.CharField(max_length=255, blank=True, null=True)
    img_url = models.CharField(max_length=255, blank=True, null=True)
    push_province_id = models.CharField(max_length=11, blank=True, null=True)
    push_province_name = models.CharField(max_length=40, blank=True, null=True)
    push_city_id = models.CharField(max_length=11, blank=True, null=True)
    push_city_name = models.CharField(max_length=40, blank=True, null=True)
    push_county_id = models.CharField(max_length=11, blank=True, null=True)
    push_county_name = models.CharField(max_length=40, blank=True, null=True)
    proxy_id = models.CharField(max_length=64, blank=True, null=True)
    begin_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    days = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    shop_name = models.CharField(max_length=200, blank=True, null=True)
    goods_id = models.CharField(max_length=64, blank=True, null=True)
    goods_name = models.CharField(max_length=200, blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_index_ads_copy'


class EhKeywords(models.Model):
    keyword_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    keyword = models.CharField(max_length=128, blank=True, null=True)
    genre = models.CharField(max_length=11, blank=True, null=True)
    hits = models.IntegerField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_keywords'


class EhKeywordsDiscover(models.Model):
    keyword_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    keyword = models.CharField(max_length=128, blank=True, null=True)
    hits = models.IntegerField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_keywords_discover'


class EhLogistics(models.Model):
    company_num = models.IntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.CharField(max_length=64, blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    logistics_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_logistics'


class EhOrderRefund(models.Model):
    order_id = models.CharField(max_length=64)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    order_sn = models.CharField(max_length=255)
    refund_sn = models.CharField(max_length=255)
    refund_status = models.IntegerField()
    refund_reason = models.TextField(blank=True, null=True)
    order_money = models.DecimalField(max_digits=10, decimal_places=2)
    refund_money = models.DecimalField(max_digits=10, decimal_places=2)
    refund_plat = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    refund_mobile = models.CharField(max_length=255, blank=True, null=True)
    fail_reason = models.CharField(max_length=255, blank=True, null=True)
    refund_time = models.CharField(max_length=15, blank=True, null=True)
    add_time = models.CharField(max_length=15, blank=True, null=True)
    refund_goods_status = models.IntegerField()
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2)
    reship_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'eh_order_refund'


class EhRefoundLog(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    refound_id = models.CharField(max_length=255, blank=True, null=True)
    order_id = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    shop_id = models.CharField(max_length=255, blank=True, null=True)
    refound_money = models.CharField(max_length=255, blank=True, null=True)
    refound_time = models.CharField(max_length=255, blank=True, null=True)
    refound_reason = models.CharField(max_length=255, blank=True, null=True)
    refond_plat = models.CharField(max_length=255, blank=True, null=True)
    refound_status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_refound_log'


class EhReship(models.Model):
    order_id = models.CharField(max_length=64)
    reship_bn = models.CharField(max_length=50)
    reship_money = models.DecimalField(max_digits=10, decimal_places=2)
    reship_status = models.IntegerField()
    reship_msg = models.TextField()
    delivery_no = models.CharField(max_length=50, blank=True, null=True)
    delivery = models.CharField(max_length=50, blank=True, null=True)
    addtime = models.CharField(max_length=50, blank=True, null=True)
    backtime = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_reship'


class EhReshipGoods(models.Model):
    reship_id = models.IntegerField()
    order_id = models.IntegerField()
    goods_name = models.CharField(max_length=255, blank=True, null=True)
    goods_id = models.CharField(max_length=255, blank=True, null=True)
    goods_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    goods_num = models.IntegerField(blank=True, null=True)
    goods_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    goods_image = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_reship_goods'


class EhSpecialtyTravel(models.Model):
    travel_id = models.CharField(max_length=64, blank=True, null=True)
    travel_name = models.CharField(max_length=100, blank=True, null=True)
    travel_name_img = models.CharField(max_length=255, blank=True, null=True)
    travel_img = models.CharField(max_length=255, blank=True, null=True)
    share_img = models.CharField(max_length=255, blank=True, null=True)
    travel_info_url = models.CharField(max_length=255, blank=True, null=True)
    travel_adder = models.CharField(max_length=500, blank=True, null=True)
    travel_tel = models.CharField(max_length=255, blank=True, null=True)
    travel_desc = models.TextField(blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    is_del = models.CharField(max_length=2, blank=True, null=True)
    province_code = models.CharField(max_length=50, blank=True, null=True)
    province_name = models.CharField(max_length=100, blank=True, null=True)
    city_code = models.CharField(max_length=50, blank=True, null=True)
    city_name = models.CharField(max_length=100, blank=True, null=True)
    county_code = models.CharField(max_length=50, blank=True, null=True)
    county_name = models.CharField(max_length=100, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_specialty_travel'


class EhSpecialtyTravelAds(models.Model):
    ads_id = models.CharField(max_length=64)
    travel_id = models.CharField(max_length=64)
    title = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    img_src = models.CharField(db_column='Img_src', max_length=255, blank=True, null=True)  # Field name made lowercase.
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    pay_type = models.IntegerField(blank=True, null=True)
    moneys = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pay_time = models.DateTimeField(blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    pay_status = models.IntegerField(blank=True, null=True)
    pay_reson = models.CharField(max_length=255, blank=True, null=True)
    t_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=11, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_specialty_travel_ads'


class EhTastesCate(models.Model):
    proxy_id = models.CharField(max_length=64, blank=True, null=True)
    cate_id = models.CharField(max_length=64, blank=True, null=True)
    cate_name = models.CharField(max_length=255, blank=True, null=True)
    cate_img = models.CharField(max_length=255, blank=True, null=True)
    stauts = models.CharField(max_length=2, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_tastes_cate'


class EhTastesCollect(models.Model):
    collect_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    proxy_id = models.CharField(max_length=64, blank=True, null=True)
    collect_identity = models.CharField(max_length=255, blank=True, null=True)
    collect_type = models.CharField(max_length=2, blank=True, null=True)
    keyword = models.CharField(max_length=64, blank=True, null=True)
    search_img = models.CharField(max_length=255, blank=True, null=True)
    order_source = models.CharField(max_length=2, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_tastes_collect'


class EhTastesGoods(models.Model):
    proxy_id = models.CharField(max_length=64, blank=True, null=True)
    cate_id = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    goods_id = models.CharField(max_length=64, blank=True, null=True)
    specialty_desc = models.CharField(max_length=255, blank=True, null=True)
    is_slide = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_tastes_goods'


class EhTastesProxy(models.Model):
    proxy_id = models.CharField(max_length=64)
    operators_id = models.CharField(max_length=64, blank=True, null=True)
    district_logo = models.CharField(max_length=255, blank=True, null=True)
    district_desc = models.TextField(blank=True, null=True)
    district_desc2 = models.TextField(blank=True, null=True)
    specialty = models.TextField(blank=True, null=True)
    specialty2 = models.TextField(blank=True, null=True)
    is_feature = models.CharField(max_length=2, blank=True, null=True)
    template_code = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_tastes_proxy'


class EhTastesSpecialty(models.Model):
    proxy_id = models.CharField(max_length=64, blank=True, null=True)
    goods_id = models.CharField(max_length=64, blank=True, null=True)
    specialty_img = models.CharField(max_length=100, blank=True, null=True)
    specialty_desc = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_tastes_specialty'


class EhTastesTemplate(models.Model):
    proxy_id = models.CharField(max_length=64, blank=True, null=True)
    template_name = models.CharField(max_length=255, blank=True, null=True)
    template_code = models.CharField(max_length=64, blank=True, null=True)
    template_url = models.CharField(max_length=255, blank=True, null=True)
    is_default = models.CharField(max_length=64, blank=True, null=True)
    status = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    province_code = models.CharField(max_length=50, blank=True, null=True)
    city_code = models.CharField(max_length=50, blank=True, null=True)
    county_code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_tastes_template'


class EhTastesYpGallery(models.Model):
    yp_gallery_id = models.CharField(max_length=50)
    province = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    show_order = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_tastes_yp_gallery'


class EhTsguserBank(models.Model):
    bank_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    bank_no = models.CharField(max_length=50, blank=True, null=True)
    bank_user = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=50, blank=True, null=True)
    bank_province_code = models.CharField(max_length=255, blank=True, null=True)
    bank_province_name = models.CharField(max_length=255, blank=True, null=True)
    bank_city_code = models.CharField(max_length=255, blank=True, null=True)
    bank_city_name = models.CharField(max_length=255, blank=True, null=True)
    bank_county_code = models.IntegerField(blank=True, null=True)
    bank_county_name = models.CharField(max_length=40, blank=True, null=True)
    bank_address = models.CharField(max_length=500, blank=True, null=True)
    logo = models.CharField(max_length=50, blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    owner_id = models.CharField(max_length=18, blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_tsguser_bank'


class EhUnionPayLog(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    biztype = models.CharField(db_column='bizType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orderid = models.CharField(db_column='orderId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txnsubtype = models.CharField(db_column='txnSubType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    signature = models.TextField(blank=True, null=True)
    traceno = models.CharField(db_column='traceNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    settleamt = models.CharField(db_column='settleAmt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    settlecurrencycode = models.CharField(db_column='settleCurrencyCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    settledate = models.CharField(db_column='settleDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txntype = models.CharField(db_column='txnType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    certid = models.CharField(db_column='certId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    encoding = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    queryid = models.CharField(db_column='queryId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    accesstype = models.CharField(db_column='accessType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    respmsg = models.CharField(db_column='respMsg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tracetime = models.CharField(db_column='traceTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txntime = models.CharField(db_column='txnTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    merid = models.CharField(db_column='merId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    currencycode = models.CharField(db_column='currencyCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    respcode = models.CharField(db_column='respCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    signmethod = models.CharField(db_column='signMethod', max_length=255, blank=True, null=True)  # Field name made lowercase.
    txnamt = models.CharField(db_column='txnAmt', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eh_union_pay_log'


class EhUser(models.Model):
    user_id = models.CharField(max_length=64, blank=True, null=True)
    user_sex = models.IntegerField(blank=True, null=True)
    real_name = models.CharField(max_length=32, blank=True, null=True)
    nick_name = models.CharField(max_length=20, blank=True, null=True)
    user_qq = models.CharField(max_length=20, blank=True, null=True)
    user_phone = models.CharField(max_length=11, blank=True, null=True)
    user_email = models.CharField(max_length=50, blank=True, null=True)
    user_photo = models.CharField(max_length=150, blank=True, null=True)
    last_time = models.DateTimeField(blank=True, null=True)
    retail_id = models.CharField(max_length=10, blank=True, null=True)
    user_status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_user'


class EhUserBank(models.Model):
    bank_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    bank_no = models.CharField(max_length=50, blank=True, null=True)
    bank_user = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=50, blank=True, null=True)
    bank_province_code = models.CharField(max_length=255, blank=True, null=True)
    bank_province_name = models.CharField(max_length=255, blank=True, null=True)
    bank_city_code = models.CharField(max_length=255, blank=True, null=True)
    bank_city_name = models.CharField(max_length=255, blank=True, null=True)
    bank_county_code = models.IntegerField(blank=True, null=True)
    bank_county_name = models.CharField(max_length=40, blank=True, null=True)
    bank_address = models.CharField(max_length=500, blank=True, null=True)
    logo = models.CharField(max_length=200, blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    owner_id = models.CharField(max_length=18, blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_user_bank'


class EhUserBonus(models.Model):
    user_id = models.CharField(max_length=64, blank=True, null=True)
    bonus_no = models.CharField(max_length=100, blank=True, null=True)
    bonus_id = models.CharField(max_length=64, blank=True, null=True)
    bonus_name = models.CharField(max_length=50, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bonus_status = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_user_bonus'


class EhUserHobby(models.Model):
    hobby_id = models.CharField(max_length=64)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    item_type = models.CharField(max_length=10, blank=True, null=True)
    item_id = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_user_hobby'


class EhUserMoneyLog(models.Model):
    user_money_log_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    money = models.CharField(max_length=50, blank=True, null=True)
    money_type_log_code = models.CharField(max_length=64, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    user_money_type_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_user_money_log'


class EhUserMoneyTypeLog(models.Model):
    money_type_log_id = models.CharField(max_length=64, blank=True, null=True)
    money_type_log_code = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    creater = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_user_money_type_log'


class EhUserTransferList(models.Model):
    user_transfer_id = models.CharField(max_length=64, blank=True, null=True)
    pay_user_id = models.CharField(max_length=64, blank=True, null=True)
    receive_user_id = models.CharField(max_length=64, blank=True, null=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_user_transfer_list'


class EhWeixinPayLog(models.Model):
    weixin_pay_log_id = models.CharField(max_length=64, blank=True, null=True)
    appid = models.CharField(max_length=32, blank=True, null=True)
    bank_type = models.CharField(max_length=16, blank=True, null=True)
    cash_fee = models.IntegerField(blank=True, null=True)
    fee_type = models.CharField(max_length=8, blank=True, null=True)
    is_subscribe = models.CharField(max_length=1, blank=True, null=True)
    mch_id = models.CharField(max_length=32, blank=True, null=True)
    nonce_str = models.CharField(max_length=32, blank=True, null=True)
    openid = models.CharField(max_length=128, blank=True, null=True)
    out_trade_no = models.CharField(max_length=32, blank=True, null=True)
    result_code = models.CharField(max_length=16, blank=True, null=True)
    return_code = models.CharField(max_length=16, blank=True, null=True)
    sign = models.CharField(max_length=255, blank=True, null=True)
    time_end = models.CharField(max_length=14, blank=True, null=True)
    total_fee = models.IntegerField(blank=True, null=True)
    trade_type = models.CharField(max_length=16, blank=True, null=True)
    transaction_id = models.CharField(max_length=32, blank=True, null=True)
    nick_name = models.CharField(max_length=200, blank=True, null=True)
    share_user_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_weixin_pay_log'


class EhWeixinRefundLog(models.Model):
    order_id = models.CharField(max_length=64, blank=True, null=True)
    return_code = models.CharField(max_length=60, blank=True, null=True)
    return_msg = models.CharField(max_length=200, blank=True, null=True)
    appid = models.CharField(max_length=60, blank=True, null=True)
    mch_id = models.CharField(max_length=60, blank=True, null=True)
    nonce_str = models.CharField(max_length=200, blank=True, null=True)
    sign = models.CharField(max_length=200, blank=True, null=True)
    result_code = models.CharField(max_length=60, blank=True, null=True)
    transaction_id = models.CharField(max_length=80, blank=True, null=True)
    out_trade_no = models.CharField(max_length=100, blank=True, null=True)
    out_refund_no = models.CharField(max_length=100, blank=True, null=True)
    refund_id = models.CharField(max_length=60, blank=True, null=True)
    refund_channel = models.CharField(max_length=60, blank=True, null=True)
    refund_fee = models.CharField(max_length=60, blank=True, null=True)
    coupon_refund_fee = models.CharField(max_length=60, blank=True, null=True)
    total_fee = models.CharField(max_length=60, blank=True, null=True)
    coupon_refund_count = models.CharField(max_length=60, blank=True, null=True)
    cash_refund_fee = models.CharField(max_length=20, blank=True, null=True)
    err_code = models.CharField(max_length=255, blank=True, null=True)
    err_code_des = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eh_weixin_refund_log'


class EmallOrderHistoryLogs(models.Model):
    order_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    pay_name = models.CharField(max_length=10, blank=True, null=True)
    pay_time = models.DateTimeField(blank=True, null=True)
    goods_id = models.CharField(max_length=64, blank=True, null=True)
    spec_id = models.CharField(max_length=64, blank=True, null=True)
    goods_count = models.IntegerField(blank=True, null=True)
    category_id = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emall_order_history_logs'


class EsActives(models.Model):
    actives_id = models.CharField(max_length=64, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    amount = models.CharField(max_length=500, blank=True, null=True)
    actives_name = models.CharField(max_length=50, blank=True, null=True)
    descs = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_push = models.CharField(max_length=64, blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    vfrom = models.IntegerField(blank=True, null=True)
    img_src = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_actives'


class EsAdmin(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_admin'


class EsAdsCostrate(models.Model):
    exposure_num_percost = models.FloatField()
    click_num_percost = models.FloatField()
    creater = models.CharField(max_length=64)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'es_ads_costrate'


class EsAdsRenewal(models.Model):
    id = models.BigIntegerField(primary_key=True)
    verrify_record_id = models.BigIntegerField()
    renewal = models.BigIntegerField()
    creater = models.CharField(max_length=64)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'es_ads_renewal'


class EsAdsStats(models.Model):
    ads_stats_id = models.CharField(max_length=64, blank=True, null=True)
    shop_ads_id = models.CharField(max_length=64, blank=True, null=True)
    ad_id = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    c_time = models.DateTimeField(blank=True, null=True)
    c_type = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    c_time_str = models.DateTimeField()
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_ads_stats'


class EsAdsVerifyRecord(models.Model):
    shop_id = models.CharField(max_length=64)
    cost = models.IntegerField()
    remaing = models.FloatField()
    exposure_num = models.DecimalField(max_digits=64, decimal_places=0, blank=True, null=True)
    click_num = models.DecimalField(max_digits=64, decimal_places=0, blank=True, null=True)
    position = models.IntegerField()
    requires = models.CharField(max_length=300, blank=True, null=True)
    picture = models.CharField(max_length=300, blank=True, null=True)
    banner_pic = models.CharField(max_length=300, blank=True, null=True)
    status = models.IntegerField()
    create_time = models.DateTimeField()
    creater = models.CharField(max_length=64, blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_ads_verify_record'


class EsApointOrder(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    order_id = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    shop_id = models.CharField(max_length=255, blank=True, null=True)
    shop_name = models.CharField(max_length=255, blank=True, null=True)
    goods_id = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    contact_phone = models.CharField(max_length=255, blank=True, null=True)
    shop_tel = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.CharField(max_length=255, blank=True, null=True)
    creater = models.CharField(max_length=255, blank=True, null=True)
    modify_time = models.CharField(max_length=255, blank=True, null=True)
    modifier = models.CharField(max_length=255, blank=True, null=True)
    order_sn = models.CharField(max_length=255, blank=True, null=True)
    is_delete = models.CharField(max_length=255, blank=True, null=True)
    es_is_read = models.CharField(max_length=255, blank=True, null=True)
    eh_is_read = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_apoint_order'


class EsAppAds(models.Model):
    ads_id = models.CharField(max_length=64)
    shop_id = models.CharField(max_length=64)
    title = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    img_src = models.CharField(db_column='Img_src', max_length=255, blank=True, null=True)  # Field name made lowercase.
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    pay_type = models.IntegerField(blank=True, null=True)
    moneys = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pay_time = models.DateTimeField(blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    pay_status = models.IntegerField(blank=True, null=True)
    pay_reson = models.CharField(max_length=255, blank=True, null=True)
    t_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=11, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_app_ads'


class EsAppAdsInfo(models.Model):
    ads_info_id = models.CharField(max_length=64, blank=True, null=True)
    ads_range = models.CharField(max_length=64, blank=True, null=True)
    ads_range_name = models.CharField(max_length=64, blank=True, null=True)
    ads_level = models.CharField(max_length=64, blank=True, null=True)
    ads_level_name = models.CharField(max_length=64, blank=True, null=True)
    ads_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ads_begin_date = models.CharField(max_length=20, blank=True, null=True)
    ads_days = models.IntegerField(blank=True, null=True)
    ads_num_max = models.IntegerField(blank=True, null=True)
    ads_status = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_app_ads_info'


class EsAppAdsPeriod(models.Model):
    ads_period_id = models.CharField(max_length=64, blank=True, null=True)
    ads_info_id = models.CharField(max_length=64, blank=True, null=True)
    ads_period_serial = models.IntegerField(blank=True, null=True)
    ads_putin_count = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_app_ads_period'


class EsAppVersion(models.Model):
    version_id = models.CharField(max_length=64, blank=True, null=True)
    os = models.CharField(max_length=40, blank=True, null=True)
    version_code = models.IntegerField(blank=True, null=True)
    version_name = models.CharField(max_length=255, blank=True, null=True)
    des = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    download = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    app_type = models.CharField(max_length=11, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_app_version'


class EsBackOrder(models.Model):
    back_order_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    fk_order_back_info_id = models.CharField(max_length=50, blank=True, null=True)
    delivery_company = models.CharField(max_length=255, blank=True, null=True)
    delivery_number = models.CharField(max_length=255, blank=True, null=True)
    order_id = models.CharField(max_length=64, blank=True, null=True)
    delivery_type_id = models.IntegerField(blank=True, null=True)
    invoice_no = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    action_user = models.CharField(max_length=30, blank=True, null=True)
    consignee = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    county_code = models.CharField(max_length=10, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    province_code = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    city_code = models.CharField(max_length=10, blank=True, null=True)
    district = models.CharField(max_length=10, blank=True, null=True)
    sign_building = models.CharField(max_length=120, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    zipcode = models.CharField(max_length=60, blank=True, null=True)
    tel = models.CharField(max_length=60, blank=True, null=True)
    mobile = models.CharField(max_length=60, blank=True, null=True)
    best_time = models.CharField(max_length=120, blank=True, null=True)
    postscript = models.CharField(max_length=255, blank=True, null=True)
    img1 = models.CharField(max_length=255, blank=True, null=True)
    img2 = models.CharField(max_length=255, blank=True, null=True)
    img3 = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=120, blank=True, null=True)
    insure_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    suppliers_id = models.SmallIntegerField(blank=True, null=True)
    creater = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=255, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_back_order'


class EsBonus(models.Model):
    bonus_id = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    less_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    get_nums = models.IntegerField(blank=True, null=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    nums = models.IntegerField(blank=True, null=True)
    out_nums = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_push = models.CharField(max_length=64, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    p_type = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    vfrom = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_bonus'


class EsBrandChain(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    brand_id = models.CharField(max_length=255, blank=True, null=True)
    brand_logo = models.CharField(max_length=255, blank=True, null=True)
    brand_name = models.CharField(max_length=255, blank=True, null=True)
    brand_desc = models.TextField(blank=True, null=True)
    brand_img = models.CharField(max_length=255, blank=True, null=True)
    brand_src = models.CharField(max_length=255, blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    brand_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_brand_chain'


class EsCommunity(models.Model):
    community_id = models.CharField(max_length=64)
    c_name = models.CharField(max_length=100, blank=True, null=True)
    c_address = models.CharField(max_length=100, blank=True, null=True)
    c_lat = models.CharField(max_length=100, blank=True, null=True)
    c_lng = models.CharField(max_length=100, blank=True, null=True)
    c_erma = models.CharField(max_length=100, blank=True, null=True)
    c_photo = models.CharField(max_length=255, blank=True, null=True)
    c_introduce = models.CharField(max_length=300, blank=True, null=True)
    owner_id = models.CharField(max_length=64, blank=True, null=True)
    openfire_id = models.CharField(max_length=64, blank=True, null=True)
    level = models.CharField(max_length=64, blank=True, null=True)
    maxmenbernum = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    ring_group_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_community'


class EsCommunityMember(models.Model):
    community_id = models.CharField(max_length=64)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    remark_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_community_member'


class EsCommunityRedpacket(models.Model):
    redpacket_id = models.CharField(max_length=64)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    total_money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    left_money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_num = models.IntegerField(blank=True, null=True)
    left_num = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_community_redpacket'


class EsCommunityRedpacketDetail(models.Model):
    redpacket_id = models.CharField(max_length=64)
    money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    receive_user_id = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_community_redpacket_detail'


class EsCron(models.Model):
    cron_id = models.CharField(max_length=64, blank=True, null=True)
    type = models.IntegerField()
    less_time = models.DateTimeField()
    message = models.TextField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_cron'


class EsCronTime(models.Model):
    cron_id = models.CharField(max_length=64, blank=True, null=True)
    act_time = models.DateTimeField(blank=True, null=True)
    order_sn = models.CharField(max_length=50, blank=True, null=True)
    sqls = models.TextField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_cron_time'


class EsDeliveryAddress(models.Model):
    delivery_address_id = models.CharField(unique=True, max_length=64)
    address_type = models.IntegerField(blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    address_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=18, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    province_code = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    city_code = models.CharField(max_length=10, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    county_code = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=1)
    post_code = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    is_default = models.CharField(max_length=1, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_delivery_address'


class EsDiscounts(models.Model):
    discounts_id = models.CharField(max_length=64, blank=True, null=True)
    good_id = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    discount = models.CharField(max_length=10, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_push = models.CharField(max_length=64, blank=True, null=True)
    dsct_name = models.CharField(max_length=30, blank=True, null=True)
    dsct_type = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_discounts'


class EsEbTransferredLog(models.Model):
    order_id = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_eb_transferred_log'


class EsFreeActive(models.Model):
    free_id = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64)
    name = models.CharField(max_length=50, blank=True, null=True)
    img_src = models.CharField(db_column='Img_src', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nums = models.IntegerField(blank=True, null=True)
    less_nums = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_push = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    vfrom = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_free_active'


class EsFreight(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_shop_id = models.CharField(max_length=64, blank=True, null=True)
    freight_name = models.CharField(max_length=255, blank=True, null=True)
    agent_type = models.IntegerField(blank=True, null=True)
    agent_user = models.CharField(max_length=64, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    create_user = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_freight'


class EsFreightDatail(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_freight_id = models.CharField(max_length=64, blank=True, null=True)
    freight_type = models.IntegerField(blank=True, null=True)
    freight_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fk_china_id = models.CharField(max_length=64, blank=True, null=True)
    china_name = models.CharField(max_length=64, blank=True, null=True)
    post_goods_count = models.IntegerField(blank=True, null=True)
    create_user = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=64, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_freight_datail'


class EsGoods(models.Model):
    goods_id = models.CharField(max_length=64)
    fk_category_brand_id = models.CharField(max_length=64, blank=True, null=True)
    fk_freight_id = models.CharField(max_length=64, blank=True, null=True)
    brand_name = models.CharField(max_length=50, blank=True, null=True)
    goods_sn = models.CharField(max_length=20, blank=True, null=True)
    goods_name = models.CharField(max_length=200, blank=True, null=True)
    goods_img = models.CharField(max_length=150, blank=True, null=True)
    shop_id = models.CharField(max_length=64)
    market_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shop_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    express_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    goods_stock = models.IntegerField(blank=True, null=True)
    sale_count = models.IntegerField(blank=True, null=True)
    warn_stock = models.IntegerField(blank=True, null=True)
    goods_unit = models.CharField(max_length=10, blank=True, null=True)
    goods_spec = models.TextField(blank=True, null=True)
    goods_desc = models.TextField(blank=True, null=True)
    attr_cat_id = models.CharField(max_length=64, blank=True, null=True)
    goods_status = models.IntegerField(blank=True, null=True)
    is_shelves = models.IntegerField(blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)
    send_province_id = models.IntegerField(blank=True, null=True)
    send_city_id = models.IntegerField(blank=True, null=True)
    send_district_id = models.IntegerField(blank=True, null=True)
    send_address = models.CharField(max_length=255, blank=True, null=True)
    invoice_type = models.IntegerField(blank=True, null=True)
    invoice_desc = models.CharField(max_length=255, blank=True, null=True)
    invoice_support_type = models.IntegerField(blank=True, null=True)
    is_refund = models.IntegerField(blank=True, null=True)
    shop_classify = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    purchase = models.IntegerField(blank=True, null=True)
    delete_flag = models.IntegerField(blank=True, null=True)
    shelves_time = models.DateTimeField(blank=True, null=True)
    down_shelves_time = models.DateTimeField(blank=True, null=True)
    history_id = models.IntegerField(blank=True, null=True)
    is_online_buy = models.CharField(max_length=255, blank=True, null=True)
    is_order = models.CharField(max_length=255, blank=True, null=True)
    is_delivery = models.CharField(max_length=255, blank=True, null=True)
    is_phone_order = models.CharField(max_length=255, blank=True, null=True)
    delivery_desc = models.CharField(max_length=255, blank=True, null=True)
    is_push = models.CharField(max_length=64, blank=True, null=True)
    vfrom = models.IntegerField(blank=True, null=True)
    is_support_logistic = models.CharField(max_length=2, blank=True, null=True)
    is_merchant = models.CharField(max_length=2, blank=True, null=True)
    logistic_desc = models.CharField(max_length=500, blank=True, null=True)
    merchant_desc = models.CharField(max_length=500, blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    panic_buying_start = models.DateTimeField(blank=True, null=True)
    panic_buying_end = models.DateTimeField(blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    select_spec_label = models.CharField(max_length=50, blank=True, null=True)
    price_interval = models.CharField(max_length=50, blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)
    quality_certification = models.TextField(blank=True, null=True)
    cost_examination = models.TextField(blank=True, null=True)
    activity_desc = models.CharField(max_length=500, blank=True, null=True)
    purchase_url = models.CharField(max_length=200, blank=True, null=True)
    deduction = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_goods'


class EsGoodsGallerys(models.Model):
    goods_id = models.CharField(max_length=64)
    shop_id = models.CharField(max_length=64)
    goods_img = models.CharField(max_length=150)
    img_type = models.IntegerField(blank=True, null=True)
    delete_flag = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    img_sequence = models.IntegerField(blank=True, null=True)
    is_cover = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_goods_gallerys'


class EsGoodsHistory(models.Model):
    goods_id = models.CharField(max_length=64)
    goods_sn = models.CharField(max_length=20, blank=True, null=True)
    goods_name = models.CharField(max_length=50)
    goods_img = models.CharField(max_length=150, blank=True, null=True)
    shop_id = models.CharField(max_length=64)
    market_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shop_price = models.DecimalField(max_digits=10, decimal_places=2)
    express_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    goods_stock = models.IntegerField(blank=True, null=True)
    sale_count = models.IntegerField(blank=True, null=True)
    warn_stock = models.IntegerField(blank=True, null=True)
    goods_unit = models.CharField(max_length=10)
    goods_spec = models.TextField(blank=True, null=True)
    goods_desc = models.TextField()
    attr_cat_id = models.CharField(max_length=64)
    goods_status = models.IntegerField()
    is_shelves = models.IntegerField(blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)
    is_refund = models.IntegerField(blank=True, null=True)
    shop_classify = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    purchase = models.IntegerField(blank=True, null=True)
    delete_flag = models.IntegerField(blank=True, null=True)
    shelves_time = models.DateTimeField(blank=True, null=True)
    down_shelves_time = models.DateTimeField(blank=True, null=True)
    parent_id = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'es_goods_history'


class EsGoodsLike(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    goods_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_goods_like'


class EsGoodsMyCats(models.Model):
    attr_cat_id = models.CharField(max_length=64, blank=True, null=True)
    cat_name = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_goods_my_cats'


class EsInvoice(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    invoice_id = models.CharField(max_length=64, blank=True, null=True)
    order_id = models.CharField(max_length=64, blank=True, null=True)
    goods_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    invoice_info = models.CharField(max_length=255, blank=True, null=True)
    creater = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=255, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_invoice'


class EsLogistics(models.Model):
    logistics_id = models.CharField(max_length=255, blank=True, null=True)
    logistics_company = models.CharField(max_length=255, blank=True, null=True)
    logistics_number = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    order_id = models.CharField(max_length=64, blank=True, null=True)
    delivery_type_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(db_column='STATUS')  # Field name made lowercase.
    invoice_no = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    action_user = models.CharField(max_length=30, blank=True, null=True)
    consignee = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    country = models.SmallIntegerField(blank=True, null=True)
    province = models.SmallIntegerField(blank=True, null=True)
    city = models.SmallIntegerField(blank=True, null=True)
    district = models.SmallIntegerField(blank=True, null=True)
    sign_building = models.CharField(max_length=120, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    zipcode = models.CharField(max_length=60, blank=True, null=True)
    tel = models.CharField(max_length=60, blank=True, null=True)
    mobile = models.CharField(max_length=60, blank=True, null=True)
    best_time = models.CharField(max_length=120, blank=True, null=True)
    postscript = models.CharField(max_length=255, blank=True, null=True)
    remark = models.CharField(max_length=120, blank=True, null=True)
    insure_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    suppliers_id = models.SmallIntegerField(blank=True, null=True)
    creater = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(db_column='MODIFIER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_logistics'


class EsLogisticsDetail(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    logistics_id = models.CharField(max_length=64, blank=True, null=True)
    logistics_number = models.CharField(max_length=255, blank=True, null=True)
    time = models.CharField(max_length=255, blank=True, null=True)
    status_desc = models.CharField(max_length=255, blank=True, null=True)
    creater = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=50, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_logistics_detail'


class EsLogisticsOld(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    logistics_company = models.CharField(max_length=255, blank=True, null=True)
    logistics_number = models.CharField(max_length=255, blank=True, null=True)
    order_id = models.CharField(max_length=64, blank=True, null=True)
    logistics_id = models.CharField(max_length=255, blank=True, null=True)
    creater = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=255, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_logistics_old'


class EsLotterSystem(models.Model):
    lotter_system_id = models.CharField(max_length=64, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    nums = models.IntegerField()
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_lotter_system'


class EsMallOrder(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    order_id = models.CharField(max_length=64, blank=True, null=True)
    order_out_time = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    delivery_address_id = models.CharField(max_length=64, blank=True, null=True)
    order_status = models.CharField(max_length=6, blank=True, null=True)
    ship_status = models.CharField(max_length=10, blank=True, null=True)
    pay_status = models.CharField(max_length=10, blank=True, null=True)
    back_status = models.IntegerField(blank=True, null=True)
    pay_name = models.CharField(max_length=10, blank=True, null=True)
    pay_union_type = models.CharField(max_length=11, blank=True, null=True)
    pay_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    order_sn = models.CharField(unique=True, max_length=64, blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    express_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pay_money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    e_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pay_all_num = models.CharField(max_length=255, blank=True, null=True)
    delivery = models.CharField(max_length=50, blank=True, null=True)
    delivery_no = models.CharField(max_length=50, blank=True, null=True)
    confirm_time = models.DateTimeField(blank=True, null=True)
    is_back = models.IntegerField(blank=True, null=True)
    remind_deliver = models.DateTimeField(blank=True, null=True)
    status_code = models.CharField(max_length=10, blank=True, null=True)
    is_speciality = models.IntegerField(blank=True, null=True)
    query_id = models.CharField(max_length=255, blank=True, null=True)
    is_deliver = models.CharField(max_length=255, blank=True, null=True)
    common = models.CharField(max_length=255, blank=True, null=True)
    delever_ondition = models.CharField(max_length=255, blank=True, null=True)
    es_is_read = models.CharField(max_length=255, blank=True, null=True)
    is_consume = models.CharField(max_length=16, blank=True, null=True)
    eh_is_read = models.CharField(max_length=255, blank=True, null=True)
    certificate = models.CharField(max_length=255, blank=True, null=True)
    invoice_no = models.CharField(max_length=50, blank=True, null=True)
    invoice_title = models.CharField(max_length=1000, blank=True, null=True)
    invoice_memo = models.TextField(blank=True, null=True)
    is_invoice = models.IntegerField(blank=True, null=True)
    deliver_type = models.IntegerField(blank=True, null=True)
    estimated_time = models.DateTimeField(blank=True, null=True)
    is_deleted = models.CharField(max_length=2, blank=True, null=True)
    sended_count = models.IntegerField(blank=True, null=True)
    cancel_code = models.IntegerField(blank=True, null=True)
    coupon = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    distribution_sign = models.CharField(max_length=2, blank=True, null=True)
    proportion_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    share_user_id = models.CharField(max_length=64, blank=True, null=True)
    share_user_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_mall_order'


class EsMallOrderDetail(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    order_id = models.CharField(max_length=64, blank=True, null=True)
    goods_id = models.CharField(max_length=64, blank=True, null=True)
    goods_count = models.CharField(max_length=10, blank=True, null=True)
    shopping_id = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    buyer_msg = models.CharField(max_length=500, blank=True, null=True)
    invoice_id = models.CharField(max_length=64, blank=True, null=True)
    goods_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    send_num = models.IntegerField(blank=True, null=True)
    back_num = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateField(blank=True, null=True)
    shop_name = models.CharField(max_length=500, blank=True, null=True)
    goods_img = models.CharField(max_length=255, blank=True, null=True)
    goods_name = models.CharField(max_length=255, blank=True, null=True)
    goods_color = models.CharField(max_length=255, blank=True, null=True)
    goods_desc = models.TextField(blank=True, null=True)
    shop_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_mall_order_detail'


class EsOperators(models.Model):
    operators_id = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField()
    province = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    contacts = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=2, blank=True, null=True)
    logo_src = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_operators'


class EsOrder(models.Model):
    order_id = models.CharField(max_length=64, blank=True, null=True)
    order_sn = models.CharField(max_length=255, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    shopping_name = models.CharField(max_length=50, blank=True, null=True)
    ship_phone = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    shop_name = models.CharField(max_length=50, blank=True, null=True)
    goods_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    goods_nums = models.IntegerField(blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    pay_name = models.IntegerField(blank=True, null=True)
    ship_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pay_status = models.IntegerField(blank=True, null=True)
    pay_time = models.DateTimeField(blank=True, null=True)
    order_status = models.IntegerField(blank=True, null=True)
    ship_status = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    delivery = models.CharField(max_length=50, blank=True, null=True)
    delivery_no = models.CharField(max_length=50, blank=True, null=True)
    pay_money = models.CharField(max_length=50, blank=True, null=True)
    epay = models.CharField(max_length=1, blank=True, null=True)
    is_back = models.IntegerField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_order'


class EsOrderGoods(models.Model):
    order_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    show_name = models.CharField(max_length=50, blank=True, null=True)
    goods_id = models.CharField(max_length=64, blank=True, null=True)
    goods_name = models.CharField(max_length=255, blank=True, null=True)
    goods_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    goods_nums = models.IntegerField(blank=True, null=True)
    goods_toal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    goods_image = models.CharField(max_length=255, blank=True, null=True)
    order_time = models.DateTimeField(blank=True, null=True)
    send_num = models.CharField(max_length=50, blank=True, null=True)
    back_num = models.CharField(max_length=50, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_order_goods'


class EsOrderGoodsCopy(models.Model):
    order_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    show_name = models.CharField(max_length=50, blank=True, null=True)
    goods_id = models.CharField(max_length=64, blank=True, null=True)
    goods_name = models.CharField(max_length=255, blank=True, null=True)
    goods_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    goods_nums = models.IntegerField(blank=True, null=True)
    goods_toal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    goods_image = models.CharField(max_length=255, blank=True, null=True)
    order_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_order_goods_copy'


class EsPayLogSn(models.Model):
    pay_log_id = models.CharField(max_length=64, blank=True, null=True)
    pay_sn = models.CharField(max_length=64)
    pay_type = models.IntegerField(blank=True, null=True)
    order_sn = models.CharField(max_length=50, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_pay_log_sn'


class EsPaymentOrder(models.Model):
    payment_order_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    receive_user_id = models.CharField(max_length=64, blank=True, null=True)
    receive_name = models.CharField(max_length=64, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_payment_order'


class EsPaymentOrderLog(models.Model):
    payment_order_id = models.CharField(max_length=64, blank=True, null=True)
    b_id = models.CharField(max_length=64)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    receive_user_id = models.CharField(max_length=64, blank=True, null=True)
    receive_name = models.CharField(max_length=64, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_payment_order_log'


class EsRedPacket(models.Model):
    redpacket_id = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    nums = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    get_nums = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_red_packet'


class EsRedPacketList(models.Model):
    redpacket_id = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    user_name = models.CharField(max_length=64, blank=True, null=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    get_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_red_packet_list'


class EsSaleInfo(models.Model):
    sale_info_id = models.CharField(max_length=64, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    descs = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    is_push = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    vfrom = models.IntegerField(blank=True, null=True)
    active_name = models.CharField(max_length=100, blank=True, null=True)
    img_src = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_sale_info'


class EsSaleinfoImage(models.Model):
    image_id = models.CharField(max_length=64, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    sale_info_id = models.CharField(max_length=64, blank=True, null=True)
    src = models.CharField(max_length=255, blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_saleinfo_image'


class EsSendSmsLog(models.Model):
    sms_id = models.CharField(max_length=64, blank=True, null=True)
    tid = models.CharField(max_length=64, blank=True, null=True)
    message = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    to_user_id = models.CharField(max_length=64, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    is_sms = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modi_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_send_sms_log'


class EsShop(models.Model):
    shop_id = models.CharField(max_length=64)
    shop_sn = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    qq = models.IntegerField(blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    is_self = models.IntegerField()
    shop_name = models.CharField(max_length=100, blank=True, null=True)
    shop_name_img = models.CharField(max_length=255, blank=True, null=True)
    shop_company = models.CharField(max_length=255, blank=True, null=True)
    shop_img = models.CharField(max_length=150)
    shop_tel = models.CharField(max_length=70, blank=True, null=True)
    shop_desc = models.TextField(blank=True, null=True)
    shop_explain = models.TextField(blank=True, null=True)
    province = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    district = models.CharField(max_length=500, blank=True, null=True)
    shop_address = models.CharField(max_length=255, blank=True, null=True)
    manual_province = models.CharField(max_length=500, blank=True, null=True)
    manual_city = models.CharField(max_length=500, blank=True, null=True)
    manual_district = models.CharField(max_length=500, blank=True, null=True)
    manual_address = models.CharField(max_length=2000, blank=True, null=True)
    shop_type = models.CharField(max_length=64, blank=True, null=True)
    service_start_time = models.DateTimeField(blank=True, null=True)
    service_end_time = models.DateTimeField(blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    t_id = models.CharField(max_length=255, blank=True, null=True)
    t_cid = models.CharField(max_length=255, blank=True, null=True)
    weixin = models.CharField(max_length=50, blank=True, null=True)
    t_status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    is_checked = models.IntegerField(blank=True, null=True)
    is_validate = models.IntegerField(blank=True, null=True)
    open_time_des = models.CharField(max_length=255, blank=True, null=True)
    is_shipping = models.CharField(max_length=2, blank=True, null=True)
    shipping_des = models.CharField(max_length=255, blank=True, null=True)
    is_online = models.CharField(max_length=255, blank=True, null=True)
    is_invoice = models.CharField(max_length=255, blank=True, null=True)
    upd_name_num = models.IntegerField(blank=True, null=True)
    upd_type_num = models.IntegerField(blank=True, null=True)
    upd_longitude_num = models.IntegerField(blank=True, null=True)
    upd_latitude_num = models.IntegerField(blank=True, null=True)
    upd_manual_num = models.IntegerField(blank=True, null=True)
    feature = models.IntegerField(blank=True, null=True)
    charge_desc = models.TextField(blank=True, null=True)
    is_true = models.CharField(max_length=255, blank=True, null=True)
    shop_status = models.IntegerField(blank=True, null=True)
    invoice_desc = models.CharField(max_length=255, blank=True, null=True)
    time_range = models.CharField(max_length=255, blank=True, null=True)
    date_range = models.CharField(max_length=255, blank=True, null=True)
    closed_status = models.IntegerField(blank=True, null=True)
    country_code = models.CharField(max_length=10, blank=True, null=True)
    verify_ratio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    auth_status = models.IntegerField(blank=True, null=True)
    license = models.CharField(max_length=255, blank=True, null=True)
    refuse_reson = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_shop'


class EsShopAds(models.Model):
    ads_info_id = models.CharField(max_length=64, blank=True, null=True)
    shop_ads_id = models.CharField(max_length=64, blank=True, null=True)
    ads_period_id = models.CharField(max_length=4000, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    shop_feature = models.IntegerField(blank=True, null=True)
    ads_img = models.CharField(max_length=255, blank=True, null=True)
    demand_remark = models.CharField(max_length=4000, blank=True, null=True)
    money = models.CharField(max_length=128, blank=True, null=True)
    qq = models.CharField(max_length=64, blank=True, null=True)
    audit_status = models.CharField(max_length=64, blank=True, null=True)
    publish_status = models.CharField(max_length=64, blank=True, null=True)
    audit_remark = models.CharField(max_length=4000, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_shop_ads'


class EsShopDiscounts(models.Model):
    id = models.AutoField()
    shop_id = models.CharField(max_length=64)
    money = models.DecimalField(max_digits=10, decimal_places=2)
    discount_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_shop_discounts'
        unique_together = (('shop_id', 'money'),)


class EsShopFollowers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    owner_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    tag = models.CharField(max_length=10, blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    remark_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_shop_followers'


class EsShopOwner(models.Model):
    user_id = models.CharField(max_length=64, blank=True, null=True)
    user_sex = models.IntegerField(blank=True, null=True)
    real_name = models.CharField(max_length=32, blank=True, null=True)
    show_name = models.CharField(max_length=20, blank=True, null=True)
    user_qq = models.CharField(max_length=20, blank=True, null=True)
    user_phone = models.CharField(max_length=11, blank=True, null=True)
    user_email = models.CharField(max_length=50, blank=True, null=True)
    user_photo = models.CharField(max_length=150, blank=True, null=True)
    user_status = models.IntegerField(blank=True, null=True)
    last_time = models.DateTimeField(blank=True, null=True)
    retail_id = models.CharField(max_length=10, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_shop_owner'


class EsShopPageviewLog(models.Model):
    pageview_id = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    c_time = models.DateTimeField(blank=True, null=True)
    c_type = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    c_time_str = models.DateTimeField()
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_shop_pageview_log'


class EsShopTypes(models.Model):
    shop_type_id = models.CharField(max_length=64, blank=True, null=True)
    type_name = models.CharField(max_length=30, blank=True, null=True)
    type_src = models.CharField(max_length=100, blank=True, null=True)
    is_default = models.CharField(max_length=2, blank=True, null=True)
    cate = models.IntegerField(blank=True, null=True)
    logo_width = models.IntegerField(blank=True, null=True)
    logo_height = models.IntegerField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    icon_src = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_shop_types'


class EsShopV3ProjectInfo(models.Model):
    project_id = models.CharField(max_length=255, blank=True, null=True)
    shop_id = models.CharField(max_length=255, blank=True, null=True)
    project_title = models.CharField(max_length=500, blank=True, null=True)
    project_img = models.CharField(max_length=255, blank=True, null=True)
    project_desc = models.TextField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_shop_v3_project_info'


class EsSlideImage(models.Model):
    slide_image_id = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    img_src = models.TextField(blank=True, null=True)
    movie_cover_img = models.CharField(max_length=200, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_slide_image'


class EsUserAll(models.Model):
    easemob_status = models.CharField(max_length=5, blank=True, null=True)
    login_status = models.CharField(max_length=10, blank=True, null=True)
    zfb_id = models.CharField(max_length=500, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    login_name = models.CharField(max_length=64, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    mobile = models.CharField(max_length=64, blank=True, null=True)
    show_name = models.CharField(max_length=64, blank=True, null=True)
    img_src = models.CharField(max_length=255, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    token = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    true_name = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    province_code = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    city_code = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    country_code = models.CharField(max_length=50, blank=True, null=True)
    parent_id = models.CharField(max_length=50, blank=True, null=True)
    nick_name = models.CharField(max_length=50, blank=True, null=True)
    verify_qrcode = models.CharField(max_length=50, blank=True, null=True)
    user_logo = models.CharField(max_length=500, blank=True, null=True)
    login_secret = models.CharField(max_length=64, blank=True, null=True)
    eb_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    eb_freeze = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    flag = models.CharField(max_length=11, blank=True, null=True)
    is_online = models.CharField(max_length=11, blank=True, null=True)
    openfire_password = models.CharField(max_length=64, blank=True, null=True)
    password2 = models.CharField(max_length=64, blank=True, null=True)
    union_id = models.CharField(max_length=64, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    verification = models.IntegerField(blank=True, null=True)
    address_zl = models.CharField(max_length=255, blank=True, null=True)
    public_key = models.CharField(max_length=255, blank=True, null=True)
    zl_password = models.CharField(max_length=255, blank=True, null=True)
    inviter = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_user_all'


class EsUserBills(models.Model):
    bills_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    show_name = models.CharField(max_length=50, blank=True, null=True)
    receive_user_id = models.CharField(max_length=50, blank=True, null=True)
    receiver_name = models.CharField(max_length=50, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payed = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pay_status = models.IntegerField(blank=True, null=True)
    user_status = models.IntegerField(blank=True, null=True)
    bills_status = models.IntegerField(blank=True, null=True)
    bills_desc = models.CharField(max_length=255, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_user_bills'


class EsUserBillsLog(models.Model):
    bill_id = models.CharField(max_length=64)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    show_name = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_user_bills_log'


class EsUserCash(models.Model):
    biz_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64)
    bank_no = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=50, blank=True, null=True)
    bank_id = models.CharField(max_length=64, blank=True, null=True)
    money = models.DecimalField(max_digits=10, decimal_places=2)
    fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    add_time = models.DateTimeField()
    status = models.IntegerField()
    reject_reason = models.CharField(max_length=1000, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    out_card_no = models.CharField(max_length=64, blank=True, null=True)
    cash_type = models.IntegerField(blank=True, null=True)
    open_id = models.CharField(max_length=64, blank=True, null=True)
    has_huifu = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_user_cash'


class EsUserChargeOrder(models.Model):
    charge_order_id = models.CharField(max_length=64, blank=True, null=True)
    bn = models.CharField(max_length=100, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    pay_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_user_charge_order'


class EsUserLotteryLog(models.Model):
    lottery_log_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    u_name = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    t_id = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'es_user_lottery_log'


class FinanceBankCard(models.Model):
    card_no = models.CharField(max_length=40, blank=True, null=True)
    card_type = models.CharField(max_length=1, blank=True, null=True)
    card_status = models.CharField(max_length=1, blank=True, null=True)
    bank_code = models.CharField(max_length=100, blank=True, null=True)
    person_name = models.CharField(max_length=60, blank=True, null=True)
    person_id = models.CharField(max_length=64, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    province_name = models.CharField(max_length=60, blank=True, null=True)
    province_code = models.CharField(max_length=40, blank=True, null=True)
    city_name = models.CharField(max_length=60, blank=True, null=True)
    city_code = models.CharField(max_length=40, blank=True, null=True)
    area_name = models.CharField(max_length=60, blank=True, null=True)
    area_code = models.CharField(max_length=40, blank=True, null=True)
    bank_site_name = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finance_bank_card'


class FinanceCashErrorLogs(models.Model):
    id = models.BigIntegerField(primary_key=True)
    biz_id = models.CharField(max_length=64)
    user_id = models.CharField(max_length=64)
    shop_name = models.CharField(max_length=100, blank=True, null=True)
    bank_user = models.CharField(max_length=100, blank=True, null=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    apply_cash_time = models.DateTimeField()
    error_desc = models.CharField(max_length=120, blank=True, null=True)
    error_code = models.CharField(max_length=30, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField()
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'finance_cash_error_logs'


class FinanceMenu(models.Model):
    menu_id = models.CharField(max_length=64)
    menu_name = models.CharField(max_length=100, blank=True, null=True)
    parent_menu = models.CharField(max_length=64, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    disp_order = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finance_menu'


class FinanceOperLog(models.Model):
    description = models.CharField(max_length=150, blank=True, null=True)
    method = models.CharField(max_length=512, blank=True, null=True)
    request_ip = models.CharField(max_length=60, blank=True, null=True)
    account = models.CharField(max_length=60, blank=True, null=True)
    operator = models.CharField(max_length=60, blank=True, null=True)
    operation_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finance_oper_log'


class FinanceRoles(models.Model):
    role_id = models.CharField(max_length=64, blank=True, null=True)
    role_name = models.CharField(max_length=100, blank=True, null=True)
    role_desc = models.CharField(max_length=100, blank=True, null=True)
    role_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finance_roles'


class FinanceRolesPrivilege(models.Model):
    role_id = models.CharField(max_length=64, blank=True, null=True)
    menu_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finance_roles_privilege'


class FinanceUser(models.Model):
    finance_user_id = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    true_name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=300)
    salt = models.CharField(max_length=64, blank=True, null=True)
    token = models.CharField(max_length=64, blank=True, null=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    user_type = models.IntegerField()
    mobile = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.CharField(max_length=512, blank=True, null=True)
    user_level = models.IntegerField()
    status = models.IntegerField()
    province = models.CharField(max_length=100, blank=True, null=True)
    province_code = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    city_code = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    county_code = models.CharField(max_length=50, blank=True, null=True)
    creater = models.CharField(max_length=64)
    created_time = models.DateTimeField()
    modifier = models.CharField(max_length=64)
    updated_time = models.DateTimeField()
    last_login_time = models.DateTimeField()
    region = models.CharField(max_length=100, blank=True, null=True)
    pay_password = models.CharField(max_length=300, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    address = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finance_user'


class FinanceUserRole(models.Model):
    user_id = models.CharField(max_length=64, blank=True, null=True)
    role_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finance_user_role'


class GoodsAttr(models.Model):
    goods_attr_id = models.CharField(unique=True, max_length=50)
    goods_id = models.CharField(max_length=50)
    fk_category_attr_id = models.CharField(max_length=50, blank=True, null=True)
    fk_category_attr_value_id = models.CharField(max_length=50, blank=True, null=True)
    attr_alias = models.CharField(max_length=40, blank=True, null=True)
    attr_name = models.CharField(max_length=40)
    attr_value = models.CharField(max_length=40)
    parent_id = models.CharField(max_length=50, blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    is_input = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'goods_attr'


class GoodsCategory(models.Model):
    fk_goods_id = models.CharField(max_length=50)
    fk_category_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'goods_category'


class GoodsChangeApply(models.Model):
    goods_apply_id = models.AutoField(primary_key=True)
    applier_id = models.CharField(max_length=64)
    apply_type = models.IntegerField()
    goods_id = models.CharField(max_length=64)
    apply_date = models.DateTimeField()
    auditor = models.CharField(max_length=64, blank=True, null=True)
    audit_type = models.IntegerField(blank=True, null=True)
    process_date = models.DateTimeField(blank=True, null=True)
    process_status = models.IntegerField(blank=True, null=True)
    process_result = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_change_apply'


class GoodsChangeLog(models.Model):
    goods_apply_id = models.AutoField(primary_key=True)
    applier_id = models.CharField(max_length=64, blank=True, null=True)
    goods_id = models.CharField(max_length=64)
    apply_date = models.DateTimeField()
    auditor = models.CharField(max_length=64, blank=True, null=True)
    audit_type = models.IntegerField(blank=True, null=True)
    process_date = models.DateTimeField(blank=True, null=True)
    process_status = models.IntegerField(blank=True, null=True)
    process_result = models.CharField(max_length=500, blank=True, null=True)
    apply_type = models.IntegerField(blank=True, null=True)
    operate_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_change_log'


class GoodsHitsLog(models.Model):
    user_id = models.CharField(max_length=64, blank=True, null=True)
    goods_id = models.CharField(max_length=64, blank=True, null=True)
    goods_name = models.CharField(max_length=50, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    shop_name = models.CharField(max_length=100, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    hits_time = models.DateField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_hits_log'


class GoodsQccodeHistory(models.Model):
    goods_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    scan_date = models.DateTimeField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_qccode_history'


class GoodsSalesVolume(models.Model):
    fk_goods_id = models.CharField(max_length=64)
    sales_volume = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_sales_volume'


class GoodsScanFootprint(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    goods_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    category_id = models.CharField(max_length=64, blank=True, null=True)
    shop_type = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    scan_date = models.DateTimeField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    scannum = models.IntegerField(db_column='scanNum', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=1, blank=True, null=True)
    item_type = models.CharField(max_length=1, blank=True, null=True)
    category_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_scan_footprint'


class GoodsSkuAttr(models.Model):
    id = models.BigIntegerField(primary_key=True)
    goods_sku_attr_id = models.CharField(max_length=50)
    fk_spec_t = models.CharField(max_length=50, blank=True, null=True)
    fk_category_attr_id = models.CharField(max_length=50, blank=True, null=True)
    fk_category_attr_value_id = models.CharField(max_length=50, blank=True, null=True)
    attr_name = models.CharField(max_length=50, blank=True, null=True)
    attr_value = models.CharField(max_length=100, blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_sku_attr'


class GoodsSnapT(models.Model):
    fk_category_brand_id = models.CharField(max_length=64, blank=True, null=True)
    brand_name = models.CharField(max_length=64, blank=True, null=True)
    goods_id = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    goods_name = models.CharField(max_length=200, blank=True, null=True)
    goods_unit = models.CharField(max_length=10, blank=True, null=True)
    spec_name = models.CharField(max_length=500, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    market_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shop_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    express_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    is_refund = models.IntegerField(blank=True, null=True)
    is_online_buy = models.CharField(max_length=255, blank=True, null=True)
    is_support_logistic = models.CharField(max_length=2, blank=True, null=True)
    is_order = models.CharField(max_length=255, blank=True, null=True)
    is_delivery = models.CharField(max_length=255, blank=True, null=True)
    is_merchant = models.CharField(max_length=2, blank=True, null=True)
    delivery_desc = models.CharField(max_length=255, blank=True, null=True)
    is_phone_order = models.CharField(max_length=255, blank=True, null=True)
    goods_spec = models.TextField(blank=True, null=True)
    goods_desc = models.TextField(blank=True, null=True)
    attr_cat_id = models.CharField(max_length=64, blank=True, null=True)
    goods_status = models.IntegerField(blank=True, null=True)
    purchase = models.IntegerField(blank=True, null=True)
    province_id = models.CharField(max_length=64, blank=True, null=True)
    city_id = models.CharField(max_length=64, blank=True, null=True)
    area_id = models.CharField(max_length=64, blank=True, null=True)
    send_province_id = models.IntegerField(blank=True, null=True)
    send_city_id = models.IntegerField(blank=True, null=True)
    send_district_id = models.IntegerField(blank=True, null=True)
    send_address = models.CharField(max_length=255, blank=True, null=True)
    invoice_type = models.IntegerField(blank=True, null=True)
    invoice_desc = models.CharField(max_length=255, blank=True, null=True)
    invoice_support_type = models.IntegerField(blank=True, null=True)
    vfrom = models.IntegerField(blank=True, null=True)
    goods_sn = models.CharField(max_length=20, blank=True, null=True)
    goods_img = models.CharField(max_length=150, blank=True, null=True)
    order_time = models.DateTimeField(blank=True, null=True)
    order_id = models.CharField(max_length=64, blank=True, null=True)
    delivery_addr = models.CharField(max_length=100, blank=True, null=True)
    spec_img = models.CharField(max_length=500, blank=True, null=True)
    spec_unit = models.CharField(max_length=20, blank=True, null=True)
    spec_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    spec_count = models.IntegerField(blank=True, null=True)
    spec_id = models.CharField(max_length=64, blank=True, null=True)
    receiver_name = models.CharField(max_length=20, blank=True, null=True)
    receiver_tel = models.CharField(max_length=20, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    merchant_id = models.CharField(max_length=64, blank=True, null=True)
    goods_operation_model = models.IntegerField(blank=True, null=True)
    cancel_code = models.IntegerField(blank=True, null=True)
    order_source = models.CharField(max_length=10, blank=True, null=True)
    distribution_sign = models.CharField(max_length=2, blank=True, null=True)
    proportion_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    share_user_id = models.CharField(max_length=64, blank=True, null=True)
    share_user_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_snap_t'


class GoodsSnapTicket(models.Model):
    id = models.BigIntegerField(primary_key=True)
    ticket_name = models.CharField(max_length=64)
    fk_ticket_id = models.CharField(max_length=64)
    goods_id = models.CharField(max_length=64)
    shop_id = models.CharField(max_length=64)
    order_id = models.CharField(max_length=64)
    goods_count = models.SmallIntegerField(blank=True, null=True)
    ticket_percent = models.CharField(max_length=64, blank=True, null=True)
    ticket_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ticket_use_type = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'goods_snap_ticket'


class GoodsSpecT(models.Model):
    spec_id = models.CharField(max_length=64)
    goods_id = models.CharField(max_length=64)
    spec_name = models.CharField(max_length=500)
    spec_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    spec_count = models.BigIntegerField(blank=True, null=True)
    spec_status = models.CharField(max_length=1, blank=True, null=True)
    spec_img = models.CharField(max_length=1000, blank=True, null=True)
    spec_unit = models.CharField(max_length=100, blank=True, null=True)
    spec_seq = models.IntegerField(blank=True, null=True)
    is_default = models.IntegerField()
    spec_barcode = models.CharField(max_length=50, blank=True, null=True)
    spec_code = models.CharField(max_length=50, blank=True, null=True)
    is_sku_attr = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'goods_spec_t'


class GoodsSubGallerys(models.Model):
    fk_goods_sub_id = models.CharField(max_length=64, blank=True, null=True)
    img_url = models.CharField(max_length=200, blank=True, null=True)
    position = models.CharField(max_length=10, blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_sub_gallerys'


class GuessUserEnjoy(models.Model):
    user_id = models.CharField(max_length=64, blank=True, null=True)
    fk_category_id = models.CharField(max_length=64)
    sales_volume = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guess_user_enjoy'


class HfApppayTransactionFlow(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField()
    order_id = models.CharField(max_length=64)
    order_date = models.CharField(max_length=64)
    trans_amt = models.CharField(max_length=64)
    buyer_id = models.CharField(max_length=64, blank=True, null=True)
    goods_desc = models.CharField(max_length=64, blank=True, null=True)
    goods_type = models.CharField(max_length=64, blank=True, null=True)
    pay_type = models.CharField(max_length=64, blank=True, null=True)
    pay_status = models.CharField(max_length=64, blank=True, null=True)
    out_trans_id = models.CharField(max_length=64, blank=True, null=True)
    req_json = models.CharField(max_length=3000, blank=True, null=True)
    resp1_json = models.CharField(max_length=3000, blank=True, null=True)
    resp2_json = models.CharField(max_length=3000, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    modifier = models.CharField(max_length=64)
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hf_apppay_transaction_flow'


class HfInsteadgrantRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField(blank=True, null=True)
    order_id = models.CharField(max_length=64)
    order_date = models.CharField(max_length=64, blank=True, null=True)
    pay_cust_id = models.CharField(max_length=64, blank=True, null=True)
    pay_acct_id = models.CharField(max_length=64, blank=True, null=True)
    trans_amt = models.CharField(max_length=64)
    bank_card_no = models.CharField(max_length=64)
    bank_id = models.CharField(max_length=64, blank=True, null=True)
    bank_name = models.CharField(max_length=64, blank=True, null=True)
    purpose = models.CharField(max_length=64, blank=True, null=True)
    cust_name = models.CharField(max_length=64, blank=True, null=True)
    mobile = models.CharField(max_length=64, blank=True, null=True)
    cert_type = models.CharField(max_length=64, blank=True, null=True)
    cert_id = models.CharField(max_length=64, blank=True, null=True)
    trans_mode = models.CharField(max_length=64, blank=True, null=True)
    fee_amt = models.CharField(max_length=64, blank=True, null=True)
    platform_seq_id = models.CharField(max_length=64, blank=True, null=True)
    req_json = models.CharField(max_length=3000, blank=True, null=True)
    resp1_json = models.CharField(max_length=3000, blank=True, null=True)
    resp2_json = models.CharField(max_length=3000, blank=True, null=True)
    trans_stat = models.CharField(max_length=64, blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField()
    creater = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    modifier = models.CharField(max_length=64)
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hf_insteadgrant_record'


class HfRefundRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField(blank=True, null=True)
    order_id = models.CharField(max_length=64)
    order_date = models.CharField(max_length=64, blank=True, null=True)
    orginal_order_id = models.CharField(max_length=64, blank=True, null=True)
    orginal_platform_seq_id = models.CharField(max_length=64)
    trans_amt = models.CharField(max_length=64)
    trans_stat = models.CharField(max_length=64, blank=True, null=True)
    div_detail = models.CharField(max_length=1000, blank=True, null=True)
    req_json = models.CharField(max_length=3000, blank=True, null=True)
    resp1_json = models.CharField(max_length=3000, blank=True, null=True)
    resp2_json = models.CharField(max_length=3000, blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField()
    creater = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    modifier = models.CharField(max_length=64)
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hf_refund_record'


class HfTransacctRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField(blank=True, null=True)
    order_id = models.CharField(max_length=64)
    order_date = models.CharField(max_length=64, blank=True, null=True)
    transfer_type = models.CharField(max_length=64, blank=True, null=True)
    out_cust_id = models.CharField(max_length=64)
    out_acct_id = models.CharField(max_length=64, blank=True, null=True)
    in_cust_id = models.CharField(max_length=64)
    in_acct_id = models.CharField(max_length=64, blank=True, null=True)
    transfer_amt = models.CharField(max_length=64)
    transfer_time = models.DateTimeField()
    req_json = models.CharField(max_length=3000, blank=True, null=True)
    resp1_json = models.CharField(max_length=3000, blank=True, null=True)
    resp2_json = models.CharField(max_length=3000, blank=True, null=True)
    trans_stat = models.CharField(max_length=64, blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField()
    creater = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    modifier = models.CharField(max_length=64)
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hf_transacct_record'


class HfUserAccInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField()
    cert_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    user_cust_id = models.CharField(max_length=64)
    acct_id = models.CharField(max_length=64)
    user_mobile = models.CharField(max_length=64, blank=True, null=True)
    fee_amt = models.CharField(max_length=64, blank=True, null=True)
    fee_acct_id = models.CharField(max_length=64, blank=True, null=True)
    card_no = models.CharField(max_length=64, blank=True, null=True)
    bank_id = models.CharField(max_length=64, blank=True, null=True)
    cash_bind_card_id = models.CharField(max_length=64, blank=True, null=True)
    div_ratio = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField()
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    modifier = models.CharField(max_length=64)
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hf_user_acc_info'


class HfWithdrawalRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=64)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    shop_name = models.CharField(max_length=64, blank=True, null=True)
    withdraw_type = models.CharField(max_length=64, blank=True, null=True)
    trans_amt = models.CharField(max_length=64)
    real_trans_amt = models.CharField(max_length=64, blank=True, null=True)
    fee_amt = models.CharField(max_length=64, blank=True, null=True)
    tx_time = models.DateTimeField()
    order_id = models.CharField(max_length=64, blank=True, null=True)
    req_json = models.CharField(max_length=3000, blank=True, null=True)
    resp1_json = models.CharField(max_length=3000, blank=True, null=True)
    resp2_json = models.CharField(max_length=3000, blank=True, null=True)
    trans_stat = models.CharField(max_length=64, blank=True, null=True)
    oper_type = models.CharField(max_length=64, blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField()
    creater = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    modifier = models.CharField(max_length=64)
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hf_withdrawal_record'


class IndexColumn(models.Model):
    column_id = models.AutoField(primary_key=True)
    column_name = models.CharField(max_length=50, blank=True, null=True)
    column_seq = models.IntegerField()
    redis_key = models.CharField(max_length=40, blank=True, null=True)
    status = models.IntegerField()
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'index_column'


class IndexHeadline(models.Model):
    headline_id = models.CharField(max_length=64)
    is_relation_goods = models.IntegerField(blank=True, null=True)
    column_id = models.IntegerField()
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    province_code = models.CharField(max_length=50, blank=True, null=True)
    city_code = models.CharField(max_length=50, blank=True, null=True)
    county_code = models.CharField(max_length=50, blank=True, null=True)
    goods_id = models.CharField(max_length=64, blank=True, null=True)
    img_url = models.CharField(max_length=500)
    status = models.IntegerField()
    recommend_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'index_headline'


class IndexPlateGoods(models.Model):
    goods_plate_id = models.AutoField(primary_key=True)
    list_plate_id = models.IntegerField()
    goods_id = models.CharField(max_length=64)
    is_index = models.IntegerField()
    seq = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'index_plate_goods'


class IndexRecommendAgent(models.Model):
    agent_user_id = models.CharField(max_length=64)
    agent_shop_id = models.CharField(max_length=64)
    seq = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'index_recommend_agent'


class IndexRecommendAgentLog(models.Model):
    operator = models.CharField(max_length=64)
    operate_type = models.IntegerField()
    operate_time = models.DateTimeField()
    agent_user_id = models.CharField(max_length=64, blank=True, null=True)
    agent_shop_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'index_recommend_agent_log'


class InvestmentInfo(models.Model):
    id = models.CharField(max_length=64, blank=True, null=True)
    investment_name = models.CharField(max_length=64, blank=True, null=True)
    investment_phone = models.CharField(max_length=20, blank=True, null=True)
    is_valid = models.CharField(max_length=1, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'investment_info'


class InviteMerchantGoodsMain(models.Model):
    goods_main_id = models.CharField(max_length=64, blank=True, null=True)
    fk_mobile = models.CharField(max_length=11, blank=True, null=True)
    merchant_name = models.CharField(max_length=50, blank=True, null=True)
    merchant_mobile = models.CharField(max_length=50, blank=True, null=True)
    merchant_person = models.CharField(max_length=50, blank=True, null=True)
    merchant_person_mobile = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=1, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    province_code = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    city_code = models.CharField(max_length=10, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    county_code = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invite_merchant_goods_main'


class InviteMerchantGoodsSub(models.Model):
    goods_sub_id = models.CharField(max_length=64, blank=True, null=True)
    fk_goods_main_id = models.CharField(max_length=64, blank=True, null=True)
    goods_name = models.CharField(max_length=64, blank=True, null=True)
    goods_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    unit = models.CharField(max_length=20, blank=True, null=True)
    stock_count = models.IntegerField(blank=True, null=True)
    spec_name = models.CharField(max_length=50, blank=True, null=True)
    distribution_condition = models.CharField(max_length=255, blank=True, null=True)
    packing_type = models.CharField(max_length=1, blank=True, null=True)
    weight_info = models.CharField(max_length=50, blank=True, null=True)
    life_time = models.CharField(max_length=20, blank=True, null=True)
    ingredients = models.CharField(max_length=50, blank=True, null=True)
    producing_area = models.CharField(max_length=200, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invite_merchant_goods_sub'


class InviteMerchantUser(models.Model):
    mobile = models.CharField(max_length=11, blank=True, null=True)
    merchant_rel_person = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invite_merchant_user'


class LogisticsCompany(models.Model):
    company_code = models.CharField(max_length=64)
    company_name = models.CharField(unique=True, max_length=50)
    seq = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logistics_company'


class LsActivityDiscountRelation(models.Model):
    activity_pid = models.CharField(max_length=64)
    activity_id = models.CharField(max_length=64)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ls_activity_discount_relation'


class LsBonusRelation(models.Model):
    bonus_pid = models.CharField(max_length=64)
    bonus_id = models.CharField(max_length=64)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ls_bonus_relation'


class LsBrandShop(models.Model):
    brand_id = models.CharField(max_length=64, blank=True, null=True)
    branche_shop_id = models.CharField(max_length=64, blank=True, null=True)
    shop_level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ls_brand_shop'


class LsCouponRelation(models.Model):
    coupon_pid = models.CharField(max_length=64)
    coupon_id = models.CharField(max_length=64)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ls_coupon_relation'


class LsFullminusRelation(models.Model):
    activity_pid = models.CharField(max_length=64)
    activity_id = models.CharField(max_length=64)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ls_fullminus_relation'


class LsGoodsCategoryRelation(models.Model):
    category_pid = models.CharField(max_length=64, blank=True, null=True)
    category_id = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ls_goods_category_relation'


class LsGoodsRelation(models.Model):
    goods_pid = models.CharField(max_length=64, blank=True, null=True)
    goods_id = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ls_goods_relation'


class LsMemberActivityRelation(models.Model):
    activity_pid = models.CharField(max_length=64)
    activity_id = models.CharField(max_length=64)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ls_member_activity_relation'


class MallActive(models.Model):
    id = models.BigIntegerField(primary_key=True)
    active_id = models.CharField(max_length=64)
    mall_id = models.CharField(max_length=64, blank=True, null=True)
    active_name = models.CharField(max_length=100, blank=True, null=True)
    active_content = models.CharField(max_length=100, blank=True, null=True)
    active_cover_pic = models.CharField(max_length=200, blank=True, null=True)
    active_pos = models.IntegerField(blank=True, null=True)
    biz_id = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mall_active'


class MallBrand(models.Model):
    id = models.BigIntegerField(primary_key=True)
    brand_id = models.CharField(unique=True, max_length=64)
    brand_code = models.CharField(max_length=10, blank=True, null=True)
    brand_name = models.CharField(max_length=50, blank=True, null=True)
    brand_desc = models.TextField(blank=True, null=True)
    brand_logo = models.CharField(max_length=200, blank=True, null=True)
    brand_state = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mall_brand'


class MallBrandStoreAttr(models.Model):
    id = models.BigIntegerField(primary_key=True)
    shop_id = models.CharField(unique=True, max_length=64)
    brand_id = models.CharField(max_length=64, blank=True, null=True)
    country_code = models.CharField(max_length=10, blank=True, null=True)
    background_nums = models.IntegerField(blank=True, null=True)
    floor_nums = models.IntegerField(blank=True, null=True)
    virtual_floor_nums = models.IntegerField(blank=True, null=True)
    search_range = models.IntegerField(blank=True, null=True)
    cs_role_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mall_brand_store_attr'


class MallCollect(models.Model):
    member_id = models.CharField(unique=True, max_length=64)
    collect_obj_type = models.IntegerField()
    obj_id = models.CharField(max_length=64)
    mall_id = models.CharField(max_length=64)
    collect_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mall_collect'


class MallFloor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    floor_id = models.CharField(max_length=64)
    shop_id = models.CharField(max_length=64)
    floor_no = models.IntegerField(blank=True, null=True)
    floor_position = models.IntegerField(blank=True, null=True)
    floor_pic = models.CharField(max_length=200, blank=True, null=True)
    guide_label = models.CharField(max_length=100, blank=True, null=True)
    floor_desc = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mall_floor'


class MallFloorGoods(models.Model):
    id = models.BigIntegerField(primary_key=True)
    shop_id = models.CharField(max_length=64)
    floor_id = models.CharField(max_length=64)
    goods_id = models.CharField(max_length=64)
    seq = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mall_floor_goods'


class MallIndexColumn(models.Model):
    id = models.BigIntegerField(primary_key=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    column_id = models.CharField(max_length=64)
    column_name = models.CharField(max_length=50)
    column_pic = models.CharField(max_length=200, blank=True, null=True)
    link_target = models.IntegerField(blank=True, null=True)
    seq = models.SmallIntegerField(blank=True, null=True)
    price_disp_type = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mall_index_column'


class MallIndexColumnGoods(models.Model):
    shop_id = models.CharField(max_length=64)
    column_id = models.CharField(max_length=64)
    goods_id = models.CharField(max_length=64)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    seq = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mall_index_column_goods'


class MallIndexPlate(models.Model):
    id = models.BigIntegerField(primary_key=True)
    brand_store_id = models.CharField(max_length=64)
    plate_id = models.CharField(unique=True, max_length=64)
    plate_name = models.CharField(max_length=20)
    plate_pic = models.CharField(max_length=200, blank=True, null=True)
    link_target_type = models.IntegerField(blank=True, null=True)
    link_page_url = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField()
    seq = models.IntegerField(blank=True, null=True)
    price_disp_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mall_index_plate'


class MallIndexPlateGoods(models.Model):
    brand_store_id = models.CharField(max_length=64)
    plate_id = models.CharField(max_length=64)
    goods_id = models.CharField(max_length=64)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mall_index_plate_goods'


class MallIndexPlatePics(models.Model):
    id = models.BigIntegerField()
    mall_id = models.CharField(max_length=64, blank=True, null=True)
    plate_id = models.CharField(max_length=64, blank=True, null=True)
    plate_pic = models.CharField(max_length=200, blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mall_index_plate_pics'


class MallIndexPlateShop(models.Model):
    brand_store_id = models.CharField(max_length=64)
    plate_id = models.CharField(max_length=64)
    shop_id = models.CharField(max_length=64)
    seq = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mall_index_plate_shop'


class MallMainBranches(models.Model):
    main_store_id = models.CharField(max_length=64)
    shop_id = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mall_main_branches'


class MallMemberInterest(models.Model):
    member_id = models.CharField(unique=True, max_length=64)
    interest_obj_type = models.IntegerField()
    object_id = models.CharField(max_length=64)
    mall_id = models.CharField(max_length=64)
    interest_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mall_member_interest'


class MallMerchants(models.Model):
    merchants_id = models.CharField(unique=True, max_length=64)
    mall_id = models.CharField(max_length=64)
    person = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    apply_floor = models.CharField(max_length=20, blank=True, null=True)
    apply_use = models.CharField(max_length=100, blank=True, null=True)
    apply_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mall_merchants'


class MallShopAttr(models.Model):
    shop_id = models.CharField(max_length=64)
    operation_type = models.IntegerField()
    floor_id = models.CharField(max_length=64, blank=True, null=True)
    shop_brand_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mall_shop_attr'


class MallShopBrand(models.Model):
    id = models.BigIntegerField(primary_key=True)
    brand_id = models.CharField(max_length=64, blank=True, null=True)
    brand_name = models.CharField(max_length=50)
    brand_pic = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mall_shop_brand'


class MallShopColumn(models.Model):
    id = models.BigIntegerField(primary_key=True)
    shop_id = models.CharField(max_length=64)
    column_id = models.CharField(max_length=64)
    seq = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mall_shop_column'


class MessageContent(models.Model):
    id = models.BigIntegerField(primary_key=True)
    from_field = models.CharField(db_column='from', max_length=50)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=50)
    message = models.TextField()
    send_time = models.DateTimeField()
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message_content'


class OnlineGoods(models.Model):
    agent_user_id = models.CharField(max_length=64)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    goods_id = models.CharField(max_length=64)
    goods_name = models.CharField(max_length=200)
    goods_img = models.CharField(max_length=150, blank=True, null=True)
    shop_price = models.DecimalField(db_column='shop_Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    goods_unit = models.CharField(max_length=10)
    column_name = models.CharField(max_length=50, blank=True, null=True)
    column_id = models.IntegerField(blank=True, null=True)
    goods_apply_id = models.CharField(max_length=36, blank=True, null=True)
    processdate = models.CharField(db_column='processDate', max_length=24, blank=True, null=True)  # Field name made lowercase.
    applydate = models.CharField(db_column='applyDate', max_length=24, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=302, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_goods'


class OrderActionLog(models.Model):
    id = models.AutoField()
    action_id = models.CharField(max_length=50, blank=True, null=True)
    fk_order_id = models.CharField(max_length=50, blank=True, null=True)
    status_type = models.IntegerField(blank=True, null=True)
    order_status = models.IntegerField(blank=True, null=True)
    shipping_status = models.IntegerField(blank=True, null=True)
    pay_status = models.IntegerField(blank=True, null=True)
    back_status = models.IntegerField()
    remark = models.CharField(max_length=255, blank=True, null=True)
    action_role = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_action_log'
        unique_together = (('id', 'back_status'),)


class OrderBackFlowInfo(models.Model):
    order_back_flow_info_id = models.CharField(max_length=50, blank=True, null=True)
    fk_order_back_info_id = models.CharField(max_length=50, blank=True, null=True)
    verify_msg = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    action_role = models.CharField(max_length=50, blank=True, null=True)
    creater = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_back_flow_info'


class OrderBackInfo(models.Model):
    order_back_info_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    order_back_no = models.CharField(max_length=50, blank=True, null=True)
    fk_order_id = models.CharField(max_length=50, blank=True, null=True)
    back_cause = models.CharField(max_length=255, blank=True, null=True)
    back_apply_type = models.IntegerField(blank=True, null=True)
    back_type = models.IntegerField(blank=True, null=True)
    back_desc = models.CharField(max_length=255, blank=True, null=True)
    back_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_type = models.IntegerField(blank=True, null=True)
    is_receive = models.CharField(max_length=1, blank=True, null=True)
    img1 = models.CharField(max_length=255, blank=True, null=True)
    img2 = models.CharField(max_length=255, blank=True, null=True)
    img3 = models.CharField(max_length=255, blank=True, null=True)
    back_expired_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    action_role = models.CharField(max_length=50, blank=True, null=True)
    verify_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=255, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_back_info'


class OrderBackTicket(models.Model):
    id = models.BigIntegerField(primary_key=True)
    ticket_name = models.CharField(max_length=64)
    fk_ticket_id = models.CharField(max_length=64)
    goods_id = models.CharField(max_length=64)
    shop_id = models.CharField(max_length=64)
    order_id = models.CharField(max_length=64)
    ticket_percent = models.CharField(max_length=64, blank=True, null=True)
    ticket_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_back_ticket'


class OrderCancellationReasons(models.Model):
    cancel_code = models.IntegerField(blank=True, null=True)
    cancel_reason = models.CharField(max_length=200, blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_cancellation_reasons'


class PaymentUserEb(models.Model):
    user_id = models.CharField(max_length=64, blank=True, null=True)
    remainder_count = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    unrecorded_count = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    freeze_count = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    freeze_yuan = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_user_eb'


class PaymentUserEbGoodstransInLogs(models.Model):
    eb_from = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    eb_num = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    receive_type = models.IntegerField(blank=True, null=True)
    recorded_time = models.DateTimeField(blank=True, null=True)
    biz_no = models.CharField(max_length=64, blank=True, null=True)
    biz_no_from = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_user_eb_goodstrans_in_logs'


class PaymentUserEbGoodstransOutLogs(models.Model):
    eb_from = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    eb_num = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    recorded_time = models.DateTimeField(blank=True, null=True)
    biz_no = models.CharField(max_length=64, blank=True, null=True)
    biz_no_from = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_user_eb_goodstrans_out_logs'


class PaymentUserEbInLogs(models.Model):
    eb_from = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    eb_num = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    receive_type = models.IntegerField(blank=True, null=True)
    recorded_time = models.DateTimeField(blank=True, null=True)
    biz_no = models.CharField(max_length=64, blank=True, null=True)
    biz_no_from = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_user_eb_in_logs'


class PaymentUserEbOutLogs(models.Model):
    eb_from = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    eb_num = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    recorded_time = models.DateTimeField(blank=True, null=True)
    biz_no = models.CharField(max_length=600, blank=True, null=True)
    biz_no_from = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_user_eb_out_logs'


class PlatMenu(models.Model):
    menu_id = models.CharField(max_length=64)
    menu_name = models.CharField(max_length=100, blank=True, null=True)
    parent_menu = models.CharField(max_length=64, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    disp_order = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plat_menu'


class PlatRoles(models.Model):
    role_id = models.CharField(max_length=64, blank=True, null=True)
    role_name = models.CharField(max_length=100, blank=True, null=True)
    role_desc = models.CharField(max_length=100, blank=True, null=True)
    role_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plat_roles'


class PlatRolesPrivilege(models.Model):
    role_id = models.CharField(max_length=64, blank=True, null=True)
    menu_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plat_roles_privilege'


class PlatUser(models.Model):
    plat_user_id = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    true_name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=300)
    salt = models.CharField(max_length=64, blank=True, null=True)
    token = models.CharField(max_length=64, blank=True, null=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    user_type = models.IntegerField()
    mobile = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.CharField(max_length=100, blank=True, null=True)
    user_level = models.IntegerField()
    status = models.IntegerField()
    province = models.CharField(max_length=100, blank=True, null=True)
    province_code = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    city_code = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    county_code = models.CharField(max_length=50, blank=True, null=True)
    creater = models.CharField(max_length=64)
    created_time = models.DateTimeField()
    modifier = models.CharField(max_length=64)
    updated_time = models.DateTimeField()
    last_login_time = models.DateTimeField(blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plat_user'


class PlatUserRole(models.Model):
    user_id = models.CharField(max_length=64, blank=True, null=True)
    role_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plat_user_role'


class RecommendCategory(models.Model):
    recomend_category_id = models.CharField(max_length=64)
    fk_category_id = models.CharField(max_length=50)
    source_category_name = models.CharField(max_length=100)
    recommend_category_name = models.CharField(max_length=100)
    recommend_category_desc = models.CharField(max_length=200)
    recommend_category_img = models.CharField(max_length=500, blank=True, null=True)
    sort_order = models.IntegerField()
    recommend_state = models.CharField(max_length=1, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modifier_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recommend_category'


class ScAddress(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    address = models.CharField(unique=True, max_length=255, blank=True, null=True)
    user_name = models.CharField(unique=True, max_length=64)
    user_pwd = models.CharField(max_length=64)
    status = models.IntegerField()
    name = models.CharField(max_length=64, blank=True, null=True)
    role = models.CharField(max_length=64, blank=True, null=True)
    txid = models.CharField(max_length=64, blank=True, null=True)
    public_key = models.CharField(max_length=64, blank=True, null=True)
    zsm_user_id = models.CharField(max_length=64, blank=True, null=True)
    zsm_role = models.CharField(max_length=64, blank=True, null=True)
    bind_time = models.DateTimeField(blank=True, null=True)
    bind_status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    modifier = models.CharField(max_length=64)
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sc_address'


class ScApiAccessRecord(models.Model):
    id = models.BigIntegerField()
    api_url = models.CharField(max_length=255, blank=True, null=True)
    api_name = models.CharField(max_length=255, blank=True, null=True)
    host = models.CharField(max_length=255, blank=True, null=True)
    req_data = models.TextField(blank=True, null=True)
    creater = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    modifier = models.CharField(max_length=64)
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sc_api_access_record'


class ScAssetIssue(models.Model):
    id = models.BigIntegerField(primary_key=True)
    address = models.CharField(max_length=64)
    user_pwd = models.CharField(max_length=64)
    symbol = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    amount = models.BigIntegerField()
    desc = models.CharField(max_length=255, blank=True, null=True)
    rule = models.CharField(max_length=255, blank=True, null=True)
    issuer = models.CharField(max_length=64, blank=True, null=True)
    metas = models.TextField(blank=True, null=True)
    txid = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField()
    creater = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    modifier = models.CharField(max_length=64)
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sc_asset_issue'


class ScClient(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_name = models.CharField(max_length=64, blank=True, null=True)
    user_pwd = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sc_client'


class ScPlatfromInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField()
    plat_address = models.CharField(max_length=64, blank=True, null=True)
    burn_address = models.CharField(max_length=64, blank=True, null=True)
    cash_address = models.CharField(max_length=64, blank=True, null=True)
    squan_symbol = models.CharField(max_length=64, blank=True, null=True)
    cash_symbol = models.CharField(max_length=64, blank=True, null=True)
    user_pwd = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sc_platfrom_info'


class ScTransaction(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    txid = models.CharField(unique=True, max_length=64, blank=True, null=True)
    user_name = models.CharField(max_length=64)
    address = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)
    amount = models.FloatField()
    to_address = models.CharField(max_length=255)
    desc = models.CharField(max_length=255, blank=True, null=True)
    tx_status = models.IntegerField()
    tx_msg = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    tx_type = models.IntegerField()
    creater = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    modifier = models.CharField(max_length=64)
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sc_transaction'


class ShopClosedApply(models.Model):
    apply_id = models.CharField(max_length=64)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    apply_person_id = models.CharField(max_length=64, blank=True, null=True)
    apply_reason = models.CharField(max_length=500, blank=True, null=True)
    apply_time = models.DateTimeField(blank=True, null=True)
    flow_status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_closed_apply'


class ShopClosedApproval(models.Model):
    apply_id = models.CharField(max_length=64)
    auditor_id = models.CharField(max_length=64, blank=True, null=True)
    auditor_type = models.IntegerField(blank=True, null=True)
    audit_result = models.IntegerField(blank=True, null=True)
    reject_reason = models.CharField(max_length=300, blank=True, null=True)
    audit_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_closed_approval'


class ShopHitsLog(models.Model):
    user_id = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    shop_name = models.CharField(max_length=100, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    province_code = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    city_code = models.CharField(max_length=20, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    county_code = models.CharField(max_length=20, blank=True, null=True)
    hits_time = models.DateField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_hits_log'


class ShopOperateReason(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    operator_type = models.IntegerField(blank=True, null=True)
    operator_id = models.CharField(max_length=64, blank=True, null=True)
    reason = models.CharField(max_length=500, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_operate_reason'


class ShopSysMenu(models.Model):
    menu_id = models.CharField(max_length=64)
    menu_name = models.CharField(max_length=100, blank=True, null=True)
    parent_menu = models.CharField(max_length=64, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    disp_order = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_sys_menu'


class ShopSysRoles(models.Model):
    role_id = models.CharField(max_length=64, blank=True, null=True)
    role_name = models.CharField(max_length=100, blank=True, null=True)
    role_desc = models.CharField(max_length=100, blank=True, null=True)
    role_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_sys_roles'


class ShopSysRolesPrivilege(models.Model):
    role_id = models.CharField(max_length=64, blank=True, null=True)
    menu_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_sys_roles_privilege'


class ShopSysUserRole(models.Model):
    user_id = models.CharField(max_length=64, blank=True, null=True)
    role_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_sys_user_role'


class ShopTypeDowngradeApply(models.Model):
    apply_id = models.CharField(max_length=64)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    apply_person_id = models.CharField(max_length=64, blank=True, null=True)
    apply_reason = models.CharField(max_length=500, blank=True, null=True)
    apply_time = models.DateTimeField(blank=True, null=True)
    flow_status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_type_downgrade_apply'


class ShopTypeDowngradeApproval(models.Model):
    apply_id = models.CharField(max_length=64)
    auditor_id = models.CharField(max_length=64, blank=True, null=True)
    auditor_type = models.IntegerField(blank=True, null=True)
    audit_result = models.IntegerField(blank=True, null=True)
    reject_reason = models.CharField(max_length=300, blank=True, null=True)
    audit_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_type_downgrade_approval'


class ShopTypeUpgrade(models.Model):
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    apply_reason = models.TextField(blank=True, null=True)
    apply_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    reject_reason = models.CharField(max_length=2000, blank=True, null=True)
    audit_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_type_upgrade'


class ShopTypeUpgradeAccessory(models.Model):
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    img_path = models.CharField(max_length=1000, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_type_upgrade_accessory'


class ShopTypeUpgradeLog(models.Model):
    apply_id = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    shop_name = models.CharField(max_length=100, blank=True, null=True)
    apply_reason = models.TextField(blank=True, null=True)
    apply_time = models.DateTimeField(blank=True, null=True)
    audit_time = models.DateTimeField(blank=True, null=True)
    audit_result = models.IntegerField(blank=True, null=True)
    reject_reason = models.CharField(max_length=2000, blank=True, null=True)
    audit_person = models.CharField(max_length=64, blank=True, null=True)
    apply_images = models.TextField(blank=True, null=True)
    apply_accessory = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_type_upgrade_log'


class ShopUser(models.Model):
    id = models.IntegerField(primary_key=True)
    plat_user_id = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    true_name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=300)
    salt = models.CharField(max_length=64, blank=True, null=True)
    token = models.CharField(max_length=64, blank=True, null=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    user_type = models.IntegerField()
    mobile = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.CharField(max_length=100, blank=True, null=True)
    user_level = models.IntegerField()
    status = models.IntegerField()
    province = models.CharField(max_length=100, blank=True, null=True)
    province_code = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    city_code = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    county_code = models.CharField(max_length=50, blank=True, null=True)
    creater = models.CharField(max_length=64)
    created_time = models.DateTimeField()
    modifier = models.CharField(max_length=64)
    updated_time = models.DateTimeField()
    last_login_time = models.DateTimeField()
    region = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_user'


class ShopingcartGoodsLog(models.Model):
    id = models.BigIntegerField(primary_key=True)
    shoping_cart_goods_id = models.CharField(max_length=64)
    goods_id = models.CharField(max_length=64)
    goods_name = models.CharField(max_length=100, blank=True, null=True)
    spec_id = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64)
    shop_name = models.CharField(max_length=50, blank=True, null=True)
    goods_num = models.IntegerField()
    user_id = models.CharField(max_length=64)
    shop_type = models.IntegerField(blank=True, null=True)
    shoping_time = models.DateField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopingcart_goods_log'


class SupplierAccount(models.Model):
    id = models.AutoField()
    merchant_id = models.CharField(max_length=64, blank=True, null=True)
    account = models.CharField(max_length=64, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    token = models.CharField(max_length=64, blank=True, null=True)
    salt = models.CharField(max_length=64, blank=True, null=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=64, blank=True, null=True)
    avatar = models.CharField(max_length=225, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    last_login_time = models.DateTimeField(blank=True, null=True)
    im_password = models.CharField(max_length=64, blank=True, null=True)
    is_permit_settlement = models.CharField(max_length=255, blank=True, null=True)
    pay_password = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    union_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_account'


class SupplierBank(models.Model):
    bank_id = models.CharField(max_length=64, blank=True, null=True)
    supplier_id = models.CharField(max_length=64, blank=True, null=True)
    bank_no = models.CharField(max_length=50, blank=True, null=True)
    bank_user = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=50, blank=True, null=True)
    bank_province_code = models.CharField(max_length=255, blank=True, null=True)
    bank_province_name = models.CharField(max_length=255, blank=True, null=True)
    bank_city_code = models.CharField(max_length=255, blank=True, null=True)
    bank_city_name = models.CharField(max_length=255, blank=True, null=True)
    bank_county_code = models.CharField(max_length=255, blank=True, null=True)
    bank_county_name = models.CharField(max_length=255, blank=True, null=True)
    bank_address = models.CharField(max_length=500, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    owner_id = models.CharField(max_length=18, blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_bank'


class SupplierCash(models.Model):
    bank_no = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=50, blank=True, null=True)
    bank_id = models.CharField(max_length=64, blank=True, null=True)
    money = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fee = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    reject_reason = models.CharField(max_length=255, blank=True, null=True)
    out_card_no = models.CharField(max_length=50, blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    cash_id = models.CharField(max_length=64, blank=True, null=True)
    supplier_id = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    audit_time = models.DateTimeField(blank=True, null=True)
    cash_type = models.IntegerField(blank=True, null=True)
    open_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_cash'


class SupplierInfo(models.Model):
    merchant_code = models.CharField(max_length=64, blank=True, null=True)
    merchant_id = models.CharField(max_length=64, blank=True, null=True)
    merchant_name = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    merchant_mobile = models.CharField(max_length=30, blank=True, null=True)
    merchant_person = models.CharField(max_length=50, blank=True, null=True)
    is_curator = models.CharField(max_length=1, blank=True, null=True)
    direct_investment_curator = models.CharField(max_length=50, blank=True, null=True)
    is_send_order_msg = models.CharField(max_length=1, blank=True, null=True)
    is_valid = models.CharField(max_length=1, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_info'


class SupplierPaymentInfo(models.Model):
    id = models.AutoField()
    payment_id = models.CharField(max_length=64, blank=True, null=True)
    supplier_id = models.CharField(max_length=64, blank=True, null=True)
    money_remainder = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    money_unrecorded = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    money_freeze = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_payment_info'


class SupplierPaymentLog(models.Model):
    id = models.IntegerField(blank=True, null=True)
    payment_id = models.CharField(max_length=64, blank=True, null=True)
    money_from = models.CharField(max_length=64, blank=True, null=True)
    money = models.CharField(max_length=64, blank=True, null=True)
    is_income = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_payment_log'


class SupplierRelateSpecInfo(models.Model):
    merchant_code = models.CharField(max_length=64, blank=True, null=True)
    merchant_name = models.CharField(max_length=100, blank=True, null=True)
    merchant_id = models.CharField(max_length=64, blank=True, null=True)
    spec_id = models.CharField(max_length=64, blank=True, null=True)
    operation_model = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_relate_spec_info'


class SysAppAdsInfo(models.Model):
    ads_id = models.CharField(max_length=64, blank=True, null=True)
    ads_name = models.CharField(max_length=255, blank=True, null=True)
    ads_type = models.CharField(max_length=2, blank=True, null=True)
    ads_img = models.CharField(max_length=255, blank=True, null=True)
    ads_desc = models.TextField(blank=True, null=True)
    ads_status = models.CharField(max_length=2, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_app_ads_info'


class SysBank(models.Model):
    bank_code = models.CharField(max_length=32)
    bank_name = models.CharField(max_length=64)
    bank_type = models.IntegerField()
    country_code = models.CharField(max_length=10)
    status = models.IntegerField()
    seq = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_bank'


class SysChina(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    level = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'sys_china'


class SysConfigInfo(models.Model):
    module_code = models.CharField(max_length=64, blank=True, null=True)
    module_name = models.CharField(max_length=64, blank=True, null=True)
    config_code = models.CharField(max_length=64, blank=True, null=True)
    config_name = models.CharField(max_length=64, blank=True, null=True)
    config_value = models.CharField(max_length=4000, blank=True, null=True)
    status = models.CharField(max_length=2, blank=True, null=True)
    remark = models.CharField(max_length=4000, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_config_info'


class SysEbTransfer(models.Model):
    eb_transfer_id = models.CharField(max_length=64, blank=True, null=True)
    pay_user_id = models.CharField(max_length=64, blank=True, null=True)
    receive_user_id = models.CharField(max_length=64, blank=True, null=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    transfer_desc = models.CharField(max_length=200, blank=True, null=True)
    transfer_time = models.DateTimeField(blank=True, null=True)
    receive_time = models.DateTimeField(blank=True, null=True)
    overtime_time = models.DateTimeField(blank=True, null=True)
    refund_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_eb_transfer'


class SysRegion(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    region_code = models.CharField(max_length=20, blank=True, null=True)
    region_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_region'


class SysRegionChina(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_region_id = models.CharField(max_length=64, blank=True, null=True)
    fk_china_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_region_china'


class SysScheduleJob(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    job_name = models.CharField(max_length=500)
    job_group = models.CharField(max_length=500)
    cron_expression = models.CharField(max_length=500)
    description = models.CharField(max_length=255, blank=True, null=True)
    bean_class = models.CharField(max_length=255)
    spring_id = models.CharField(max_length=500, blank=True, null=True)
    method_name = models.CharField(max_length=255)
    job_status = models.CharField(max_length=1)
    is_concurrent = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_schedule_job'


class SysScheduleJobLog(models.Model):
    job_name = models.CharField(max_length=255, blank=True, null=True)
    job_type = models.IntegerField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    job_desc = models.TextField(blank=True, null=True)
    execute_start_time = models.DateTimeField(blank=True, null=True)
    execute_end_time = models.DateTimeField(blank=True, null=True)
    execute_status = models.IntegerField(blank=True, null=True)
    execute_error_des = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_schedule_job_log'


class SystemVersions(models.Model):
    system_versions_id = models.CharField(max_length=64)
    system_name = models.CharField(max_length=64)
    system_code = models.CharField(max_length=64)
    system_versions = models.CharField(max_length=64)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_versions'


class TagArticleDictionary(models.Model):
    tag_id = models.CharField(max_length=64)
    tag_name = models.CharField(max_length=64)
    tag_type = models.CharField(max_length=1)
    ico = models.CharField(max_length=500, blank=True, null=True)
    article_cover_num = models.IntegerField(blank=True, null=True)
    article_cover_h = models.IntegerField(blank=True, null=True)
    article_cover_w = models.IntegerField(blank=True, null=True)
    seq = models.IntegerField()
    create_time = models.DateTimeField()
    is_show = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tag_article_dictionary'


class TagDictionary(models.Model):
    tag_id = models.CharField(max_length=64)
    tag_name = models.CharField(max_length=64)
    tag_type = models.CharField(max_length=1)
    ico = models.CharField(max_length=500, blank=True, null=True)
    seq = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tag_dictionary'


class TagRelationshipSearchtype(models.Model):
    tag_relationship_id = models.CharField(max_length=64)
    tag_id = models.CharField(max_length=64)
    searchtype_id = models.CharField(max_length=64)
    tag_type = models.CharField(max_length=1)
    seq = models.IntegerField()
    create_time = models.DateTimeField()
    creater = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tag_relationship_searchtype'


class Ticket701AuthUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    auth_user_701_id = models.CharField(max_length=64)
    fk_fund_pool_id = models.CharField(max_length=64)
    fk_ticket_id = models.CharField(max_length=64)
    login_name = models.CharField(max_length=32)
    auth_user_id = models.CharField(max_length=64)
    auth_type = models.IntegerField()
    auth_amount = models.DecimalField(max_digits=12, decimal_places=2)
    state = models.IntegerField()
    contacts = models.CharField(max_length=32)
    contacts_tel = models.CharField(max_length=32)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ticket_701_auth_user'


class Ticket701AuthUserBatch(models.Model):
    id = models.BigIntegerField(primary_key=True)
    auth_user_batch_id = models.CharField(max_length=64)
    fk_fund_pool_id = models.CharField(max_length=64)
    fk_batch_id = models.CharField(max_length=64)
    fk_ticket_id = models.CharField(max_length=64)
    fk_auth_user_id = models.CharField(max_length=64)
    receive_user_count = models.SmallIntegerField()
    receive_amount = models.DecimalField(max_digits=12, decimal_places=2)
    auth_amount = models.DecimalField(max_digits=12, decimal_places=2)
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ticket_701_auth_user_batch'


class Ticket701Batch(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fk_fund_pool_id = models.CharField(max_length=64)
    batch_id = models.CharField(max_length=64)
    amount_total = models.DecimalField(max_digits=12, decimal_places=2)
    amount_use = models.DecimalField(max_digits=12, decimal_places=2)
    state = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_701_batch'


class Ticket701FundPool(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fund_pool_id = models.CharField(max_length=64)
    fk_ticket_id = models.CharField(max_length=64)
    shop_id = models.CharField(max_length=64)
    shop_role = models.IntegerField(blank=True, null=True)
    amount_total = models.DecimalField(max_digits=12, decimal_places=2)
    amount_use = models.DecimalField(max_digits=12, decimal_places=2)
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ticket_701_fund_pool'


class Ticket701History(models.Model):
    id = models.BigIntegerField(primary_key=True)
    batch_history_id = models.CharField(max_length=64, blank=True, null=True)
    fk_fund_pool_id = models.CharField(max_length=64)
    fk_batch_id = models.CharField(max_length=64)
    fk_ticket_id = models.CharField(max_length=64)
    ticket_name = models.CharField(max_length=64)
    fk_auth_user_id = models.CharField(max_length=64)
    auth_type = models.IntegerField()
    shop_id = models.CharField(max_length=64)
    origin_type = models.IntegerField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    state = models.IntegerField()
    create_time = models.DateTimeField()
    over_time = models.DateTimeField()
    is_register = models.CharField(max_length=1)
    receive_user_id = models.CharField(max_length=64, blank=True, null=True)
    receive_user_tel = models.CharField(max_length=64, blank=True, null=True)
    receive_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_701_history'


class TicketCategory(models.Model):
    id = models.AutoField()
    ticket_id = models.CharField(unique=True, max_length=64)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    ticket_type = models.SmallIntegerField(unique=True, blank=True, null=True)
    ticket_category = models.CharField(max_length=64, blank=True, null=True)
    ticket_name = models.CharField(max_length=64, blank=True, null=True)
    ticket_logo = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_category'
        unique_together = (('id', 'ticket_id'),)


class TicketGiveHistory(models.Model):
    give_history_id = models.CharField(max_length=64, blank=True, null=True)
    fk_give_ticket_id = models.CharField(max_length=64)
    give_type = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    user_id = models.CharField(max_length=64)
    distribute_user_id = models.CharField(max_length=64, blank=True, null=True)
    distribute_user_account = models.CharField(max_length=64, blank=True, null=True)
    distribute_user_name = models.CharField(max_length=64, blank=True, null=True)
    receive_user_id = models.CharField(max_length=64, blank=True, null=True)
    receive_user_account = models.CharField(max_length=64, blank=True, null=True)
    receive_user_name = models.CharField(max_length=64, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ticket_give_history'


class TicketGiveInfo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    give_ticket_id = models.CharField(max_length=64)
    fk_ticket_id = models.CharField(max_length=64)
    distribute_user_id = models.CharField(max_length=64)
    ticket_name = models.CharField(max_length=64)
    amount_total = models.DecimalField(max_digits=12, decimal_places=2)
    amount_use = models.DecimalField(max_digits=12, decimal_places=2)
    give_type = models.IntegerField()
    give_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    give_count = models.SmallIntegerField()
    state = models.IntegerField()
    remark = models.CharField(max_length=20)
    create_time = models.DateTimeField()
    over_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_give_info'


class TicketMeykiFundPool(models.Model):
    id = models.BigIntegerField(primary_key=True)
    meyki_fund_pool_id = models.CharField(max_length=64)
    fk_ticket_id = models.CharField(max_length=64)
    shop_id = models.CharField(max_length=64)
    shop_role = models.IntegerField(blank=True, null=True)
    login_name = models.CharField(max_length=64)
    shop_name = models.CharField(max_length=64)
    contacts = models.CharField(max_length=32, blank=True, null=True)
    contacts_tel = models.CharField(max_length=32, blank=True, null=True)
    province = models.CharField(max_length=100)
    province_code = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=100)
    city_code = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=100)
    county_code = models.CharField(max_length=50, blank=True, null=True)
    publish_type = models.IntegerField()
    amount_recovery = models.DecimalField(max_digits=12, decimal_places=2)
    amount_total = models.DecimalField(max_digits=12, decimal_places=2)
    amount_use = models.DecimalField(max_digits=12, decimal_places=2)
    state = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ticket_meyki_fund_pool'


class TicketMeykiLuckybag(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fk_ticket_id = models.CharField(max_length=64)
    luckybag_id = models.CharField(max_length=64)
    shop_id = models.CharField(max_length=64)
    amount_total = models.DecimalField(max_digits=12, decimal_places=2)
    amount_use = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    luckybag_count = models.SmallIntegerField()
    luckybag_receive_count = models.SmallIntegerField(blank=True, null=True)
    luckybag_price = models.DecimalField(max_digits=12, decimal_places=2)
    luckybag_lat = models.CharField(max_length=32)
    luckybag_lon = models.CharField(max_length=32)
    state = models.IntegerField()
    is_haskey = models.CharField(max_length=1)
    luckybag_key = models.CharField(max_length=255, blank=True, null=True)
    key_origin_type = models.IntegerField(blank=True, null=True)
    create_user = models.CharField(max_length=64)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ticket_meyki_luckybag'


class TicketMeykiLuckybagHistory(models.Model):
    luckybag_history_id = models.CharField(max_length=64)
    fk_luckybag_id = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    user_id = models.CharField(max_length=64)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ticket_meyki_luckybag_history'


class TicketTransaction(models.Model):
    id = models.BigIntegerField(primary_key=True)
    ticket_name = models.CharField(max_length=64)
    fk_ticket_id = models.CharField(max_length=64)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    shop_name = models.CharField(max_length=64, blank=True, null=True)
    origin_type = models.IntegerField()
    origin_id = models.CharField(max_length=64, blank=True, null=True)
    origin_source = models.CharField(max_length=64, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ticket_transaction'


class TicketUserFundPool(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fk_ticket_id = models.CharField(max_length=64)
    ticket_name = models.CharField(max_length=64)
    user_id = models.CharField(max_length=64)
    amount_total = models.DecimalField(max_digits=12, decimal_places=2)
    amount_use = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ticket_user_fund_pool'


class UnionRefundReqLog(models.Model):
    refund_req_id = models.CharField(max_length=64)
    mer_id = models.CharField(max_length=100, blank=True, null=True)
    order_id = models.CharField(max_length=64, blank=True, null=True)
    txn_order_id = models.CharField(max_length=64, blank=True, null=True)
    txn_time = models.CharField(max_length=40, blank=True, null=True)
    txn_amt = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    refund_amt = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    back_order_id = models.CharField(max_length=64, blank=True, null=True)
    trace_no = models.CharField(max_length=64, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'union_refund_req_log'


class UserOperateLog(models.Model):
    operator = models.CharField(max_length=64, blank=True, null=True)
    opt_method = models.CharField(max_length=64, blank=True, null=True)
    opt_uri = models.CharField(max_length=128)
    opt_time = models.DateTimeField()
    opt_desc = models.CharField(max_length=512, blank=True, null=True)
    opt_platform = models.CharField(max_length=128, blank=True, null=True)
    biz_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_operate_log'


class WeixinSignUser(models.Model):
    user_id = models.CharField(max_length=64, blank=True, null=True)
    open_id = models.CharField(max_length=64, blank=True, null=True)
    union_id = models.CharField(max_length=64, blank=True, null=True)
    nick_name = models.TextField(blank=True, null=True)
    head_imgurl = models.CharField(max_length=500, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weixin_sign_user'


class YpRelUserShopingcart(models.Model):
    id = models.BigIntegerField(primary_key=True)
    shoping_cart_id = models.CharField(max_length=64)
    shoping_cart_type = models.IntegerField()
    user_id = models.CharField(max_length=64)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    spec_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yp_rel_user_shopingcart'


class YpShopingcartGoods(models.Model):
    id = models.BigIntegerField(primary_key=True)
    shoping_cart_goods_id = models.CharField(max_length=64)
    goods_id = models.CharField(max_length=64)
    spec_id = models.CharField(max_length=64, blank=True, null=True)
    shop_id = models.CharField(max_length=64)
    goods_num = models.IntegerField()
    user_id = models.CharField(max_length=64)
    shop_type = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=255, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    union_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yp_shopingcart_goods'


class Zh701Dept(models.Model):
    id = models.IntegerField(primary_key=True)
    dept_id = models.CharField(max_length=32, blank=True, null=True)
    dept_name = models.CharField(max_length=150, blank=True, null=True)
    parent_dept = models.CharField(max_length=32, blank=True, null=True)
    dept_num = models.CharField(max_length=32, blank=True, null=True)
    is_parent = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zh_701_dept'


class Zh701DeptUser(models.Model):
    id = models.IntegerField(primary_key=True)
    dept_id = models.CharField(max_length=32, blank=True, null=True)
    user_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zh_701_dept_user'


class Zh701Goods(models.Model):
    goods_id = models.CharField(max_length=64)
    fk_category_brand_id = models.CharField(max_length=64, blank=True, null=True)
    brand_name = models.CharField(max_length=50, blank=True, null=True)
    goods_sn = models.CharField(max_length=20, blank=True, null=True)
    goods_name = models.CharField(max_length=200)
    goods_img = models.CharField(max_length=150, blank=True, null=True)
    goods_stock = models.IntegerField(blank=True, null=True)
    goods_spec = models.TextField(blank=True, null=True)
    goods_desc = models.TextField()
    goods_status = models.IntegerField()
    shelves_time = models.DateTimeField(blank=True, null=True)
    down_shelves_time = models.DateTimeField(blank=True, null=True)
    is_online_buy = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    tax_price_interlval = models.CharField(max_length=50, blank=True, null=True)
    shop_price_interval = models.CharField(max_length=50, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zh_701_goods'


class Zh701GoodsAttr(models.Model):
    goods_attr_id = models.CharField(max_length=50)
    goods_id = models.CharField(max_length=50)
    fk_category_attr_id = models.CharField(max_length=50, blank=True, null=True)
    fk_category_attr_value_id = models.CharField(max_length=50, blank=True, null=True)
    attr_alias = models.CharField(max_length=40, blank=True, null=True)
    attr_name = models.CharField(max_length=40)
    attr_value = models.CharField(max_length=40)
    parent_id = models.CharField(max_length=50, blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zh_701_goods_attr'


class Zh701GoodsCategory(models.Model):
    fk_goods_id = models.CharField(max_length=50)
    fk_category_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'zh_701_goods_category'


class Zh701GoodsGallerys(models.Model):
    goods_id = models.CharField(max_length=64)
    goods_img = models.CharField(max_length=150)
    img_type = models.IntegerField(blank=True, null=True)
    delete_flag = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    img_sequence = models.IntegerField(blank=True, null=True)
    is_cover = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zh_701_goods_gallerys'


class Zh701GoodsSkuAttr(models.Model):
    id = models.BigIntegerField(primary_key=True)
    goods_sku_attr_id = models.CharField(max_length=50)
    fk_spec_t = models.CharField(max_length=50, blank=True, null=True)
    fk_category_attr_id = models.CharField(max_length=50, blank=True, null=True)
    fk_category_attr_value_id = models.CharField(max_length=50, blank=True, null=True)
    attr_name = models.CharField(max_length=50, blank=True, null=True)
    attr_value = models.CharField(max_length=100, blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zh_701_goods_sku_attr'


class Zh701GoodsSpecT(models.Model):
    spec_id = models.CharField(max_length=64)
    goods_id = models.CharField(max_length=64)
    spec_name = models.CharField(max_length=500)
    country_id = models.IntegerField(blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    spec_count = models.IntegerField(blank=True, null=True)
    spec_status = models.CharField(max_length=1, blank=True, null=True)
    spec_book_min = models.IntegerField(blank=True, null=True)
    spec_img = models.CharField(max_length=1000, blank=True, null=True)
    spec_unit = models.CharField(max_length=100, blank=True, null=True)
    spec_seq = models.IntegerField(blank=True, null=True)
    spec_barcode = models.CharField(max_length=50, blank=True, null=True)
    spec_code = models.CharField(max_length=50, blank=True, null=True)
    is_default = models.IntegerField()
    price_tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_spec = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shelves_time = models.DateTimeField(blank=True, null=True)
    down_shelves_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zh_701_goods_spec_t'


class Zh701GoodsSupplier(models.Model):
    suplier_id = models.CharField(max_length=64)
    suplier_code = models.CharField(max_length=64, blank=True, null=True)
    supplier_name = models.CharField(max_length=64, blank=True, null=True)
    goods_id = models.CharField(max_length=64)
    spec_id = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zh_701_goods_supplier'


class Zh701Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    menu_id = models.CharField(max_length=32, blank=True, null=True)
    menu_name = models.CharField(max_length=100, blank=True, null=True)
    parent_menu = models.CharField(max_length=32, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    is_parent = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zh_701_menu'


class Zh701Role(models.Model):
    id = models.IntegerField(primary_key=True)
    role_id = models.CharField(max_length=32, blank=True, null=True)
    role_name = models.CharField(max_length=100, blank=True, null=True)
    role_desc = models.CharField(max_length=100, blank=True, null=True)
    role_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zh_701_role'


class Zh701RoleMenu(models.Model):
    id = models.IntegerField(primary_key=True)
    role_id = models.CharField(max_length=32, blank=True, null=True)
    menu_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zh_701_role_menu'


class Zh701RoleUser(models.Model):
    id = models.IntegerField(primary_key=True)
    role_id = models.CharField(max_length=32, blank=True, null=True)
    user_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zh_701_role_user'


class Zh701SupplierInfo(models.Model):
    suplier_code = models.CharField(max_length=64, blank=True, null=True)
    suplier_id = models.CharField(max_length=64, blank=True, null=True)
    supplier_name = models.CharField(max_length=100, blank=True, null=True)
    contacts = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=30, blank=True, null=True)
    inviter = models.CharField(max_length=50, blank=True, null=True)
    supply_mode = models.CharField(max_length=20, blank=True, null=True)
    supply_mode_name = models.CharField(max_length=20, blank=True, null=True)
    operation_mode = models.CharField(max_length=20, blank=True, null=True)
    operation_mode_name = models.CharField(max_length=20, blank=True, null=True)
    is_send_order_msg = models.CharField(max_length=1, blank=True, null=True)
    c_company_name = models.CharField(max_length=50, blank=True, null=True)
    c_register_address = models.CharField(max_length=50, blank=True, null=True)
    c_registered_capital = models.IntegerField(blank=True, null=True)
    c_established_date = models.DateTimeField(blank=True, null=True)
    c_social_credit_code = models.CharField(max_length=50, blank=True, null=True)
    c_law_person = models.CharField(max_length=50, blank=True, null=True)
    c_register_office = models.CharField(max_length=100, blank=True, null=True)
    c_company_type = models.CharField(max_length=50, blank=True, null=True)
    c_company_type_name = models.CharField(max_length=50, blank=True, null=True)
    c_busniss_term_start = models.DateTimeField(blank=True, null=True)
    c_busniss_term_end = models.DateTimeField(blank=True, null=True)
    c_yearly_report_time = models.DateTimeField(blank=True, null=True)
    c_business_scope = models.CharField(max_length=1000, blank=True, null=True)
    law_person_identity_card_photo_front = models.CharField(max_length=200, blank=True, null=True)
    law_person_identity_card_photo_back = models.CharField(max_length=200, blank=True, null=True)
    bank_card_photo_front = models.CharField(max_length=200, blank=True, null=True)
    bank_card_photo_back = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zh_701_supplier_info'


class Zh701User(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=32, blank=True, null=True)
    user_account = models.CharField(max_length=64, blank=True, null=True)
    user_name = models.CharField(max_length=64, blank=True, null=True)
    password = models.CharField(max_length=32, blank=True, null=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=32, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=32, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zh_701_user'


class ZsmAliPayLog(models.Model):
    ali_pay_log_id = models.CharField(max_length=64)
    notify_time = models.DateTimeField()
    notify_type = models.CharField(max_length=64)
    notify_id = models.CharField(max_length=64)
    app_id = models.CharField(max_length=255)
    charset = models.CharField(max_length=10)
    version = models.CharField(max_length=3)
    sign_type = models.CharField(max_length=64)
    sign = models.TextField()
    trade_no = models.CharField(max_length=64)
    out_trade_no = models.CharField(max_length=64)
    out_biz_no = models.CharField(max_length=64, blank=True, null=True)
    buyer_id = models.CharField(max_length=30, blank=True, null=True)
    buyer_logon_id = models.CharField(max_length=255, blank=True, null=True)
    seller_id = models.CharField(max_length=30, blank=True, null=True)
    seller_email = models.CharField(max_length=100, blank=True, null=True)
    trade_status = models.CharField(max_length=64, blank=True, null=True)
    total_amount = models.CharField(max_length=10, blank=True, null=True)
    receipt_amount = models.CharField(max_length=255, blank=True, null=True)
    invoice_amount = models.CharField(max_length=255, blank=True, null=True)
    buyer_pay_amount = models.CharField(max_length=255, blank=True, null=True)
    point_amount = models.CharField(max_length=255, blank=True, null=True)
    refund_fee = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    body = models.CharField(max_length=512, blank=True, null=True)
    gmt_create = models.DateTimeField(blank=True, null=True)
    gmt_payment = models.DateTimeField(blank=True, null=True)
    gmt_refund = models.DateTimeField(blank=True, null=True)
    gmt_close = models.CharField(max_length=255, blank=True, null=True)
    fund_bill_list = models.CharField(max_length=255, blank=True, null=True)
    refund_status = models.CharField(max_length=64, blank=True, null=True)
    passback_params = models.CharField(max_length=1000, blank=True, null=True)
    voucher_detail_list = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_ali_pay_log'


class ZsmCityagentBuyRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField(blank=True, null=True)
    buy_tx_id = models.CharField(max_length=64)
    fk_buy_user_id = models.CharField(max_length=64, blank=True, null=True)
    fk_shop_user_id = models.CharField(max_length=64, blank=True, null=True)
    fk_shop_id = models.CharField(max_length=64)
    shop_name = models.CharField(max_length=64, blank=True, null=True)
    shop_img = models.CharField(max_length=255, blank=True, null=True)
    pay_amount = models.DecimalField(max_digits=10, decimal_places=2)
    ticket_amount = models.DecimalField(max_digits=10, decimal_places=2)
    ticket_id = models.CharField(max_length=64, blank=True, null=True)
    pay_type = models.IntegerField()
    buy_time = models.DateTimeField()
    pay_status = models.IntegerField()
    out_trans_id = models.CharField(max_length=64, blank=True, null=True)
    refunded_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_all_refund = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_cityagent_buy_record'


class ZsmCityagentRefundRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField()
    buy_tx_id = models.CharField(max_length=64)
    fk_buy_user_id = models.CharField(max_length=64)
    fk_shop_id = models.CharField(max_length=64)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2)
    refund_time = models.DateTimeField()
    out_trans_id = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField()
    remark = models.CharField(max_length=64)
    creater = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    modifier = models.CharField(max_length=64)
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'zsm_cityagent_refund_record'


class ZsmCredit(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_user_id = models.CharField(max_length=64)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_credit'


class ZsmCreditConfig(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    role_id = models.CharField(max_length=64, blank=True, null=True)
    fk_user_id = models.CharField(max_length=64, blank=True, null=True)
    receive = models.DecimalField(max_digits=10, decimal_places=3)
    verify = models.DecimalField(max_digits=10, decimal_places=2)
    newly_user = models.DecimalField(max_digits=10, decimal_places=2)
    good_evaluate = models.DecimalField(max_digits=10, decimal_places=2)
    recovery = models.DecimalField(max_digits=10, decimal_places=2)
    bad_evaluate = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_credit_config'


class ZsmCreditRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_user_id = models.CharField(max_length=64)
    fk_act_user_id = models.CharField(max_length=64)
    fk_service_id = models.CharField(max_length=64, blank=True, null=True)
    service_type = models.IntegerField(blank=True, null=True)
    payment_type = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_credit_record'


class ZsmIdentityLog(models.Model):
    identity_id = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    user_rold = models.CharField(max_length=200, blank=True, null=True)
    shop_id = models.CharField(max_length=64, blank=True, null=True)
    shop_user = models.CharField(max_length=64, blank=True, null=True)
    is_check = models.CharField(max_length=64, blank=True, null=True)
    reject_reason = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_identity_log'


class ZsmIncome(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_user_id = models.CharField(max_length=64)
    total = models.DecimalField(max_digits=10, decimal_places=4)
    alive = models.DecimalField(max_digits=10, decimal_places=4)
    freeze = models.DecimalField(max_digits=10, decimal_places=4)
    expect = models.DecimalField(max_digits=10, decimal_places=4)
    status = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    hf_money = models.DecimalField(max_digits=10, decimal_places=4)
    hf_freeze = models.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'zsm_income'


class ZsmIncomeBak0824(models.Model):
    id = models.CharField(max_length=64)
    fk_user_id = models.CharField(max_length=64)
    total = models.DecimalField(max_digits=10, decimal_places=4)
    alive = models.DecimalField(max_digits=10, decimal_places=4)
    freeze = models.DecimalField(max_digits=10, decimal_places=4)
    expect = models.DecimalField(max_digits=10, decimal_places=4)
    status = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    hf_money = models.DecimalField(max_digits=10, decimal_places=4)
    hf_freeze = models.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'zsm_income_bak0824'


class ZsmIncomeConfig(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_user_id = models.CharField(max_length=64)
    total = models.DecimalField(max_digits=10, decimal_places=4)
    system = models.DecimalField(max_digits=10, decimal_places=4)
    first = models.DecimalField(max_digits=10, decimal_places=4)
    second = models.DecimalField(max_digits=10, decimal_places=4)
    status = models.IntegerField()
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_income_config'


class ZsmIncomeConfigLock(models.Model):
    fk_user_id = models.CharField(max_length=64)
    total = models.DecimalField(max_digits=10, decimal_places=4)
    system = models.DecimalField(max_digits=10, decimal_places=4)
    partner = models.DecimalField(max_digits=10, decimal_places=4)
    store = models.DecimalField(max_digits=10, decimal_places=4)
    credit = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    ticket = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    lock_guest = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    status = models.IntegerField()
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_income_config_lock'


class ZsmIncomeConfigLockLog(models.Model):
    fk_user_id = models.CharField(max_length=255, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    system = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    partner = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    store = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    creater = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    cause = models.CharField(max_length=900, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_income_config_lock_log'


class ZsmIncomeRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_user_id = models.CharField(max_length=64)
    fk_act_user_id = models.CharField(max_length=64, blank=True, null=True)
    fk_service_id = models.CharField(max_length=64, blank=True, null=True)
    service_type = models.IntegerField(blank=True, null=True)
    payment_type = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    withdrawal_status = models.CharField(max_length=10, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_income_record'


class ZsmIncomeRecordAllBak(models.Model):
    id = models.CharField(max_length=64)
    fk_user_id = models.CharField(max_length=64)
    fk_act_user_id = models.CharField(max_length=64, blank=True, null=True)
    fk_service_id = models.CharField(max_length=64, blank=True, null=True)
    service_type = models.IntegerField(blank=True, null=True)
    payment_type = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    withdrawal_status = models.CharField(max_length=10, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_income_record_all_bak'


class ZsmIncomeRecordBak0813(models.Model):
    id = models.CharField(max_length=64)
    fk_user_id = models.CharField(max_length=64)
    fk_act_user_id = models.CharField(max_length=64, blank=True, null=True)
    fk_service_id = models.CharField(max_length=64, blank=True, null=True)
    service_type = models.IntegerField(blank=True, null=True)
    payment_type = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    withdrawal_status = models.CharField(max_length=10, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_income_record_bak0813'


class ZsmIncomeRecordBak20180801(models.Model):
    id = models.CharField(max_length=64)
    fk_user_id = models.CharField(max_length=64)
    fk_act_user_id = models.CharField(max_length=64, blank=True, null=True)
    fk_service_id = models.CharField(max_length=64, blank=True, null=True)
    service_type = models.IntegerField(blank=True, null=True)
    payment_type = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    withdrawal_status = models.CharField(max_length=10, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_income_record_bak20180801'


class ZsmInstantActivity(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_user_id = models.CharField(max_length=64)
    fk_shop_id = models.CharField(max_length=64)
    title = models.CharField(max_length=32)
    look = models.IntegerField()
    image1 = models.CharField(max_length=100)
    detail1 = models.CharField(max_length=256)
    image2 = models.CharField(max_length=100, blank=True, null=True)
    detail2 = models.CharField(max_length=256, blank=True, null=True)
    image3 = models.CharField(max_length=100, blank=True, null=True)
    detail3 = models.CharField(max_length=256, blank=True, null=True)
    image4 = models.CharField(max_length=100, blank=True, null=True)
    detail4 = models.CharField(max_length=256, blank=True, null=True)
    image5 = models.CharField(max_length=100, blank=True, null=True)
    detail5 = models.CharField(max_length=256, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_instant_activity'


class ZsmLocaleBonusRecord(models.Model):
    signin_id = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    type_name = models.CharField(max_length=100, blank=True, null=True)
    bonus_set_id = models.IntegerField(blank=True, null=True)
    logcale_type = models.IntegerField(blank=True, null=True)
    bout = models.IntegerField(blank=True, null=True)
    bout_name = models.CharField(max_length=50, blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_locale_bonus_record'


class ZsmLocaleBonusSet(models.Model):
    locale_type = models.IntegerField(blank=True, null=True)
    bout = models.IntegerField(blank=True, null=True)
    bout_name = models.CharField(max_length=50, blank=True, null=True)
    totality = models.IntegerField(blank=True, null=True)
    win_sum = models.IntegerField(blank=True, null=True)
    left_sum = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_locale_bonus_set'


class ZsmLocaleSigninInfo(models.Model):
    mobile = models.CharField(max_length=11, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    type_name = models.CharField(max_length=100, blank=True, null=True)
    fk_user_id = models.CharField(max_length=64, blank=True, null=True)
    locale_type = models.IntegerField(blank=True, null=True)
    is_winning = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_locale_signin_info'


class ZsmQrcodeInfo(models.Model):
    rd = models.CharField(max_length=500, blank=True, null=True)
    fk_user_id = models.CharField(max_length=500, blank=True, null=True)
    shop_id = models.CharField(max_length=500, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    qrcode_url = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    creater = models.CharField(max_length=500, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=500, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_qrcode_info'


class ZsmShopHuifuInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField()
    shop_user_id = models.CharField(max_length=64)
    shop_id = models.CharField(max_length=64)
    user_cust_id = models.CharField(max_length=64)
    mer_cust_id = models.CharField(max_length=64, blank=True, null=True)
    acct_id = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64)
    create_time = models.DateTimeField()
    modifier = models.CharField(max_length=64)
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'zsm_shop_huifu_info'


class ZsmShopSetConfiguration(models.Model):
    shop_id = models.CharField(max_length=64)
    province = models.CharField(max_length=500, blank=True, null=True)
    province_code = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    city_code = models.IntegerField(blank=True, null=True)
    district = models.CharField(max_length=500, blank=True, null=True)
    district_code = models.IntegerField(blank=True, null=True)
    third_scan_ratio = models.IntegerField(blank=True, null=True)
    app_scan_ratio = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=500, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=500, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_shop_set_configuration'


class ZsmTicket(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_user_id = models.CharField(max_length=64)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    alive = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_ticket'


class ZsmTicketAwardRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField()
    award_id = models.CharField(max_length=64, blank=True, null=True)
    ticket_id = models.CharField(max_length=64, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    user_amount = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    user_id = models.CharField(max_length=64, blank=True, null=True)
    award_role = models.CharField(max_length=64, blank=True, null=True)
    award_status = models.IntegerField(blank=True, null=True)
    award_date = models.DateTimeField(blank=True, null=True)
    txid = models.CharField(max_length=255)
    txdate = models.DateTimeField()
    fund_pool_id = models.CharField(max_length=64, blank=True, null=True)
    issue_id = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    readed = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_ticket_award_record'


class ZsmTicketBurnPool(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField()
    burn_address = models.CharField(max_length=64, blank=True, null=True)
    burn_amount = models.DecimalField(max_digits=10, decimal_places=4)
    fund_pool_id = models.CharField(max_length=64, blank=True, null=True)
    txid = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_ticket_burn_pool'


class ZsmTicketBurnRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField()
    award_id = models.CharField(max_length=64, blank=True, null=True)
    burn_date = models.DateTimeField()
    burn_address = models.CharField(max_length=64, blank=True, null=True)
    burn_amount = models.DecimalField(max_digits=10, decimal_places=4)
    fund_pool_id = models.CharField(max_length=64, blank=True, null=True)
    txid = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_ticket_burn_record'


class ZsmTicketCheckInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField()
    check_amount = models.DecimalField(max_digits=10, decimal_places=4)
    shop_id = models.CharField(max_length=64)
    shop_name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=64)
    user_name = models.CharField(max_length=100)
    check_channel = models.IntegerField()
    txdate = models.DateTimeField()
    txid = models.CharField(max_length=64)
    status = models.IntegerField()
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_ticket_check_info'


class ZsmTicketCheckRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField()
    check_info_id = models.CharField(max_length=64)
    ticket_id = models.CharField(max_length=64)
    check_amount = models.DecimalField(max_digits=10, decimal_places=4)
    txdate = models.DateTimeField()
    txid = models.CharField(max_length=64)
    status = models.IntegerField()
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_ticket_check_record'


class ZsmTicketCostRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField()
    ticket_id = models.CharField(max_length=64)
    add_value = models.DecimalField(max_digits=10, decimal_places=4)
    txid = models.CharField(max_length=64)
    txdate = models.DateTimeField()
    status = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_ticket_cost_record'


class ZsmTicketFundPool(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField()
    issue_date = models.DateTimeField()
    issue_address = models.CharField(max_length=64, blank=True, null=True)
    issue_amount = models.DecimalField(max_digits=12, decimal_places=2)
    balance = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    txid = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_ticket_fund_pool'


class ZsmTicketGroup(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField()
    ticket_id = models.CharField(max_length=64)
    ticket_address = models.CharField(max_length=64)
    user_id = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    cost = models.DecimalField(max_digits=10, decimal_places=4)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    issue_userid = models.CharField(max_length=64)
    issue_data = models.DateTimeField()
    fund_pool_id = models.CharField(max_length=64, blank=True, null=True)
    txid = models.CharField(max_length=255)
    txdate = models.DateTimeField()
    status = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    agent_id = models.CharField(max_length=64, blank=True, null=True)
    buy_tx_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_ticket_group'


class ZsmTicketGroupRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField()
    old_ticket_id = models.CharField(max_length=64)
    new_ticket_id = models.CharField(max_length=64)
    txid = models.CharField(max_length=255)
    txdate = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    cost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    action_type = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_ticket_group_record'


class ZsmTicketIssueRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField()
    issue_id = models.CharField(max_length=64, blank=True, null=True)
    fund_id = models.CharField(max_length=64)
    issue_userid = models.CharField(max_length=64)
    issue_date = models.DateTimeField()
    issue_address = models.CharField(max_length=64, blank=True, null=True)
    issue_reson = models.CharField(max_length=64, blank=True, null=True)
    issue_reson_desc = models.CharField(max_length=225, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    txid = models.CharField(max_length=225)
    status = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_ticket_issue_record'


class ZsmTicketLog(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    creater = models.CharField(max_length=255, blank=True, null=True)
    creater_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=255, blank=True, null=True)
    modifier_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_ticket_log'


class ZsmTicketNumber(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_user_id = models.CharField(max_length=64)
    fk_act_user_id = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    alive = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    service_type = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_ticket_number'


class ZsmTicketReceiveConfig(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_user_id = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    alive = models.DecimalField(max_digits=10, decimal_places=2)
    number = models.IntegerField()
    left_number = models.IntegerField()
    type = models.IntegerField()
    is_qrcode = models.IntegerField(blank=True, null=True)
    is_map = models.IntegerField(blank=True, null=True)
    is_shop = models.IntegerField(blank=True, null=True)
    detail = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_ticket_receive_config'


class ZsmTicketRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    fk_from_user_id = models.CharField(max_length=64)
    fk_to_user_id = models.CharField(max_length=64)
    service_type = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_ticket_record'


class ZsmTicketUserAccountRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField()
    user_id = models.CharField(max_length=64)
    user_type = models.CharField(max_length=64, blank=True, null=True)
    ticket_id = models.CharField(max_length=64, blank=True, null=True)
    txid = models.CharField(max_length=255)
    txdate = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    cost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    issue_userid = models.CharField(max_length=64, blank=True, null=True)
    issue_data = models.CharField(max_length=64, blank=True, null=True)
    fund_pool_id = models.CharField(max_length=64, blank=True, null=True)
    issue_id = models.CharField(max_length=64, blank=True, null=True)
    action = models.IntegerField(blank=True, null=True)
    ticket_status = models.IntegerField(blank=True, null=True)
    amount_type = models.IntegerField(blank=True, null=True)
    inacc_type = models.IntegerField(blank=True, null=True)
    outacc_type = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    service_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_ticket_user_account_record'


class ZsmTicketUserReceiveRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField(blank=True, null=True)
    frome_user_id = models.CharField(max_length=64, blank=True, null=True)
    frome_user_name = models.CharField(max_length=64, blank=True, null=True)
    receive_user_id = models.CharField(max_length=64)
    receive_time = models.DateTimeField()
    ticket_id = models.CharField(max_length=64, blank=True, null=True)
    receive_type = models.IntegerField(blank=True, null=True)
    receive_type_name = models.CharField(max_length=64, blank=True, null=True)
    share_id = models.CharField(max_length=64, blank=True, null=True)
    txid = models.CharField(max_length=64, blank=True, null=True)
    txdate = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    cost = models.DecimalField(max_digits=10, decimal_places=4)
    issue_userid = models.CharField(max_length=64, blank=True, null=True)
    issue_data = models.DateTimeField()
    fund_pool_id = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField()
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_ticket_user_receive_record'


class ZsmTicketUserShareRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField()
    share_user_id = models.CharField(max_length=64)
    share_time = models.DateTimeField(blank=True, null=True)
    time_limit = models.IntegerField(blank=True, null=True)
    effective_time = models.DateTimeField(blank=True, null=True)
    share_type = models.IntegerField(blank=True, null=True)
    share_type_name = models.CharField(max_length=64, blank=True, null=True)
    share_channel = models.IntegerField(blank=True, null=True)
    share_channel_name = models.CharField(max_length=64, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=4)
    share_numer = models.IntegerField(blank=True, null=True)
    amount_type = models.IntegerField(blank=True, null=True)
    signle_amount = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    share_id = models.CharField(max_length=64, blank=True, null=True)
    cityagent_buy_tx_id = models.CharField(max_length=64, blank=True, null=True)
    status = models.IntegerField()
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_ticket_user_share_record'


class ZsmUserCashAccount(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField()
    user_id = models.CharField(max_length=64, blank=True, null=True)
    cash_address = models.CharField(max_length=64, blank=True, null=True)
    user_role = models.IntegerField()
    active_amount = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    freeze_amount = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_user_cash_account'


class ZsmUserCashAccountRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField()
    user_id = models.CharField(max_length=64, blank=True, null=True)
    cash_address = models.CharField(max_length=64, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    action = models.IntegerField(blank=True, null=True)
    trans_type = models.IntegerField(blank=True, null=True)
    trans_status = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_user_cash_account_record'


class ZsmUserShop(models.Model):
    user_id = models.CharField(max_length=200, blank=True, null=True)
    shop_id = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_user_shop'


class ZsmUserTicketAccount(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    version = models.IntegerField()
    user_id = models.CharField(max_length=64, blank=True, null=True)
    ticketr_address = models.CharField(max_length=64, blank=True, null=True)
    user_role = models.IntegerField()
    active_amount = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    freeze_amount = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    active_amount2 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    freeze_amount2 = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)
    creater = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=64, blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zsm_user_ticket_account'
