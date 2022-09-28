# -*- coding: utf-8 -*-
import math

def get_club_activity_point(club_member_point_list):
    cash_club_activity_point = sum([math.log((i/2000+1)) for i in club_member_point_list])
    return round((10 * (0.2 - 1 / (10 - len(club_member_point_list) + 5)) * cash_club_activity_point), 1)

print get_club_activity_point([33333] * 2)
