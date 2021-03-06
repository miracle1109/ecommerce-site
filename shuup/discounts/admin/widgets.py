# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2021, Shuup Commerce Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from shuup.admin.forms.quick_select import QuickAddRelatedObjectMultiSelect
from shuup.utils.django_compat import reverse_lazy


class QuickAddHappyHourMultiSelect(QuickAddRelatedObjectMultiSelect):
    url = reverse_lazy("shuup_admin:discounts_happy_hour.new")
