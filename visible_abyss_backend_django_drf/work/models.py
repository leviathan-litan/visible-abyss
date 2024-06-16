from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 公司
class Company(models.Model):

    company_name = models.CharField(
        verbose_name="名称",
        max_length=200,
        help_text="公司或组织的名称",
        unique=True,
    )

    company_description = models.TextField(
        verbose_name="描述",
        max_length=200,
        help_text="公司或组织的描述或说明"
    )

    class Meta:
        verbose_name = "公司 / 组织"
        verbose_name_plural = verbose_name

# 公司
class Department(models.Model):

    department_name = models.CharField(
        verbose_name="名称",
        max_length=200,
        help_text="部门名称",
        unique=True,
    )

    department_description = models.TextField(
        verbose_name="描述",
        max_length=200,
        help_text="对当前部门的描述"
    )

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = verbose_name

# 工作 / 职业分类
class Work(models.Model):

    work_name = models.CharField(
        verbose_name="工作",
        max_length=200,
        unique=True,
    )

    class Meta:
        verbose_name = "工作"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.work_name

# 技能：所拥有的技能，兴趣也属于技能的一部分
class Skill(models.Model):

    skill_name = models.CharField(
        verbose_name="技能",
        max_length=200,
        unique=True,
    )

    class Meta:
        verbose_name = "技能"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.skill_name

# 成就：称号、成就、资格评定、认证、奖项
class Archievement(models.Model):

    class Meta:
        verbose_name = "成就"
        verbose_name_plural = verbose_name

# 工作经历
class WorkExperience(models.Model):

    user = models.ForeignKey(
        verbose_name="姓名",
        to=User,
        on_delete=models.CASCADE,
    )

    company = models.ForeignKey(
        verbose_name="公司",
        to=Company,
        on_delete=models.DO_NOTHING,
    )
    work = models.ForeignKey(
        verbose_name="职位",
        to=Work,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    department = models.ForeignKey(
        verbose_name="部门",
        to=Department,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )

    begin_at = models.DateField(
        verbose_name="在职时间「起始」",
        null=True,
        blank=True,
    )
    end_at = models.DateField(
        verbose_name="在职时间「结束」",
        null=True,
        blank=True,
    )

    skills = models.ManyToManyField(
        verbose_name="技能",
        to=Skill,
        blank=True,
    )

    archievement = models.ManyToManyField(
        verbose_name="成就",
        to=Archievement,
        blank=True,
    )

    work_content = models.TextField(
        verbose_name="工作内容",
        max_length=5000,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        editable=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="更新时间",
        auto_now=True,
        editable=True,
    )

    class Meta:
        verbose_name = "工作经历"
        verbose_name_plural = verbose_name
