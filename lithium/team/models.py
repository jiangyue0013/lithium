from django.db import models


class Team(models.Model):
    username = models.CharField(max_length=128, unique=True, verbose_name="用户名")
    name = models.CharField(max_length=128, verbose_name="队伍名称")
    victory = models.IntegerField(default=0, verbose_name="胜场数")
    draw = models.IntegerField(default=0, verbose_name="平局数")
    lose = models.IntegerField(default=0, verbose_name="负场数")
    goals_num = models.IntegerField(default=0, verbose_name="进球数")
    goals_conceded = models.IntegerField(default=0, verbose_name="失球数")

    @property
    def score(self):
        return self.victory * 3 + self.draw
    
    @property
    def goal_difference(self):
        return self.goals_num - self.goals_conceded

    class Meta:
        verbose_name = verbose_name_plural = "队伍"
    
    def __str__(self) -> str:
        return self.name