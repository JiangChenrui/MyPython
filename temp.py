# -*- coding: tf-8 -*-
def inbox_collect_gift_20(ctx, info, name, ret, v1, v2):
    v1 = ctx.user.vip_config_act[7]
    ctx.user.add_coins(v1)

