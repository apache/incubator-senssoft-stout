# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from django.core.exceptions import ObjectDoesNotExist
from op_tasks.models import UserAchievement, Achievement


def checkAchievements(request):
    user = request.user

    tasksComplete(user)
    genTaskAccuracy(user)
    devTaskAccuracy(user)
    genTaskAccuracy(user)
    referralsOne(user)
    referralsTwo(user)
    referralsThree(user)
    referralsFour(user)


def tasksComplete(user):
    return True


def genTaskAccuracy(user):
    award = False
    userprofile = user.userprofile
    genAccuracyAchivement = Achievement.objects.get(name='genTaskAccuracy')

    try:
        userAchievement = UserAchievement.objects.get(userprofile=userprofile, achievement=genAccuracyAchivement)
    except ObjectDoesNotExist:
        if userprofile.bestDevAccuracy > 89:
            userAchievement = UserAchievement(userprofile=userprofile, achievement=genAccuracyAchivement)
            userAchievement.save()
            award=True
    return award


def devTaskAccuracy(user):
    award = False
    userprofile = user.userprofile
    devAccuracyAchivement = Achievement.objects.get(name='devTaskAccuracy')

    try:
        userAchievement = UserAchievement.objects.get(userprofile=userprofile, achievement=devAccuracyAchivement)
    except ObjectDoesNotExist:
        if userprofile.bestDevAccuracy > 89:
            userAchievement = UserAchievement(userprofile=userprofile, achievement=devAccuracyAchivement)
            userAchievement.save()
            award=True
    return award


def referralsOne(user):
    """
    checks referrals in userprofile to see if a certain level is met
    :param user: the user object to check
    :return: boolean, true if condition met, false otherwise
    """
    return referralsCheck(user, 3, 'referralsOne')


def referralsTwo(user):
    """
    checks referrals in userprofile to see if level two is met
    :param user: the user object to check
    :return: award - boolean, true if condition met, false otherwise
    """
    return referralsCheck(user, 6, 'referralsTwo')


def referralsThree(user):
    """

    :param user:
    :return:
    """
    return referralsCheck(user, 9, 'referralsThree')


def referralsFour(user):
    """

    :param user:
    :return:
    """
    return referralsCheck(user, 12, 'referralsFour')


def referralsCheck(user, count, achievementName):
    """
    general method to check different levels of referrals
    :param user: the user object to check
    :param count: the level to check
    :param achievementName: the name of the achievement
    :return: boolean - true if level met, false otherwise
    """
    award = False
    userprofile = user.userprofile
    referralsAchievement = Achievement.objects.get(name=achievementName)

    # first check if user already has achievement
    try:
        userAchievement = UserAchievement.objects.get(userprofile=userprofile, achievement=referralsAchievement)
    except ObjectDoesNotExist:
        if userprofile.referrals >= count :
            userAchievement = UserAchievement(userprofile=userprofile, achievement=referralsAchievement)
            userAchievement.save()
            award = True
    return award